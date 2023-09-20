from django.contrib.auth.models import User
from django.db import models

STATUS_CHOICES = (
    ('', 'What is your use of the academy?'),
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    ('author', 'Author'),
)

class User1(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, default='profile.jpg')
    status = models.CharField(
        max_length=150,
        choices=STATUS_CHOICES,
        default='What is your use of the academy?',
    )

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = []