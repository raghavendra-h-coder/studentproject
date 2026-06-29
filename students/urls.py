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
    path("update-modelform/<int:id>/", views.update_student_modelform, name="update-student-modelform"),
    path("create-department-modelform/", views.create_student_department_modelform, name="create-student-department-modelform"),
    path("update-department-modelform/<int:id>/", views.update_student_department_modelform, name="update-student-department-modelform"),
    path("create-course-modelform/", views.create_student_course_manytomany_modelform, name="create-student-course-modelform"),
    path("update-course-modelform/<int:id>/", views.update_student_course_manytomany_modelform, name="update-student-course-modelform"),
    path("view/many-many/", views.student_course_manytomany_list, name="student-course-mtm-list"),

]