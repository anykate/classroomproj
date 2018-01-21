from django.db import models


# Create your models here.
class Student(models.Model):
    student = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.student

    class Meta:
        ordering = '-created_at',


class Subject(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='subjects')
    subject = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = '-created_at',
