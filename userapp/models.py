from django.db import models


# Create your models here.

class BookModel(models.Model):
    book_id=models.AutoField(primary_key=True)
    book_name=models.CharField(max_length=50)
    book_price=models.IntegerField()
    book_image=models.ImageField(upload_to='profile images',null=True)

    class Meta:
        db_table='book_add'

class UserModel(models.Model):
    user_id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    remember_me = models.BooleanField(default=False)
    registered_at = models.DateTimeField(auto_now_add=True,null=True)  # saves date & time of registration

    class Meta:
        db_table = 'user_signup'



class TournamentModel(models.Model):
    tournament_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)   # Football, Cricket, etc.
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    registration_deadline = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200)
    registration_fee = models.CharField(max_length=150,null=True)
    description = models.TextField(null=True, blank=True)
    organizer = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='organized_tournaments',
                                  null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # when added
    updated_at = models.DateTimeField(auto_now=True)      # last update

    class Meta:
        db_table = 'tournament_add'

class TournamentRegistration(models.Model):
    user_id=models.ForeignKey(UserModel, on_delete=models.CASCADE,null=True)
    registration_id = models.AutoField(primary_key=True)
    tournament = models.ForeignKey(TournamentModel, on_delete=models.CASCADE, related_name="registrations")
    team_name = models.CharField(max_length=150)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    proof = models.ImageField(upload_to='profile images',null=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tournament_registration'

    def __str__(self):
        return f"{self.team_name} - {self.tournament.name}"
