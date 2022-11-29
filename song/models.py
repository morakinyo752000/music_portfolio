from django.db import models

# Create your models here.

class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to='media')
    title = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True, upload_to='media')
    description = models.TextField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
