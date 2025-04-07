from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Question(models.Model):
    text = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def total_answers(self):
        return self.answers.count()
    
    def q_answers(self):
        return Answer.objects.filter(question=self).order_by("-created_date")


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_answers', blank=True)

    def total_likes(self):
        return self.likes.count()

