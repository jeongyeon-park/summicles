from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.TextField(verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    summary = models.TextField(verbose_name='요약')
    Tag = models.CharField(max_length=128, verbose_name='태그')
    # img = models.ImageField()
    date = models.DateField(auto_now_add=True, verbose_name='등록날짜')

    class Meta:
        db_table = 'article'
        verbose_name = '기사'
        verbose_name_plural = '기사'
