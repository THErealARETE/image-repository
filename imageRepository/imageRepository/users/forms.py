from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class UserCreationform(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)    
    password2 = forms.CharField(label = 'confirm Password' , widget = forms.PasswordInput)
# what is widget ??

    class Meta:
        model = User
        fields = ('first_name', 'last_name' , 'email')



class AdminUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField

    class Meta:
        model = User
        fields = '__all__'        