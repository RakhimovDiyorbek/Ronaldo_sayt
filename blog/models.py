from django.db import models

# Create your models here.


class Index(models.Model):
    title = models.TextField()
    image = models.ImageField(upload_to='about_rasm/')
    name = models.CharField(max_length=222)
    date_bith = models.CharField(max_length=222)
    adress = models.CharField(max_length=222)
    email = models.EmailField()
    phone = models.CharField(max_length=222)

    def __str__(self):
        return self.name


class Educations(models.Model):
    year = models.CharField(max_length=222)
    name = models.CharField(max_length=222)
    university = models.CharField(max_length=222)
    body = models.TextField()

    def __str__(self):
        return self.name


class Experience(models.Model):
    year = models.CharField(max_length=222)
    position = models.CharField(max_length=222)
    university = models.CharField(max_length=222)
    body = models.TextField()

    def __str__(self):
        return self.position




class Skill(models.Model):
    name = models.CharField(max_length=222)
    foiz = models.CharField(max_length=222)
    last_week = models.CharField(max_length=222)
    last_month = models.CharField(max_length=222)

    def __str__(self):
         return self.name


class Dasturlash(models.Model):
    Photoshop = models.CharField(max_length=222)
    jQuery = models.CharField(max_length=222)
    HTML5 = models.CharField(max_length=222)
    CSS3 = models.CharField(max_length=222)
    WordPress = models.CharField(max_length=222)
    SEO = models.CharField(max_length=222)


    def __str__(self):
       return self.Photoshop



class Awards(models.Model):
    title = models.CharField(max_length=222)
    body = models.CharField(max_length=222)
    description = models.TextField()
    yil = models.CharField(max_length=222)

    def __str__(self):
       return self.title



class Blog(models.Model):
    title = models.CharField(max_length=221)
    body = models.CharField(max_length=221)
    image = models.ImageField(upload_to='blog/')

    def __str__(self):
        return self.title


class Single(models.Model):
    title = models.CharField(max_length=222)
    title2 = models.CharField(max_length=222)
    name = models.CharField(max_length=222)
    body1 = models.TextField()
    body2 = models.TextField()
    body3 = models.TextField()
    body4 = models.TextField()
    image = models.ImageField(upload_to='single-image/')
    image2 = models.ImageField(upload_to='single-image2/')

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=222)
    last_name = models.CharField(max_length=222)
    email = models.EmailField()
    message = models.TextField()


    def __str__(self):
        return self.first_name



class Comment(models.Model):
    name = models.CharField(max_length=222)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    message = models.TextField()


    def __str__(self):
        return self.name



