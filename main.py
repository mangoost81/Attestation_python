import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})


sets = data['whoAmI'].unique()

onehot = pd.DataFrame()

for i in sets:
    onehot[i] = (data['whoAmI'] == i).astype(int)

print(onehot)