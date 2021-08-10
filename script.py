from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


# username = input('Enter Username: ')
# password = input('Enter Password: ')
username = 'vule2003'
password = 'rrn121517kndV'
mood = input('Which playlist are you feeling today?\n[A] :^) \n[B] moonlight uh \n[C] sponkbup \n[D] w0w \n[E] oldies \n[F] Random \n[G] Choose a playlist\n[E] Choose a song\n').lower()
if mood == 'g':
    playlist_choice = str(input('What playlist would you like to hear?\n')).lower()
if mood == 'e':
    song_choice = input('What song would you like to hear?\n').lower()
volume = int(input('What volume would you like the volume at?\n'))
shuffle = input('Do you want shuffle on or off? \n[A] On [B] Off\n').lower()



PATH = 'C:\Program Files (x86)\chromedriver.exe'


driver = webdriver.Chrome(PATH)
driver.delete_all_cookies()

driver.get("https://open.spotify.com")
driver.maximize_window()



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

    # Turns shuffle on/off depending on what is already selected
    shuffle_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[4]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/div[1]/button[1]")))
    shuffle_checker = shuffle_button.get_attribute('aria-checked').lower()

    if shuffle == 'a':
        if shuffle_checker != 'true':
            shuffle_button.click()
            print('Shuffle Enabled')
        if shuffle_checker == 'true':
            shuffle_button.click()
            time.sleep(2)
            shuffle_button.click()
            print('Shuffle Already On')
    if shuffle == 'b':
        if shuffle_checker != 'false':
            shuffle_button.click()
            print('Shuffle Disabled')


except:
    driver.quit()
    print('Failed before selecting playlists')



# Assigns Spotify Playlists to variables
playlist1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, ":^)")))
playlist2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "moonlight uh")))
playlist3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "sponkbup")))
playlist4 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "w0w")))
playlist5 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "oldies")))
playlists = [playlist1, playlist2, playlist3, playlist4, playlist5]


def random_playlist():
    rand_playlist  = random.choice(playlists)
    rand_playlist.click()

def click_play():
    time.sleep(2)
    play_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div[2]/div[3]/main/div[2]/div[2]/div/div/div[2]/section/div[2]/div[2]/div/button[1]")))
    play_button.click()
    
# Changes Volume Slider
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

    def get_vol():
        curr_vol = current_volume.get_attribute('style')
        start = curr_vol.find('orm:') + len('orm:')
        end = curr_vol.find('%;')
        vol = curr_vol[start:end]
        return int(float(vol))

    upper_range = volume + 6
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

# Chooses the chosen playlist in mood
if mood == 'a':
    playlist1.click()
    click_play()
elif mood == 'b':
    playlist2.click()
    click_play()
elif mood == 'c':
    playlist3.click()
    click_play()
elif mood == 'd':
    playlist4.click()
    click_play()
elif mood == 'e':
    playlist5.click()
    click_play()
elif mood == 'f':
    random_playlist()
    click_play()
elif mood == 'g':
    playlist = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, playlist_choice)))
    playlist.click()
    click_play()
elif mood == 'e':
    search_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "icon.search-icon")))
    search_button.click()

    search_bar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "_748c0c69da51ad6d4fc04c047806cd4d-scss.f3fc214b257ae2f1d43d4c594a94497f-scss")))
    search_bar.send_keys(song_choice)
    search_bar.send_keys(Keys.RETURN)

    song1 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "e8ea6a219247d88aa936a012f6227b0d-scss.bddcb131e9b40fa874148a30368d83f8-scss")))
    double = ActionChains(driver)
    double.double_click(song1).perform()


#Change looping for choosing songs so that the song repeats
# create another file that stores names of playlists that user can input, then switch playlist variables to the correct name 