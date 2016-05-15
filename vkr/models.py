from django.db import models

# Create your models here.

class theory(models.Model):
    class Meta():
        db_table = "theory"
    theory_title = models.CharField(max_length = 200)
    theory_text = models.TextField()
    theory_date = models.DateField()
    theory_slug = models.SlugField(max_length= 50, default='default')