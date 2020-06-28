from django.urls import path

from . import views

urlpatterns = [
    # Home and landing page
    path('', views.home_page_view, name='home'),
    path('learn/', views.landing_page_view, name='landing'),

    # Detail view accesible to anyone
    path('post/<int:pk>/', post_detail_view, name='post_detail'),

    # Views accesible only for companies
    path('post/all/', post_list_view, name='post_list_view'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create_view'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/submissions/',
         post_submission_list_view, name='post_submission_list'),

    # Views accesible only for regular users
    path('post/<int:pk>/new/', submission_create_view, name='submission_create')
    path('submission/<int:pk>/', submission_detail_view, name='submission_detail'),
    path('submission/<int:pk>/delete/',
         submission_delete_view, name='submission_delete'),
    path('submission/all/', submission_list_view, name='submission_list'),

]
