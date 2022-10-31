from pydoc_data.topics import topics
from django.urls import path
from .views import (
                    activitiesPage, createRoom, deleteMessage, deleteRoom, home, 
                    loginPage, room, topicsPage, updateRoom, 
                    deleteRoom, logoutUser, registerPage, updateUser, userProfile)


urlpatterns = [
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name="logout"),
    path('register/', registerPage, name='register'),
    path('profile/<str:pk>/', userProfile, name='user_profile'),
    path('', home, name="home"),
    path('room/<int:pk>', room, name="room"),
    path('create-room/', createRoom, name="create_room"),
    path('update-room/<int:pk>', updateRoom, name="update_room"),
    path('delete-room/<int:pk>', deleteRoom, name="delete_room"),
    path('delete-message/<int:pk>', deleteMessage, name='delete_message'),
    path('update-user/', updateUser, name="update_user"),
    path('topics/', topicsPage, name="topics"),
    path('activity/', activitiesPage, name="activities"),
]