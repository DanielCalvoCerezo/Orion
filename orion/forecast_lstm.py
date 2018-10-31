import tensorflow as tf
import pandas as pd

data_path = ""
pid_df = pd.read_csv(data_path, header=None, parse_dates=[3], names=["row_id","pid","ts","val"])

print pid_df.head()




