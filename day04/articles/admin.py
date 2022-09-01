from django.contrib import admin
from .models import Article
# Register your models here.

# 가장 기본적으로 추가하는 방법
# admin.site.register(Article)

# 응용편
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'updated_at']
    list_display_links = ['id', 'title']

admin.site.register(Article, ArticleAdmin)