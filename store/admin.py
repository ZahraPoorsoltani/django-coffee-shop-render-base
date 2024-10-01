from django.contrib import admin
from store.models import Product
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class ProductAdmin(SummernoteModelAdmin):
    date_hierarchy ='created_date'
    empty_value_display = 'empty'
    list_display = ('id','title_persian','status','published_date','image')
    summernote_fields = ('content',)


admin.site.register(Product,ProductAdmin)
