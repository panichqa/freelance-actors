from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from actors_agency.models import Agency



User = get_user_model()

class AgencyViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.agency = Agency.objects.create(
            name="Test Agency",
            city="Test City",
            description="This is a test description."
        )


    def test_agency_list_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse("actors_agency:agency-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "actors_agency/agency_list.html")
        self.assertContains(response, "Test Agency")


    def test_agency_detail_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse("actors_agency:agency-detail", kwargs={"pk": self.agency.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "actors_agency/agency_detail.html")
        self.assertContains(response, "Test Agency")


    def test_agency_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse("actors_agency:agency-create"), {
            "name": "New Agency",
            "city": "New City",
            "description": "New description."
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Agency.objects.filter(name="New Agency").exists())


    def test_agency_update_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse("actors_agency:agency-update", kwargs={"pk": self.agency.pk}), {
            "name": "Updated Agency",
            "city": "Updated City",
            "description": "Updated description."
        })
        self.assertEqual(response.status_code, 302)
        self.agency.refresh_from_db()
        self.assertEqual(self.agency.name, "Updated Agency")


    def test_agency_delete_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse("actors_agency:agency-delete", kwargs={"pk": self.agency.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Agency.objects.filter(pk=self.agency.pk).exists())
