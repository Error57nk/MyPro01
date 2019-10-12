from django.db import models


class FeedBackModels(models.Model):
    Name = models.CharField(max_length=100)
    MailId = models.EmailField(max_length=100)
    Profession = models.CharField(max_length=100)
    Sub = models.CharField(max_length=50)
    Msg = models.CharField(max_length=300)

    def __str__(self):
        return self.Name

