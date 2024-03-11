import os
import sys
sys.path.append("C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml")

i = 1



while (i < 25):
    print(f"graph{i}")

    os.system("python -m mlgame -f 120 --one-shot -i ./ml/ml_play_template.py . --difficulty NORMAL --level " + str(i))

    
    x = input("continue(y/n/r)")
    path = 'C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml/graph'
    data_list = os.listdir(path)
    if (x == "y"):
        if (os.path.exists(path + "/graph" + str(i)) != True):
            os.mkdir(path + "/graph" + str(i))
            for data_path in data_list:
                if (".pickle" in data_path):
                    os.rename(path + "/" + data_path, path + "/graph" + str(i) + '/' + data_path)
            

    for data_path in data_list:
        if (".pickle" in data_path and os.path.exists(path + "/" + data_path)):
            os.remove(path + "/" + data_path)

    if (x == "n"): 
        break
    elif (x == "r"):
        continue
    i += 1
    
#& C:/Users/weiso131/anaconda3/envs/AI/python.exe c:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml/data_collect.py



    