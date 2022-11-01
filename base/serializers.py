from rest_framework.serializers import ModelSerializer
from .models import Advocate

class AdvocateSerializer(ModelSerializer):
    class Meta:
        model = Advocate
        fields = '__all__'
