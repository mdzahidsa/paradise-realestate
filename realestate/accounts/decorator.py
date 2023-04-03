from django.shortcuts import redirect

def user_not_authenticated(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Redirect to some URL if user is authenticated
            return redirect('errorpage')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func