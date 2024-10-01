from django import template
from django.utils import timezone
from article.models import Post
from store.models import CartItem,Product,Category
from django.db.models import Sum

register = template.Library()

@register.inclusion_tag('pending_order.html')
def order_lists(login_user):
    pending_orders = CartItem.objects.filter(user= login_user,is_paid = 'pending')
    total_price = 0
    for item in pending_orders:
        total_price += item.quantity * item.product.price

    return {'orders':pending_orders, 'total_price': total_price}

@register.inclusion_tag('total_order_basket.html')
def total_order_basket(login_user):
    pending_orders = CartItem.objects.filter(user= login_user,is_paid = 'pending').count()
    return{'total_order':pending_orders}

@register.inclusion_tag('newest_order.html')
def newest_order():
    all_products= Product.objects.filter(status = 1,published_date__lte= timezone.now()).order_by('-published_date')[:6]
    return {'prods':all_products}

@register.inclusion_tag('most_sale.html')
def most_sale():
    product_ids= CartItem.objects.values('product_id').annotate(total_sale= Sum('quantity')).order_by('-total_sale').values_list('product')
    prods = Product.objects.filter(pk__in=product_ids)
    prods |= Product.objects.exclude(pk__in=product_ids)[:6]
    return{'prods':prods}

@register.inclusion_tag('store_category.html')
def store_category():
    all_cat = Category.objects.all()
    return {'cats':all_cat}

@register.inclusion_tag('article_category.html')
def article_category():
    all_cat = Category.objects.all()
    return {'cats':all_cat}

@register.inclusion_tag('article_latest.html')
def latest_article():
    posts = Post.objects.filter(status = 1,published_date__lte= timezone.now()).\
        order_by('-published_date')[:4]
    return {'articles':posts}
