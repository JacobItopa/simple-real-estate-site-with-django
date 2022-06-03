
from django.contrib import admin
from django.urls import path
from Listing.views import listing_list, listing_retrive, listing_create, listing_update, listing_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list),
    path('listings/<int:pk>/', listing_retrive),
    path('listings/<int:pk>/update', listing_update),
    path('listings/<int:pk>/delete', listing_delete),
    path('create/', listing_create),
    
]
