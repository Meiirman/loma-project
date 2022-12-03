from users.models import LomaUser

def get_access_data(user):
    current_user = LomaUser.objects.get(user=user)
    
    return current_user.get_accesse