import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# system: macOS Monterey
# display: 2560 × 1600
# browser: Google Chrome ver.100.0.4896.127

url = 'https://mail.qq.com/'
username = ''
password = ''
target_mail_address = 'teemovv@outlook.com'

subject_text = ''
main_text = ''


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')

    chrome = webdriver.Chrome(options=options)

    chrome.get(url)
    chrome.maximize_window()

    login_frame = chrome.find_element(By.CSS_SELECTOR,'#login_frame')
    chrome.switch_to.frame(login_frame)

    username_input = chrome.find_element(By.CSS_SELECTOR,'#u')
    password_input = chrome.find_element(By.CSS_SELECTOR,'#p')
    login_button =   chrome.find_element(By.CSS_SELECTOR,'#login_button')

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()

    chrome.switch_to.default_content()

    time.sleep(1)
    # XPATH、SELECTOR 失效 原因未知
    # compose_button = chrome.find_element(By.XPATH,'//*[@id="mailMainApp"]/div[2]/div/div[1]')
    # print(compose_button)
    ActionChains(chrome).move_by_offset(90,90).click().w3c_actions.perform()

    time.sleep(1)

    to_input =  chrome.find_element(By.CSS_SELECTOR,'#mailMainApp > div.frame_main.vue2_app > div.compose_wrapper > div > div.compose_mail > div.compose_mail_wrapper > section > div:nth-child(3) > div.compose_mailInfo_item_inputWrapper.compose_mailInfo_item_inputWrapper_address > div > div.compose_mailAddress_table_wrapper > table > tr > td > div.compose_mailAddress_inputWrapper > input')
    to_input.send_keys(target_mail_address)



    text = chrome.find_element(By.CSS_SELECTOR,'#ueditor > p')
    text.send_keys(main_text)

    subject_input = chrome.find_element(By.XPATH,'//*[@id="mailMainApp"]/div[4]/div[1]/div/div[1]/div[1]/div[2]/div[2]/input')
    subject_input.send_keys(subject_text)

    send_button = chrome.find_element(By.CSS_SELECTOR,'#mailMainApp > div.frame_main.vue2_app > div.compose_wrapper > div > div.compose_mail > div.compose_footer > div:nth-child(2) > button.xm_btn.compose_header_btn.compose_header_btn_send.xm_btn_Blue.xm_btn_Compose')

    send_button.click()