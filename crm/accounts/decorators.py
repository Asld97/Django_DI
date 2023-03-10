from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func): # view_func -> decorated function
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated: # -> only not authenticated user can be on this site
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name             
            if group in allowed_roles:                
                return view_func(request, *args, **kwargs)
            else:
                return redirect('crm-login')
                # return HttpResponse('You are not authorized to view this page !!!!')
            
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        if group == 'customer':
            return redirect('crm-user-page')
        
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        
        
    return wrapper_func
