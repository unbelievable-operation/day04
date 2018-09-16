from django.db import models

# Create your models here.


class StudentInfo(models.Model):
    tel = models.CharField(max_length=11, null=True, unique=True, verbose_name='电话')
    address = models.CharField(max_length=50, null=True, verbose_name='地址')

    class Meta:
        db_table = 'student_info'


class Grade(models.Model):
    g_name = models.CharField(max_length=10, unique=True, verbose_name='班级')

    class Meta:
        db_table = 'grade'


class Course(models.Model):
    c_name = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = 'course'


class Student(models.Model):
    s_name = models.CharField(max_length=10, unique=True, verbose_name='姓名')
    s_age = models.IntegerField(default=16, verbose_name='年龄')
    s_sex = models.BooleanField(default=1, verbose_name='性别')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    operate_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    math = models.DecimalField(max_digits=4, decimal_places=2, null=True, verbose_name='数学')
    chinese = models.DecimalField(max_digits=4, decimal_places=2, null=True, verbose_name='语文')
    stu_info = models.OneToOneField(StudentInfo, null=True, verbose_name='联系方式')
    g = models.ForeignKey(Grade, null=True, on_delete=models.SET_NULL, verbose_name='年级')
    c = models.ManyToManyField(Course, verbose_name='课程', related_name='course')

    class Meta:
        db_table = 'student'

