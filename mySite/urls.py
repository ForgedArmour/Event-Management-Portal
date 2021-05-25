
from django.urls import path
from mySite import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("signup", views.signup, name='signup'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("profile", views.profile, name='profile'),
    path("handleCreateEvent", views.handleCreateEvent, name='handleCreateEvent'),
    path("error", views.error, name='error'),
    path("createEvent", views.createEvent, name='createEvent'),
    path("eventregister/<int:myid>", views.eventview, name='viewevent'),
    path("regevents", views.regevents, name='regevents')
    
]