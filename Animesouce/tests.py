from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import New

ARTICLE = {"title": "Bleach", "anons": "анонс", "full_text": "текст", "date": "2024-01-01 10:00",
           "image": "https://example.com/bleach.jpg"}


class NewsPermissionsTests(TestCase):
    def setUp(self):
        self.article = New.objects.create(title="Old", anons="a", full_text="t", date=timezone.now())
        self.user = User.objects.create_user("user", password="Str0ngPass!")
        self.staff = User.objects.create_user("staff", password="Str0ngPass!", is_staff=True)

    def test_anonymous_cannot_create_edit_or_delete(self):
        # Аноним не может создать, изменить или удалить статью
        self.client.post(reverse("create"), ARTICLE)
        self.client.post(reverse("news-update", args=[self.article.pk]), {**ARTICLE, "title": "Hacked"})
        self.client.post(reverse("news-delete", args=[self.article.pk]))
        self.assertEqual(New.objects.count(), 1)
        self.assertEqual(New.objects.get().title, "Old")

    def test_regular_user_is_forbidden(self):
        self.client.login(username="user", password="Str0ngPass!")
        self.assertEqual(self.client.post(reverse("news-delete", args=[self.article.pk])).status_code, 403)
        self.client.post(reverse("create"), ARTICLE)
        self.assertEqual(New.objects.count(), 1)

    def test_staff_can_manage_news(self):
        self.client.login(username="staff", password="Str0ngPass!")
        response = self.client.post(reverse("create"), ARTICLE)
        created = New.objects.get(title="Bleach")
        self.assertRedirects(response, reverse("news-detail", args=[created.pk]))
        self.client.post(reverse("news-delete", args=[self.article.pk]))
        self.assertFalse(New.objects.filter(pk=self.article.pk).exists())

    def test_invalid_form_keeps_errors(self):
        self.client.login(username="staff", password="Str0ngPass!")
        response = self.client.post(reverse("create"), {**ARTICLE, "image": "javascript:alert(1)"})
        self.assertContains(response, "исправьте ошибки")
        self.assertFalse(New.objects.filter(title="Bleach").exists())

    def test_public_pages_render_and_hide_admin_buttons(self):
        for url in (reverse("home"), reverse("about"), reverse("creators"), reverse("new"),
                    reverse("news-detail", args=[self.article.pk])):
            self.assertEqual(self.client.get(url).status_code, 200, url)
        self.assertNotContains(self.client.get(reverse("news-detail", args=[self.article.pk])), "Удалить")
        self.assertEqual(self.client.get(reverse("news-delete", args=[self.article.pk])).status_code, 302)
