from django.contrib import admin
from frontend.models import *
# Register your models here.

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Index

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass    

@admin.register(LatestBlog)
class LatestBlogAdmin(admin.ModelAdmin):
    pass

@admin.register(AboutUs)
class AboutUs(admin.ModelAdmin):
    pass

@admin.register(Aboutusimage)
class AboutUsImg(admin.ModelAdmin):
    pass

@admin.register(blog)
class Blog(admin.ModelAdmin):
    pass

@admin.register(contact)
class Contact(admin.ModelAdmin):
    pass

@admin.register(id)
class Id(admin.ModelAdmin):
    pass

@admin.register(Category)
class Categories(admin.ModelAdmin):
    pass