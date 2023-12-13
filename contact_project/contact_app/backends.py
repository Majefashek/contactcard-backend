from django.contrib.auth.backends import ModelBackend
from .models import User

class CustomLoginBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
       
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        else:
            if user.password==password:
                return user
        return None
