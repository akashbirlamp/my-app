from django.db import models

# create models

#id is a primary key by default create

class Movie(models.Model):                  #program m class name movie or database m table name movie rhega
    actor = models.CharField(max_length=30)   # varible name or table in coloum name rhega
    actor_movies = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    movie_logo = models.CharField(max_length=100)

    def __str__(self):
        return self.actor + '---' +self.actor_movies


class Song(models.Model):
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE) #on_delet mtlb primary table se movie delet kre toh foreinkey se bhi delet ho jaye
    file_type = models.CharField(max_length=50)
    song_name = models.CharField(max_length=100)