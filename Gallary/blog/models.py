from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(default='这是标题', max_length=50)
    date = models.DateField()
    image = models.ImageField(default='default.png', upload_to='images/')
    text = models.CharField(default='这是正文', max_length=50)

    def __str__(self):
        return self.title
