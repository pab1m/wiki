from django.core.validators import validate_image_file_extension
from django.db import models
from django.contrib.auth.models import User

class Authors(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('ПІБ', max_length=50)
    bio = models.TextField("Біографія")
    photo = models.ImageField(upload_to='authors_img')

    def __str__(self):
        return self.title

class About(models.Model):
    bio = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='about_img')

    def __str__(self):
        return self.bio

