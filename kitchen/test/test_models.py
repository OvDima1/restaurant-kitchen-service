from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Cook, Dish


class ModelsTests(TestCase):
    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="usertest",
            password="user12345",
            first_name="testfirst",
            last_name="testlast",
        )

        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})",
        )

    def test_create_cook_with_experience(self):
        username = "usertest"
        password = "user12345"
        years_of_experience = 23
        cook = get_user_model().objects.create_user(username=username,
                                                    password=password,
                                                    years_of_experience=years_of_experience,)

        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)
