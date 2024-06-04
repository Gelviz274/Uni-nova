# recommendation.py
import random
from Usuarios.models import UserProfile

def get_featured_users(num_users=4):
    users = list(UserProfile.objects.exclude(user__isnull=True))
    return random.sample(users, min(num_users, len(users)))
