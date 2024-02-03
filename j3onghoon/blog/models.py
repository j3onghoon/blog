from django.db import models
from django.db.models import CharField, TextField


class Post(models.Model):
    title = CharField(max_length=100)
    content = TextField()

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = CharField(max_length=100)
