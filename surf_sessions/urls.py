from . import views
from django.urls import path

urlpatterns = [
    path('log/', views.log_session, name='log-session'),
    path('session/delete/<int:session_id>/', views.delete_session, name='delete-session'),
    path('edit/<int:session_id>/', views.edit_session, name='edit-session'),
    path('mysessions/', views.MySessionList.as_view(), name='my-sessions'),
    path('', views.SessionList.as_view(), name='home'),
]