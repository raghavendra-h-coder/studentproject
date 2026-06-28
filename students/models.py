from django.db import models

#basic model
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    fee = models.IntegerField()

    def __str__(self):
        return self.name

#one to many relationship
"""
with related_name we can access course.students.all()
without related_name we can access student.studentFK_set.all()
"""
class StudentFK(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="students"
    )

    def __str__(self):
        return self.name