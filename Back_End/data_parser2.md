

```python
names_all = ['all_size','boy_size','girl_size','all_height','all_weight','boy_height',
         'boy_weight','girl_height','girl_weight','boy_top_long_chest',
         'boy_top_long_sleeve','boy_top_long_height','boy_top_long_sweep',
         'boy_top_long_undefined','boy_top_short_chest','boy_top_short_sleeve',
         'boy_top_short_height','boy_top_short_sweep','boy_bottom_pants_height',
         'boy_bottom_pants_crotch','boy_bottom_pants_waist','boy_bottom_pants_hip',
         'boy_bottom_pants_inseam','boy_bottom_pants_adjustable','boy_bottom_short_waist',
         'boy_bottom_short_hip','boy_bottom_short_inseam','boy_bottom_short_adjustable',
         'girl_top_long_chest','girl_top_long_sleeve','girl_top_long_height','girl_top_long_sweep',
         'girl_top_short_chest','girl_top_short_sleeve','girl_top_short_height',
         'girl_top_short_sweep','girl_bottom_long_waist','girl_bottom_long_hip','girl_bottom_long_inseam',
         'girl_bottom_long_adjustable','girl_bottom_short_waist','girl_bottom_short_hip',
         'girl_bottom_short_inseam','girl_bottom_short_adjustable','girl_dress_hollow_to_floor',
         'girl_dress_bust', 'girl_dress_waist','girl_dress_hips','girl_dress_sleeve',
         'girl_dress_inseam','girl_dress_height']
```


```python
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import codecs
import csv
```


```python
file = pd.read_csv('data_v8.csv', names = names_all)
```


```python
file.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>all_size</th>
      <th>boy_size</th>
      <th>girl_size</th>
      <th>all_height</th>
      <th>all_weight</th>
      <th>boy_height</th>
      <th>boy_weight</th>
      <th>girl_height</th>
      <th>girl_weight</th>
      <th>boy_top_long_chest</th>
      <th>...</th>
      <th>girl_bottom_short_hip</th>
      <th>girl_bottom_short_inseam</th>
      <th>girl_bottom_short_adjustable</th>
      <th>girl_dress_hollow_to_floor</th>
      <th>girl_dress_bust</th>
      <th>girl_dress_waist</th>
      <th>girl_dress_hips</th>
      <th>girl_dress_sleeve</th>
      <th>girl_dress_inseam</th>
      <th>girl_dress_height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>NaN</th>
      <td>Sizes for all</td>
      <td>Boy size</td>
      <td>Girl size</td>
      <td>All</td>
      <td>NaN</td>
      <td>Boy</td>
      <td>NaN</td>
      <td>Girl</td>
      <td>NaN</td>
      <td>boy Top (long sleeve)</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Girl Dress</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Brand</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Height</td>
      <td>Weight</td>
      <td>Height</td>
      <td>Weight</td>
      <td>Height</td>
      <td>Weight</td>
      <td>Chest</td>
      <td>...</td>
      <td>Hip</td>
      <td>Inseam</td>
      <td>Adjustable Y/N</td>
      <td>Hollow to Floor</td>
      <td>Bust</td>
      <td>Waist</td>
      <td>Hips</td>
      <td>sleeve</td>
      <td>Inseam</td>
      <td>height</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>6-9mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>9-12mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>12-18mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 51 columns</p>
</div>




```python
file = file.iloc[2:]
file["boy_actual_height"] = np.nan
file["girl_actual_height"] = np.nan
```


```python
import re
unit = None
def checkUnit(data):
    unit = None
    if data[-1] is "\"":
        unit = 'inches'
    elif data[-2:] is 'cm' or 'CM':
        unit = 'cm'
    return unit

def heightParser(data, unit):
    if data is None:
        return
    nums = data.split('-')
    if unit is 'cm':
        return float(re.findall(r'\d+\.?\d+', nums[len(nums) - 1])[0])
    else:
        return float(re.findall(r'\d+\.?\d+', nums[len(nums) - 1])[0]) * 2.54  
```


```python
def height_generalizer(data, unit):
    if data is None:
        return
    nums = re.findall(r'\d+\.?\d+', data)
    if len(nums) is 1:
        return nums[0] + unit
    else:
        return nums[0] + '-' + nums[1] + unit
```


```python
# names_all = ['all_size','boy_size','girl_size','all_height','all_weight','boy_height',
#        'boy_weight','girl_height''girl_weight','boy_top_long_chest',
#         'boy_top_long_sleeve','boy_top_long_height','boy_top_long_sweep',
#         'boy_top_long_undefined','boy_top_short_chest','boy_top_short_sleeve',
#         'boy_top_short_height','boy_top_short_sweep','boy_bottom_pants_height',
#        'boy_bottom_pants_crotch','boy_bottom_pants_waist','boy_bottom_pants_hip',
#         'boy_bottom_pants_inseam','boy_bottom_pants_adjustable','boy_bottom_short_waist',
#         'boy_bottom_short_hip','boy_bottom_short_inseam','boy_bottom_short_adjustable',
#         'girl_top_long_chest','girl_top_long_sleeve','girl_top_long_height','girl_top_long_sweep',
#         'girl_top_short_chest','girl_top_short_sleeve','girl_top_short_height',
#         'girl_top_short_sweep','girl_bottom_long_waist','girl_bottom_long_hip','girl_bottom_long_inseam',
#         'girl_bottom_long_adjustable','girl_bottom_short_waist','girl_bottom_short_hip',
#         'girl_bottom_short_inseam','girl_bottom_short_adjustable','girl_dress_hollow_to_floor',
#         'girl_dress_bust', 'girl_dress_waist','girl_dress_hips','girl_dress_sleeve',
#         'girl_dress_inseam','girl_dress_height']
all_height = file['all_height'].values
boy_height = file['boy_height'].values
girl_height = file['girl_height'].values
boy_actual_height = file['boy_actual_height'].values
girl_actual_height = file['girl_actual_height'].values
boy_top_long_height = file['boy_top_long_height'].values
boy_top_short_height = file['boy_top_short_height'].values
boy_bottom_pants_height = file['boy_bottom_pants_height'].values
girl_top_long_height = file['girl_top_long_height'].values
girl_top_short_height = file['girl_top_short_height'].values
girl_dress_height = file['girl_dress_height'].values
```


```python
import math  # math.isnan(x) check if x is nan
unit = None
for i in range(len(all_height)):
    if type(all_height[i]) is str or math.isnan(all_height[i]) is False:
        data = str(all_height[i])
        if checkUnit(data) is not None:
            unit = checkUnit(data)
        ah = None
        try:
            ah = heightParser(data, unit)
        except ValueError as ve:
            print('could not convert string to float')
        except IndexError as ie:
            print('index out of range')
        general_height = height_generalizer(data, unit)
        if general_height is not None:
            all_height[i] = general_height
        boy_actual_height[i] = ah
        girl_actual_height[i] = ah
