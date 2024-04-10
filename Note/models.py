from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.db.models import Q
from django.utils.text import slugify

# Create your models here.
class Note(models.Model):
    owner = models.ForeignKey(get_user_model(), related_name="notes", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length= 400)
    body = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # this_note = Note.objects.filter(Q(slug = self.slug) & Q(owner = self.owner) ).exists()

        # if not this_note:
        #     self.slug = slugify(self.title)

        # if this_note:
        #    self.slug = self.slug + "-1"
        super(Note, self).save(*args, **kwargs) 
    
    def get_absolute_url(self):
        return reverse('view_note', kwargs={'username': self.owner.get_username(), 'slug': self.slug})

    class Meta:
        ordering = ('-date_created', '-date_updated')

