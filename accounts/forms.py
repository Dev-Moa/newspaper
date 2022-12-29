from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ( "username","email", "age", ) #

class CustomUserChange(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ( "username","email", "age", ) #