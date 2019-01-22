from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.urls import reverse
from selenium.webdriver.support.ui import WebDriverWait
from django.contrib.auth.models import User
import time


class PlanClaseTestCase(LiveServerTestCase):
    def setUp(self):
        # self.browser = webdriver.Firefox()
        self.browser = webdriver.Chrome()
        self.user = User.objects.create_user(username='tester',
                                             email='tester@tester.com',
                                             password='p455w0rd')

    # Auxiliary function to add view subdir to URL
    def _get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    def tearDown(self):
        self.browser.quit()

    def test_create_plan(self):
        browser = self.browser
        browser.get(self._get_full_url('home'))
        assert 'Planifica fácil y rápido' in browser.page_source

        go_to_planificaciones = browser.find_element_by_link_text(
            'Planificaciones')
        # time.sleep(10)

        go_to_planificaciones.click()

        assert 'Elige la planificación que deseas crear.' in \
            browser.page_source

        go_to_plan_clase = browser.find_element_by_link_text(
            'Plan de Clase')
        go_to_plan_clase.click()

        assert 'Nuevo Plan de Clase' in browser.page_source


        # submit = browser.find_element_by_id('id_submit')

        # username.send_keys('tester')
        # password.send_keys('p455w0rd')

        # submit.send_keys(Keys.RETURN)

        # wait = WebDriverWait(browser, 10)
        # wait.until(lambda browser: browser.find_element_by_id('userName'))

        # assert 'Hello, tester' in browser.page_source
