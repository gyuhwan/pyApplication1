
gun = 10
a= "Life is too short, You need Python"

b = a[5:7]
print(b)

import requests

def get_lotto_numbers():
    url = "https://www.fullayer.com/lottowinnumber/fo/lottowinnumberlist"
    response = requests.get(url)
    print(response.content )
    # 여기서 당첨번호 정보를 파싱하여 텍스트 파일로 저장하는 로직을 추가하세요.


def profile(name, age = 45, main_lang = "Python") :
    gun = 20
    print("이름 : {0}\t나이 : {1}\t사용언어 : {2}"\
          .format(name, age, main_lang))

def Profile2( name, age, *language):
    global gun 
    gun = 100
    print("이름 : {0}\t나이 : {1}\t사용언어 :".format(name, age), end=" ")
    for lang in language :
        print(lang, end =" ")
    print()

def chechNumber_ret(gun, solger):
    gun = gun - solger
    return gun


def stdWeight( height, gender):
    mHeight = height / 100
    if gender == "남자" :
        stdWeight = mHeight * mHeight * 22
    elif gender == "여자" :
        stdWeight = mHeight * mHeight * 21
    
    print( "키 %dcm %s의 표준 체중은 %.2fkg 입니다"% (height, gender, stdWeight ))


get_lotto_numbers()

print(a)

print("gun : {0}".format(gun))
profile("유재석", 50, "Python")
print("gun : {0}".format( gun))
profile( age= 55, main_lang="Python", name="조세호")

Profile2("박명수", 57, "Python", "C", "C#",  "Java")
gun = chechNumber_ret( 30, 5)

print("gun : {0}".format(gun))

stdWeight(175, "남자")
stdWeight(175, "여자")

print("java", "python", end="?\n\r")
print("무엇?")