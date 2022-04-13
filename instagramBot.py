from botInfo import username,password,username2,password2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class InstagramBot:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs',{'intl.accept_languages':'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe',chrome_options=self.browserProfile)
        self.username = username
        self.password = password
        self.followers = []


    def logIn(self):
        self.browser.get("https://www.instagram.com/")
        sleep(3)
        usernameInput = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input')

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        sleep(3)

        self.browser.find_element_by_xpath("//button[text()='Not Now']").click()
        sleep(2)
        self.browser.find_element_by_xpath("//button[text()='Not Now']").click()
        sleep(2)


    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        sleep(2)
        self.browser.find_element_by_class_name("k9GMp").find_elements_by_class_name("Y8-fY")[1].click()
        sleep(2)

        pzuss = self.browser.find_element_by_class_name("isgrP")

        followersCount = len(pzuss.find_elements_by_tag_name("li"))
        print(f"first count: {followersCount}")

        # loopCounter = 0
        self.browser.execute_script('return sayfa = document.querySelector(".isgrP")')
        while True:
            # if loopCounter > 3:
                # break
            self.browser.execute_script('sayfa.scrollTo(0,sayfa.scrollHeight);')
            sleep(3)
            new_height = len(pzuss.find_elements_by_tag_name("li"))
            sleep(2)
            print(f"second count : {new_height}")
            if followersCount == new_height:
                break
            else:
                followersCount = new_height
            # loopCounter +=1

            followers = pzuss.find_elements_by_tag_name("li")
            sleep(1)

        followersList = []
        for user in followers:
            name = user.find_element_by_tag_name("a").get_attribute("href")
            # print(name)
            followersList.append(name)

        for i in followersList:
            self.followers.append(i)

        with open("followers.txt","w",encoding='UTF-8') as file:
            for item in followersList:
                file.write(item + "\n")


    def iFollow(self):
        self.browser.get(f"https://www.instagram.com/{self.username}/")
        sleep(2)
        button = self.browser.find_element_by_class_name('k9GMp ').find_elements_by_tag_name("li")[2]
        button.click()
        sleep(2)
        psuzz = self.browser.find_element_by_class_name('isgrP')
        followersCount = len(psuzz.find_elements_by_tag_name("li"))
        print(f"count : {followersCount}")

        self.browser.execute_script("return sayfa = document.querySelector('.isgrP')")
        while True:
            self.browser.execute_script("sayfa.scrollTo(0,sayfa.scrollHeight);")
            sleep(3)
            newCount = len(psuzz.find_elements_by_tag_name("li"))
            sleep(3)
            print(f"new count: {newCount}")
            if followersCount == newCount:
                break
            else:
                followersCount = newCount

            followers = psuzz.find_elements_by_tag_name("li")
            sleep(2)

        usersList = []
        for user in followers:
            link = user.find_element_by_tag_name('a').get_attribute('href')
            usersList.append(link)

        count = 1
        with open('iFollow.txt','w',encoding ='UTF-8') as file:
            for item in usersList:
                file.write(f"{count}-{item}\n")
                count+=1

        comparisonx = []
        for user in usersList:
            if user not in self.followers:
                print(user)
                comparisonx.append(user)

        with open('comparison.txt','w',encoding='UTF-8') as file:
            for item in comparisonx:
                file.write(item + "\n")


    def followUsers(self,username):
        searchButton = self.browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        searchButton.send_keys(username)
        sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div').click()
        sleep(4)
        try:
            followButton = self.browser.find_element_by_xpath('//button[text()="Follow"]')
            if followButton.text == "Follow":
                followButton.click()
                sleep(2)
                print(username + " was followed.")
            else:
                print(username + "are already following.")
        except:
            print(username + " An error has been encountered.")


    def unFollowUsers(self,username):
        searchButton = self.browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        searchButton.send_keys(username)
        sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div').click()
        sleep(3)
        try:
            self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button').click()
            sleep(2)
            unFollowButton = self.browser.find_element_by_xpath("//button[text()='Unfollow']")
            if unFollowButton.text == 'Unfollow':
                unFollowButton.click()
                sleep(3)
                print(username +"--> Tracking has been exited.")
        except:
            print(username + " An error has been encountered.")


    def likePost(self,username,amount):
        searchButton = self.browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        searchButton.send_keys(username)
        sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div').click()
        sleep(3)

        self.browser.find_element_by_class_name('v1Nh3').click()
        i = 1
        while i <= amount:
            sleep(1)
            self.browser.find_element_by_class_name('fr66n').click()
            sleep(3)
            self.browser.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            sleep(3)
            i+=1
        self.browser('https://instagram.com/'+ self.username)


    def addComment(self,username,message,amount):

        searchButton = self.browser.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        searchButton.send_keys(username)
        sleep(2)
        self.browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div').click()
        sleep(3)

        self.browser.find_element_by_class_name('v1Nh3').click()
        i = 1
        while i <= amount:
            sleep(4)
            try:
                commentButton = self.browser.find_element_by_class_name("Ypffh")
                commentButton.click()
                sleep(4)
                commentButton = self.browser.find_element_by_class_name("Ypffh")
                commentButton.click()
                sleep(4)
            except:
                print('An error has been encountered.')
            commentButton.send_keys(message)
            self.browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]').click()
            sleep(2)
            self.browser.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
            sleep(3)
            i += 1
        self.browser('https://instagram.com/'+ self.username)


hikmetbot = InstagramBot(username,password)

# hikmetbot.logIn()
# hikmetbot.getFollowers()
# hikmetbot.iFollow()
# hikmetbot.followUsers('#username')
# hikmetbot.unFollowUsers('#username')
# hikmetbot.likePost('#username',1)
# hikmetbot.addComment('#username','',1)
