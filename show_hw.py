import os
import sys
sys.path.append("C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml")

i = 0



while (i < 23):
    i += 1
    if (i == 18 ): continue
    print(f"graph{i}")

    os.system("python -m mlgame -f 120 --one-shot -i ./ml/ml_play.py . --difficulty NORMAL --level " + str(i))
    
    