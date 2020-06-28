from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy

from . import models


def landing_page_view(request):
    return render(request, 'landing.html')


"""
    Home page is list view of all posts, with query and filter functionality.

"""


def home_page_view(request):
    posts = models.Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)


"""
    CRUD functionality for posts, the detail view can be accessed by anyone while the other 
    views are restricted to only the logged in user which has to be also a company user which 
    has been approved. There are two views which allow a company to see all its posts and a view 
    to see the all the submissions for a specific post.

"""


class PostDetailView(DetailView):
    model = models.Post
    template_name = 'post_detail.html'


def post_list_view(request):
    # render all posts of a company
    # get user object from request and query all submission from his id
    # render as list
    render('post_list_view.html')


class PostCreateView(CreateView):
    model = models.Post
    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.company = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = models.Post
    template_name = 'post_edit.html'
    fields = ['title', 'description', 'date_due']


class PostDeleteView(DeleteView):
    model = models.Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


def post_submission_list_view(request, pk):  # view all submission of post
    # query all submission with by looking for the post filed which
    # which matches the current post
    return render('post_submission_list.html')
