from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=500, blank=False)
    date_posted = models.DateTimeField(
        auto_now_add=True, blank=False)
    date_due = models.DateField()
    company = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)
   # need to add file fields in the future

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})


class Submission(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="user")
    description = models.TextField(max_length=500, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    # need to add file fields in the future

    def __str__(self):
        return f"Submission - {self.user}"

    def get_absolute_url(self):
        return reverse("submission_detail", kwargs={"pk": self.pk})