for i in range(len(boy_height)):
    if type(boy_height[i]) is str or math.isnan(boy_height[i]) is False:
        data = str(boy_height[i])
        if checkUnit(data) is not None:
            unit = checkUnit(data)
        bh = None
        try:
            bh = heightParser(data, unit)
        except ValueError as ve:
            print('could not convert string to float')
        except IndexError as ie:
            print('index out of range')
        general_height = height_generalizer(data, unit)
        if general_height is not None:
            boy_height[i] = general_height
        boy_actual_height[i] = bh
for i in range(len(girl_height)):
    if type(girl_height[i]) is str or math.isnan(girl_height[i]) is False:
        data = str(girl_height[i])
        if checkUnit(data) is not None:
            unit = checkUnit(data)
        gh = None
        try:
            gh = heightParser(data, unit)
        except ValueError as ve:
            print('could not convert string to float')
        except IndexError as ie:
            print('index out of range')
        general_height = height_generalizer(data, unit)
        if general_height is not None:
            girl_height[i] = general_height
        girl_actual_height[i] = gh
for i in range(len(boy_top_long_height)):
    if math.isnan(boy_actual_height[i]) is False:
        continue
    if type(boy_top_long_height[i]) is str or math.isnan(boy_top_long_height[i]) is False:
        data = str(boy_top_long_height[i])
        if checkUnit(data) is not None:
            unit = checkUnit(data)
        gh = None
        try:
            gh = heightParser(data, unit)
        except ValueError as ve:
            print('could not convert string to float')
        except IndexError as ie:
            print('index out of range')
        general_height = height_generalizer(data, unit)
        if general_height is not None:
            boy_top_long_height[i] = general_height
        boy_actual_height[i] = gh
        
for i in range(len(boy_top_short_height)):
    if math.isnan(boy_actual_height[i]) is False:
        continue
    if type(boy_top_short_height[i]) is str or math.isnan(boy_top_short_height[i]) is False:
        data = str(boy_top_short_height[i])
        if checkUnit(data) is not None:
            unit = checkUnit(data)
        gh = None
        try:
            gh = heightParser(data, unit)
        except ValueError as ve:
            print('could not convert string to float')
        except IndexError as ie:
            print('index out of range')
        general_height = height_generalizer(data, unit)
        if general_height is not None:
            boy_top_short_height[i] = general_height
        boy_actual_height[i] = gh
        
for i in range(len(girl_top_long_height)):
    if math.isnan(girl_actual_height[i]) is False:
        continue
    if type(girl_top_long_height[i]) is str or math.isnan(girl_top_long_height[i]) is False:
        data = str(girl_top_long_height[i])
        if checkUnit(data) is not None:
            unit = checkUnit(data)
        gh = None
        try:
            gh = heightParser(data, unit)
        except ValueError as ve:
            print('could not convert string to float')
        except IndexError as ie:
            print('index out of range')
        general_height = height_generalizer(data, unit)
        if general_height is not None:
            girl_top_long_height[i] = general_height
        girl_actual_height[i] = gh
        
for i in range(len(girl_dress_height)):
    if math.isnan(girl_actual_height[i]) is False:
        continue
    if type(girl_dress_height[i]) is str or math.isnan(girl_dress_height[i]) is False:
        data = str(girl_dress_height[i])
        if checkUnit(data) is not None:
            unit = checkUnit(data)
        gh = None
        try:
            gh = heightParser(data, unit)
        except ValueError as ve:
            print('could not convert string to float')
        except IndexError as ie:
            print('index out of range')
        general_height = height_generalizer(data, unit)
        if general_height is not None:
            girl_dress_height[i] = general_height
        girl_actual_height[i] = gh
