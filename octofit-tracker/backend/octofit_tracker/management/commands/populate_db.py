
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **kwargs):
        # Eliminar datos existentes en orden seguro (hijos -> padres), uno por uno
        for obj in Activity.objects.all():
            obj.delete()
        for obj in Leaderboard.objects.all():
            obj.delete()
        # Limpiar relaciones ManyToMany antes de borrar Workouts
        for workout in Workout.objects.all():
            workout.suggested_for.clear()
        for obj in Workout.objects.all():
            obj.delete()
        # Limpiar relaciones ForeignKey antes de borrar Users
        for user in User.objects.all():
            user.team = None
            user.save()
        for obj in User.objects.all():
            obj.delete()
        for obj in Team.objects.all():
            obj.delete()

        # Crear equipos
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Crear usuarios
        ironman = User.objects.create(
            email='ironman@marvel.com', username='ironman', first_name='Tony', last_name='Stark', team=marvel
        )
        captain = User.objects.create(
            email='cap@marvel.com', username='cap', first_name='Steve', last_name='Rogers', team=marvel
        )
        batman = User.objects.create(
            email='batman@dc.com', username='batman', first_name='Bruce', last_name='Wayne', team=dc
        )
        superman = User.objects.create(
            email='superman@dc.com', username='superman', first_name='Clark', last_name='Kent', team=dc
        )

        # Crear actividades
        Activity.objects.create(user=ironman, activity_type='Running', duration=30, calories_burned=300)
        Activity.objects.create(user=captain, activity_type='Cycling', duration=45, calories_burned=400)
        Activity.objects.create(user=batman, activity_type='Swimming', duration=60, calories_burned=500)
        Activity.objects.create(user=superman, activity_type='Yoga', duration=40, calories_burned=200)

        # Crear workouts y asignar a equipos
        full_body = Workout.objects.create(name='Full Body', description='Entrenamiento completo')
        cardio = Workout.objects.create(name='Cardio', description='Entrenamiento cardiovascular')
        full_body.suggested_for.add(marvel)
        cardio.suggested_for.add(dc)

        # Crear leaderboard
        Leaderboard.objects.create(user=ironman, score=100)
        Leaderboard.objects.create(user=captain, score=90)
        Leaderboard.objects.create(user=batman, score=110)
        Leaderboard.objects.create(user=superman, score=95)

        self.stdout.write(self.style.SUCCESS('La base de datos octofit_db ha sido poblada con datos de prueba.'))
