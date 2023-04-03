from django.contrib import admin
from .models import User
from .models import Listing
# Register your models here.
admin.site.register(User)

# Register your models here.
admin.site.register(Listing)


admin.site.site_header = "Paradise Real Estate Admin Login"