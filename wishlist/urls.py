from django.urls import path
from wishlist.views import show_wishlist, get_xml, get_json

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', get_xml, name='get_xml'),
    path('json/', get_json, name='get_json'),
]