from django.db import models


class SearchData(models.Model):
    
    keywords = models.CharField(
        max_length=100,
        verbose_name='ключевые слова'
        )
    class Meta:
        ordering = ('keywords',)
        verbose_name = 'ключевое слово'
        verbose_name_plural = 'ключевые слова'

    def __str__(self):
        return self.keywords

    
class UserInfo(models.Model):
    
    search_data = models.ForeignKey(
        SearchData, 
        on_delete= models.CASCADE
        )
    
    url = models.CharField(
        max_length=50,
        verbose_name='ссылка'
        )
    avatar_url = models.CharField(
        max_length=50, 
        verbose_name='ссылка на аватарку',
        default='отсутсвует'
        )
    name = models.CharField(
        max_length=50,
        verbose_name='имя пользователя'
        )
    full_name = models.CharField(
        max_length=50,
        verbose_name='полное имя пользователя'
        )
    bio = models.TextField(
        max_length=300,
        verbose_name='bio',
        default='отсутсвует'
        )
    tags = models.TextField(
        max_length=3000, 
        verbose_name='подписки',
        default='отсутсвует'
        )
    phone = models.CharField(
        max_length=50,
        verbose_name='номер телефона, если есть',
        default='отсутсвует'
        )
    link = models.CharField(
        max_length=50,
        verbose_name='ссылка на сайт,если есть',
        default='отсутсвует'
        )
    posts = models.IntegerField(
        verbose_name='количество постов',
        default='отсутсвует'
        )
    count_followers = models.IntegerField(
        verbose_name='количество подписчиков',
        default='отсутсвует'
        )
    followers = models.TextField(
        max_length=3000, 
        verbose_name='подписчики',
        default='отсутсвует'
        )
    count_following = models.IntegerField(
        verbose_name='количество подписок',
        default='отсутсвует'
        )
    folowing = models.TextField(
        max_length=3000, 
        verbose_name='подписки',
        default='отсутсвует'
        )
    user_id = models.CharField(
        max_length=50,
        verbose_name='id'
        )
    class Meta:
        verbose_name = 'Информация пользователя'
        verbose_name_plural = 'Информация пользователей'

    def __str__(self):
        return self.full_name
    
    