from django.urls import path
from . import views
urlpatterns = [
    path('abc/',views.abc, name= 'abc'),
    path('mnb/',views.mnb, name= 'mnb'),
]

