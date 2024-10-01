from django.shortcuts import render,get_object_or_404
from article.models import Post
from django.utils import timezone
from datetime import timedelta

from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.
def index(request,**kwargs):
    posts = Post.objects

    if request.GET:
        cat_item = []
        date_item = {'today':0,'yesterday':0}

        today = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
        yesterday = today-timedelta(hours=24)
        date_item_convert = {'today': today,
                             'yesterday':yesterday}
        

        dict_convert = dict(request.GET.lists())
        for key,values in dict_convert.items():
            if key == 'filter[category]':
                posts = Post.objects.filter(status = 1,published_date__lte= timezone.now(),
                                            category__name__in = values) 
            elif key == 'filter[date][0]':
                date_item['today'] =1
            elif key == 'filter[date][1]':
                date_item['yesterday'] =1

        if cat_item:
            posts = posts.filter(status = 1,published_date__lte= timezone.now(),
                                   category__name__in = cat_item)

        
        if date_item['today'] and date_item['yesterday']:
            posts = posts.filter(status = 1,published_date__range= (date_item_convert['yesterday'],
                                                                   timezone.now()),)
        elif date_item['today']:
            posts = posts.filter(status = 1,published_date__range= (date_item_convert['today'],
                                                                    timezone.now()),)
        elif date_item['yesterday']:
            posts = posts.filter(status = 1,published_date__range= (date_item_convert['yesterday'],
                                                                    date_item_convert['today']),)


    if kwargs.get('cat_name')!=None:
        cat_name = kwargs['cat_name']
        posts = posts.filter(status = 1,published_date__lte= timezone.now(),
                                   category__name = cat_name) 
        
    else:
        posts = posts.filter(status = 1,published_date__lte= timezone.now()).order_by('-published_date')
    
    my_filter = {}
    if kwargs.get('order_name')!=None:
        order_name = kwargs['order_name']
        if order_name == 'newest':
            my_filter['order'] = 'newest'
            posts = posts.order_by('-published_date')
        elif order_name=='most_viewed':
            my_filter['order'] = 'most_viewed'
            posts = posts.order_by('-counted_view')


    try:
        page_number =  request.GET.get('page')        
        paginator = Paginator(posts,3)
        page_obj = paginator.get_page(page_number)   

    except EmptyPage:
        page_obj = paginator.get_page(1) 
    except PageNotAnInteger:
        page_obj = paginator.get_page(1) 

    return render(request,'article/index.html',{'posts':page_obj,'my_filter':my_filter})

def detail(request,**kwargs):
    post=Post()
    if kwargs.get('post_id')!=None:
        post_id = kwargs['post_id']
        post = get_object_or_404(Post,id=post_id,status = 1,published_date__lte= timezone.now())
        cnt =post.counted_view 
        post.counted_view = cnt+1
        post.save()


        prev_post = Post.objects.filter(id__lt=post_id,status=1,published_date__lte= timezone.now()
                                 ).order_by('-id')
    
        next_post = Post.objects.filter(id__gt=post_id,status=1,published_date__lte= timezone.now()
                                 ).order_by('id')
    

        if len(prev_post):
            prev_post = prev_post[0]

        if len(next_post):
            next_post = next_post[0]
    
    return render(request,'article/article-details.html',{'post':post,
                                                          'prev_post':prev_post,'next_post':next_post})