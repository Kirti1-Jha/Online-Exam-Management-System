from django.test import TestCase
from django.contrib.auth.models import User

class LoginTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="Kirti",
            password="Kirtipass123"
        )

    def test_user_login(self):
        login = self.client.login(
            username="Kirti",
            password="Kirtipass123"
        )

        self.assertTrue(login)
