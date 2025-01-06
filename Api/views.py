from django.conf import settings
from django.core.mail import send_mail
from django_filters import rest_framework as django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, serializers, status, viewsets
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter
from .documents import EmployeeDocument
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee, Post, Stagiaires,Supplier,Professor
from .serializer import EmployeSerializer, PostSerializer, StagiairesSerializer,SupplierSerializer,ProfessorSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class StagiairesViewSet(viewsets.ModelViewSet):
    queryset = Stagiaires.objects.all().order_by('-id')  
    serializer_class = StagiairesSerializer  

    def list(self, request):
        # Récupérer tous les stagiaires
        serializer = self.get_serializer(self.queryset, many=True) 
        return Response(serializer.data, status=status.HTTP_200_OK)  

    def create(self, request):
        # Créer un nouveau stagiaire
        serializer = self.get_serializer(data=request.data)  
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
#employe


# class EmployeFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='icontains') 
#     email = django_filters.CharFilter(lookup_expr='icontains') 

#     class Meta:
#         model = Employee
#         fields = ['name', 'email']  

class EmployeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ['name', 'email'] 
    ordering_fields = '__all__'  
    ordering = ['id']  

    def list(self, request, *args, **kwargs):
        search_term = request.query_params.get('q', None)

        if search_term:
            results = EmployeeDocument.search().query("multi_match", query=search_term, fields=['name', 'surname', 'email'])
            ids = [result.id for result in results]
            self.queryset = self.queryset.filter(id__in=ids)

        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            employe = serializer.save()

            # Indexer l'employé dans Elasticsearch
            EmployeeDocument(
                id=employe.id,
                name=employe.name,
                surname=employe.surname,
                email=employe.email,
                telephone=employe.telephone
            ).save()

            subject = 'New Account Creation'
            message = (
                f'Dear {employe.name},\n\n'
                'You have been successfully registered in our employees. '
                f'Username: {employe.email}\n'
                f'Telephone: {employe.telephone}.\n\n'
                'Best regards,\nThe BTS Team.'
            )
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[employe.email],
                fail_silently=False,
            )
            return Response({
                'message': 'Employé créé avec succès.',
                'employe': serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        employe_id = self.kwargs['pk']
        
        # Récupérer l'employé depuis Elasticsearch
        try:
            employe = EmployeeDocument.get(id=employe_id)
        except Exception as e:
            return Response({'error': 'Employé non trouvé.'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(employe)  
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        employe = self.get_object()
        serializer = self.get_serializer(employe, data=request.data)
        if serializer.is_valid():
            employe_updated = serializer.save()

            # Mettre à jour l'employé dans Elasticsearch
            EmployeeDocument(
                id=employe_updated.id,
                name=employe_updated.name,
                surname=employe_updated.surname,
                email=employe_updated.email,
                telephone=employe_updated.telephone
            ).save()

            return Response({
                'message': 'Employé mis à jour avec succès.',
                'employe': serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        employe = self.get_object()
        self.perform_destroy(employe)

        # Supprimer l'employé d'Elasticsearch
        EmployeeDocument.get(id=employe.id).delete()

        return Response(status=status.HTTP_204_NO_CONTENT)




#post employee
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-id')  
    serializer_class = PostSerializer  

    def list(self, request):
        # Récupérer tous les posts
        serializer = self.get_serializer(self.queryset, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)  

    def create(self, request):
        # Créer un nouveau post
        serializer = self.get_serializer(data=request.data)  
        if serializer.is_valid(): 
            post = serializer.save()  
            return Response({
                'message': 'Post registered successfully.',
                'post': serializer.data
            }, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

