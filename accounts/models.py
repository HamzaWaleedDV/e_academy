from django.contrib.auth.models import User
from django.db import models

STATUS_CHOICES = (
    ('', 'What is your use of the academy?'),
    ('student', 'Student'),
    ('teacher', 'Teacher'),
    ('author', 'Author'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, default='profile.jpg')
    status = models.CharField(
        max_length=150,
        choices=STATUS_CHOICES,
        default='What is your use of the academy?',
    )

    USERNAME_FIELD = 'user__username'

    def __str__(self):
        return self.user.username