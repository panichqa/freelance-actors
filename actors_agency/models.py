from django.contrib.auth.models import AbstractUser

from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone


class Actor(AbstractUser):
    gender = models.CharField(max_length=10)
    bio = models.TextField(default="No biography available")
    date_joined = models.DateTimeField(default=timezone.now)

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
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name="characters")

    def __str__(self):
        return self.name


class ActorAgency(models.Model):
    actor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="actor_agencies")
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name="agencies")
    character = models.ForeignKey(Character, on_delete=models.CASCADE, related_name="characters")
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.actor.username} - {self.character.name} ({self.agency.name})"
