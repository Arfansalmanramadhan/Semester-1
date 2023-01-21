

import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
import json
import requests
import numpy as np
import pandas as pd
import os
from IPython.display import display
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))


countries_data = pd.read_csv(
    r'Metadata_Country_API_NY.GDP.MKTP.KD.ZG_DS2_en_csv_v2_4701072.csv').iloc[:, :-1]
display(countries_data.head(), countries_data.shape)


data_url = 'https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson'
response = requests.get(data_url)
print(response.status_code)
income_order = {'High income': 4, 'Upper middle income': 3,
                'Lower middle income': 2, 'Low income': 1, 'Unavailable': 0}
countries_data['Incomeint'] = countries_data.IncomeGroup
# force to convert data type to Int, needed to make legend later
countries_data['Incomeint'] = countries_data.Incomeint.replace(
    income_order).astype('Int64')

# merge the two dataframes, default is inner. We need to be able to paint most of the map.
merged = geo_data.merge(countries_data, left_on='ISO_A3',
                        right_on='Country Code')
merged.head()

palette = sns.light_palette('steelblue', as_cmap=True)
fig, ax = plt.subplots(1, 1, figsize=(20, 20))
divider = make_axes_locatable(ax)
merged.plot(column='Incomeint', cmap=palette,
            categorical=True, legend=True, ax=ax)
ax = plt.gca()

plt.fill_between(x=np.arange(-200, 200), y1=-23,
                 y2=23, alpha=0.03, color='yellow')


def replace_legend_items(legend, mapping):
    for txt in legend.texts:
        for k, v in mapping.items():
            if txt.get_text() == str(k):
                txt.set_text(v)


legend_order = {4: 'High income', 3: 'Upper middle income',
                2: 'Lower middle income', 1: 'Low income', 0:  'Unavailable'}
replace_legend_items(ax.get_legend(), legend_order)
plt.show()