```


```python
file['boy_actual_height'] = boy_actual_height
file['girl_actual_height'] = girl_actual_height
file
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>all_size</th>
      <th>boy_size</th>
      <th>girl_size</th>
      <th>all_height</th>
      <th>all_weight</th>
      <th>boy_height</th>
      <th>boy_weight</th>
      <th>girl_height</th>
      <th>girl_weight</th>
      <th>boy_top_long_chest</th>
      <th>...</th>
      <th>girl_bottom_short_adjustable</th>
      <th>girl_dress_hollow_to_floor</th>
      <th>girl_dress_bust</th>
      <th>girl_dress_waist</th>
      <th>girl_dress_hips</th>
      <th>girl_dress_sleeve</th>
      <th>girl_dress_inseam</th>
      <th>girl_dress_height</th>
      <th>boy_actual_height</th>
      <th>girl_actual_height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>#sen</th>
      <td>6-9mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>9-12mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>12-18mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>18-24mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>2Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>3Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>4Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>5Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>6Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>6X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>7Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>8Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>10Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>12Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>#sen</th>
      <td>14Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>NaN</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>NaN</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7 for All Mankind</th>
      <td>9-12mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>30.5cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>19"</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>30.5</td>
      <td>30.5</td>
    </tr>
    <tr>
      <th>7 for All Mankind</th>
      <td>12-18mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>32cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>19 3/4"</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>32.0</td>
      <td>32.0</td>
    </tr>
    <tr>
      <th>7 for All Mankind</th>
      <td>18-24mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>35cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20 1/2"</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>35.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>7 for All Mankind</th>
      <td>2Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>35cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>20 1/2"</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>35.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>7 for All Mankind</th>
      <td>3Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>38cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>21"</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>38.0</td>
      <td>38.0</td>
    </tr>
    <tr>
      <th>7 for All Mankind</th>
      <td>4Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>22"</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>7 for All Mankind</th>
      <td>5Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>43.5cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>23"</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>43.5</td>
      <td>43.5</td>
    </tr>
    <tr>
      <th>7 for All Mankind</th>
      <td>6Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>46cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>24"</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>46.0</td>
      <td>46.0</td>
    </tr>
    <tr>
      <th>7 for All Mankind</th>
      <td>6X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>48.5cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>25"</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>48.5</td>
      <td>48.5</td>
    </tr>
    <tr>
      <th>7 for All Mankind</th>
      <td>7Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>51cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>26"</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>51.0</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>7 for All Mankind</th>
      <td>8Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>53cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>27"</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>53.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>7 for All Mankind</th>
      <td>10Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>55cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28.5"</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>55.0</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>7 for All Mankind</th>
      <td>12Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>58cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>30"</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>58.0</td>
      <td>58.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>NaN</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>NaN</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>NaN</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>NaN</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>NaN</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>NaN</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>Billy Bandit</th>
      <td>6m</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>67cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>67.0</td>
      <td>67.0</td>
    </tr>
    <tr>
      <th>Billy Bandit</th>
      <td>9m</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>71cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>71.0</td>
      <td>71.0</td>
    </tr>
    <tr>
      <th>Billy Bandit</th>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>74cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>74.0</td>
      <td>74.0</td>
    </tr>
    <tr>
      <th>Billy Bandit</th>
      <td>18</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>81cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>81.0</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>Billy Bandit</th>
      <td>2y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>86cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>86.0</td>
      <td>86.0</td>
    </tr>
    <tr>
      <th>Billy Bandit</th>
      <td>3</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>94cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>94.0</td>
      <td>94.0</td>
    </tr>
    <tr>
      <th>Billy Bandit</th>
      <td>4</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>102cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>102.0</td>
      <td>102.0</td>
    </tr>
    <tr>
      <th>Billy Bandit</th>
      <td>5</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>108cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>108.0</td>
      <td>108.0</td>
    </tr>
    <tr>
      <th>Billy Bandit</th>
      <td>6</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>114cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>114.0</td>
      <td>114.0</td>
    </tr>
    <tr>
      <th>Billy Bandit</th>
      <td>8</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>126cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>126.0</td>
      <td>126.0</td>
    </tr>
    <tr>
      <th>Billy Bandit</th>
      <td>10</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>138cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>138.0</td>
      <td>138.0</td>
    </tr>
    <tr>
      <th>Billy Bandit</th>
      <td>12</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>150cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>150.0</td>
      <td>150.0</td>
    </tr>
    <tr>
      <th>NaN</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>popupshop</th>
      <td>6-12m</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>80cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>52</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>80.0</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>popupshop</th>
      <td>12-18m</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>86cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>54</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>86.0</td>
      <td>86.0</td>
    </tr>
    <tr>
      <th>popupshop</th>
      <td>1-2y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>92cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>56</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>92.0</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>popupshop</th>
      <td>2-3y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>98cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>57</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>98.0</td>
      <td>98.0</td>
    </tr>
    <tr>
      <th>popupshop</th>
      <td>3-4y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>104cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>58</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>104.0</td>
      <td>104.0</td>
    </tr>
    <tr>
      <th>popupshop</th>
      <td>4-5y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>110cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>59</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>110.0</td>
      <td>110.0</td>
    </tr>
    <tr>
      <th>popupshop</th>
      <td>5-6y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>116cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>60</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>116.0</td>
      <td>116.0</td>
    </tr>
    <tr>
      <th>popupshop</th>
      <td>6-7y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>122cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>62</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>122.0</td>
      <td>122.0</td>
    </tr>
    <tr>
      <th>popupshop</th>
      <td>7-8y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>128cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>64</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>128.0</td>
      <td>128.0</td>
    </tr>
    <tr>
      <th>popupshop</th>
      <td>9-10y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>140cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>68</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>140.0</td>
      <td>140.0</td>
    </tr>
    <tr>
      <th>popupshop</th>
      <td>11-12y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>152cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>76</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>152.0</td>
      <td>152.0</td>
    </tr>
  </tbody>
</table>
<p>1021 rows × 53 columns</p>
</div>




```python
file = file.dropna(axis = 0, how = 'all')
```


```python
file = file.reset_index()
```


