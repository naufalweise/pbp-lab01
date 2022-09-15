from django.urls import path
from wishlist.views import show_wishlist, get_xml, get_json, get_json_by_id

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', get_xml, name='get_xml'),
    path('json/', get_json, name='get_json'),
    path('json/<int:id>', get_json_by_id, name='get_json_by_id')
]