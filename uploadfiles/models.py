from django.db import models

# Create your models here.
class Article(models.Model):
    file_obj = models.FileField(upload_to='files/', verbose_name='Файл')