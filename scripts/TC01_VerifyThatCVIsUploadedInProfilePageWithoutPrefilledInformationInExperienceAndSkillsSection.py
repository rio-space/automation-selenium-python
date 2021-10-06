import unittest
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from data import _directory
from functions import Login
from datetime import datetime
from xpath import Profile, Experience_Skills


class TC01_VerifyThatCVIsUploadedInProfilePageWithoutPrefilledInformationInExperienceAndSkillsSection(
    unittest.TestCase):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    def test_login(self):
        print('====== TC-01 execution has started. ======')
        # Login to Shortlyster
        Login.login(self)

    def test_upload_cv(self):
        # Click Upload CV button
        self.driver.find_element_by_xpath(Profile.btn_upload).click()

        # Verify if dialog box is displayed when upload button is clicked
        dlg_upload = self.driver.find_element_by_xpath(Profile.dlg_upload)
        self.assertTrue(dlg_upload.is_displayed, "Upload CV/Resume Dialog is not displayed.")
        print("====== Upload CV/Resume Dialog is displayed. ======")

        # Get state of prefill checkbox
        chk_prefill = self.driver.find_element_by_xpath(Profile.chk_prefill_on)

        # Set chkPrefill to off, if status is on. Otherwise, keep status to off
        if chk_prefill.is_displayed() is True:
            self.driver.find_element_by_xpath(Profile.btn_prefill).click()

        # Upload CV/Resume
        self.driver.find_element_by_name("cv-upload").send_keys(_directory.data_path + "/Riolyn Tumaneng_resume.pdf")

        # Check Progress bar / status of upload is displayed
        sts_bar_upload = self.driver.find_element_by_xpath(Profile.sts_bar_upload)
        self.assertTrue(sts_bar_upload.is_displayed, "Upload status is not displayed.There is a problem with the file.")
        print("====== Upload status is displayed to notify the user. ======")

        # Get Upload Status
        msg_upload_no_prefill_success = self.driver.find_element_by_xpath(Profile.msg_upload_no_prefill_success)

        # Wait until Uploading status is completed
        wait = WebDriverWait(self.driver, 10)
        wait.until(visibility_of(msg_upload_no_prefill_success))

        # Verify if successful message is displayed
        self.assertTrue(msg_upload_no_prefill_success.is_displayed, "Upload of CV/Resume is not successful.")
        print("====== Upload of CV/Resume is successful. ======")

        # Get current Date Time
        now = datetime.now()
        dt_current = now.strftime("%d %b %Y, %I:%M%p").replace(" 0", "")

        # Click Cancel button
        self.driver.find_element_by_xpath(Profile.btn_cancel).click()

        # Verify if a CV/resume is available with latest timestamp
        str_filename = self.driver.find_element_by_xpath(Profile.lnk_download_file).text
        dt_upload = self.driver.find_element_by_xpath(Profile.dt_upload).text
        self.assertIsNotNone(str_filename, "No file is available in the CV/Resume Upload section.")
        self.assertEqual(dt_upload.upper(), dt_current.upper(),
                         "Uploaded CV/Resume is not updated. Timestamp is not updated.")
        print("====== %s is available in CV/Resume Upload section with as of %s. ======" % (str_filename, dt_upload))

        time.sleep(2)

        # Verify if Needs Review Status is not displayed in Experience and Skills section
        try:
            sts_review = self.driver.find_element_by_xpath(Profile.msg_es_needs_review).is_displayed()
        except NoSuchElementException:
            sts_review = False
            pass

        self.assertFalse(sts_review, "Experience and Skills section is pre-filled from the uploaded "
                                     "CV/resume.")
        print('====== Experience and Skills section is not pre-filled with information. ======')

        print('====== TC-01 execution has been completed. ======')

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
