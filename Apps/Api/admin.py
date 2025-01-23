from django.contrib import admin

from .models import Employee, Post, Stagiaires,Professor,CustomUser

# Register your models here.

@admin.register(Stagiaires)
class Stagiaires(admin.ModelAdmin):
    list_display=('id','nom','prenom','email','telephone')

@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display=('id','post_name')


@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
   pass

@admin.register(Employee)
class Employee(admin.ModelAdmin):
    list_display=('id','name','surname','email','adress','telephone','typecontrat','gender','contrat','hiring_date','photo','salary','post')


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject', 'phone')
    search_fields = ('first_name', 'last_name', 'email', 'subject')
    ordering = ('last_name',)

