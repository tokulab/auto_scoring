import subprocess
import os
import sys
import glob

import color_string as cs

def count_characters(path):
    count = 0
    with open(path) as f:
        while True:
            c = f.read(1)
            if not c:
                break
            count += 1
    return str(count)

def count_lines(path):
    count = 0
    with open(path) as f:
        for line in f:
            count += 1
    return str(count)

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
        #elif "19rd097" in path or "19rd123" in path or "1XrdXXX" in path: 
        elif "19rd021" in path or "19rd023" in path or "19rd097" in path or "19rd114" in path or "17rd045" in path or "18rd028" in path or "18rd074" in path or "18rd129" in path or "18rd154" in path or "19rd018" in path or "19rd020" in path or "19rd084" in path or "19rd099" in path or "19rd155" in path or "19rd157" in path or "17rd415" in path or "19RD123" in path or "19rd169" in path or "19rd118" in path:
            print(cs.str_color("問題が発生したため実行をスキップします", "RED"))
            return
        # cファイルなら何もしない
        elif ".c" in name:
            print(cs.str_color("\t"*nest + "cファイルです\t" + path, "BLUE"))
            print(cs.str_color("\t"*(nest+1) + "行数\t" + count_lines(path), "PURPLE"))
            print(cs.str_color("\t"*(nest+1) + "文字数\t" + count_characters(path), "PURPLE"))
        # 9番の実行ファイルを実行する
        #elif "09" in name:
        elif name[-1] == "9":
            print(cs.str_color("\t"*nest + "プログラムを実行します\t" + path, "GREEN"))
            p = subprocess.Popen([path], stdin=subprocess.PIPE, stdout=subprocess.PIPE) #
            print(p.communicate("5\n".encode())[0].decode())
        # その他のファイルの場合
        else:
            print(cs.str_color("\t"*nest + "その他のファイルです\t" + path, "BLUE"))

# main文
if __name__ == "__main__":
    #subprocess.call("ls")
    args = sys.argv # コマンドライン引数を取得

    # 引数の数が間違っていた場合
    if len(args) != 2:
        print(cs.str_color("コマンドライン引数の数が間違っています！", "RED"))
        print("\n使い方\n")
        print("python " + args[0] + " フォルダのパス ")
        sys.exit()

    exe(args[1], 0)
