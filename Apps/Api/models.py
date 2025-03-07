from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from rest_framework.exceptions import ValidationError
from django.utils.text import slugify

class CustomUser(AbstractUser):
    photo=models.ImageField(blank=True,null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slug = slugify(self.username)
            counter = 1
            while CustomUser.objects.filter(slug=unique_slug).exists():
                unique_slug = f'{unique_slug}-{counter}'
                counter += 1
            self.slug = unique_slug

        # Hash the password if it's not already hashed
        if self.pk:  # User exists
            original_password = CustomUser.objects.get(pk=self.pk).password
            if self.password != original_password:  # Password has changed
                self.set_password(self.password)
        else:  # New user
            if self.password:  # Ensure password is provided
                self.set_password(self.password)

        # Call the parent class's save method
        super().save(*args, **kwargs)

class Stagiaires(models.Model):

    nom=models.CharField(max_length=45,blank=False,null=False)
    prenom=models.CharField(max_length=45,blank=False,null=False)
    email=models.EmailField()
    telephone=models.CharField(max_length=12,null=False,blank=False)
    def __str__(self):
        return self.nom


class Post(models.Model):

    post_name=models.CharField(max_length=120,null=False,blank=False)
    def __str__(self):
       return self.post_name




class Employee(models.Model):

    name=models.CharField(max_length=45,blank=False,null=False)
    surname=models.CharField(max_length=45,blank=False,null=False)
    email=models.EmailField()
    telephone=models.CharField(max_length=12,null=False,blank=False)
   # title=models.CharField(max_length=255,null=False,blank=False)
    gender=models.CharField(max_length=50, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
    ])
    salary=models.CharField(max_length=255,null=False,blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    adress=models.CharField(max_length=255,null=False,blank=False)
    typecontrat=models.CharField(max_length=255,null=False,blank=False)

    contrat=models.FileField(upload_to='pdf_contrats/')
    hiring_date=models.DateTimeField(default=timezone.now)
    photo = models.ImageField(upload_to='pdf_contrats/', null=True, blank=True)

    def __str__(self):
        return self.name
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

class Professor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Payment(models.Model):
    product_name = models.CharField(max_length=255)
    amount = models.IntegerField()  # Montant en cents
    currency = models.CharField(max_length=3)
    stripe_session_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} - {self.amount} {self.currency}"





