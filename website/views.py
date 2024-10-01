from django.shortcuts import render
from store.models import CartItem
# Create your views here.
def index(request):
    context = {}
    if request.user.is_authenticated:
        pending_orders = CartItem.objects.filter(user= request.user,is_paid = 'pending')
        total_price = 0
        for item in pending_orders:
            total_price += item.quantity * item.product.price
        total_order = pending_orders.count()
        context['total_price'] = total_price
        context['total_order'] = total_order
        context['orders'] = pending_orders
        
    return render(request,'index.html',context)

def handler404(request, exception, template_name="404.html"):
    return render(request,'404.html',status=404)

def handler500(request,*args, **argv):
    return render(request,'500.html',status=500)
