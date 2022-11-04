from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Advocate, Company


class CompanySerializer(ModelSerializer):
    employee_count = SerializerMethodField(read_only=True)
    class Meta:
        model = Company
        fields = '__all__'

    def get_employee_count(self, obj):
        count = obj.advocate_set.count()
        return count

class AdvocateSerializer(ModelSerializer):
    company = CompanySerializer()
    class Meta:
        model = Advocate
        fields =  ['profile_pic', 'username', 'name', 'bio', 'twitter', 'company']
