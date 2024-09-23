from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from actors_agency.models import Actor, Agency, Character

class AdminTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin",
        )
        self.client.force_login(self.admin_user)

        self.agency = Agency.objects.create(name="Test Agency", city="Test City", description="A test agency.")
        self.actor = Actor.objects.create(
            username="testactor",
            first_name="Test",
            last_name="Actor",
            gender="M",
            bio="Test bio."
        )
        self.character = Character.objects.create(
            name="Test Character",
            gender="M",
            description="Test description",
            agency=self.agency
        )

    def test_actor_username_listed(self):
        url = reverse("admin:actors_agency_actor_changelist")
        self.assertContains(self.client.get(url), self.actor.username)

    def test_actor_detail_username_listed(self):
        url = reverse("admin:actors_agency_actor_change", args=[self.actor.id])
        self.assertContains(self.client.get(url), self.actor.username)

    def test_agency_name_listed(self):
        url = reverse("admin:actors_agency_agency_changelist")
        self.assertContains(self.client.get(url), self.agency.name)

    def test_agency_detail_name_listed(self):
        url = reverse("admin:actors_agency_agency_change", args=[self.agency.id])
        self.assertContains(self.client.get(url), self.agency.name)

    def test_character_name_listed(self):
        url = reverse("admin:actors_agency_character_changelist")
        self.assertContains(self.client.get(url), self.character.name)

    def test_character_detail_name_listed(self):
        url = reverse("admin:actors_agency_character_change", args=[self.character.id])
        self.assertContains(self.client.get(url), self.character.name)
