from .models import UserProfile

def user_profile(request):
    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            profile = None
        return {
            'authenticated_user_profile': profile,
            'authenticated_user_name': request.user.first_name or request.user.username,
        }
    return {}
