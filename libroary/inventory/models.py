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

class Book(Media):
    language = models.ForeignKey(Language)
    country = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)

    def __str__(self):
        return self.title 
    
class DVD(Media):
    languages = models.ManyToManyField(Language, related_name="audio_lang")
    subtitles = models.ManyToManyField(Language, related_name="sub_lang")
    length_hours = models.IntegerField()
    length_minutes = models.IntegerField()
    length_seconds = models.IntegerField()
    video_format = models.CharField(max_length=10)
    
    def __str__(self):
        return self.title + " (" + self.author.name + " " + self.author.last_name + ")"
 

