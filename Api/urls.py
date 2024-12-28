from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import EmployeViewSet, PostViewSet, StagiairesViewSet,SupplierViewSet,ProfessorViewSet

router = DefaultRouter()
router.register(r'employes', EmployeViewSet)
router.register(r'stagiaires', StagiairesViewSet)
router.register(r'posts', PostViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'professors', ProfessorViewSet)
urlpatterns = [

    path('', include(router.urls)),
   
]