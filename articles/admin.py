from django.contrib import admin
from .models import article,Comment
# Register your models here.

class CommentInline(admin.StackedInline): # new
    model = Comment
class ArticleAdmin(admin.ModelAdmin): # new
    inlines = [
        CommentInline,
    ]
admin.site.register(article,ArticleAdmin)
admin.site.register(Comment)