from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from actors_agency.models import Actor


class ActorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Actor