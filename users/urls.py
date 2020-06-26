from django.urls import path

from . import views

urlpatterns = [
    path('signup/user', views.RegularUserSignUpView.as_view(),
         name='regular_user_signup'),
    path('signup/company/', views.CompanyUserSignUpView.as_view(),
         name='company_user_signup')
]
