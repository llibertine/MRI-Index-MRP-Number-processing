import numpy as np
import pandas as pd

# CSV import into pandas
df = pd.read_csv("C:/path/result2016.csv")

# column "Number" change to string
df["Number"] = df["Number"].astype(str)

# slice all but the two first positions of the MRP-numbers
# 0 = start, -12 = end, 1 = step
df["Number"]= df["Number"].str.slice(0, -12, 1)

# write saved list to csv again, without index
df.to_csv("C:/Users/libertine/Desktop/result2016-sliced.csv", index = None)

# count a certain MRP-country in column and return sum
substring = "DE"
print(df.Number.str.count(substring).sum())
