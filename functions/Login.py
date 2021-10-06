from constants import EnvironmentURLs, UserCredentials
from xpath import Login


def login(self):
    self.driver.get(EnvironmentURLs.LOGIN)
    self.driver.implicitly_wait(15)

    # Check if Sign in Page is displayed or accessible
    self.assertEqual("Sign in to Shortlyster", self.driver.title, "Sign in Page is not displayed.")
    print("====== Sign in to Shortlyster Page is displayed. Proceed to Login ======")

    self.driver.find_element_by_name("email").send_keys(UserCredentials.EMAIL)
    print("====== User email is entered. ======")
    self.driver.find_element_by_name("password").send_keys(UserCredentials.PASSWORD)
    print("====== User password is entered. ======")
    self.driver.implicitly_wait(15)
    self.driver.find_element_by_xpath(Login.btn_submit).click()

    profile = self.driver.find_element_by_id("app")

    # Check if Sign in Page is displayed or accessible
    self.assertTrue(profile.is_displayed, "Unsuccessful sign in.")
    print("====== User Profile is displayed. ======")
