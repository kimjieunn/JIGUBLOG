from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils.text import slugify
from .fields import ThumbnailImageField
# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length=50)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL, verbose_name="CATEGORY")
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='간단하게 포스트에 대해 설명해주세요.')
    image = ThumbnailImageField(upload_to = 'photo/%Y/%m', null=True, blank=True)
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now=True)
    tags = TaggableManager(blank=True, help_text='쉼표로 구분해서 작성해주세요.')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="OWNER", blank=True, null=True)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*arg, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="OWNER", blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category_detail', args=(self.id,))

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*arg, **kwargs)


class Site(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = ThumbnailImageField(upload_to = 'photo/%Y/%m', null=True, blank=True)
    url = models.URLField("Site URL")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="OWNER", blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *arg, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*arg, **kwargs)
