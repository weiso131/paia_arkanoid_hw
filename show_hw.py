import os
import sys
sys.path.append("C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml")





for i in range(1, 25):
    if (i == 18 or i == 24):
        print("沒訓練這關")
    print(f"graph{i}")
    os.system("python -m mlgame -f 120 --one-shot -i ./ml/ml_play.py . --difficulty NORMAL --level " + str(i))
    
    