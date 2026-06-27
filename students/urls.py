from django.urls import path
#path() is used to map a URL pattern to a view.
from . import views

urlpatterns = [
    path("home/", views.home),
    path("<int:id>/", views.student_details),
    path("context-filters/<int:id>/", views.student_details_filters_context),
    path("profile/", views.student_profile),
    path("courses/", views.course_details),
    path("courses-with-extend/", views.course_details_with_extend),
]