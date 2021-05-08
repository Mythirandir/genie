from django.urls import path
from . import views


urlpatterns = [
    path('signup_persona/', views.register, name='signup_persona'),
    path('login_persona/', views.login_request, name='login_persona'),
    path('persona_admin/', views.persona, name='persona_admin'),
    path('persona_logout/', views.logout_request, name='persona_logout'),
    path('persona_add_event/', views.add_events, name='add_event'),
    path('<int:pk>/', views.view_event, name='view_event'),
    path('update/<int:pk>/', views.update_event, name='update_event'),
    path('<int:pk>/delete', views.delete_event, name='delete_view'),
]
