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

#可以有很多專案檔(py檔)，有被python執行的專案檔，其檔名之程式語言為__name__，顯示為字串"__main__；沒被執行的就叫做模組module。
#以tools.py專案檔為例，其不是執行檔，是模組module，其檔名之程式語言為為__name__，顯示為字串"__tools__"。