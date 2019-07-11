import os
import sys
import glob
import zipfile

import color_string as cs

def c_compile(path, nest):
    file_dir_path_list = glob.glob(path+"/*") # ファイル名とフォルダ名のリストを取得

    if len(file_dir_path_list) == 0:
        return

    #del file_dir_path_list[0] # 先頭の要素を削除
    file_dir_path_list = sorted(file_dir_path_list) # 辞書順にソート
    file_dir_name_list = [os.path.basename(r) for r in file_dir_path_list] # ファイル名のみ取得

    for path, name in zip(file_dir_path_list, file_dir_name_list):
        # もしもディレクトリなら再帰処理
        if os.path.isdir(path):
            print(cs.str_color("\t"*nest + "再帰処理を実行します\t" + path, "YELLOW"))
            c_compile(path, nest+1)
        # cファイルならばコンパイル
        elif ".c" in path:
            print(cs.str_color("\t"*nest + "ファイルをコンパイルします\t" + path, "GREEN"))
            os.system('gcc -o ' + '"' + path.strip('.c') + '" "' + path + '"')
        # それ以外は何もしない
        else:
            print(cs.str_color("\t"*nest + "その他のファイルです\t" + path, "BLUE"))


# main文
if __name__ == "__main__":
    args = sys.argv # コマンドライン引数を取得

    # 引数の数が間違っていた場合
    if len(args) != 2:
        print(str_color("コマンドライン引数の数が間違っています！"), "RED")
        print("\n使い方\n")
        print("python " + args[0] + " フォルダのパス ")
        sys.exit()

    c_compile(args[1], 0)
