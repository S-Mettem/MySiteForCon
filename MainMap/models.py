from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    human_name = models.CharField(max_length=50, default=name)
    icon = models.ImageField(upload_to='category/%Y/%m/%d/', max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return str(self.name)


class Sight(models.Model):
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE,
                                 null=True)

    name = models.CharField(max_length=100, default='Sight%d')
    human_name = models.CharField(max_length=50, default=name)
    description = models.TextField(max_length=2000,
                                   default='Описание достопримечательности')

    address = models.CharField(max_length=25, default='Нигде')
    photo = models.ImageField(upload_to='photo_sights/%Y/%m/%d/', max_length=255,
                              default=None)

    web = models.CharField(max_length=75, null=True, blank=True, default=None)
    price = models.IntegerField(default=0)
    longitude = models.CharField(max_length=11, default="00.00000000")
    latitude = models.CharField(max_length=11, default='00.00000000')

    def __str__(self):
        return str(self.name)

