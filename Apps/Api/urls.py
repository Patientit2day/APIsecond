from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import EmployeViewSet, PostViewSet,PaymentViewSet, CustomUserViewSet,StagiairesViewSet,SupplierViewSet,ProfessorViewSet

router = DefaultRouter()
router.register(r'employes', EmployeViewSet)
router.register(r'stagiaires', StagiairesViewSet)
router.register(r'posts', PostViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'professors', ProfessorViewSet)
router.register(r'payments', PaymentViewSet, basename='payment')
router.register(r'users', CustomUserViewSet)
urlpatterns = [

    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]