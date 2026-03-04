from django.test import TestCase
from .test_login import *
# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User

class UserRegistrationTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("password123"))