from django.db import models
from django.contrib.auth import get_user_model


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    date_posted = models.DateTimeField(auto_now_add=True, blank=False)
    date_due = models.DateField()
    company = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
   # need to add file fields in the future


class Submission(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE)
    description = models.TextField(max_length=500, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    # need to add file fields in the future
