from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Bool value to distiguish between user types
    is_company = models.BooleanField(default=False)

    # Field for both users
    bio = models.TextField(max_length=400, blank=True)
    is_verified = models.BooleanField(default=True)

    # Fields for Company Accounts
    SECTOR_CHOICES = (
        ('Finance', 'Finance'),
        ('Technology', 'Technology'),
        ('Marketing', 'Marketing'),
        ('Consulting', 'Consulting'),
        ('Engineering', 'Engineering'),
    )
    company_name = models.CharField(max_length=200, blank=True)
    sector = models.CharField(choices=SECTOR_CHOICES,
                              max_length=40, blank=True)
    website = models.URLField(blank=True)

    # Fields for regular Users
    major = models.CharField(max_length=50, blank=True)
    university = models.CharField(max_length=100, blank=True)
