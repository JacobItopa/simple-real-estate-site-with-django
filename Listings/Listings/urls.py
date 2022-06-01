
from django.contrib import admin
from django.urls import path
from Listing.views import listing_list, listing_retrive

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list),
    path('listings/<int:pk>/', listing_retrive),
]
