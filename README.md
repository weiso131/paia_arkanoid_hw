# 基於遊戲的機器學習入門第一次作業

## 成果展示

https://github.com/weiso131/paia_arkanoid_hw/assets/131360912/fce54b6d-d9df-4313-9677-549589b908a4

## 模型訓練
### 資料收集
1. 執行data_collect.py，使用ml_play_template.py的算法打磚塊
2. ml_play_template.py充滿了各種random，收集資料時可以重複玩某一關直到通關
3. 收集到的資料會存成.pickle，會儲存磚塊、球、盤子的位置、執行的動作等資料(詳見ml_play_template.py)
### 資料清理與轉換
1. train_data_generator.py會使用tool.data_clean.data_compare()來確保同樣的情況，都記錄相同的動作
2. 會以越接近結尾的資料其紀錄的動作為準
3. 清理完畢後，會將所儲存的資料的位置全部標示到np_array上(使用tool.data_generator.get_graph())，並以.pickle儲存

### 使用pytorch CNN做訓練
1. 由於關卡是固定的，過擬和似乎變成一個好選擇???
2. 礙於時間(其實是懶)，我沒有蒐集第18和24關的資料，如果有蒐集應該也能通關

