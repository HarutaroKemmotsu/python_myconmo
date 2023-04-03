#Winmergeを起動し比較するためのモジュール######################################

def up_win(File1,File2):

    import os.path #ファイル確認のためのモジュール
    import subprocess #WinMergeを開くためのモジュール

    if os.path.exists(File1) and os.path.exists(File2): #二つのファイルが存在したとき真
            return subprocess.run(["C:\Program Files\WinMerge\WinMergeU.exe", File1, File2], check=True) #Winmerge起動させ二つのファイル比較
    else:
        print ("→ファイル読み込みに失敗しました\n")
        #ファイルが存在しない時、返り値をfalseとしておく
        return "false"
