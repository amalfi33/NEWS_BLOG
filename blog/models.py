
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField("Название", max_length=255)
    image = models.ImageField('Картинка', upload_to='category_image/')  
    slug = models.SlugField('Ссылка', unique=True)

    def __str__(self):
        return self.title

    def get_link(self):
        return reverse('category_detail_url', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.post.title + ' ' + self.author.username
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

class Post(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    text = models.TextField('Содержание')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null= True, blank= True)
    image = models.ImageField('Картинка поста', upload_to="post_image/")
    date = models.DateTimeField('Дата создания поста', default=timezone.now)
    slug = models.SlugField('Ссылка', unique=True)
    view = models.IntegerField('Проссмотры', default = 0)
    
    def __str__(self):
        return self.title

    def get_link(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})
    
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'