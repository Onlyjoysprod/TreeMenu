from django.db import models
from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(max_length=125, unique=True, verbose_name='Menu title')

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=125, verbose_name='Item title')
    menu = models.ForeignKey(Menu, blank=True, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='childrens', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'

    def get_absolute_url(self):
        return reverse('item_detail', args=[str(self.id)])

    def __str__(self):
        return self.title
