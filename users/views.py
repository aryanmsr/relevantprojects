from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import RegularUserCreationForm, CompanyUserCreationForm


class RegularUserSignUpView(CreateView):
    form_class = RegularUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'


class CompanyUserSignUpView(CreateView):
    form_class = CompanyUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
