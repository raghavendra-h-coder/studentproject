from django.urls import path
#path() is used to map a URL pattern to a view.
from . import views
#from . import views

urlpatterns = [
    path("home/", views.home),
    path("<int:id>/", views.student_details),
]