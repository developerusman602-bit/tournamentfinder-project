from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TournamentModel
from .models import TournamentRegistration
from .serializers import RegistrationSerializer
from rest_framework import status
from .serializers import UserSerializer
from .models import UserModel

@api_view(['GET'])
def get_tournaments(request):
    tournaments = TournamentModel.objects.all().values()
    return Response(list(tournaments))

@api_view(['GET'])
def get_tournament(request, id):
    try:
        tournament = TournamentModel.objects.get(tournament_id=id)
        return Response({
            "id": tournament.tournament_id,
            "name": tournament.name,
            "category": tournament.category,
            "start_date": tournament.start_date,
            "location": tournament.location,
            "fee": tournament.registration_fee,
            "description": tournament.description,
        })
    except TournamentModel.DoesNotExist:
        return Response({"error": "Tournament not found"}, status=404)

@api_view(['GET'])
def get_register(request):
    register = TournamentRegistration.objects.all().values()
    return Response(list(register))


@api_view(['POST'])
def register_tournament(request):
    serializer = RegistrationSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message": "Tournament registered successfully"},
            status=status.HTTP_201_CREATED
        )

    return Response(
        serializer.errors,
        status=status.HTTP_400_BAD_REQUEST
    )

@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_user(request, id):
    user = UserModel.objects.get(user_id=id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

