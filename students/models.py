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
class StudentFK(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name