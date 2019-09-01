from django.db import models

# Create your models here.


class Log(models.Model):
    text = models.CharField(default='这里写标题', max_length=50)
    image = models.ImageField(default='default.png', upload_to='images/')
    title = models.CharField(default='这是标题', max_length=50)

    def __str__(self):
        return self.title
