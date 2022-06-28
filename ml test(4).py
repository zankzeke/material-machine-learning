# dataframes特征化（Featurizing dataframes）
# 将ElementFraction 应用于所有数据
from matminer.datasets.dataset_retrieval import load_dataset
df = load_dataset("brgoch_superhard_training")   # 取超硬材料数据库
print(df.head())
print("---" * 20)
import pandas as pd
# 显示Dateframe所有列（参数设置为None代表显示所有行，也可以自行设置数字）
pd.set_option('display.max_columns',None)
# Dateframe自动换行（Flase关闭自动换行）
pd.set_option('expand_frame_repr',False)
from matminer.featurizers.composition import ElementFraction

ef = ElementFraction()

if __name__ == '__main__':
    df = ef.featurize_dataframe(df,"composition")

print(df.head())
