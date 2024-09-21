from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Actor(AbstractUser):
    gender = models.CharField(max_length=10)
    bio = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("actor-detail", kwargs={"pk": self.pk})


class Agency(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, default=2)

    def __str__(self):
        return self.name

class ActorAgency(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.actor.username} - {self.character.name} ({self.agency.name})"
