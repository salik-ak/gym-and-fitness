from django.db import models

# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()

    def __str__(self):
         return self.course_name


class Trainers(models.Model):
    trainers_name = models.CharField(max_length=255)
    trainers_spec = models.CharField(max_length=255)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    trainers_image = models.ImageField(upload_to='trainers')

    def __str__(self):
         return 'Mr.' + self.trainers_name + ' - (' + self.trainers_spec + ')'


class Admissions(models.Model):
    s_name = models.CharField(max_length=255)
    s_phone = models.CharField(max_length=10)
    s_email = models.EmailField()
    trainers_name = models.ForeignKey(Trainers, on_delete=models.CASCADE)
    admission_date = models.DateField()
    started_on = models.DateField(auto_now=True)
