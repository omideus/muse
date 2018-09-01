from django.db import models

# Create your models here.


class MuseumObject(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان شیء')
    ded_id = models.IntegerField(verbose_name='شناسه شیء')
    description = models.TextField(verbose_name='توضیحات مربوط به شیء')
    image = models.ImageField(upload_to='media/object-image', verbose_name='تصویر شیء')

    def __str__(self):
        return self.title
