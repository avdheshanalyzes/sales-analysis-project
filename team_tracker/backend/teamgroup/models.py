from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)  # optional if you want
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Member(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.role})"
