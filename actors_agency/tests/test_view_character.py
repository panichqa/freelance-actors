from django.test import TestCase
from django.urls import reverse
from actors_agency.models import Character, Agency
from django.contrib.auth import get_user_model


User = get_user_model()

class CharacterViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.agency = Agency.objects.create(
            name="Test Agency",
            city="Test City",
            description="This is a test description."
        )
        self.character = Character.objects.create(
            name="Test Character",
            gender="M",
            description="This is a test character.",
            agency=self.agency
        )


    def test_character_list_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse("actors_agency:characters-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "actors_agency/characters_list.html")
        self.assertContains(response, "Test Character")


    def test_character_detail_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse("actors_agency:character-detail", kwargs={"pk": self.character.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "actors_agency/character_detail.html")
        self.assertContains(response, "Test Character")


    def test_character_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse("actors_agency:character-create"), {
            "name": "New Character",
            "gender": "F",
            "description": "New character description.",
            "agency": self.agency.pk
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Character.objects.filter(name="New Character").exists())


    def test_character_update_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse("actors_agency:character-update", kwargs={"pk": self.character.pk}), {
            "name": "Updated Character",
            "gender": "M",
            "description": "Updated character description.",
            "agency": self.agency.pk
        })
        self.assertEqual(response.status_code, 302)
        self.character.refresh_from_db()
        self.assertEqual(self.character.name, "Updated Character")


    def test_character_delete_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse("actors_agency:character-delete", kwargs={"pk": self.character.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Character.objects.filter(pk=self.character.pk).exists())
