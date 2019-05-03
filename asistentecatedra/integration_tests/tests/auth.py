from integration_tests.base_test import IntegrationTestCase
from django.contrib.auth import get_user_model
User = get_user_model()


class AuthTestCase(IntegrationTestCase):
    def test_login(self):
        self.user = User.objects.create_user(
            username='tester',
            email='tester@tester.com',
            password='p455w0rd'
        )
        self.driver.get('http://localhost:8000/accounts/login/')
        username = self.driver.find_element_by_id('id_username')
        password = self.driver.find_element_by_id('id_password')
        form = self.driver.find_element_by_id('loginForm')

        assert 'Asistente de Cátedra' in self.driver.title
        assert 'Bienvenido a "Asistente de Cátedra"' in self.driver.page_source

        username.send_keys('tester@tester.com')
        password.send_keys('Admin123')
        form.submit()

        assert 'Planificaciones' in self.driver.page_source
        assert 'planificaciones' in self.driver.current_url

