from django.test import TestCase
from django.urls import reverse
from actors_agency.models import Actor


class ActorViewTests(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create_user(
            username="testuser",
            password="testpassword",
            gender="M",
            bio="This is a test bio."
        )
        self.client.login(username="testuser", password="testpassword")


    def test_actor_list_view(self):
        response = self.client.get(reverse("actors_agency:actor-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "actors_agency/actor_list.html")
        self.assertContains(response, "testuser")


    def test_actor_detail_view(self):
        response = self.client.get(reverse("actors_agency:actor-detail", kwargs={"pk": self.actor.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "actors_agency/actor_detail.html")
        self.assertContains(response, self.actor.username)


    def test_actor_create_view(self):
        response = self.client.post(reverse("actors_agency:actor-create"), {
            "username": "newuser",
            "password": "newpassword",
            "gender": "F",
            "bio": "This is a new actor."
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Actor.objects.filter(username="newuser").exists())


    def test_actor_update_view(self):
        response = self.client.post(reverse("actors_agency:actor-update", kwargs={"pk": self.actor.pk}), {
            "username": "updateduser",
            "password": "testpassword",
            "gender": "M",
            "bio": "Updated bio."
        })
        self.assertEqual(response.status_code, 302)
        self.actor.refresh_from_db()
        self.assertEqual(self.actor.username, "updateduser")
        self.assertEqual(self.actor.bio, "Updated bio.")


    def test_actor_delete_view(self):
        response = self.client.post(reverse("actors_agency:actor-delete", kwargs={"pk": self.actor.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Actor.objects.filter(pk=self.actor.pk).exists())
