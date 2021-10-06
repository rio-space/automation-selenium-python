import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from data import _directory
from functions import Login
from datetime import datetime
from xpath import Profile


class TC03_VerifyThatUserIsAbleToUploadAndDeleteCVInProfilePage(unittest.TestCase):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()

    def test_login(self):
        print('====== TC-03 execution has started. ======')
        # Login to Shortlyster
        Login.login(self)

    def test_upload_delete_cv(self):
        # Click Upload CV button
        self.driver.find_element_by_xpath(Profile.btn_upload).click()

        # Verify if dialog box is displayed when upload button is clicked
        dlg_upload = self.driver.find_element_by_xpath(Profile.dlg_upload)
        self.assertTrue(dlg_upload.is_displayed, "Upload CV/Resume Dialog is not displayed.")
        print("====== Upload CV/Resume Dialog is displayed. ======")

        # Get state of prefill checkbox
        chk_prefill = self.driver.find_element_by_xpath(Profile.chk_prefill_on)

        # Set chkPrefill = off, if status is on. Otherwise, keep status = off
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

        # Click Cancel button
        self.driver.find_element_by_xpath(Profile.btn_cancel).click()

        # Get current Date Time
        now = datetime.now()
        dt_current = now.strftime("%d %b %Y, %I:%M%p").replace(" 0", "")

        # Verify if a CV/resume is available with latest timestamp
        str_filename = self.driver.find_element_by_xpath(Profile.lnk_download_file).text
        dt_upload = self.driver.find_element_by_xpath(Profile.dt_upload).text
        self.assertIsNotNone(str_filename, "No file is available in the CV/Resume Upload section.")
        self.assertEqual(dt_upload.upper(), dt_current.upper(),
                         "Uploaded CV/Resume is not updated. Timestamp is not updated.")
        print("====== %s is available in CV/Resume Upload section with as of %s. ======" % (str_filename, dt_upload))

        # Click Delete button
        self.driver.find_element_by_xpath(Profile.btn_delete).click()
        self.driver.switch_to.alert.accept()
        time.sleep(2)

        # Verify if CV/Resume is deleted
        try:
            lnk_download_file = self.driver.find_element_by_xpath(Profile.lnk_download_file).is_displayed()
        except NoSuchElementException:
            lnk_download_file = False
            pass

        self.assertFalse(lnk_download_file, "File is not deleted in the CV/Resume Upload section.")
        print("====== %s is deleted fin CV/Resume Upload section. ======" % str_filename)

        print('====== TC-03 execution has been completed. ======')

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
