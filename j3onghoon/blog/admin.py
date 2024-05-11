from django.contrib import admin

from .models import Post, Work, WorkDetail, WorkKeyWord, Career, KeyWord

admin.site.register(Post)
admin.site.register(Career)
admin.site.register(Work)
admin.site.register(WorkDetail)
admin.site.register(WorkKeyWord)
admin.site.register(KeyWord)
