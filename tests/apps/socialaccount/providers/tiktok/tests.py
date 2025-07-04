from django.test import TestCase

from allauth.socialaccount.providers.tiktok.provider import TikTokProvider
from tests.apps.socialaccount.base import OAuth2TestsMixin
from tests.mocking import MockedResponse


class TikTokTests(OAuth2TestsMixin, TestCase):
    provider_id = TikTokProvider.id

    def get_mocked_response(self):
        return MockedResponse(
            200,
            """
        {
          "data": {
            "user": {
                "open_id": "44322889",
                "username": "username123",
                "display_name": "Nice Display Name",
                "avatar_url": "https://example.com/avatar.jpg",
                "profile_deep_link": "https://example.com/profile"
            }
          }
        }
        """,
        )

    def get_expected_to_str(self):
        return "username123"
