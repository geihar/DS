from django.db import models
from datetime import date
from django.urls import reverse

class Category(models.Model):
    name = models.CharField('Категории', max_length=120)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Actor(models.Model):
    name = models.CharField('Имя', max_length=120)
    age = models.PositiveIntegerField('Возраст', default=0)
    description = models.TextField()
    image = models.ImageField('Изображеие', upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Актеры и Режисеры'
        verbose_name_plural = 'Актеры и Режисеры'


class Genre(models.Model):
    name = models.CharField('Имя', max_length=120)
    description = models.TextField('Описание')
    url = models.SlugField(max_length=120, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    title = models.CharField('Имя', max_length=120)
    tagline = models.CharField('Слоган', max_length=100, default='')
    description = models.TextField('Описание')
    poster = models.ImageField('Изображеие', upload_to='movies/')
    year = models.PositiveIntegerField('Дата выхода', default=2020)
    country = models.CharField('Страна', max_length=30)
    director = models.ManyToManyField(Actor, verbose_name='Режисер', related_name='film_director')
    actor = models.ManyToManyField(Actor, verbose_name='Актеры', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры')
    world_premiere = models.DateField('Премьера в мире', default=date.today)
    budget = models.PositiveIntegerField('Бюджет', default=0,  help_text='Указан в долларах')
    fees_in_usa = models.PositiveIntegerField('Сборы в США', default=0,  help_text='Указан в долларах')
    fees_in_world = models.PositiveIntegerField('Сборы в Мире', default=0,  help_text='Указан в долларах')
    category = models.ForeignKey(Category, verbose_name='Каткгории', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=120, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie_detail', kwargs={'slug': self.url})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class MoviesShots(models.Model):
    name = models.CharField('Заголовок', max_length=120)
    description = models.TextField('Описание')
    image = models.ImageField('Изображеие', upload_to='movies_shots/')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кадры из фильма'
        verbose_name_plural = 'Кадры из фильма'


class RatingStars(models.Model):
    value = models.PositiveSmallIntegerField('Значение', default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Звезды рейтинга'
        verbose_name_plural = 'Звезды рейтинга'


class Rating(models.Model):
    ip = models.CharField('IP адресс', max_length=15)
    star = models.ForeignKey(RatingStars, on_delete=models.CASCADE, verbose_name='звезда')
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=120)
    text = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, verbose_name='Фильм', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
