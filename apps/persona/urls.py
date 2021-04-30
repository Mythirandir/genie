from django.urls import path
from . import views
from .views import AddEvents, EventList


urlpatterns = [
    path('signup_persona/', views.register, name='signup_persona'),
    path('login_persona/', views.login_request, name='login_persona'),
    path('persona_admin/', views.persona, name='persona_admin'),
    path('persona_logout/', views.logout_request, name='persona_logout'),
    path('persona_add_event/', AddEvents.as_view(), name='add_event'),
    path('persona_event_list/', EventList.as_view(), name='event_list'),
]
