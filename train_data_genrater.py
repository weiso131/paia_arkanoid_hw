from tool.data_clean import data_compare
from tool.data_generator import get_graph
from os import listdir
import pickle
def pickle_read(path):
    with open(path, 'rb') as f:
        
        data = pickle.load(f)
        return data

path = "C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml/"

# for dir_path in listdir(path + "graph/"):
#     print(dir_path)
#     data_list = listdir(path + "graph/" + dir_path)
#     for i in range(len(data_list) - 2, -1, -1):
#         for j in range(len(data_list) - 1, i, -1):
#             #print(f"new:{data_list[i]}, old:{data_list[j]}")
#             data_compare(old_data_path=path + "graph/" + dir_path + '/' + data_list[j], new_data_path=path + "graph/" + dir_path + '/' + data_list[i])

print("清理完畢")
i = 0
for dir_path in listdir(path + "graph/"):
    print(dir_path)
    data_list = listdir(path + "graph/" + dir_path)
    for data_path in data_list:
        datas = pickle_read(path + "graph/" + dir_path + '/' + data_path)
        train_data = []
        for data in datas:
            graph_data = get_graph(data[0])

            train_data.append((graph_data, data[1]))


        name = str(i).zfill(4)
        with open("C:/Users/weiso131/Desktop/paia2.4.5/resources/app.asar.unpacked/games/arkanoid/ml/train_data/" + name + ".pickle", "wb") as f:
            pickle.dump(train_data, f)

        i += 1


