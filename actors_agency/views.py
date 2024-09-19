from django.shortcuts import render
from django.views import generic
from .models import Actor, Agency, Character, ActorAgency

def index(request):
    num_actors = Actor.objects.count()
    num_agencies = Agency.objects.count()
    num_characters = Character.objects.count()
    num_actor_agencies = ActorAgency.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_actors": num_actors,
        "num_agencies": num_agencies,
        "num_characters": num_characters,
        "num_visits": num_visits + 1,
    }

    return render(request, "actors_agency/index.html", context=context)

class ActorDetailView(generic.DetailView):
    model = Actor
    template_name = "actors_agency/actor_detail.html"
