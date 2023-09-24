from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, default='academy_courses/static/profile.jpg')
    courses = models.JSONField(null=True)

    def __str__(self):
        return self.user.username