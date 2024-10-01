from django import template
from django.utils import timezone
from article.models import Post,Category

register = template.Library()



def convert_query_to_dict(querydict):
    querydict = dict(querydict.lists())   
    return querydict.items()



register.filter('convert_query_to_dict', convert_query_to_dict)

@register.inclusion_tag('article/newest_article.html')
def newest_article():
     posts = Post.objects.filter(status=1,published_date__lte= timezone.now()
                                      ).order_by('-published_date')[:5]
     return {'posts':posts}



@register.inclusion_tag('article/article_category.html')
def article_category_cnt():
    posts = Post.objects.filter(status=1,published_date__lte= timezone.now())
    cats = Category.objects.all()
    cat_dict = {}
    for cat in cats:
        cnt_post = posts.filter(category=cat).count()
        cat_dict[cat.name]=cnt_post

    return {'cats':cat_dict}

@register.inclusion_tag('article/article_category_names.html')
def article_category_names():
    cats = Category.objects.all()
    return {'cats':cats}

