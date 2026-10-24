from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    pub_date = models.DateTimeField("Published Date", auto_now_add=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.choice_text} {self.votes}"

