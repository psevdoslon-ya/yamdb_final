from django.contrib import admin

from .models import Comment, Review, User

admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Review)
