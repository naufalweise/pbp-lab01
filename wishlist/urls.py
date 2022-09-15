from django.urls import path
from wishlist.views import show_wishlist, get_xml

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', get_xml, name='get_xml'),
]