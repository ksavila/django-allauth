from django.test import TestCase

from allauth.socialaccount.providers.agave.provider import AgaveProvider
from tests.apps.socialaccount.base import OAuth2TestsMixin
from tests.mocking import MockedResponse


class AgaveTests(OAuth2TestsMixin, TestCase):
    provider_id = AgaveProvider.id

    def get_mocked_response(self):
        return MockedResponse(
            200,
            """
        {
        "status": "success",
        "message": "User details retrieved successfully.",
        "version": "2.0.0-SNAPSHOT-rc3fad",
        "result": {
          "first_name": "John",
          "last_name": "Doe",
          "full_name": "John Doe",
          "email": "jon@doe.edu",
          "phone": "",
          "mobile_phone": "",
          "status": "Active",
          "create_time": "20180322043812Z",
          "username": "jdoe"
          }
        }
        """,
        )

    def get_expected_to_str(self):
        return "jdoe"
