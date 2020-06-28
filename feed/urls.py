from django.urls import path

from . import views

urlpatterns = [
    # Home and landing page
    path('', views.home_page_view, name='home'),
    path('learn/', views.landing_page_view, name='landing'),

    # Detail view accesible to anyone
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),

    # Views accesible only for companies
    path('post/all/', views.post_list_view, name='post_list'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/submissions/',
         views.post_submission_list_view, name='post_submission_list'),

    # Views accesible only for regular users
    path('post/<int:pk>/new/', views.submission_create_view,
         name='submission_create'),
    path('submission/<int:pk>/', views.SubmissionDetailView.as_view(),
         name='submission_detail'),
    path('submission/<int:pk>/delete/',
         views.SubmissionDeleteView.as_view(), name='submission_delete'),
    path('submission/all/', views.submission_list_view,
         name='submission_list'),

]
