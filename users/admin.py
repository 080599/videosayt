from django.contrib import admin
from content.models import User, Video, Comment

admin.site.register(User)
admin.site.register(Video)
admin.site.register(Comment)