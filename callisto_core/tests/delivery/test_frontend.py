from django.contrib.auth import get_user_model

from wizard_builder.tests import test_frontend as wizard_builder_tests

User = get_user_model()


class CoreElementHelper(
    wizard_builder_tests.ElementHelper,
):
    pass


class EncryptedFrontendTest(
    wizard_builder_tests.FrontendTest,
):
    passphrase = 'soooooo seekrit'

    @property
    def element(self):
        return CoreElementHelper(self.browser)

    def setUp(self):
        super().setUp()
        self.browser.find_element_by_css_selector(
            '[name="key"]').send_keys(self.passphrase)
        self.browser.find_element_by_css_selector(
            '[name="key_confirmation"]').send_keys(self.passphrase)
        self.browser.find_element_by_css_selector(
            '[type="submit"]').click()
