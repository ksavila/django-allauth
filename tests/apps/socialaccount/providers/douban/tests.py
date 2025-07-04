from django.test import TestCase

from allauth.socialaccount.providers.douban.provider import DoubanProvider
from tests.apps.socialaccount.base import OAuth2TestsMixin
from tests.mocking import MockedResponse


class DoubanTests(OAuth2TestsMixin, TestCase):
    provider_id = DoubanProvider.id

    def get_mocked_response(self):
        return MockedResponse(
            200,
            """
            {"name": "guoqiao",
             "created": "2009-02-18 01:07:52",
             "is_suicide": false,
             "alt": "http://www.douban.com/people/qguo/",
             "avatar": "http://img3.douban.com/icon/u3659811-3.jpg",
             "signature": "",
             "uid": "qguo",
             "is_banned": false,
             "desc": "\u4e0d\u662f\u5f88\u7231\u8bfb\u4e66",
             "type": "user",
             "id": "3659811",
             "large_avatar": "http://img3.douban.com/icon/up3659811-3.jpg"}
""",
        )

    def get_expected_to_str(self):
        return "guoqiao"
