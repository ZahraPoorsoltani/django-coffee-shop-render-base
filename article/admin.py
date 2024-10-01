from django.contrib import admin
from article.models import Category,Post
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy ='created_date'
    empty_value_display = 'empty'
    list_display = ('id','title','status','published_date','image')
    summernote_fields = ('content',)

admin.site.register(Post,PostAdmin)
admin.site.register(Category)