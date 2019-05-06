from django.test import LiveServerTestCase
from selenium import webdriver
from django.urls import reverse


class IntegrationTestCase(LiveServerTestCase):
    """
    A base test case for Selenium, providing hepler methods for generating
    clients and logging in profiles.
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Chrome()

    # Auxiliary function to add view subdir to URL
    def _get_full_url(self, namespace):
        return self.live_server_url + reverse(namespace)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()
