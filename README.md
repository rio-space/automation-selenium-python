# compono-qa-challenge

### **Part 01. Exploratory Exercise**
>Refer to [qa-challenge-exploratory.pdf](https://github.com/rio-space/compono-qa-challenge/blob/main/qa-challenge-exploratory.pdf)
### **Part 02. Automation Exercise**
#### The test framework used is _Selenium with Python_. 
>I do have basic knowledge in Selenium and Python, since I only have hands-on experience with proprietary technology, I have consider what is the easiest to use based on knowledge today, install and configure based on the goal and requirements of the activity.
#### Prerequisites
> - [x] Python should be installed
> - [x] Python IDE should be installed to run the test (recommended and easy to use- PyCharm)
> - [x] Selenium Webdriver should be installed. Alternatively, you can run _pip install -r requirements.txt_ once you have Python installed.

#### Summary of the Automation Tests
>- I have written 3 scripts which can be run individually
>   - TC01_VerifyThatCVIsUploadedInProfilePageWithoutPrefilledInformationInExperienceAndSkillsSection.py
>   - TC02_VerifyThatCVIsUploadedInProfilePageWithPrefilledInformationInExperienceAndSkillsSection.py
>   - TC03_VerifyThatUserIsAbleToUploadAndDeleteCVInProfilePage.py

>- Before running, there is a need to update these files:
>   - [EnvironmentURLs.py](https://github.com/rio-space/compono-qa-challenge/blob/main/constants/EnvironmentURLs.py) - update LOGIN variable with test environment url
>   - [UserCredentials.py](https://github.com/rio-space/compono-qa-challenge/blob/main/constants/UserCredentials.py) - update EMAIL and PASSWORD variables with access to Shortlyster

>- Assumptions
>   - For TC01, User should does not have information that "NEEDS REVIEW" under Experiences and Skills section. In short, good scenario for a new users
>   - Same data file is used for all the scripts

#### Additional 
> I have recorded the execution of these 3 scripts and you have the option to download from [here](https://github.com/rio-space/compono-qa-challenge/blob/main/compono-qa-challenge.mp4)

#### Challenge
> The provided test environment (https://candidate-qa-exercise.reviews.compono.dev/signup) is suddendly not accessible on my end so I ended up using the [Shortlyster](https://candidate.shortlyster.com/signin) site for this activity
![test environment is not accessible](https://github.com/rio-space/compono-qa-challenge/blob/main/qa-environment_not_accessible.png)

Let me know if you have questions!👍
