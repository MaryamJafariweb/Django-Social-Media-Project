from django.contrib import admin
from .models import Post, Comment, Vote
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'slug', 'create')
    list_filter = ('create', 'update')
    prepopulated_fields = {'slug': ('body',)}
    search_fields = ('slug',)
    raw_id_fields = ('user',)


admin.site.register(Post, PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'create', 'is_reply')
    raw_id_fields = ('user', 'post', 'reply')


admin.site.register(Vote)
