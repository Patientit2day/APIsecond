from django.test import TestCase
from .models import Supplier

class SupplierModelTest(TestCase):

    def setUp(self):
        Supplier.objects.create(name="Test Supplier", email="supplier@example.com", phone="1234567890", address="123 Test St")

    def test_supplier_creation(self):
        supplier = Supplier.objects.get(name="Test Supplier")
        self.assertEqual(supplier.name, "Test Supplier")
        self.assertEqual(supplier.email, "supplier@example.com")
        self.assertEqual(supplier.phone, "1234567890")
        self.assertEqual(supplier.address, "123 Test St")

    def test_supplier_string_representation(self):
        supplier = Supplier.objects.get(name="Test Supplier")
        self.assertEqual(str(supplier), "Test Supplier")

from django.test import TestCase
from .models import Supplier

class SupplierModelTest(TestCase):

    def setUp(self):
        # Créer un fournisseur pour les tests
        self.supplier = Supplier.objects.create(
            name="Test Supplier",
            email="supplier@example.com",
            phone="1234567890",
            address="123 Test St"
        )

    def test_supplier_creation(self):
        supplier = Supplier.objects.get(name="Test Supplier")
        self.assertEqual(supplier.name, "Test Supplier")
        self.assertEqual(supplier.email, "supplier@example.com")
        self.assertEqual(supplier.phone, "1234567890")
        self.assertEqual(supplier.address, "123 Test St")

    def test_supplier_string_representation(self):
        supplier = Supplier.objects.get(name="Test Supplier")
        self.assertEqual(str(supplier), "Test Supplier")

    def test_supplier_deletion(self):
        # Vérifier que le fournisseur existe avant la suppression
        self.assertTrue(Supplier.objects.filter(id=self.supplier.id).exists())

        # Supprimer le fournisseur
        self.supplier.delete()

        # Vérifier que le fournisseur n'existe plus après la suppression
        self.assertFalse(Supplier.objects.filter(id=self.supplier.id).exists())