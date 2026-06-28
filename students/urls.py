from django.urls import path
#path() is used to map a URL pattern to a view.
from . import views

urlpatterns = [
    path("home_basic/", views.home),
    path("<int:id>/", views.student_details),
    path("context-filters/<int:id>/", views.student_details_filters_context),
    path("profile/", views.student_profile),
    path("courses/<str:feature_name>", views.course_details_feature_name),
    path("create/", views.create_student, name="create-student"),
    path("view/", views.student_list, name="student-list"),
    path("update/<int:id>/", views.update_student, name="update-student"),
    path("delete/<int:id>/", views.delete_student, name="delete-student"),
    path("home/", views.student_home, name="student-home"),
    path("create-form/", views.create_student_form,name="create-student-form"),
    path("create-modelform/", views.create_student_modelform, name="create-student-modelform"),
    path("update-modelform/<int:id>/", views.update_student_modelform, name="update-student-modelform")
]