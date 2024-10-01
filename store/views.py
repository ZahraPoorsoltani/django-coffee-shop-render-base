from django.shortcuts import render,get_object_or_404,redirect
from store.models import Product,CartItem
from django.utils import timezone
from django.contrib import messages
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.db.models import Sum

# Create your views here.
def index(request,**kwargs):
    context ={}
    context['order'] = 'most_sale'
    if request.GET:
        prods = Product.objects
        dict_convert = dict(request.GET.lists())
        for key,values in dict_convert.items():
            if key == 'filter[category]':
                prods = prods.filter(status = 1,published_date__lte= timezone.now(),category__name__in = values) 

            elif key == 'filter[cafflevel]':
                prods = prods.filter(status = 1,published_date__lte= timezone.now(),caffein_level__in= values)
            elif key == 'filter[minrange]':
                if isinstance(values,list):
                    value = int(values[0])
                prods = prods.filter(status = 1,published_date__lte= timezone.now(),price__gte=value)
            elif key == 'filter[maxrange]':
                if isinstance(values,list):
                    value = int(values[0])
                prods = prods.filter(status = 1,published_date__lte= timezone.now(),price__lte=value)
               
            elif key == 'filter[available]':
                prods = prods.filter(count_number__gt=0)
            else:
                prods= Product.objects.filter(status = 1,published_date__lte= timezone.now())                       

    elif kwargs.get('order_name')!= None:
        order_val = kwargs['order_name']
        if order_val == 'most_sale':
            context['order'] = 'most_sale'
            product_ids= CartItem.objects.values('product_id').annotate(total_sale= Sum('quantity')).order_by('-total_sale').values_list('product')
            prods = Product.objects.filter(pk__in=product_ids)
            prods |= Product.objects.exclude(pk__in=product_ids)
        elif order_val == 'most_cheap':
            context['order'] = 'most_cheap'
            prods = Product.objects.filter(status = 1,published_date__lte= timezone.now()).order_by('price')
        elif order_val == 'most_expensive':
            prods = Product.objects.filter(status = 1,published_date__lte= timezone.now()).order_by('-price')
            context['order'] = 'most_expensive'
        
    elif kwargs.get('category_name')!= None:
        cat_val = kwargs['category_name']
        prods = Product.objects.filter(status = 1,published_date__lte= timezone.now(),category__name = cat_val) 
    else:
        prods= Product.objects.filter(status = 1,published_date__lte= timezone.now())                       

    try:
        page_number =  request.GET.get('page') 
        paginator = Paginator(prods,4)
        page_obj = paginator.get_page(page_number)   

    except EmptyPage:
        page_obj = paginator.get_page(1) 
    except PageNotAnInteger:
        page_obj = paginator.get_page(1) 
    context["prods"]= page_obj
    return render(request,'store/index.html',context)

def detail(request,**kwargs):
    prod =Product()
    prod_id = kwargs['prod_id']
    prod= get_object_or_404(Product,id=prod_id,status = 1,published_date__lte= timezone.now())
    if  request.method == 'POST':
        if request.user.is_authenticated:  
            quantity = int(request.POST['quantity'])
            if prod.count_number>quantity:
                prod.count_number = prod.count_number-quantity
                prod.save()
                new_cart = CartItem()
                new_cart.user = request.user
                new_cart.product = prod
                new_cart.quantity = quantity 
                new_cart.is_paid = False
                new_cart.save()
                messages.add_message(request,messages.SUCCESS,
                                    'سفارش شما با موفقیت ثبت شد.')
            else:
                messages.add_message(request,messages.ERROR,f"موجودی انبار {prod.count_number} میباشد")
        else:
            messages.add_message(request,messages.ERROR,'لطفا ابتدا وارد حساب کاربری خود شوید.')

        
    
    return render(request, 'store/product-detail.html',{'prod':prod})

def buy_items(request):
    prod = Product()
    prod_id = 0
    try:
        if  request.method == 'POST':
            prod_id = int(request.POST['prod_id'])
            prod = get_object_or_404(Product,id=prod_id)
            
            if request.user.is_authenticated:  
                try:
                    quantity = int(request.POST['quantity'])
                    
                    ##check prod_id
                    if prod:
                        if prod.is_available and prod.status and prod.published_date<=timezone.now():
                            new_cart = CartItem()
                            new_cart.user = request.user
                            new_cart.product = prod
                            new_cart.quantity = quantity 
                            new_cart.is_paid = False
                            new_cart.save()
                            messages.add_message(request,messages.SUCCESS,
                                                'سفارش شما با موفقیت ثبت شد.')
                        else:
                            messages.add_message(request,messages.ERROR,'خطایی رخ داد لطفا دوباره تلاش کنید')
                except:
                    messages.add_message(request,messages.ERROR,'خطایی رخ داد لطفا دوباره تلاش کنید')
        
    except:
        messages.add_message(request,messages.ERROR,'خطایی رخ داد لطفا دوباره تلاش کنید')

    return redirect('store/product-detail.html',{'prod':prod})
    
            