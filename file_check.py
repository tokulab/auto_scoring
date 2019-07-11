import os
import sys
import glob

import color_string as cs

# main文
if __name__ == "__main__":
    args = sys.argv # ↲コマンドライン引数を取得

    # 引数の数が間違っていた場合
    if len(args) != 2:#3:
        print(str_color("コマンドライン引数の数が間違っています！"), "RED")
        print("\n使い方\n")
        print("python " + args[0] + " フォルダのパス ")# + "csvの保存先のパス")
        sys.exit()

    # ファイル・ディレクトリのリストを取得
    dic_list = glob.glob(args[1]+"/*") # 取得
    del dic_list[0]# 先頭の要素を削除
    dic_list = sorted(dic_list) # 辞書順にソート
    #print(dic_list)

    #
    print("name".ljust(64) + "folder".ljust(16) + "file num".ljust(16))
    for i in dic_list:
        print(i.ljust(64) + cs.bool_color(os.path.isdir(i)) + cs.count_color(len(glob.glob(i+"/*"))))
