import subprocess
import os
import sys
import glob

import color_string as cs

def exe(path, nest):
    # ディレクトリ内のファイル名とフォルダ名をリストとして取得
    file_dir_path_list = glob.glob(path+"/*") 

    # ディレクトリの中身が空の場合は終了
    if len(file_dir_path_list) == 0:
        return

    file_dir_path_list = sorted(file_dir_path_list) # 辞書順にソート
    file_dir_name_list = [os.path.basename(r) for r in file_dir_path_list] # ファイル名のみ取得

    for path, name in zip(file_dir_path_list, file_dir_name_list):
        # ディレクトリの場合
        if os.path.isdir(path):
            print(cs.str_color("\t"*nest + "再帰処理を実行します\t" + path, "YELLOW"))
            exe(path, nest+1)
        # 排除するディレクトリ
        #elif "19rd021" in path or "19rd023" in path or "19rd097" in path or "19rd114" in path:
        #    return
        # cファイルなら何もしない
        elif ".c" in name:
            print(cs.str_color("\t"*nest + "cファイルです\t" + path, "BLUE"))
        # 9番の実行ファイルを実行する
        #elif "09" in name:
        elif name[-1] == "6":
            print(cs.str_color("\t"*nest + "プログラムを実行します\t" + path, "GREEN"))
            p = subprocess.Popen([path], stdin=subprocess.PIPE, stdout=subprocess.PIPE) #
            print(p.communicate("informal information\n".encode())[0].decode())
        # その他のファイルの場合
        else:
            print(cs.str_color("\t"*nest + "その他のファイルです\t" + path, "BLUE"))

# main文
if __name__ == "__main__":
    #subprocess.call("ls")
    args = sys.argv # コマンドライン引数を取得

    # 引数の数が間違っていた場合
    if len(args) != 2:
        print(cs.str_color("コマンドライン引数の数が間違っています！"), "RED")
        print("\n使い方\n")
        print("python " + args[0] + " フォルダのパス ")
        sys.exit()

    exe(args[1], 0)
