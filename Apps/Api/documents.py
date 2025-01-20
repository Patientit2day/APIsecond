
from django_elasticsearch_dsl import Document, fields
from .models import Employee

class EmployeeDocument(Document):
    class Index:
        name = 'employees'  # Nom de l'index

    class Django:
        model = Employee  # Le modèle associé

        fields = [
            'id',
            'name',
            'surname',
            'email',
            'telephone',
            'gender',
            'salary',
            'address',
            'typecontrat',
            'hiring_date',
        ]
