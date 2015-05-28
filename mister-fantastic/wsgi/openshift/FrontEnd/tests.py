# coding: utf-8
from django_webtest import WebTest


class TestApp(WebTest):
    fixtures = ['users.json']


    def testDB(self):
        page = self.app.get('/')
        if page.status_int != 200:
            assert False