```python
print(type(file['boy_size'][2]))
# fs stand for fillingSize
all_size = file['all_size']
boy_size = file['boy_size']
girl_size = file['girl_size']
for i in range(len(all_size)):
    if type(boy_size[i]) is not str and math.isnan(boy_size[i]) is True:
        boy_size[i] = all_size[i]
    if type(girl_size[i]) is not str and math.isnan(girl_size[i]) is True:
        girl_size[i] = all_size[i]
file['boy_size'] = boy_size
file['girl_size'] = girl_size
file
```

    <class 'float'>


    /usr/local/lib/python3.5/dist-packages/ipykernel_launcher.py:8: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    /usr/local/lib/python3.5/dist-packages/ipykernel_launcher.py:10: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      # Remove the CWD from sys.path while we load stuff.





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>all_size</th>
      <th>boy_size</th>
      <th>girl_size</th>
      <th>all_height</th>
      <th>all_weight</th>
      <th>boy_height</th>
      <th>boy_weight</th>
      <th>girl_height</th>
      <th>girl_weight</th>
      <th>...</th>
      <th>girl_bottom_short_adjustable</th>
      <th>girl_dress_hollow_to_floor</th>
      <th>girl_dress_bust</th>
      <th>girl_dress_waist</th>
      <th>girl_dress_hips</th>
      <th>girl_dress_sleeve</th>
      <th>girl_dress_inseam</th>
      <th>girl_dress_height</th>
      <th>boy_actual_height</th>
      <th>girl_actual_height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>#sen</td>
      <td>6-9mo</td>
      <td>6-9mo</td>
      <td>6-9mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>#sen</td>
      <td>9-12mo</td>
      <td>9-12mo</td>
      <td>9-12mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>#sen</td>
      <td>12-18mo</td>
      <td>12-18mo</td>
      <td>12-18mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>#sen</td>
      <td>18-24mo</td>
      <td>18-24mo</td>
      <td>18-24mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>#sen</td>
      <td>2Y</td>
      <td>2Y</td>
      <td>2Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>#sen</td>
      <td>3Y</td>
      <td>3Y</td>
      <td>3Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>#sen</td>
      <td>4Y</td>
      <td>4Y</td>
      <td>4Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>#sen</td>
      <td>5Y</td>
      <td>5Y</td>
      <td>5Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>#sen</td>
      <td>6Y</td>
      <td>6Y</td>
      <td>6Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>#sen</td>
      <td>6X</td>
      <td>6X</td>
      <td>6X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>#sen</td>
      <td>7Y</td>
      <td>7Y</td>
      <td>7Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>#sen</td>
      <td>8Y</td>
      <td>8Y</td>
      <td>8Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>#sen</td>
      <td>10Y</td>
      <td>10Y</td>
      <td>10Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>#sen</td>
      <td>12Y</td>
      <td>12Y</td>
      <td>12Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>#sen</td>
      <td>14Y</td>
      <td>14Y</td>
      <td>14Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>7 for All Mankind</td>
      <td>9-12mo</td>
      <td>9-12mo</td>
      <td>9-12mo</td>
      <td>30.5cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>30.5</td>
      <td>30.5</td>
    </tr>
    <tr>
      <th>16</th>
      <td>7 for All Mankind</td>
      <td>12-18mo</td>
      <td>12-18mo</td>
      <td>12-18mo</td>
      <td>32cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>32.0</td>
      <td>32.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>7 for All Mankind</td>
      <td>18-24mo</td>
      <td>18-24mo</td>
      <td>18-24mo</td>
      <td>35cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>35.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>7 for All Mankind</td>
      <td>2Y</td>
      <td>2Y</td>
      <td>2Y</td>
      <td>35cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>35.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>7 for All Mankind</td>
      <td>3Y</td>
      <td>3Y</td>
      <td>3Y</td>
      <td>38cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>38.0</td>
      <td>38.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>7 for All Mankind</td>
      <td>4Y</td>
      <td>4Y</td>
      <td>4Y</td>
      <td>41cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>7 for All Mankind</td>
      <td>5Y</td>
      <td>5Y</td>
      <td>5Y</td>
      <td>43.5cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>43.5</td>
      <td>43.5</td>
    </tr>
    <tr>
      <th>22</th>
      <td>7 for All Mankind</td>
      <td>6Y</td>
      <td>6Y</td>
      <td>6Y</td>
      <td>46cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>46.0</td>
      <td>46.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>7 for All Mankind</td>
      <td>6X</td>
      <td>6X</td>
      <td>6X</td>
      <td>48.5cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>48.5</td>
      <td>48.5</td>
    </tr>
    <tr>
      <th>24</th>
      <td>7 for All Mankind</td>
      <td>7Y</td>
      <td>7Y</td>
      <td>7Y</td>
      <td>51cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>51.0</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>7 for All Mankind</td>
      <td>8Y</td>
      <td>8Y</td>
      <td>8Y</td>
      <td>53cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>53.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>7 for All Mankind</td>
      <td>10Y</td>
      <td>10Y</td>
      <td>10Y</td>
      <td>55cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>55.0</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>7 for All Mankind</td>
      <td>12Y</td>
      <td>12Y</td>
      <td>12Y</td>
      <td>58cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>58.0</td>
      <td>58.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>7 for All Mankind</td>
      <td>14Y</td>
      <td>14Y</td>
      <td>14Y</td>
      <td>61cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>61.0</td>
      <td>61.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>A076</td>
      <td>2Y</td>
      <td>2Y</td>
      <td>2Y</td>
      <td>92cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>92.0</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>857</th>
      <td>Zaza Couture</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>54-55cm</td>
      <td>64-72 lbs.</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>55.0</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>858</th>
      <td>Zaza Couture</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>56-57cm</td>
      <td>72-80 lbs.</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>57.0</td>
      <td>57.0</td>
    </tr>
    <tr>
      <th>859</th>
      <td>Zaza Couture</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>58-59cm</td>
      <td>80-90 lbs.</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>59.0</td>
      <td>59.0</td>
    </tr>
    <tr>
      <th>860</th>
      <td>Zaza Couture</td>
      <td>16</td>
      <td>16</td>
      <td>16</td>
      <td>60-61cm</td>
      <td>90-100 lbs.</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>61.0</td>
      <td>61.0</td>
    </tr>
    <tr>
      <th>861</th>
      <td>Zutano</td>
      <td>6-12 months</td>
      <td>6-12 months</td>
      <td>6-12 months</td>
      <td>26-28cm</td>
      <td>17-22 lbs.</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28.0</td>
      <td>28.0</td>
    </tr>
    <tr>
      <th>862</th>
      <td>Zutano</td>
      <td>12-18 months</td>
      <td>12-18 months</td>
      <td>12-18 months</td>
      <td>28-30cm</td>
      <td>22-27 lbs.</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>30.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>863</th>
      <td>Zutano</td>
      <td>18-24 months</td>
      <td>18-24 months</td>
      <td>18-24 months</td>
      <td>30-32cm</td>
      <td>27-30 lbs.</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>32.0</td>
      <td>32.0</td>
    </tr>
    <tr>
      <th>864</th>
      <td>Billy Bandit</td>
      <td>6m</td>
      <td>6m</td>
      <td>6m</td>
      <td>67cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>67.0</td>
      <td>67.0</td>
    </tr>
    <tr>
      <th>865</th>
      <td>Billy Bandit</td>
      <td>9m</td>
      <td>9m</td>
      <td>9m</td>
      <td>71cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>71.0</td>
      <td>71.0</td>
    </tr>
    <tr>
      <th>866</th>
      <td>Billy Bandit</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>74cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>74.0</td>
      <td>74.0</td>
    </tr>
    <tr>
      <th>867</th>
      <td>Billy Bandit</td>
      <td>18</td>
      <td>18</td>
      <td>18</td>
      <td>81cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>81.0</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>868</th>
      <td>Billy Bandit</td>
      <td>2y</td>
      <td>2y</td>
      <td>2y</td>
      <td>86cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>86.0</td>
      <td>86.0</td>
    </tr>
    <tr>
      <th>869</th>
      <td>Billy Bandit</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>94cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>94.0</td>
      <td>94.0</td>
    </tr>
    <tr>
      <th>870</th>
      <td>Billy Bandit</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>102cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>102.0</td>
      <td>102.0</td>
    </tr>
    <tr>
      <th>871</th>
      <td>Billy Bandit</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>108cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>108.0</td>
      <td>108.0</td>
    </tr>
    <tr>
      <th>872</th>
      <td>Billy Bandit</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>114cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>114.0</td>
      <td>114.0</td>
    </tr>
    <tr>
      <th>873</th>
      <td>Billy Bandit</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>126cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>126.0</td>
      <td>126.0</td>
    </tr>
    <tr>
      <th>874</th>
      <td>Billy Bandit</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>138cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>138.0</td>
      <td>138.0</td>
    </tr>
    <tr>
      <th>875</th>
      <td>Billy Bandit</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>150cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>150.0</td>
      <td>150.0</td>
    </tr>
    <tr>
      <th>876</th>
      <td>popupshop</td>
      <td>6-12m</td>
      <td>6-12m</td>
      <td>6-12m</td>
      <td>80cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>80.0</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>877</th>
      <td>popupshop</td>
      <td>12-18m</td>
      <td>12-18m</td>
      <td>12-18m</td>
      <td>86cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>86.0</td>
      <td>86.0</td>
    </tr>
    <tr>
      <th>878</th>
      <td>popupshop</td>
      <td>1-2y</td>
      <td>1-2y</td>
      <td>1-2y</td>
      <td>92cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>92.0</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>879</th>
      <td>popupshop</td>
      <td>2-3y</td>
      <td>2-3y</td>
      <td>2-3y</td>
      <td>98cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>98.0</td>
      <td>98.0</td>
    </tr>
    <tr>
      <th>880</th>
      <td>popupshop</td>
      <td>3-4y</td>
      <td>3-4y</td>
      <td>3-4y</td>
      <td>104cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>104.0</td>
      <td>104.0</td>
    </tr>
    <tr>
      <th>881</th>
      <td>popupshop</td>
      <td>4-5y</td>
      <td>4-5y</td>
      <td>4-5y</td>
      <td>110cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>110.0</td>
      <td>110.0</td>
    </tr>
    <tr>
      <th>882</th>
      <td>popupshop</td>
      <td>5-6y</td>
      <td>5-6y</td>
      <td>5-6y</td>
      <td>116cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>116.0</td>
      <td>116.0</td>
    </tr>
    <tr>
      <th>883</th>
      <td>popupshop</td>
      <td>6-7y</td>
      <td>6-7y</td>
      <td>6-7y</td>
      <td>122cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>122.0</td>
      <td>122.0</td>
    </tr>
    <tr>
      <th>884</th>
      <td>popupshop</td>
      <td>7-8y</td>
      <td>7-8y</td>
      <td>7-8y</td>
      <td>128cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>128.0</td>
      <td>128.0</td>
    </tr>
    <tr>
      <th>885</th>
      <td>popupshop</td>
      <td>9-10y</td>
      <td>9-10y</td>
      <td>9-10y</td>
      <td>140cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>140.0</td>
      <td>140.0</td>
    </tr>
    <tr>
      <th>886</th>
      <td>popupshop</td>
      <td>11-12y</td>
      <td>11-12y</td>
      <td>11-12y</td>
      <td>152cm</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>152.0</td>
      <td>152.0</td>
    </tr>
  </tbody>
