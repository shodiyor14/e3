from django.db import models

class Watches(models.Model):
    title = models.CharField(max_length=333)
    description = models.TextField()
    price = models.CharField(max_length=777)
    data = models.DateTimeField(auto_created=True)
    image = models.ImageField(upload_to='media')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'watch'
        verbose_name_plural = 'watches'


