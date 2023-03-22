from django.db import models


class User(models.Model):
    username = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.username


class Task(models.Model):
    title = models.CharField(max_length=150)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_finished = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.user}"
