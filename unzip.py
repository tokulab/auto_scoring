import os
import sys
import glob
import zipfile

import color_string as cs

# main文
if __name__ == "__main__":
    args = sys.argv # ↲コマンドライン引数を取得

    # 引数の数が間違っていた場合
    if len(args) != 3:
        print(cs.str_color("コマンドライン引数の数が間違っています！", "RED"))
        print("\n使い方\n")
        print("python " + args[0] + " フォルダのパス " + "csvの保存先のパス")
        sys.exit()

    # ファイル・ディレクトリのリストを取得
    source_list = glob.glob(args[1]+"/*") # ファイル名とフォルダ名取得
    del source_list[0]# 先頭の要素()を削除
    source_list = sorted(source_list) # 辞書順にソート

    # 全ファイルを解凍
    for source in source_list:
        zip_file_name = glob.glob(source+"/*") # ファイル名とフォルダ名を取得

        if len(zip_file_name) == 0:
            print(cs.str_color(source.ljust(64) + "フォルダが空です！", "RED"))
            continue

        # zipファイルの場合
        if '.zip' in zip_file_name[0]:
            print(source.ljust(64) + cs.str_color("zip file!", "GREEN"))
            with zipfile.ZipFile(zip_file_name[0]) as existing_zip:
                existing_zip.extractall(args[2] + "/" + os.listdir(source+"/")[0].strip(".zip").lower())

        # rarファイルの場合
        elif '.rar' in zip_file_name[0]:
            print(cs.str_color(source.ljust(64) + "rar file!", "RED"))
            #with rarfile.RarFile(zip_file_name[0]) as existing_rar:
            #    existing_rar.extractall(args[2] + "/" + os.listdir(source+"/")[0].strip(".zip"))

        # ディレクトリの場合
        elif os.path.isdir(zip_file_name[0]):
            print(cs.str_color(source.ljust(64) + "ディレクトリです！", "RED"))

        else:
            print(cs.str_color(source.ljust(64) + "不明なファイルです！", "RED"))

        #time.sleep(1)
