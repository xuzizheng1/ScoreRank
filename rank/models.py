from django.db import models


class Score(models.Model):
    client = models.CharField(max_length=4)
    score = models.IntegerField()

    def __str__(self):
        return self.client+'--'+str(self.score)
