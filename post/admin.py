from django.contrib import admin
from .models import Post, PostView,Category, Comment,Author

# Register your models here.

admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Author)