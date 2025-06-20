from django.urls import path
from .views import Home,About,Contact,Programmes


urlpatterns = [
    path('', Home.as_view(), name = "home"),
     path('about/',About.as_view(), name = "abouttt"),
     path('contact/', Contact.as_view(), name = "contact"),
     path('programmes/', Programmes.as_view(), name = "programmes"),
     
]
