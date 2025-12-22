from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='標題')
    slug = models.CharField(max_length=200, verbose_name='網址標識')
    body = models.TextField(verbose_name='文章內容')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='發佈日期')

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = '文章'
        verbose_name_plural = '文章列表'

    def __str__(self):
        return self.title