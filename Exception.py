class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("한자리 나누기 전용 계산기입니다.")

    num1 = int(input("첫번째 숫자: "))
    num2 = int(input("두번째 숫자: "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("10 이상의 숫자를 입력할 수 없습니다.")
    print(f"{num1} / {num2} = {int(num1 / num2)}")


except ZeroDivisionError as err:
    print("{}".format(err))
except ValueError :
    print("잘못된 값이 입력되었습니다.")
except BigNumberError as err:
    print("한자리 숫자만 입력할 수 있습니다. :{}.".format(err))
except Exception as err: 
    print(err)    