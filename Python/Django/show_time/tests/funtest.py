from selenium import webdriver
import unittest

class AriWalksIntoABar(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_shows_time_and_travels_to_the_future(self):
        #User = Ari
        #Ari walks into a bar with a muffin, a duck, and a bar of soap
        #She gets on her laptop and pulls up a clock website
        self.browser.get('http://localhost:8000')
        self.assertIn('Time', self.browser.title)
        self.fail("Ari slipped on the soap, landed on the duck and it quacked!")

        #She looks at the first box which tells her that this is the time

        #A box under it says what the current time is

        #A button under the time box allows time travel

        #Time travel randomizes how much time to the future she will travel


        #When she clicks the time travel button, the current time changes to the future time and indicates how many hours have been travelled

if __name__ == '__main__':
    unittest.main()