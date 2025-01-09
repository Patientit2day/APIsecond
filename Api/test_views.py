from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Supplier

class SupplierAPITest(APITestCase):

    def test_create_supplier(self):
        url = reverse('supplier-list')  # Assurez-vous que cette URL est correctement définie dans votre routing
        data = {
            'name': 'New Supplier',
            'email': 'new_supplier@example.com',
            'phone': '0987654321',
            'address': '456 Another St'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Supplier.objects.count(), 1)
        self.assertEqual(Supplier.objects.get().name, 'New Supplier')

    def test_get_supplier(self):
        Supplier.objects.create(name="Existing Supplier", email="existing_supplier@example.com", phone="1234567890", address="789 Existing St")
        url = reverse('supplier-list')  # Assurez-vous que cette URL est correctement définie dans votre routing
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Existing Supplier")