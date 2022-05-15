from unicodedata import category
from django.db import models

# Create your models here.

category_choice = (
    ('Accaracides', 'Accaracides'),
    ('Injectibles', 'Injectibles'),
    ('Salts', 'Salts'),
    ('Dewormers', 'Dewormers'),
    ('Levamisoles', 'Levamisoles'),
    ('Seeds', 'Seeds'),
)


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=True)
    item_name = models.CharField(max_length=50, blank=True, null=True)
    quantity = models.IntegerField(default='0', blank=False, null=True)
    receive_quantity = models.IntegerField(default='0', blank=True, null=True)
    received_from = models.CharField(max_length=30, blank=True, null=True)
    issue_quantity = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)


def __str__(self):
    return self.item_name
