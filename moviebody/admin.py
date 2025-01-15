from django.contrib import admin
from .models import Country, Genre, Year, MovieTag, Movie, Like
from django.db.models import Count

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
    list_display = ('year',)
    search_fields = ('year',)

@admin.register(MovieTag)
class MovieTagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user')
    search_fields = ('movie__title', 'user__username')

    def movie_like_count(self, obj):
        # Like sonini ko'rsatish
        return obj.movie.like_count
    movie_like_count.short_description = "Like soni"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'movie_year', 'language', 'age_limit', 'like_count')  # get_most_liked olib tashlandi
    search_fields = ('title', 'description')
    list_filter = ('country', 'language', 'genres')

    def like_count(self, obj):
        # Like sonini hisoblash
        return obj.like_set.count()
    like_count.short_description = "Like soni"
