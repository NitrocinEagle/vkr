from django.db import models
from ckeditor.fields import RichTextField


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextField()
    task_text = RichTextField()
    date_published = models.DateField()
    slug = models.SlugField(max_length=50, default='lesson')

    def __str__(self):
        return self.title
