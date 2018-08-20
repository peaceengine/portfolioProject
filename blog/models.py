from django.db import models
import datetime

class Blog(models.Model):
    title = models.CharField(max_length = 255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.title

    def summary(self):
        wordList = self.body.split()
        shortened = ""
        for i in range(min(20, len(wordList))):
            shortened += " " + wordList[i]
        return (shortened + " ...")

    def pub_date_pretty(self):
        return self.pub_date.strftime("%b %e %Y")
