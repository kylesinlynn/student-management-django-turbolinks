
from django.db import models

import student

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    nrc = models.CharField(max_length=100)
    dob = models.DateField()
    phone = models.CharField(max_length=20)
    CONTACT = (
        ('Yangon', 'Yangon'),
        ('Mandalay', 'Mandalay'),
    )
    contact = models.CharField(max_length=100, choices=CONTACT, default=0)
    
    def __str__(self):
        return self.name

# class Mark(models.Model):
#     student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
#     ac_year = models.CharField(max_length=4)
#     mark1 = models.IntegerField()
#     mark2 = models.IntegerField()
#     mark3 = models.IntegerField()
#     remark = models.TextField(max_length=280)
    
#     def __str__(self):
#         return self.student_id.name

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    dltid = models.CharField(max_length=10)
    year = models.CharField(max_length=4)
    mark = models.IntegerField()
    remark = models.TextField(max_length=280)
    
    def __str__(self):
        return self.student.name