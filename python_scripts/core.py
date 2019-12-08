import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import glob


def read_csvs(path, index_col=None, header=0):
    all_files = glob.glob(path + "/*.csv")
    frame = pd.DataFrame()
    list_ = []
    for file_ in all_files:
        df = pd.read_csv(file_, index_col=index_col, header=header)
        list_.append(df)
    frame = pd.concat(list_).reset_index(drop=True)
    return frame


def missing_info(df, title=None):
    print(title)
    sum_missing = df.isnull().sum()
    ratio_missing = df.isnull().sum()/df.shape[0]

    missing_table = pd.DataFrame({
                            'sum': sum_missing,
                            'ratio': ratio_missing
                        })
    return missing_table


def _take_patch_info(patch):
    return patch.get_height(), patch.get_x() + patch.get_width()/2


def plot_bar_with_pval_lines(feature, data, signficant_pairs):
    fig, ax = plt.subplots(1, 1)

    g = sns.countplot(
        feature,
        data=data,
        order=data[feature].value_counts().index,
        ax=ax
    )

    # Remove right and top frame
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)

    patches = ax.patches
    for pair in signficant_pairs:
        patch1 = patches[pair[0]]
        patch2 = patches[pair[1]]

        height1, center1 = _take_patch_info(patch1)
        height2, center2 = _take_patch_info(patch2)
        max_height = max(height1, height2)

        # Draw a signficant mark and a line like rotated "]"
        ax.vlines(center1, max_height + 1, max_height + 3)
        ax.vlines(center2, max_height + 1, max_height + 3)
        ax.hlines(max_height + 3, center1, center2)
        ax.text(np.mean([center1, center2]), max_height + 4, '*')


def multiple_lambda(df, col1, col2):
    return list(map(lambda x, y: x + y, df[col1], df[col2]))