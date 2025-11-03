from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from .models import UserModel,TournamentModel, TournamentRegistration
from userapp.models import BookModel

from.models import *

# Create your views here.


def login(request):
    return render(request,'user_dashboard.html')

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        user = UserModel()
        user.fullname = request.POST.get('fullname')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')   # ⚠️ better to hash before saving
        user.remember_me = True if request.POST.get('remember') else False
        user.save()
        return redirect('/login')   # redirect to home or login after signup
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember_me")

        try:
            user = UserModel.objects.get(email=email)
            # If you stored raw password (not recommended), just compare directly
            if user.password == password:
                request.session['user_id'] = user.user_id
                request.session['fullname'] = user.fullname

                # Handle remember_me
                if remember_me:
                    request.session.set_expiry(1209600)  # 2 weeks
                else:
                    request.session.set_expiry(0)  # browser close -> logout

                return redirect('/user_dashboard')  # go to user page
            else:
                messages.error(request, "Invalid password!")
        except UserModel.DoesNotExist:
            messages.error(request, "User not found! Please register first.")

    return render(request, "login.html")

def user_dashboard(request):
    if "user_id" in request.session:
        user_obj = UserModel.objects.get(user_id=request.session['user_id'])
        print(user_obj)
        return render(request, "user_dashboard.html", {'data':user_obj})
    else:
        return redirect("/login")

def logout_view(request):
    del request.session['user_id']
    return redirect("/login")



def organizer(request):
    return render(request,'organizer_dashboard.html')

def tournament(request):
    tournament=TournamentModel.objects.all()
    return  render(request,'tournament.html',{'data':tournament})

def view_tournament(request,id):
    tournament=TournamentModel.objects.get(tournament_id=id)
    return render(request, 'tournament_details.html', {'data': tournament})

def add_book(request):
    if request.method=='POST':
        book_add=BookModel()
        book_add.book_name=request.POST.get('name1')
        book_add.book_price=request.POST.get('number')
        book_add.book_image=request.FILES.get('photo')
        book_add.save()
        return redirect('/add')
    return render(request,'add.html')


def organizer_dashboard(request):
    # Ensure user is logged in
    if 'user_id' not in request.session:
        return redirect('login')  # redirect if not logged in

    # Get current logged-in organizer
    user_id = request.session['user_id']
    organizer = UserModel.objects.get(user_id=user_id)

    # If tournament form submitted
    if request.method == 'POST':
        tournament = TournamentModel()
        tournament.name = request.POST.get('name')
        tournament.category = request.POST.get('category')
        tournament.start_date = request.POST.get('start_date')
        tournament.end_date = request.POST.get('end_date')
        tournament.registration_deadline = request.POST.get('registration_deadline')
        tournament.location = request.POST.get('location')
        tournament.registration_fee = request.POST.get('fees')
        tournament.description = request.POST.get('description')
        tournament.organizer = organizer
        tournament.save()

        return redirect('/tournament')  # redirect after saving

    # ✅ No tournament list here — only the form
    context = {
        'username': request.session.get('username')
    }

    return render(request, 'organizer_dashboard.html', context)



def register_tournament(request, id):
    if 'user_id' in request.session:
        user = UserModel.objects.get(user_id=request.session['user_id'])
        tournament = TournamentModel.objects.get(tournament_id=id)

        if request.method == "POST":
            regist=TournamentRegistration()
            regist.user_id=user
            regist.tournament = tournament
            regist.team_name = request.POST.get("team_name")
            regist.location = request.POST.get("location")
            regist.phone = request.POST.get("phone")
            regist.email = request.POST.get("email")
            regist.proof = request.FILES.get("proof")
            regist.save()
            return redirect('/tournament')

        return render(request, 'tournament_register.html', {"data": tournament})
    else:
        return redirect('/')


def about(request):
    return render(request,'about.html')


def contact(request):
    return  render(request,'contact.html')




def my_dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')

    user = UserModel.objects.get(user_id=request.session['user_id'])

    # 1️⃣ Tournaments organized by the user
    my_tournaments = TournamentModel.objects.filter(organizer=user)

    # 2️⃣ All registrations for the tournaments they organized
    registered_teams = TournamentRegistration.objects.filter(tournament__in=my_tournaments)

    # 3️⃣ Tournaments the user registered for (as a participant)
    my_registrations = TournamentRegistration.objects.filter(user_id=user)

    context = {
        'my_tournaments': my_tournaments,
        'registered_teams': registered_teams,
        'my_registrations': my_registrations,
    }

    return render(request, 'my_dashboard.html', context)



def update_tournament(request, tournament_id):
    tournament = get_object_or_404(TournamentModel, pk=tournament_id)

    if request.method == "POST":
        tournament.name = request.POST.get("name")
        tournament.category = request.POST.get("category")
        tournament.start_date = request.POST.get("start_date")
        tournament.end_date = request.POST.get("end_date")
        tournament.registration_deadline = request.POST.get("registration_deadline")
        tournament.location = request.POST.get("location")
        tournament.registration_fee = request.POST.get("fees")
        tournament.description = request.POST.get("description")
        tournament.save()
        return redirect('my_dashboard')

    return render(request, "update_tournament.html", {"tournament": tournament})

# ✅ Delete Tournament
def delete_tournament(request, tournament_id):
    tournament = get_object_or_404(TournamentModel, tournament_id=tournament_id)
    tournament.delete()
    return redirect('/my_dashboard')


# ✅ Cancel Registration
def delete_registration(request, registration_id):
    registration = get_object_or_404(TournamentRegistration, registration_id=registration_id)
    registration.delete()
    return redirect('/my_dashboard')


