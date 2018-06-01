import pandas as pd
import matplotlib.pyplot as mlpt
from matplotlib import style
style.use('ggplot')

web_stats = {'Day': [1, 2, 3, 4, 5, 6, 7],
             'Bounce_Rate': [34, 45, 64, 38, 56, 44, 52],
             'Visitors': [59, 78, 45, 39, 74, 55, 59]
             }
df = pd.DataFrame(web_stats)
print(df)
print(df.head())
df.set_index('Day', inplace=True)
print(df)
