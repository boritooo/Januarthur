from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField(null=True)

    def __str__(self):
        return self.name
    
class Painter(models.Model):
    name = models.CharField(max_length=50, null=True)
    about = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    age = models.IntegerField(null = True)
    profile_picture = models.ImageField(upload_to='profile_picture/', blank=True)
    date_born = models.DateField(null=True)
    group = models.ManyToManyField(Group, related_name='painters')

    def __str__(self):
        return self.name

class Painting(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.TextField(blank=True)
    released_date = models.DateField(auto_now=True)
    photo = models.ImageField(upload_to='images/', blank=True)
    painters = models.ForeignKey(Painter, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
    



