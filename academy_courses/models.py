from django.db import models
from django.core.validators import FileExtensionValidator
from django.conf.global_settings import AUTH_USER_MODEL
from django.utils.translation import gettext as _

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


class Comment(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


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
    

class TransactionStatus(models.IntegerChoices):
    Pending = 0, _('Pending')
    Completed = 1, _('Completed')


class Transaction(models.Model):
    user_id = models.IntegerField()
    course_id = models.IntegerField()
    course = models.CharField(max_length=255)
    amount = models.FloatField()
    customer = models.JSONField(default=dict)
    status = models.IntegerField(
        choices=TransactionStatus.choices, default=TransactionStatus.Pending
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Order(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return str(self.id)
    
    class Meta:
            verbose_name = _('Order')
            verbose_name_plural = _('Orders')
    

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)    
    course = models.CharField(max_length=255)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)