# coding: utf-8
from django_webtest import WebTest


class TestApp(WebTest):
    fixtures = ['users.json']


    def testDB(self):
        page = self.app.get('/backend/')
        html = str(page.html.b)
        if page.status_int != 200 or html[3:-4] != "Hello from BackEnd":
            assert False
