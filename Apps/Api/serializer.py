from rest_framework import serializers

from .models import Employee, Post, Stagiaires,Supplier,Professor,Payment,CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'photo']

from django.contrib.auth import get_user_model



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'photo']

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class StagiairesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stagiaires
        fields = '__all__'  # Incluez tous les champs que vous souhaitez exposer

    def validate_email(self, value):
        # Vérifiez si l'email existe déjà dans la base de données
        if Stagiaires.objects.filter(email=value).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé.")
        return value

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'name',
            'surname',
            'email',
            'telephone',
            'gender',
            'salary',
            'post',
            'adress',
            'typecontrat',
            'contrat',
            'hiring_date',
            'photo',
        ] # Incluez tous les champs que vous souhaitez exposer

    def validate_email(self, value):
        # Vérifiez si l'email existe déjà dans la base de données
        if Employee.objects.filter(email=value).exists():
            raise serializers.ValidationError("Cet email est déjà utilisé.")
        return value
class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields =['id','post_name']  # Incluez tous les champs que vous souhaitez exposer




class PaymentSerializer(serializers.Serializer):
    product_name = serializers.CharField(max_length=255)
    amount = serializers.IntegerField()  # En cents
    currency = serializers.CharField(max_length=3)