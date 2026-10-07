from rest_framework import serializers
from .models import TournamentModel, UserModel
from .models import TournamentRegistration

class TournamentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentModel
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TournamentRegistration
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'