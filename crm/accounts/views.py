from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm
from .filters import OrderFilter

def home(request):
    customers = Customer.objects.all()
    orders = Order.objects.all().order_by('-id')

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()
    
    context = {
        'customers': customers,
        'orders': orders,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'delivered': delivered,
        'pending': pending,

         }

    return render(request, 'accounts/dashboard.html', context)

def registerPage(request):
    context = {}
    return render(request, 'accounts/register.html', context)

def loginPage(request):
    context = {}
    return render(request, 'accounts/login.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

def customer(request, pk):
    customer = Customer.objects.get(id=pk)

    orders = customer.order_set.all()
    orders_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {
        'customer': customer,
        'orders': orders,
        'orders_count': orders_count,
        'myFilter': myFilter,
        
    }

    return render(request, 'accounts/customer.html', context)

def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)    
    # form = OrderForm(initial={'customer': customer})
    if request.method == 'POST':        
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save() # Saving to Database
            return redirect('/')

    context = {
        'formset': formset,        
        } 

    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):

    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':        
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save() # Saving to Database
            return redirect('/')

    context = {
        'form': form,
        } 

    return render(request, 'accounts/update_form.html', context)

def deleteOrder(request, pk):

    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
        
    context = {
        'item': order,
        } 

    return render(request, 'accounts/delete.html', context)