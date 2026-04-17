
from django.db import models
from djongo import models as djongo_models
from bson import ObjectId


# Modelo de Equipo
class Team(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Modelo de Usuario
class User(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    team = models.ForeignKey('Team', on_delete=models.SET_NULL, null=True, related_name='members')

    def __str__(self):
        return self.username

# Modelo de Actividad
class Activity(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(help_text='Duración en minutos')
    calories_burned = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} ({self.date})"

# Modelo de Workout
class Workout(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.ManyToManyField('Team', related_name='suggested_workouts', blank=True)

    def __str__(self):
        return self.name

# Modelo de Leaderboard
class Leaderboard(models.Model):
    id = djongo_models.ObjectIdField(primary_key=True, default=ObjectId, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='leaderboard_entries')
    score = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}"