</table>
<p>887 rows × 54 columns</p>
</div>




```python
all_height = file['all_height']
boy_height = file['boy_height']
girl_height = file['girl_height']
for i in range(len(all_height)):
    if type(boy_height[i]) is not str and math.isnan(boy_height[i]) is True:
        boy_height[i] = all_height[i]
    if type(girl_height[i]) is not str and math.isnan(girl_height[i]) is True:
        girl_height[i] = all_height[i]
file['boy_height'] = boy_height
file['girl_height'] = girl_height
file
```

    /usr/local/lib/python3.5/dist-packages/ipykernel_launcher.py:6: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    /usr/local/lib/python3.5/dist-packages/ipykernel_launcher.py:8: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      





<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>all_size</th>
      <th>boy_size</th>
      <th>girl_size</th>
      <th>all_height</th>
      <th>all_weight</th>
      <th>boy_height</th>
      <th>boy_weight</th>
      <th>girl_height</th>
      <th>girl_weight</th>
      <th>...</th>
      <th>girl_bottom_short_adjustable</th>
      <th>girl_dress_hollow_to_floor</th>
      <th>girl_dress_bust</th>
      <th>girl_dress_waist</th>
      <th>girl_dress_hips</th>
      <th>girl_dress_sleeve</th>
      <th>girl_dress_inseam</th>
      <th>girl_dress_height</th>
      <th>boy_actual_height</th>
      <th>girl_actual_height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>#sen</td>
      <td>6-9mo</td>
      <td>6-9mo</td>
      <td>6-9mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>#sen</td>
      <td>9-12mo</td>
      <td>9-12mo</td>
      <td>9-12mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>#sen</td>
      <td>12-18mo</td>
      <td>12-18mo</td>
      <td>12-18mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>#sen</td>
      <td>18-24mo</td>
      <td>18-24mo</td>
      <td>18-24mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>#sen</td>
      <td>2Y</td>
      <td>2Y</td>
      <td>2Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>#sen</td>
      <td>3Y</td>
      <td>3Y</td>
      <td>3Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>#sen</td>
      <td>4Y</td>
      <td>4Y</td>
      <td>4Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>#sen</td>
      <td>5Y</td>
      <td>5Y</td>
      <td>5Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>#sen</td>
      <td>6Y</td>
      <td>6Y</td>
      <td>6Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>#sen</td>
      <td>6X</td>
      <td>6X</td>
      <td>6X</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>#sen</td>
      <td>7Y</td>
      <td>7Y</td>
      <td>7Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>#sen</td>
      <td>8Y</td>
      <td>8Y</td>
      <td>8Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>#sen</td>
      <td>10Y</td>
      <td>10Y</td>
      <td>10Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>#sen</td>
      <td>12Y</td>
      <td>12Y</td>
      <td>12Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>#sen</td>
      <td>14Y</td>
      <td>14Y</td>
      <td>14Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>7 for All Mankind</td>
      <td>9-12mo</td>
      <td>9-12mo</td>
      <td>9-12mo</td>
      <td>30.5cm</td>
      <td>NaN</td>
      <td>30.5cm</td>
      <td>NaN</td>
      <td>30.5cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>30.5</td>
      <td>30.5</td>
    </tr>
    <tr>
      <th>16</th>
      <td>7 for All Mankind</td>
      <td>12-18mo</td>
      <td>12-18mo</td>
      <td>12-18mo</td>
      <td>32cm</td>
      <td>NaN</td>
      <td>32cm</td>
      <td>NaN</td>
      <td>32cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>32.0</td>
      <td>32.0</td>
    </tr>
    <tr>
      <th>17</th>
      <td>7 for All Mankind</td>
      <td>18-24mo</td>
      <td>18-24mo</td>
      <td>18-24mo</td>
      <td>35cm</td>
      <td>NaN</td>
      <td>35cm</td>
      <td>NaN</td>
      <td>35cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>35.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>18</th>
      <td>7 for All Mankind</td>
      <td>2Y</td>
      <td>2Y</td>
      <td>2Y</td>
      <td>35cm</td>
      <td>NaN</td>
      <td>35cm</td>
      <td>NaN</td>
      <td>35cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>35.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>19</th>
      <td>7 for All Mankind</td>
      <td>3Y</td>
      <td>3Y</td>
      <td>3Y</td>
      <td>38cm</td>
      <td>NaN</td>
      <td>38cm</td>
      <td>NaN</td>
      <td>38cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>38.0</td>
      <td>38.0</td>
    </tr>
    <tr>
      <th>20</th>
      <td>7 for All Mankind</td>
      <td>4Y</td>
      <td>4Y</td>
      <td>4Y</td>
      <td>41cm</td>
      <td>NaN</td>
      <td>41cm</td>
      <td>NaN</td>
      <td>41cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>41.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>21</th>
      <td>7 for All Mankind</td>
      <td>5Y</td>
      <td>5Y</td>
      <td>5Y</td>
      <td>43.5cm</td>
      <td>NaN</td>
      <td>43.5cm</td>
      <td>NaN</td>
      <td>43.5cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>43.5</td>
      <td>43.5</td>
    </tr>
    <tr>
      <th>22</th>
      <td>7 for All Mankind</td>
      <td>6Y</td>
      <td>6Y</td>
      <td>6Y</td>
      <td>46cm</td>
      <td>NaN</td>
      <td>46cm</td>
      <td>NaN</td>
      <td>46cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>46.0</td>
      <td>46.0</td>
    </tr>
    <tr>
      <th>23</th>
      <td>7 for All Mankind</td>
      <td>6X</td>
      <td>6X</td>
      <td>6X</td>
      <td>48.5cm</td>
      <td>NaN</td>
      <td>48.5cm</td>
      <td>NaN</td>
      <td>48.5cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>48.5</td>
      <td>48.5</td>
    </tr>
    <tr>
      <th>24</th>
      <td>7 for All Mankind</td>
      <td>7Y</td>
      <td>7Y</td>
      <td>7Y</td>
      <td>51cm</td>
      <td>NaN</td>
      <td>51cm</td>
      <td>NaN</td>
      <td>51cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>51.0</td>
      <td>51.0</td>
    </tr>
    <tr>
      <th>25</th>
      <td>7 for All Mankind</td>
      <td>8Y</td>
      <td>8Y</td>
      <td>8Y</td>
      <td>53cm</td>
      <td>NaN</td>
      <td>53cm</td>
      <td>NaN</td>
      <td>53cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>53.0</td>
      <td>53.0</td>
    </tr>
    <tr>
      <th>26</th>
      <td>7 for All Mankind</td>
      <td>10Y</td>
      <td>10Y</td>
      <td>10Y</td>
      <td>55cm</td>
      <td>NaN</td>
      <td>55cm</td>
      <td>NaN</td>
      <td>55cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>55.0</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>27</th>
      <td>7 for All Mankind</td>
      <td>12Y</td>
      <td>12Y</td>
      <td>12Y</td>
      <td>58cm</td>
      <td>NaN</td>
      <td>58cm</td>
      <td>NaN</td>
      <td>58cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>58.0</td>
      <td>58.0</td>
    </tr>
    <tr>
      <th>28</th>
      <td>7 for All Mankind</td>
      <td>14Y</td>
      <td>14Y</td>
      <td>14Y</td>
      <td>61cm</td>
      <td>NaN</td>
      <td>61cm</td>
      <td>NaN</td>
      <td>61cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>61.0</td>
      <td>61.0</td>
    </tr>
    <tr>
      <th>29</th>
      <td>A076</td>
      <td>2Y</td>
      <td>2Y</td>
      <td>2Y</td>
      <td>92cm</td>
      <td>NaN</td>
      <td>92cm</td>
      <td>NaN</td>
      <td>92cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>92.0</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>857</th>
      <td>Zaza Couture</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>54-55cm</td>
      <td>64-72 lbs.</td>
      <td>54-55cm</td>
      <td>NaN</td>
      <td>54-55cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>55.0</td>
      <td>55.0</td>
    </tr>
    <tr>
      <th>858</th>
      <td>Zaza Couture</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>56-57cm</td>
      <td>72-80 lbs.</td>
      <td>56-57cm</td>
      <td>NaN</td>
      <td>56-57cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>57.0</td>
      <td>57.0</td>
    </tr>
    <tr>
      <th>859</th>
      <td>Zaza Couture</td>
      <td>14</td>
      <td>14</td>
      <td>14</td>
      <td>58-59cm</td>
      <td>80-90 lbs.</td>
      <td>58-59cm</td>
      <td>NaN</td>
      <td>58-59cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>59.0</td>
      <td>59.0</td>
    </tr>
    <tr>
      <th>860</th>
      <td>Zaza Couture</td>
      <td>16</td>
      <td>16</td>
      <td>16</td>
      <td>60-61cm</td>
      <td>90-100 lbs.</td>
      <td>60-61cm</td>
      <td>NaN</td>
      <td>60-61cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>61.0</td>
      <td>61.0</td>
    </tr>
    <tr>
      <th>861</th>
      <td>Zutano</td>
      <td>6-12 months</td>
      <td>6-12 months</td>
      <td>6-12 months</td>
      <td>26-28cm</td>
      <td>17-22 lbs.</td>
      <td>26-28cm</td>
      <td>NaN</td>
      <td>26-28cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>28.0</td>
      <td>28.0</td>
    </tr>
    <tr>
      <th>862</th>
      <td>Zutano</td>
      <td>12-18 months</td>
      <td>12-18 months</td>
      <td>12-18 months</td>
      <td>28-30cm</td>
      <td>22-27 lbs.</td>
      <td>28-30cm</td>
      <td>NaN</td>
      <td>28-30cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>30.0</td>
      <td>30.0</td>
    </tr>
    <tr>
      <th>863</th>
      <td>Zutano</td>
      <td>18-24 months</td>
      <td>18-24 months</td>
      <td>18-24 months</td>
      <td>30-32cm</td>
      <td>27-30 lbs.</td>
      <td>30-32cm</td>
      <td>NaN</td>
      <td>30-32cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>32.0</td>
      <td>32.0</td>
    </tr>
    <tr>
      <th>864</th>
      <td>Billy Bandit</td>
      <td>6m</td>
      <td>6m</td>
      <td>6m</td>
      <td>67cm</td>
      <td>NaN</td>
      <td>67cm</td>
      <td>NaN</td>
      <td>67cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>67.0</td>
      <td>67.0</td>
    </tr>
    <tr>
      <th>865</th>
      <td>Billy Bandit</td>
      <td>9m</td>
      <td>9m</td>
      <td>9m</td>
      <td>71cm</td>
      <td>NaN</td>
      <td>71cm</td>
      <td>NaN</td>
      <td>71cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>71.0</td>
      <td>71.0</td>
    </tr>
    <tr>
      <th>866</th>
      <td>Billy Bandit</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>74cm</td>
      <td>NaN</td>
      <td>74cm</td>
      <td>NaN</td>
      <td>74cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>74.0</td>
      <td>74.0</td>
    </tr>
    <tr>
      <th>867</th>
      <td>Billy Bandit</td>
      <td>18</td>
      <td>18</td>
      <td>18</td>
      <td>81cm</td>
      <td>NaN</td>
      <td>81cm</td>
      <td>NaN</td>
      <td>81cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>81.0</td>
      <td>81.0</td>
    </tr>
    <tr>
      <th>868</th>
      <td>Billy Bandit</td>
      <td>2y</td>
      <td>2y</td>
      <td>2y</td>
      <td>86cm</td>
      <td>NaN</td>
      <td>86cm</td>
      <td>NaN</td>
      <td>86cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>86.0</td>
      <td>86.0</td>
    </tr>
    <tr>
      <th>869</th>
      <td>Billy Bandit</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>94cm</td>
      <td>NaN</td>
      <td>94cm</td>
      <td>NaN</td>
      <td>94cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>94.0</td>
      <td>94.0</td>
    </tr>
    <tr>
      <th>870</th>
      <td>Billy Bandit</td>
      <td>4</td>
      <td>4</td>
      <td>4</td>
      <td>102cm</td>
      <td>NaN</td>
      <td>102cm</td>
      <td>NaN</td>
      <td>102cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>102.0</td>
      <td>102.0</td>
    </tr>
    <tr>
      <th>871</th>
      <td>Billy Bandit</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>108cm</td>
      <td>NaN</td>
      <td>108cm</td>
      <td>NaN</td>
      <td>108cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>108.0</td>
      <td>108.0</td>
    </tr>
    <tr>
      <th>872</th>
      <td>Billy Bandit</td>
      <td>6</td>
      <td>6</td>
      <td>6</td>
      <td>114cm</td>
      <td>NaN</td>
      <td>114cm</td>
      <td>NaN</td>
      <td>114cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>114.0</td>
      <td>114.0</td>
    </tr>
    <tr>
      <th>873</th>
      <td>Billy Bandit</td>
      <td>8</td>
      <td>8</td>
      <td>8</td>
      <td>126cm</td>
      <td>NaN</td>
      <td>126cm</td>
      <td>NaN</td>
      <td>126cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>126.0</td>
      <td>126.0</td>
    </tr>
    <tr>
      <th>874</th>
      <td>Billy Bandit</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>138cm</td>
      <td>NaN</td>
      <td>138cm</td>
      <td>NaN</td>
      <td>138cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>138.0</td>
      <td>138.0</td>
    </tr>
    <tr>
      <th>875</th>
      <td>Billy Bandit</td>
      <td>12</td>
      <td>12</td>
      <td>12</td>
      <td>150cm</td>
      <td>NaN</td>
      <td>150cm</td>
      <td>NaN</td>
      <td>150cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>150.0</td>
      <td>150.0</td>
    </tr>
    <tr>
      <th>876</th>
      <td>popupshop</td>
      <td>6-12m</td>
      <td>6-12m</td>
      <td>6-12m</td>
      <td>80cm</td>
      <td>NaN</td>
      <td>80cm</td>
      <td>NaN</td>
      <td>80cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>80.0</td>
      <td>80.0</td>
    </tr>
    <tr>
      <th>877</th>
      <td>popupshop</td>
      <td>12-18m</td>
      <td>12-18m</td>
      <td>12-18m</td>
      <td>86cm</td>
      <td>NaN</td>
      <td>86cm</td>
      <td>NaN</td>
      <td>86cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>86.0</td>
      <td>86.0</td>
    </tr>
    <tr>
      <th>878</th>
      <td>popupshop</td>
      <td>1-2y</td>
      <td>1-2y</td>
      <td>1-2y</td>
      <td>92cm</td>
      <td>NaN</td>
      <td>92cm</td>
      <td>NaN</td>
      <td>92cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>92.0</td>
      <td>92.0</td>
    </tr>
    <tr>
      <th>879</th>
      <td>popupshop</td>
      <td>2-3y</td>
      <td>2-3y</td>
      <td>2-3y</td>
      <td>98cm</td>
      <td>NaN</td>
      <td>98cm</td>
      <td>NaN</td>
      <td>98cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>98.0</td>
      <td>98.0</td>
    </tr>
    <tr>
      <th>880</th>
      <td>popupshop</td>
      <td>3-4y</td>
      <td>3-4y</td>
      <td>3-4y</td>
      <td>104cm</td>
      <td>NaN</td>
      <td>104cm</td>
      <td>NaN</td>
      <td>104cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>104.0</td>
      <td>104.0</td>
    </tr>
    <tr>
      <th>881</th>
      <td>popupshop</td>
      <td>4-5y</td>
      <td>4-5y</td>
      <td>4-5y</td>
      <td>110cm</td>
      <td>NaN</td>
      <td>110cm</td>
      <td>NaN</td>
      <td>110cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>110.0</td>
      <td>110.0</td>
    </tr>
    <tr>
      <th>882</th>
      <td>popupshop</td>
      <td>5-6y</td>
      <td>5-6y</td>
      <td>5-6y</td>
      <td>116cm</td>
      <td>NaN</td>
      <td>116cm</td>
      <td>NaN</td>
      <td>116cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>116.0</td>
      <td>116.0</td>
    </tr>
    <tr>
      <th>883</th>
      <td>popupshop</td>
      <td>6-7y</td>
      <td>6-7y</td>
      <td>6-7y</td>
      <td>122cm</td>
      <td>NaN</td>
      <td>122cm</td>
      <td>NaN</td>
      <td>122cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>122.0</td>
      <td>122.0</td>
    </tr>
    <tr>
      <th>884</th>
      <td>popupshop</td>
      <td>7-8y</td>
      <td>7-8y</td>
      <td>7-8y</td>
      <td>128cm</td>
      <td>NaN</td>
      <td>128cm</td>
      <td>NaN</td>
      <td>128cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>128.0</td>
      <td>128.0</td>
    </tr>
    <tr>
      <th>885</th>
      <td>popupshop</td>
      <td>9-10y</td>
      <td>9-10y</td>
      <td>9-10y</td>
      <td>140cm</td>
      <td>NaN</td>
      <td>140cm</td>
      <td>NaN</td>
      <td>140cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>140.0</td>
      <td>140.0</td>
    </tr>
    <tr>
      <th>886</th>
      <td>popupshop</td>
      <td>11-12y</td>
      <td>11-12y</td>
      <td>11-12y</td>
      <td>152cm</td>
      <td>NaN</td>
      <td>152cm</td>
      <td>NaN</td>
      <td>152cm</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>152.0</td>
      <td>152.0</td>
    </tr>
  </tbody>
