from http import server
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from Listing.views import listing_list, listing_retrive, listing_create, listing_update, listing_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listing_list),
    path('listings/<int:pk>/', listing_retrive),
    path('listings/<int:pk>/update', listing_update),
    path('listings/<int:pk>/delete', listing_delete),
    path('create/', listing_create),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)