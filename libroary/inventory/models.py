from django.db import models

class Room(models.Model):
    room_name = models.CharField(max_length=255)

    def __str__(self):
        return self.room_name

class Shelf(models.Model):
    shelf_name = models.CharField(max_length=20)
    room = models.ForeignKey(Room)

    def __str__(self):
        return self.shelf_name + " (" + self.room.room_name + ")"

class Compartment(models.Model):
    shelf = models.ForeignKey(Shelf)
    compartment_name = models.CharField(max_length=20)

    def __str__(self):
        return self.compartment_name + " - " + self.shelf.shelf_name + " (" + self.shelf.room.room_name + ")"

class Tag(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag

class Author(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_birth = models.DateField()
    date_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.last_name

class Language(models.Model):
    language = models.CharField(max_length=255)

    def __str__(self):
        return self.language

class Media(models.Model):
    title = models.CharField(max_length=255)
    author = models.ManyToManyField(Author)
    release_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    location = models.ForeignKey(Compartment)
    description = models.TextField()
    cover = models.ImageField(upload_to="books", null=True, blank=True)

class Genre(models.Model):
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.genre

class Book(Media):
    category = "book"
    language = models.ForeignKey(Language)
    country = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, null=True, blank=True)

    def __str__(self):
        return self.title 
    
class DVD(Media):
    category = "dvd"
    languages = models.ManyToManyField(Language, related_name="audio_lang")
    subtitles = models.ManyToManyField(Language, related_name="sub_lang")
    length_hours = models.IntegerField()
    length_minutes = models.IntegerField()
    length_seconds = models.IntegerField()
    video_format = models.CharField(max_length=10)
    genre = models.ForeignKey(Genre, null=True, blank=True)
    
    def __str__(self):
        return self.title + " (" + self.author.name + " " + self.author.last_name + ")"

class Band(models.Model):
    name = models.CharField(max_length=255)
    foundet = models.DateField()
    disbanded = models.DateField()
    country = models.ForeignKey(Language)

    def __str__(self):
        return self.name

class Interpret(Author):
    band = models.ManyToManyField(Band)

    def __str__(self):
        return self.name + " " + self.last_name + " - " + self.band.name

class Title(models.Model):
    name = models.CharField(max_length=255)
    interpret = models.ForeignKey(Interpret)
    length_hour = models.IntegerField()
    length_minutes = models.IntegerField()
    length_seconds = models.IntegerField()

    def __str__(self):
        return self.name

class Music(Media):
    category = "music"
    languages = models.ManyToManyField(Language)
    media = models.CharField(max_length=30)
    media_tyoe = models.CharField(max_length=30)
    band = models.ForeignKey(Band, null=True, blank=True)
    titles = models.ManyToManyField(Title)

    def __str__(self):
        return self.name + " (" + self.band + ")"

