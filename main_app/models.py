from django.db import models
from django.contrib.auth.models import User


class Announcer(models.Model):
    ann_name = models.CharField(max_length=250)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.ann_name} {self.user}'

    class Meta:
        ordering = ['ann_name']
        verbose_name = 'Объявитель'
        verbose_name_plural = 'Объявители'


class Category(models.Model):
    cat_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.cat_name}'

    class Meta:
        ordering = ['cat_name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Advert(models.Model):
    adv_name = models.CharField(max_length=200, verbose_name='Заголовок')
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='image/%Y/%m/%d/', blank=True)
    video = models.FileField(upload_to='video/%Y/%m/%d/', blank=True)
    file = models.FileField(upload_to='file/%Y/%m/%d/', blank=True)
    announcer = models.ForeignKey(Announcer, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self) -> str:
        return f'{self.adv_name} - {self.category} by {self.announcer}'


class Reply(models.Model):
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField("Текст ответа")
    created_reply = models.DateTimeField(auto_now_add=True)
    taken = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_reply']
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self) -> str:
        return f'Reply by {self.user} on {self.advert}'