</table>
<p>887 rows × 54 columns</p>
</div>




```python
all_weight = file['all_weight']
boy_weight = file['boy_weight']
girl_weight = file['girl_weight']
for i in range(len(all_height)):
    if type(boy_weight[i]) is not str and math.isnan(boy_weight[i]) is True:
        boy_weight[i] = all_weight[i]
    if type(girl_weight[i]) is not str and math.isnan(girl_weight[i]) is True:
        girl_weight[i] = all_weight[i]
file['boy_weight'] = boy_weight
file['girl_weight'] = girl_weight
```

    /usr/local/lib/python3.5/dist-packages/ipykernel_launcher.py:6: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      
    /usr/local/lib/python3.5/dist-packages/ipykernel_launcher.py:8: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
      



```python
file["boy_actual_weight"] = np.nan
file["girl_actual_weight"] = np.nan
file.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>index</th>
      <th>all_size</th>
      <th>boy_size</th>
      <th>girl_size</th>
      <th>all_height</th>
      <th>all_weight</th>
      <th>boy_height</th>
      <th>boy_weight</th>
      <th>girl_height</th>
      <th>girl_weight</th>
      <th>...</th>
      <th>girl_dress_bust</th>
      <th>girl_dress_waist</th>
      <th>girl_dress_hips</th>
      <th>girl_dress_sleeve</th>
      <th>girl_dress_inseam</th>
      <th>girl_dress_height</th>
      <th>boy_actual_height</th>
      <th>girl_actual_height</th>
      <th>boy_actual_weight</th>
      <th>girl_actual_weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>#sen</td>
      <td>6-9mo</td>
      <td>6-9mo</td>
      <td>6-9mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>#sen</td>
      <td>9-12mo</td>
      <td>9-12mo</td>
      <td>9-12mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>#sen</td>
      <td>12-18mo</td>
      <td>12-18mo</td>
      <td>12-18mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>#sen</td>
      <td>18-24mo</td>
      <td>18-24mo</td>
      <td>18-24mo</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>#sen</td>
      <td>2Y</td>
      <td>2Y</td>
      <td>2Y</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 56 columns</p>
</div>




```python
kg = ['kg', 'KG']
lbs = ['lbs', 'LBS']
```


```python
def checkWeightUnit(data):
    unit = None
    for item in kg:
        if item in data:
            unit = 'kg'
            return unit
    for item in lbs:
        if item in data:
            unit = 'lbs'
            return unit
