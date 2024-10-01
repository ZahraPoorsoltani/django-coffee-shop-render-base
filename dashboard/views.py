from django.shortcuts import render
from store.models import CartItem
from django.db.models import Sum,Count
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    context ={}
    if request.user.is_authenticated:
        all_orders = CartItem.objects.filter(user=request.user)
        context['all_orders']=all_orders
        paid_order = all_orders.filter(is_paid = 'paid')
        paid_status = all_orders.values('is_paid').annotate(dcount=Count('is_paid'))
        total_paid = 0
        for item in paid_order:
            total_paid += item.total_price
        context['total_paid']=total_paid
        context['num_order']= paid_status.filter(is_paid='paid')[0]['dcount']
        context['paid_status']= paid_status
    return render(request,'dashboard/index.html',context)

@login_required
def edit_profile(request):
    return render(request,'dashboard/profile-edit.html')