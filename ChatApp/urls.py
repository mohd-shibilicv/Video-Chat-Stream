from django.urls import path
from . import views


urlpatterns = [
    path('', views.lobby, name = 'lobby'),
    path('room/', views.room, name = 'room'),
    path('get_token/', views.getToken, name = 'get-token'),
    path('create_member/', views.createMember, name = 'create-member'),
    path('get_member/', views.getMember, name = 'get-member'),
    path('delete_member/', views.deleteMember, name = 'delete-member'),
]