from django.urls import path
from wishlist.views import show_wishlist, get_xml, get_json, get_json_by_id, get_xml_by_id, register
from . import views
app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', get_xml, name='get_xml'),
    path('json/', get_json, name='get_json'),
    path('json/<int:id>', get_json_by_id, name='get_json_by_id'),
    path('xml/<int:id>', get_xml_by_id, name='get_xml_by_id'),
    path('register/', register, name="register"),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('ajax/', views.show_wishlist_ajax, name='ajax'),
    path('create/', views.create_wishlist, name="create_wishlist"),
]