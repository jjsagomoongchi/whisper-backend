from undetected_chromedriver                 import Chrome
from time                                    import sleep
from selenium.webdriver.common.by            import By
from selenium.common.exceptions              import TimeoutException
from selenium.webdriver.support.ui           import WebDriverWait
from selenium.webdriver.support              import expected_conditions as EC
from selenium.webdriver.common.keys          import Keys
from selenium.webdriver.common.alert         import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options       import Options


## 헤드리스 모드

options = Options()
#options.add_argument('--headless')
#options.add_argument('--disable-gpu')

class Google:
    def __init__(self) -> None:
        self.url    = 'https://accounts.google.com/ServiceLogin'
        self.driver = Chrome(options=options,use_subprocess=True); self.driver.get(self.url)
        self.time   = 10
        

    
    def login(self, email, password):
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'identifier'))).send_keys(f'{email}\n')
        sleep(2)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'Passwd'))).send_keys(f'{password}\n')

        self.code()

    def code(self):

        ## 헤드리스 모드

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

        ## buster captcha 설치 (현재 확인 안해서 주석으로 해 놓음)

        #sleep(3)
        #self.driver.get('https://chrome.google.com/webstore/detail/buster-captcha-solver-for/mpbjkejclgfgadiemmefgebjfooflfhl')
        #sleep(self.time)      
        #WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Chrome에 추가']"))).click()
        #sleep(2)
        #action1 = ActionChains(self.driver)
        #action1.send_keys(Keys.TAB)
        #action1.send_keys(Keys.ENTER)
        #action1.perform()
        #sleep(5)
        #action1.perform()
        
        ## 코랩 페이지 들어가고 실행

        self.driver.get('https://colab.research.google.com/drive/1I_gvsqownvBD2IHZStJChccv5q5HbuOV?hl=ko')
        sleep(5)
        action2 = ActionChains(self.driver)
        action2.key_down(Keys.CONTROL).send_keys(Keys.F9).key_up(Keys.CONTROL)
        action2.perform()
        sleep(5)
        ActionChains(self.driver).key_down(Keys.SHIFT).send_keys(Keys.TAB).key_up(Keys.SHIFT).send_keys(Keys.ENTER).perform()
        sleep(8)
        ActionChains(self.driver).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
        sleep(30)

        ## trycloudflare.com 들어간 문자열 찾기 (미완성)]
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="output-body"]/div/div/div/div[2]/code')))
        result_text = element.text
        print(result_text)
        
if __name__ == "__main__":
    #  ---------- EDIT ----------
    email = '' # 이메일
    password = '' # 비번
    #  ---------- EDIT ----------                                                                                                                                                         
    
    google = Google()
    google.login(email, password)
