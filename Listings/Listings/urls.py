
from django.contrib import admin
from django.urls import path
from Listing.views import listing_list, listing_retrive, listing_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list),
    path('listings/<int:pk>/', listing_retrive),
    path('create/', listing_create),
]
