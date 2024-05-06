from django.db import models
from django.db.models import CharField, TextField


class Post(models.Model):
    title = CharField(max_length=100)
    content = TextField()

    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    # todo
    # updated 에 index 적용하는 것 생각해보기
    updated = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = CharField(max_length=100)


class Career(models.Model):
    position = CharField(max_length=100)
    company_name = CharField(max_length=100)
    company_link = CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)


class Work(models.Model):
    career = models.ForeignKey('Career', on_delete=models.CASCADE)
    overview = models.CharField(max_length=100)


class WorkDetail(models.Model):
    work = models.ForeignKey('Work', on_delete=models.CASCADE)
    detail = models.TextField()


class WorkKeyWord(models.Model):
    work = models.ForeignKey('Work', on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100)
