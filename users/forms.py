from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Forms for the admin page


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'bio', 'company_name',
                  'sector', 'major', 'university', 'is_company']


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['email', 'bio', 'company_name',
                  'sector', 'major', 'university', 'is_company']

# Forms for the views


class CompanyUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'company_name', 'sector']

    def save(self):
        user_profile = super(CompanyUserCreationForm, self).save(commit=False)
        user_profile.is_company = True
        user_profile.save()
        return user_profile


class CompanyUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'company_name', 'sector']


class RegularUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'major', 'university']


class RegularUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'major', 'university']
