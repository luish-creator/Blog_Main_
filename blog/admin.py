# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import post, category, Comment


class ComentItemInline(admin.TabularInline):
      model = Comment
      raw_id_fields = ['post']


class PostAdmin(admin.ModelAdmin):
      search_fields = ['title','intrp','body']
      list_display = ('title','category','created_at','status')
      list_filter = ['category','created_at','status']
      inlines = [ComentItemInline]


class CategoryAdmin(admin.ModelAdmin):
      search_fields = ['title']
      list_display = ('title',)


class CommentAdmin(admin.ModelAdmin):
      search_fields = ('name','post','created_ad',)


admin.site.register(post,PostAdmin)
admin.site.register(category,CategoryAdmin)
admin.site.register(Comment,CommentAdmin)