from django.db import models
from django_prose_editor.fields import ProseEditorField
from django.contrib.auth.models import User
from django.conf import settings


class Page(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = ProseEditorField()
    image = models.ImageField(upload_to='media/pages/')
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
