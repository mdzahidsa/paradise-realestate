"""realestate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

from . import views


urlpatterns = [
   
    path('register', views.register,name='register'),
    path('login', views.login_view,name='login_view'),
    path('logout', views.logout,name='logout'),
    path('owner', views.owner,name='owner'),
    path('tenant', views.tenant,name='tenant'),
    path('user_listing_create', views.create_listing,name='create_listing'),
    path('user_listing', views.my_listings,name='my_listings'),
    path('all_listings',views.all_listings, name='all_listings'),
    path('underconstruction',views.underconstruction, name='underconstruction'),
    path('listing_detail/<int:pk>',views.listing_detail, name='listing_detail'),
    
]

