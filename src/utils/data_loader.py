from preprocessing import preprocess_data
import pandas as pd
from config import INPUT_DATA_PATH,OUTPUT_DATA_PATH

df=pd.read_csv(INPUT_DATA_PATH)

df=preprocess_data(df)

df.to_csv(OUTPUT_DATA_PATH,index=False)
