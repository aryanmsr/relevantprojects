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
    print(context)
    return render(request, 'home.html', context)


"""
    CRUD functionality for posts, the detail view can be accessed by anyone while the other 
    views are restricted to only the logged in user which has to be also a company user which 
    has been approved. There are two views which allow a company to see all its posts and a view 
    to see the all the submissions for a specific post.

"""


class PostDetailView(DetailView):
    model = models.Post
    template_name = 'post/post_detail.html'


def post_list_view(request):
    # render all posts of a company
    # get user object from request and query all submission from his id
    # render as list
    logged_in_company_id = request.user.id
    posts = models.Post.objects.filter(
        company=logged_in_company_id)
    return render(request, 'post/post_list.html', context={'posts': posts})


class PostCreateView(CreateView):
    model = models.Post
    template_name = 'post/post_create.html'
    fields = ['title', 'description', 'date_due']

    def form_valid(self, form):
        form.instance.company = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = models.Post
    template_name = 'post/post_edit.html'
    fields = ['title', 'description', 'date_due']


class PostDeleteView(DeleteView):
    model = models.Post
    template_name = 'post/post_delete.html'
    success_url = reverse_lazy('home')


def post_submission_list_view(request, pk):  # view all submission of post
    # query all submission with by looking for the post filed which
    # which matches the current post
    return render(request, 'post/post_submission_list.html')


"""
    The views for CRUD functionality for the submission model which can be accesed
    only by regular users.
"""


def submission_create_view(request, pk):
    # create new post with foreign key with id pk
    return render(request, 'submission/submission_create.html')


class SubmissionDetailView(DetailView):
    model = models.Submission
    template_name = 'submission/submission_detail.html'


class SubmissionDeleteView(DeleteView):
    model = models.Submission
    template_name = 'submission/submission_delete.html'
    success_url = reverse_lazy('home')


def submission_list_view(request):
    # get all submissions of the logged in user
    logged_in_user_id = request.user.id
    submissions = models.Submission.objects.filter(user=logged_in_user_id)
    return render(request, 'submission/submission_list.html', context={'submissions': submissions})
