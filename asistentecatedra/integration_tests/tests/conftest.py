# system_tests/conftest.py

import pytest
from selenium import webdriver
from django.contrib.auth import get_user_model
User = get_user_model()


TESTEMAIL = 'tester@tester.com'
TESTPASSWORD = 'p455w0rd'


@pytest.fixture()
def user(db):
    """Add a test user to the database."""
    user_ = User.objects.create_user(
        username='tester',
        email=TESTEMAIL,
        password=TESTPASSWORD,
    )

    return user_


@pytest.fixture(scope='module')
def driver(request):
    """Provide a selenium webdriver instance."""
    # SetUp
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver_ = webdriver.Chrome(options=options)

    yield driver_

    # TearDown
    driver_.quit()


@pytest.fixture()
def authenticated_browser(browser, client, live_server, user):
    """Return a browser instance with logged-in user session."""
    client.login(email=TESTEMAIL, password=TESTPASSWORD)
    cookie = client.cookies['sessionid']

    browser.get(live_server.url)
    browser.add_cookie({
        'name': 'sessionid',
        'value': cookie.value,
        'secure': False, 'path': '/'
    })

    browser.refresh()

    return browser
