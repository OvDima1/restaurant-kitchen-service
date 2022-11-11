from django.test import TestCase

from kitchen.forms import CookCreationForm, CookUpdateForm


class FormsTests(TestCase):
    def test_cook_creation_form(self):
        form_data = {
            "username": "testuser",
            "password1": "user12345",
            "password2": "user12345",
            "first_name": "testfirst",
            "last_name": "testlast",
            "years_of_experience": 20,
        }
        form = CookCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_cook_update_form(self):
        form_data = {"years_of_experience": 5,
                     "first_name": "Rick",
                     "last_name": "Jonson",
                     }
        form = CookUpdateForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
