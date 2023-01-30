from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter
# from django.contrib.auth.forms import UserCreationForm # -> Django built-in user creation form
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login') # -> We cane use name from urls
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
    
    if request.user.is_authenticated: # -> only not authenticated user can be on this site
        return redirect('/')
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid(): # -> check for User login (similarity etc), password(if long enough, proper signs used etc)
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}')
            return redirect('/login') # -> We cane use name from urls
    else:
        form = CreateUserForm()

    context = {'form': form}

    return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username') # -> username is get from input name tag
        password = request.POST.get('password') # -> password is get from input name tag    
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login') # -> We cane use name from urls
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

@login_required(login_url='/login') # -> We cane use name from urls
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

@login_required(login_url='/login') # -> We cane use name from urls
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

@login_required(login_url='/login') # -> We cane use name from urls
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

@login_required(login_url='/login') # -> We cane use name from urls
def deleteOrder(request, pk):

    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
        
    context = {
        'item': order,
        } 

    return render(request, 'accounts/delete.html', context)