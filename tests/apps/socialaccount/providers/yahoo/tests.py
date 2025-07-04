from django.test import TestCase

from allauth.socialaccount.providers.yahoo.provider import YahooProvider
from tests.apps.socialaccount.base import OAuth2TestsMixin
from tests.mocking import MockedResponse


class YahooTests(OAuth2TestsMixin, TestCase):
    provider_id = YahooProvider.id

    def get_mocked_response(self):
        response_data = """
        {
         "sub": "FSVIDUW3D7FSVIDUW3D72F2F",
         "name": "Jane Doe",
         "given_name": "Jane",
         "family_name": "Doe",
         "preferred_username": "j.doe",
         "email": "janedoe@example.com",
         "email_verified": true,
         "picture": "http://example.com/janedoe/me.jpg"
        }
        """  # noqa
        return MockedResponse(200, response_data)

    def get_expected_to_str(self):
        return "janedoe@example.com"
