import pandas as pd
import sys

def split_csv_file(pathname, row_size):
    data = pd.read_csv(pathname, encoding='utf8')
    data = data.sort_values(['datadate'], ascending=True) #sort by column: datadate
    data = data.reset_index(drop=True)
    size_chunk = int(data.shape[0] / row_size) + 1

    for x in range(size_chunk):
        if data.shape[0] >= row_size:
            data_temp = data.head(row_size)
        else:
            data_temp = data.head(data.shape[0])
        data_temp.to_csv("data_split_%02d.csv" % x, index=None, header=True)
        data.drop(data.index[list(data_temp.index)], inplace=True)
        data = data.reset_index(drop=True)
        print("data_split_%02d.csv" % x, " created with size %d" % data_temp.shape[0]," rows")

if len(sys.argv) <=2:
    print("input not enough")
    print("python split_file.py <path csv> <small csv row size>")
    print("eg: python split_file.py", "'D:\input.csv'", "10000")
else:
    filepath = sys.argv[1]
    rowsize = int(sys.argv[2])
    split_csv_file(filepath, rowsize)