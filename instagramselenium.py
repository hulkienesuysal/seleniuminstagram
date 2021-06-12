from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver=webdriver.Chrome(executable_path=r'C:\Users\chromedriver.exe')

driver.get("http://www.instagram.com")
sn=1

sleep(sn)

username=driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys("username giriniz") #username giriniz

password=driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
password.send_keys("password giriniz") #password giriniz

loginbutton=driver.find_element_by_xpath('//*[@id="loginForm"]/div[1]/div[3]/button').click()

sleep(sn+3)
  
driver.get('https://www.instagram.com/' + "username giriniz") #username giriniz 

followerscount=driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/span').text
followersLink = driver.find_element_by_css_selector('ul li a').click()

sleep(sn+2)

followersList = driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

pop_up_window = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='isgrP']")))
  
while numberOfFollowersInList < int(followerscount):
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window)
    numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

followers = []
with open("instagram.txt", "a") as f:
    f.write("----Takipciler----\n")
for user in followersList.find_elements_by_css_selector('li'):
    user="{}".format(user.find_element_by_css_selector('a').get_attribute('href'))
    user=user[26:-1]
    print(user)
    with open("instagram.txt", "a") as f:
        f.write(user+"\n")
    followers.append(user)
    if len(followers) == int(followerscount):  
        followersout=driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button').click()

followingcount=driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text
followingLink = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
sleep(sn+2)
followingList = driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
numberOfFollowingInList = len(followingList.find_elements_by_css_selector('li'))

pop_up_window = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='isgrP']")))

while numberOfFollowingInList < int(followingcount):
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',pop_up_window)
    numberOfFollowingInList = len(followingList.find_elements_by_css_selector('li'))
following = []
with open("instagram.txt", "a") as f:
    f.write("\n----Takip Ettiklerim----\n")
for user in followingList.find_elements_by_css_selector('li'):
    user="{}".format(user.find_element_by_css_selector('a').get_attribute('href'))
    user=user[26:-1]
    print(user)
    with open("instagram.txt", "a") as f:
        f.write(user+"\n")
    following.append(user)

takipetmeyenler=[]
for follow in following:
    if follow not in followers:
        takipetmeyenler.append(follow)

with open("instagram.txt", "a") as f:
    f.write("\n----Takip Etmeyenler----\n")
    for takip in takipetmeyenler:
        f.write(takip+"\n")

takipetmediklerim=[]
for follow in followers:
    if follow not in following:
        takipetmediklerim.append(follow)

with open("instagram.txt", "a") as f:
    f.write("\n----Takip Etmediklerim----\n")
    for takip in takipetmediklerim:
        f.write(takip+"\n")