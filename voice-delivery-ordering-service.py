from selenium import webdriver
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import os
import time

def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        data=r.record(source,duration=3)
        print('\n')
        text=r.recognize_google(data,language='ko-kr')
    return text
def speek(string):
    tts_kr=gTTS(text=string, lang='ko')
    tts_kr.save('C:/Users/user/Desktop/temp.mp3')
    playsound('C:/Users/user/Desktop/temp.mp3')
    os.remove('C:/Users/user/Desktop/temp.mp3')
def setPos():
    speek("○○○○○○○로 주문하시겠습니까?")
    temp=listen()
    print(temp)
    if "네"in temp or "예"in temp or "얘"in temp:
        driver.find_element_by_name('address_input').clear()
        driver.find_element_by_name("address_input").send_keys('○○○○○○○○○\n')
    else:
        speek("주문할 위치를 말씀해주세요")
        temp=listen()
        driver.find_element_by_name('address_input').clear()
        driver.find_element_by_name("address_input").send_keys(temp+'\n')
        
def setCtg():
    speek("어떤 종류로 주문하시겠습니까?")
    cate=listen()
    print(cate)
    if "프랜차이즈"in cate: 
        iz=4
    elif "치킨"in cate: 
        iz=5
    elif "피자"in cate or "양식"in cate: iz=6
    elif "중국"in cate: iz=7
    elif "한식"in cate: iz=8
    elif "일식"in cate or "돈까스"in cate: iz=9
    elif "족발"in cate or "보쌈"in cate: iz=10
    elif "야식"in cate: iz=11
    elif "분식"in cate: iz=12
    elif "카페"in cate or "디저트"in cate: iz=13
    elif "편의점"in cate or "마트"in cate: iz=14
    print(cate)
    jz=str(iz)
    return jz
    
def setMenu():
    speek('무엇을 주문하시겠습니까?')
    menu=listen()
    print(menu)
    if '1'  in menu or '일'in menu:  
        return '1'
    elif '이'in menu or '2'in menu: 
        return str('2')
    elif '삼'in menu or '3'in menu:
        return str('3')
    elif '사'in menu or '4'in menu:     
        return str('4')
    elif '오'  in menu or '5'in menu:    
        return str('5')
    elif '육'  in menu or '6'in menu:  
        return str('6')
    elif '칠'  in menu or '7'in menu:  
        return str('7')
    elif '팔'  in menu or '8'in menu: 
        return str('8')
    elif '구'  in menu or '9'in menu:  
        return str('9')
    elif '십'  in menu or '10'in menu:  
        return str('10')
    elif '주문'in menu:
        return str('0')
    
def payway():
    way=listen()
    if '현금'in way:
        return '0'
    elif '카드'in way:
        return '1'
        
driver = webdriver.Chrome('C:/Users/user/Desktop/chromedriver/chromedriver')
driver.implicitly_wait(3)
driver.get('https://www.yogiyo.co.kr/mobile/#/login/')
myid='○○○○○○○○○○'
mypw='○○○○○○○○○○'
driver.find_element_by_name('loginEmail').send_keys(myid)
driver.find_element_by_name('loginPwd').send_keys(mypw,'\n')
setPos()
i=setCtg()
driver.find_element_by_xpath('//*[@id="category"]/ul/li['+i+']').click()
driver.find_element_by_xpath('//*[@id="content"]/div/div[4]/div/div[2]/div['+i+']/div/table/tbody/tr/td[2]/div/div[1]').click()
while True:
    k=setMenu()
    if k=='0': 
        driver.find_element_by_xpath('//*[@id="content"]/div[2]/div[2]/ng-include/div/div[2]/div[5]/a[2]').click()
        break
    else:
        try:
            driver.find_element_by_xpath('//*[@id="menu"]/div/div[2]/div[2]/div/ul/li['+k+']/table/tbody/tr/td[1]/div[2]').click()
            driver.find_element_by_xpath('/html/body/div[10]/div/div[3]/button[1]').click()
        except:
            speek('메뉴를 다시 선택하세요')
l=payway()
if l=='1':
    driver.find_element_by_xpath('//*[@id="content"]/div/form[1]/div[1]/div[2]/div[3]/div[2]/div/div[3]/label[1]').click()
elif l=='0':
    driver.find_element_by_xpath('//*[@id="content"]/div/form[1]/div[1]/div[2]/div[3]/div[2]/div/div[3]/label[2]').click()
