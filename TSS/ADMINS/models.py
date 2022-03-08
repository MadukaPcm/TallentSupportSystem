from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User,Group
from django.utils.translation import gettext as _

# Create your models here.
class Role(Group):
    class Meta:
        proxy = True
        app_label = 'auth'
        verbose_name = _('Role')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True)
    image = models.FileField(upload_to='uploads/profile', validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg'])])
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username

class Tallent(models.Model):
    name = models.CharField(max_length=20,null=True,blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    un_deleted = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True,null=True)
    Tallent = models.ForeignKey(Tallent, on_delete=models.CASCADE, blank=True,null=True)

    artist_name= models.CharField(max_length=20,null=False,blank=False, unique=True)
    sex = models.CharField(max_length=8,null=False,blank=False)
    phone = models.CharField(max_length=10,null=False,blank=False, unique=True)
    region = models.CharField(max_length=20,null=False,blank=False)
    district = models.CharField(max_length=20,null=False,blank=False)
    street = models.CharField(max_length=20,null=False,blank=False, unique=True)
    office_name = models.CharField(max_length=20,null=False,blank=False)
    date_added = models.DateField(auto_now_add=True)
    un_deleted = models.BooleanField(default=True)

    def __str__(self):
        return self.artist_name

class Media(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    title = models.CharField(max_length=30,null=False,blank=False)
    description = models.TextField(max_length=1024*2)
    video_file = models.FileField(upload_to='uploads/videos',
                 validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
    thumbnail = models.FileField(upload_to='uploads/images', 
                validators=[FileExtensionValidator(allowed_extensions=['png','jpg','jpeg'])])
    date_created = models.DateField(auto_now_add=True)
    un_deleted = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Follower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True,null=True)
    Media = models.ManyToManyField(Media)

    phone = models.CharField(max_length=15,null=False,blank=False,unique=True)
    status = models.BooleanField(default=True)
    follow_date = models.DateField(auto_now_add=True)
    un_deleted = models.BooleanField(default=True)

    def __str__(self):
        return self.phone 

