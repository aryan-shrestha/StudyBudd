from django.urls import path
from .views import getRoom, getRooms, getRoutes

urlpatterns = [
    path('', getRoutes),
    path('rooms/', getRooms),
    path('rooms/<int:pk>', getRoom),
]