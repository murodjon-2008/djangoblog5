from django.db import models

class Posts(models.Model):
    img = models.ImageField(upload_to='media')
    name = models.CharField(max_length=250)
    about = models.CharField(max_length=250)
    join_date = models.DateTimeField()
    comment = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return self.name
