from . import views
from django.urls import path

urlpatterns = [
    path('log/', views.log_session, name='log-session'),
    path('mysessions/', views.user_session_list, name='user-sessions'),
    path('', views.SessionList.as_view(), name='home'),
]