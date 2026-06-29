
# Register your models here.
from django.contrib import admin
from .models import Student, StudentFK, Course, Department, CourseMany


# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    #list_display used to display the columns in the grid
    list_display = (
        "id",
        "name",
        "age",
        "course",
    )

    #search_fields adds up a search bar, upon entering a value, it searhes in the defined columns only
    search_fields = (
        "name",
        "course",
    )

    #we can filter out the records with all distinct values of course column
    list_filter = (
        "course",
    )

    #only sorting is made available on id column, by default its desc - means desc
    ordering = (
        "-id",
    )

@admin.register(StudentFK)
class StudentFKAdmin(admin.ModelAdmin):

    #list_display used to display the columns in the grid
    list_display = (
        "id",
        "name",
        "age",
        "course",
    )

    #search_fields adds up a search bar, upon entering a value, it searhes in the defined columns only
    search_fields = (
        "name",
        "course",
    )

    #we can filter out the records with all distinct values of course column
    list_filter = (
        "course",
    )

    #only sorting is made available on id column, by default its desc - means desc
    ordering = (
        "-id",
    )

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    #list_display used to display the columns in the grid
    list_display = (
        "id",
        "name",
        "duration",
        "fee",
    )

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(CourseMany)
class CourseManyAdmin(admin.ModelAdmin):
    pass
