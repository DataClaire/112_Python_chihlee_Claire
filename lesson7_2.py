import tools

def main():
    while(True):
        tools.playGame()
        playAgain = input(f"您還要繼續嗎？(y,n)")
        if playAgain == "n":
            break

print("遊戲結束")

if __name__ == "__main__": #(我自己的說法)如果檔名指定某個執行檔，就執行該檔。
    main()

#可以有很多專案檔(py檔)，有被python執行的執行檔，其檔名之程式語言為__name__，字串是"__main__；沒被執行的就叫做module。
#以tools.py專案檔為例，不是執行檔，是模組module，其檔名之程式語言為為__name__，字串為"__tools__"。