```


```python
td = 'abdkg'
checkWeightUnit(td)
```




    'kg'




```python
def weight_generalizer(weight, unit):
    for i in range(len(weight)):
        if checkWeightUnit(weight[i]) is not None:
            unit = checkWeightUnit(weight[i])
        nums = re.findall(r'\d+\.?\d+', data)
        if len(nums) is 1:
            weight[i] = nums[0] + unit
        else:
            weight[i] = nums[0] + '-' + nums[1] + unit        
```


```python
weight_columns = ['all_weight', 'boy_weight', 'girl_weight']
for column in weight_columns:
    weight = file[column]
    weight_generalizer(weight, unit)
    file[column] = weight
```


    

    TypeErrorTraceback (most recent call last)

    <ipython-input-80-7cb1e32e1384> in <module>()
          2 for column in weight_columns:
          3     weight = file[column]
    ----> 4     weight_generalizer(weight, unit)
          5     file[column] = weight


    <ipython-input-79-36399814dc54> in weight_generalizer(weight, unit)
          1 def weight_generalizer(weight, unit):
          2     for i in range(len(weight)):
    ----> 3         if checkWeightUnit(weight[i]) is not None:
          4             unit = checkWeightUnit(weight[i])
          5         nums = re.findall(r'\d+\.?\d+', data)


    <ipython-input-78-70f261dcd253> in checkWeightUnit(data)
          2     unit = None
          3     for item in kg:
    ----> 4         if item in data:
          5             unit = 'kg'
          6             return unit


    TypeError: argument of type 'float' is not iterable



```python

```
