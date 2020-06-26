from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Bool value to distiguish between user types
    is_company = models.BooleanField(default=False)
    is_regular_user = models.BooleanField(default=False)

    # Field for both users
    bio = models.TextField(max_length=400, blank=True)

    # Fields for Company Accounts
    SECTOR_CHOICES = (
        (1, 'Finance'),
        (2, 'Technology'),
        (3, 'Marketing'),
        (4, 'Consulting'),
        (5, 'Engineering'),
    )
    company_name = models.CharField(max_length=200)
    sector = models.CharField(choices=SECTOR_CHOICES,
                              max_length=40)

    # Fields for regular Users
    major = models.CharField(max_length=50, blank=True)
    university = models.CharField(max_length=100, blank=True)
