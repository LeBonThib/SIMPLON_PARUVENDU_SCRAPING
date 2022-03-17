#%%
import pandas as pd
import json

#%%
data = []
with open('../paruvendu_api/outputs/data_harvest1.json','r') as sample:
    for line in sample:
        data.append(json.loads(line.strip()))

with open('../paruvendu_api/outputs/data_harvest2.json','r') as sample:
    for line in sample:
        data.append(json.loads(line.strip()))

with open('../paruvendu_api/outputs/data_harvest3.json','r') as sample:
    for line in sample:
        data.append(json.loads(line.strip()))

with open('../paruvendu_api/outputs/data_harvest4.json','r') as sample:
    for line in sample:
        data.append(json.loads(line.strip()))

with open('../paruvendu_api/outputs/data_harvest5.json','r') as sample:
    for line in sample:
        data.append(json.loads(line.strip()))     

#%%
df = pd.DataFrame.from_dict(data)

#%%
df.head()

#%%
file = df.to_json('../paruvendu_api/outputs/data_harvest_full.json', orient='records', lines=True)
# %%
