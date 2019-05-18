import pandas as pd

# data_train = []
# headers = []
#
# with open("../data/raw/zhengqi_train.txt") as f:
#     first_line = f.readline()
#     headers = first_line.split()
#     for i in f.readlines():
#         if len(i.split()) != 39:
#             print(i)
#             continue
#         data_train.append(i.split())
#
# df_train = pd.DataFrame(data_train)
#
# print(df_train)
# df_train.to_csv("../data/df/df_train.csv", header=headers)


data_test = []
headers = []

with open("../data/raw/zhengqi_test.txt") as f:
    first_line = f.readline()
    headers = first_line.split()
    for i in f.readlines():
        if len(i.split()) != 38:
            print(i)
            continue
        data_test.append(i.split())

df_test = pd.DataFrame(data_test)

df_test.to_csv("../data/df/df_test.csv", header=headers)
