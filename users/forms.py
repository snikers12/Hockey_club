from django import forms

from users.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image', 'gender', 'birth_date', 'favorite_position', 'about']