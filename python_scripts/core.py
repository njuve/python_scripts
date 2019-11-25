import pandas as pd
import glob

def read_csvs(path, index_col = None, header = 0):
    all_files = glob.glob(path + "/*.csv")
    frame = pd.DataFrame()
    list_ = []
    for file_ in all_files:
        df = pd.read_csv(file_, index_col=index_col, header=header)
        list_.append(df)
    frame = pd.concat(list_)
    return frame