from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

ACTIVE_CHOICES = (
    ("", "Select status"),
    ("active", "Active"),
    (" ", "Inactive"),
)


SOCIAL_MEDIA_ICONS = [
    ("", "Select an icon"),
    ("fa-facebook", "Facebook"),
    ("fa-twitter", "Twitter"),
    ("fa-instagram", "Instagram"),
    ("fa-linkedin", "LinkedIn"),
    ("fa-youtube", "YouTube"),
    ("fa-pinterest", "Pinterest"),
    ("fa-tumblr", "Tumblr"),
    ("fa-flickr", "Flickr"),
    ("fa-github", "GitHub"),
    ("fa-bitbucket", "Bitbucket"),
    ("fa-gitlab", "GitLab"),
    ("fa-stack-overflow", "Stack Overflow"),
    ("fa-medium", "Medium"),
    ("fa-reddit", "Reddit"),
    ("fa-whatsapp", "WhatsApp"),
    ("fa-skype", "Skype"),
]



class Course(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=5000)
    price = models.FloatField()
    hour = models.IntegerField()
    min = models.IntegerField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Video(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=1000)
    video = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['mov','avi','mp4','webm','mkv', 'wmv', 'ogg'])])
    created_at = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Opinion(models.Model):
    name = models.CharField(max_length=50)
    career = models.CharField(max_length=100)
    image = models.ImageField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class New(models.Model):
    subject = models.CharField(max_length=70)
    message = models.TextField(max_length=5000)


class Slider(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    is_active = models.CharField(
        max_length=50,
        choices=ACTIVE_CHOICES,
        default='Select status',
    )

class Urls(models.Model):
    title = models.CharField(max_length=30, default="My Urls")
    icon = models.CharField(
        default='Select an icon',
        choices=SOCIAL_MEDIA_ICONS,
        max_length=100
    )
    url = models.URLField()

    def __str__(self):
        return self.title