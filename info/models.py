from django.db import models

# Create your models here.

Coun_choices = (
        ('이성영', '이성영'),
        ('정현재', '정현재'),
        ('김현정', '김현정'),
        ('문보라', '문보라'),
        ('박지숙', '박지숙'),
        ('김수미', '김수미'),
        ('강주연', '강주연'),
        ('노미나', '노미나'),
        ('곽은영', '곽은영'))
Gender_choices = (
    ('남자', '남자'),
    ('여자', '여자'))
status_choices = (
    ('진행','진행'),
    ('종결','종결'))

class Client(models.Model):
    name = models.CharField(verbose_name='내담자 이름', max_length=10, unique=True)
    reg = models.DateField(null=True, verbose_name='등록날짜')
    coun = models.CharField(null=True,blank=True, default="", choices=Coun_choices, max_length=3, verbose_name='최초상담자')
    gender = models.CharField(null=True, blank=True, default="", choices=Gender_choices, max_length=2, verbose_name='성별')
    age = models.IntegerField(null=True, blank=True, default=0, verbose_name='연령')
    status = models.CharField(null=True, blank=True, default="", choices=status_choices, max_length=2, verbose_name='진행 상황')
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'client'
        verbose_name = '내담자목록'
        verbose_name_plural = '내담자목록'