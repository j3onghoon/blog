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

    def __str__(self):
        return self.title


class Category(models.Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class Career(models.Model):
    position = CharField(max_length=100)
    company_name = CharField(max_length=100)
    company_link = CharField(max_length=100)
    overview = models.TextField()

    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.company_name


class Work(models.Model):
    career = models.ForeignKey('Career', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WorkDetail(models.Model):
    work = models.ForeignKey('Work', on_delete=models.CASCADE)
    detail = models.TextField()

    def __str__(self):
        return f'{self.work.name}: {self.detail}'


class KeyWord(models.Model):
    name = CharField(max_length=100)

    def __str__(self):
        return self.name


class WorkKeyWord(models.Model):
    work = models.ForeignKey('Work', on_delete=models.CASCADE)
    keyword = models.ForeignKey('KeyWord', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.work.name}: {self.keyword.name}'
