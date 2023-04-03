from django.shortcuts import render
from accounts.models import Listing
from django.core.paginator import Paginator

# Create your views here.

def index(request):

    listings = Listing.objects.all()
    paginator = Paginator(listings, 3) # 3 listings per page
    page = request.GET.get('page')
    listings = paginator.get_page(page)
    return render(request, "index.html", {'listings' : listings})