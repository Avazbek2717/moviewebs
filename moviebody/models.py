from django.db import models
from django.db.models import Count


from django.db import models
from user.models import BaseModel, User  # BaseModel va User import qilinadi


class Country(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Genre(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Year(BaseModel):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)


class MovieTag(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(BaseModel):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/')
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    language = models.CharField(max_length=50, choices=[('EN', 'English'), ('UZ', 'Uzbek')])
    age_limit = models.IntegerField()
    duration = models.DurationField()
    genres = models.ManyToManyField(Genre)
    movie_year = models.ForeignKey(Year, on_delete=models.CASCADE)
    description = models.TextField()
    file = models.FileField(upload_to='movies/')
    movie_tag = models.ManyToManyField(MovieTag)

    @property
    def like_count(self):
        # Har bir film uchun like sonini hisoblash
        return self.like_set.count()
    
    @classmethod
    def most_liked_movies(cls):
        # Eng ko'p like bo'lgan kinolarni olish
        return cls.objects.annotate(num_likes=Count('like')).order_by('-num_likes')

    def __str__(self):
        return self.title

    def __str__(self):
        return self.title

class Like(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} likes {self.movie.title}"
