from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings

class Page(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    content = RichTextField()
    image = models.ImageField(upload_to='pages/')
    created_at = models.DateTimeField(auto_now_add=True)  # Mantener solo uno
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Referencia al modelo de usuario personalizado
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title
