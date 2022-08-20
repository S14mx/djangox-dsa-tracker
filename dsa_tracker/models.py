from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class CompletedQuestion(models.Model):
    name = models.CharField(max_length=64)
    notes = models.CharField(max_length=128)
    time_to_complete = models.CharField(max_length=32)
    completed = models.DateTimeField(auto_now_add=True)
    completed_by = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_question', args=[str(self.id)])
