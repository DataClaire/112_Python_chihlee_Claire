import random

def playGame():
    min = 1
    max = 100
    count = 0
    target = random.randint(min,max)
    print(f"答案是:{target}")
    print("============猜數字遊戲=================\n")
    while(True):
        keyin = int(input(f"猜數字的範圍{min}~{max}:"))
        count += 1
        if(keyin >= min and keyin <= max):
            if keyin == target:
                print(f"賓果!猜對了, 答案是:{keyin}")
                break
            elif keyin > target:
                print("再小一點")
                max = keyin - 1
            elif keyin < target:
                print("再大一點")
                min = keyin + 1
            print(f"加油!您已經猜了{count}次")
            continue
        else:
            print("請輸入提示範圍內的數字")
    print(f"您猜了{count}次")


class Student():
    def __init__(self, name:str,chinese:int,english:int,math:int): #self代表我自己這個實體
        self.name = name               #為自己這個實體建立四個attribute = 自訂初始化的設定
        self.chinese = chinese
        self.english = english
        self.math = math

    def sum(self)->int:   #在class裡稱為功能function,在實體裡稱為方法method; method只能在實體執行
        return self.chinese + self.english + self.math 
    
def getStudent(name:str, chinese=int, english=int, math=int) -> Student:
    return Student(name=name, chinese=chinese, english=english, math=math)