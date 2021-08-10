from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

volume = int(input('What volume would you like the volume at?\n'))
username = 'vule2003'
password  = 'rrn121517kndV'

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://open.spotify.com")

try:
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "_3f37264be67c8f40fa9f76449afdb4bd-scss._1f2f8feb807c94d2a0a7737b433e19a8-scss")))
    login_button.click()
    user_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-username")))
    user_field.send_keys(username)
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login-password")))
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)

    # Closes Spotify Cookie Policy Notice
    cookies_notice = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "onetrust-close-btn-container")))
    cookies_notice.click()
    

    # current_volume = WebDriverWait(driver, 10).until(
        # EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/footer/div/div[3]/div/div[3]/div/div")))

    # volume_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/footer/div/div[3]/div/div[3]/div/div/div/button")))
    # target_volume = ''
    # print(current_volume.get_attribute('style'))
    # if current_volume.get_attribute('style') != "--progress-bar-transform:{}%;".format(volume):
    #     target = 
    # actions = ActionChains(driver)
    # actions.click_and_hold(volume_button).perform()

except:
    driver.quit()
    print('Failed before selecting playlists')


# Temp. Clicks and Holds on Volume Button
# playback_volume_bar = WebDriverWait(driver, 10).until(
#         EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div[2]/div[2]/footer/div/div[3]/div/div[3]/div/div/div/button")))
# actions = ActionChains(driver)
# actions.click_and_hold(playback_volume_bar).perform()


def volume_changer():
    actions1 = ActionChains(driver)
    actions2 =ActionChains(driver)
    actions3 =ActionChains(driver)
    actions4 =ActionChains(driver)
    current_volume = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/footer/div/div[3]/div/div[3]/div/div")))
    actions1.move_to_element(current_volume).perform()
    
    volume_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/footer/div/div[3]/div/div[3]/div/div/div/button")))

    # print(current_volume.get_attribute('style'))
    # print(volume_button.get_attribute('aria-label'))
    def get_vol():
        curr_vol = current_volume.get_attribute('style')
        start = curr_vol.find('orm:') + len('orm:')
        end = curr_vol.find('%;')
        vol = curr_vol[start:end]
        return int(float(vol))

    upper_range = volume + 4
    lower_range = volume - 5
    vol_range = range(lower_range, upper_range)

    while get_vol() not in vol_range:
        if get_vol() > volume:
            print(get_vol())
            actions2.drag_and_drop_by_offset(volume_button, -3, 0).perform()
        if get_vol() < volume:
            print(get_vol())
            actions3.drag_and_drop_by_offset(volume_button, 3, 0).perform()
    actions4.release().perform()


volume_changer()