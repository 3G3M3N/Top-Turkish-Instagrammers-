import pandas as pd
import numpy as np
df = pd.read_csv("top_1000_instagrammers.csv")
asd = df.loc[(df["Audience Country"]=="Turkey")]
asd.shape
