# Test For Models

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user_with_email_successfulA(self):
        email = "test@example.com"
        password = "testpass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password)

        self.assertEqual(user.email, email)
        self.assertEqual(user.password, password)
