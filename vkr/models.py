from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class theory(models.Model):
    class Meta():
        db_table = "theory"
    theory_title = models.CharField(max_length = 200)
    theory_text = RichTextField()
    theory_date = models.DateField()
    #theory_slug = models.SlugField(max_length= 50, default='default')
    def __unicode__(self):
        return self.theory_title
