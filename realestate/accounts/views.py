from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login
from .forms import SignUpForm,Loginform
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Listing
from .forms import ListingForm
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin

def listing_detail(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'Viewdetaillist.html', {'listing': listing})
def underconstruction(request):
        return render(request,'underconstruction.html')
# Create your views here.

@login_required
def create_listing(request):
    if request.user.is_authenticated and request.user.is_owner:
        if request.method == 'POST':
            form = ListingForm(request.POST, request.FILES)
            if form.is_valid():
                listing = form.save(commit=False)
                listing.user = request.user
                listing.save()
                return redirect('my_listings')
        else:
            form = ListingForm()
        return render(request, 'user_listing_create.html', {'form': form})
    else:
        return render(request,'errorpage.html')

@login_required
def my_listings(request):
    if request.user.is_authenticated and request.user.is_owner:
        listings = Listing.objects.filter(user=request.user)
        return render(request, 'user_listing.html', {'listings': listings})
    else:
        return render(request,'errorpage.html')

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'Registered successfully'
            return redirect('login_view')
        else:
            messages = 'Form Not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html',{'form':form, 'msg':msg})

def login_view(request):
    form = Loginform(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect("admin")
            elif user is not None and user.is_owner:
                login(request, user)
                return redirect("owner")
            elif user is not None and user.is_tenant:
                login(request, user)
                return redirect("tenant")
            else:
                msg = 'Invalid credentials'
                return redirect('login')
        else:
            msg = 'error'
    return render(request,'login.html',{'form':form, 'msg':msg})

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def owner(request):
    if request.user.is_authenticated and request.user.is_owner:
        return render(request,'owner.html')
    else:
        return render(request,'errorpage.html')
@login_required
def tenant(request):
    if request.user.is_authenticated and request.user.is_tenant:
        return render(request,'tenant.html')
    else:
        return render(request,'errorpage.html')
    

def all_listings(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 9) # 9 listings per page
    page = request.GET.get('page')
    listings = paginator.get_page(page)
    return render(request, 'all_listings.html', {'listings': listings})




    