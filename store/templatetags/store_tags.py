from django import template
from article.models import Category
from store.models import Product

register = template.Library()

def convert_query_to_dict(querydict):
    querydict = dict(querydict.lists())   
    return querydict.items()



register.filter('convert_query_to_dict', convert_query_to_dict)


@register.inclusion_tag('store/store_category_names.html')
def store_category_names():
    cats = Category.objects.all()
    return {'cats':cats}

@register.inclusion_tag('store/product-price-range.html')
def prod_price_range():
    price_field = Product.objects.values_list('price')
    if(price_field):
        min_price = price_field.order_by('price').first()[0]
        max_price = price_field.order_by('-price').first()[0]
    else:
        min_price =0
        max_price=10000

    return {'min':min_price,'max':max_price}