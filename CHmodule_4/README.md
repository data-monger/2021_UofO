```python
# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to change the path if needed.)
school_data_to_load =  "Resources/schools_complete.csv"  
student_data_to_load = "Resources/students_complete.csv" 

# Read the School Data and Student Data and store into a Pandas DataFrame
school_data_df = pd.read_csv(school_data_to_load)
student_data_df = pd.read_csv(student_data_to_load)
updated_student_data_df = pd.read_csv(student_data_to_load)

updated_student_data_df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>student_name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school_name</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Cleaning Student Names and Replacing Substrings in a Python String
# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]
score = list(range(1, 101))

# Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")
    updated_student_data_df["student_name"] = updated_student_data_df["student_name"].str.replace(word,"")
    
    
```

    <ipython-input-1-2c363e452562>:20: FutureWarning: The default value of regex will change from True to False in a future version.
      student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")
    <ipython-input-1-2c363e452562>:21: FutureWarning: The default value of regex will change from True to False in a future version.
      updated_student_data_df["student_name"] = updated_student_data_df["student_name"].str.replace(word,"")
    


```python
# Check names.
student_data_df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>student_name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school_name</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Bryan Miranda</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>94</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>Sheena Carter</td>
      <td>F</td>
      <td>11th</td>
      <td>Huang High School</td>
      <td>82</td>
      <td>80</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>Nicole Baker</td>
      <td>F</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>96</td>
      <td>69</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>Michael Roth</td>
      <td>M</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>95</td>
      <td>87</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>Matthew Greene</td>
      <td>M</td>
      <td>10th</td>
      <td>Huang High School</td>
      <td>96</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Check data types.
student_data_df.dtypes
```




    Student ID        int64
    student_name     object
    gender           object
    grade            object
    school_name      object
    reading_score     int64
    math_score        int64
    dtype: object




```python
# Check schools.
school_data_df.head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>school_name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
    <tr>
      <th>5</th>
      <td>5</td>
      <td>Wilson High School</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
    </tr>
    <tr>
      <th>6</th>
      <td>6</td>
      <td>Cabrera High School</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
    </tr>
    <tr>
      <th>7</th>
      <td>7</td>
      <td>Bailey High School</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
    </tr>
    <tr>
      <th>8</th>
      <td>8</td>
      <td>Holden High School</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
    </tr>
    <tr>
      <th>9</th>
      <td>9</td>
      <td>Pena High School</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Check data types.
school_data_df.dtypes
```




    School ID       int64
    school_name    object
    type           object
    size            int64
    budget          int64
    dtype: object



## Deliverable 1: Replace the reading and math scores.

### Replace the 9th grade reading and math scores at Thomas High School with NaN.


```python
# Install numpy using conda install numpy or pip install numpy. 
# Step 1. Import numpy as np.
import numpy as np

```


```python
# Step 2. Use the loc method on the student_data_df to select all the reading scores from the 9th grade at Thomas High School and replace them with NaN.
updated_student_data_df.loc[(updated_student_data_df["school_name"] == "Thomas High School") 
                          & (updated_student_data_df["grade"] == "9th"), "reading_score"]= np.NaN
```


```python
#  Step 3. Refactor the code in Step 2 to replace the math scores with NaN.
updated_student_data_df.loc[(updated_student_data_df["school_name"] == "Thomas High School") 
                          & (updated_student_data_df["grade"] == "9th"), "math_score"] = np.NaN
```


```python
#  Step 4. Check the student data for NaN's. 
updated_student_data_df.loc[(updated_student_data_df["school_name"] == "Thomas High School") 
                          & (updated_student_data_df["grade"] == "9th")]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>student_name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school_name</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>37537</th>
      <td>37537</td>
      <td>Erik Snyder</td>
      <td>M</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>37538</th>
      <td>37538</td>
      <td>Tanya Martinez</td>
      <td>F</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>37539</th>
      <td>37539</td>
      <td>Noah Erickson</td>
      <td>M</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>37540</th>
      <td>37540</td>
      <td>Austin Meyer</td>
      <td>M</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>37543</th>
      <td>37543</td>
      <td>Madison Hampton</td>
      <td>F</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>NaN</td>
      <td>NaN</td>
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
    </tr>
    <tr>
      <th>39152</th>
      <td>39152</td>
      <td>Lori Moore</td>
      <td>F</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39153</th>
      <td>39153</td>
      <td>William Hubbard</td>
      <td>M</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39157</th>
      <td>39157</td>
      <td>Kristen Gonzalez</td>
      <td>F</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39164</th>
      <td>39164</td>
      <td>Joseph Anthony</td>
      <td>M</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>39167</th>
      <td>39167</td>
      <td>Rebecca Tanner</td>
      <td>F</td>
      <td>9th</td>
      <td>Thomas High School</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>461 rows × 7 columns</p>
</div>




```python
# Check Not Na's
updated_student_data_df[updated_student_data_df['reading_score'].notna()]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>student_name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school_name</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66.0</td>
      <td>79.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94.0</td>
      <td>61.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90.0</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67.0</td>
      <td>58.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97.0</td>
      <td>84.0</td>
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
    </tr>
    <tr>
      <th>39163</th>
      <td>39163</td>
      <td>John Reese</td>
      <td>M</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>90.0</td>
      <td>75.0</td>
    </tr>
    <tr>
      <th>39165</th>
      <td>39165</td>
      <td>Donna Howard</td>
      <td>F</td>
      <td>12th</td>
      <td>Thomas High School</td>
      <td>99.0</td>
      <td>90.0</td>
    </tr>
    <tr>
      <th>39166</th>
      <td>39166</td>
      <td>Dawn Bell</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>95.0</td>
      <td>70.0</td>
    </tr>
    <tr>
      <th>39168</th>
      <td>39168</td>
      <td>Desiree Kidd</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>99.0</td>
      <td>90.0</td>
    </tr>
    <tr>
      <th>39169</th>
      <td>39169</td>
      <td>Carolyn Jackson</td>
      <td>F</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>95.0</td>
      <td>75.0</td>
    </tr>
  </tbody>
</table>
<p>38709 rows × 7 columns</p>
</div>




```python
# Check Not Na's
updated_student_data_df[updated_student_data_df['math_score'].notna()]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>student_name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school_name</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66.0</td>
      <td>79.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94.0</td>
      <td>61.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90.0</td>
      <td>60.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67.0</td>
      <td>58.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97.0</td>
      <td>84.0</td>
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
    </tr>
    <tr>
      <th>39163</th>
      <td>39163</td>
      <td>John Reese</td>
      <td>M</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>90.0</td>
      <td>75.0</td>
    </tr>
    <tr>
      <th>39165</th>
      <td>39165</td>
      <td>Donna Howard</td>
      <td>F</td>
      <td>12th</td>
      <td>Thomas High School</td>
      <td>99.0</td>
      <td>90.0</td>
    </tr>
    <tr>
      <th>39166</th>
      <td>39166</td>
      <td>Dawn Bell</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>95.0</td>
      <td>70.0</td>
    </tr>
    <tr>
      <th>39168</th>
      <td>39168</td>
      <td>Desiree Kidd</td>
      <td>F</td>
      <td>10th</td>
      <td>Thomas High School</td>
      <td>99.0</td>
      <td>90.0</td>
    </tr>
    <tr>
      <th>39169</th>
      <td>39169</td>
      <td>Carolyn Jackson</td>
      <td>F</td>
      <td>11th</td>
      <td>Thomas High School</td>
      <td>95.0</td>
      <td>75.0</td>
    </tr>
  </tbody>
</table>
<p>38709 rows × 7 columns</p>
</div>



## Deliverable 2 : Repeat the school district analysis

### District Summary


```python
# Combine the data into a single dataset
school_data_complete_df = pd.merge(student_data_df, school_data_df, 
                                   how="left", on=["school_name", "school_name"])

# Combine updated student data into a single dataset
updated_school_data_complete_df = pd.merge(updated_student_data_df[updated_student_data_df['math_score'].notna()], school_data_df,
                                    how="left", on=["school_name", "school_name"])

```


```python
# Check complete Data Set
school_data_complete_df.count()
```




    Student ID       39170
    student_name     39170
    gender           39170
    grade            39170
    school_name      39170
    reading_score    39170
    math_score       39170
    School ID        39170
    type             39170
    size             39170
    budget           39170
    dtype: int64




```python
# Check updated Data Set
updated_school_data_complete_df.count()
```




    Student ID       38709
    student_name     38709
    gender           38709
    grade            38709
    school_name      38709
    reading_score    38709
    math_score       38709
    School ID        38709
    type             38709
    size             38709
    budget           38709
    dtype: int64




```python
# Calculate the Totals (Schools... 
school_count = len(school_data_complete_df["school_name"].unique())

# ...and Students)
student_count = school_data_complete_df["Student ID"].count()
updated_student_count = updated_school_data_complete_df["Student ID"].count()

# Calculate the Total Budget
total_budget = school_data_df["budget"].sum()

print ("Schools:" , school_count)
print ("Students:", student_count)
print ("Updated Students:", updated_student_count)
print ("Total Budget:", total_budget)
```

    Schools 15
    Students 39170
    Updated Students 38709
    Total Budget  24649428
    


```python
# Calculate the Average Scores using the "clean_student_data".
average_reading_score = school_data_complete_df["reading_score"].mean()
average_math_score = school_data_complete_df["math_score"].mean()

print ("Average Reading Score:" , average_reading_score )
print ("Average Math Score:" , average_math_score )
```

    Average Reading Score 81.87784018381414
    Average Math Score 78.98537145774827
    


```python
# Calculate the Average Scores using the "updated_student_data".
updated_average_reading_score = updated_school_data_complete_df["reading_score"].mean()
updated_average_math_score = updated_school_data_complete_df["math_score"].mean()

print ("Updated Average Reading Score:" , updated_average_reading_score )
print ("Updated Average Math Score:" , updated_average_math_score )
```

    Updated Average Reading Score 81.85579580976001
    Updated Average Math Score 78.93053295099331
    


```python
# Step 1. Get the number of students that are in ninth grade at Thomas High School.
# These students have no grades. 
ths_fresh_df = student_data_df.loc[(student_data_df["school_name"] == "Thomas High School") 
                  & (student_data_df["grade"] == "9th"), "Student ID"].count()

#ths_fresh_df = school_data_complete_df.loc[(school_data_df["school_name"]=="Thomas High School")
#                    & (school_data_complete_df["grade"] == "9th"), "Student ID"].count()

#test_df = updated_school_data_complete_df.loc[(updated_school_data_complete_df["school_name"]=="Thomas High School")
#                    & (updated_school_data_complete_df["grade"] == "9th"), "Student ID"].count()
#print (test_df)



# Get the total student count 
student_count = school_data_complete_df["Student ID"].count()


# Step 2. Subtract the number of students that are in ninth grade at 
# Thomas High School from the total student count to get the new total student count.
    #### Not necesssary- i created a new dataframe

print ("Thomas High School Freshman:", ths_fresh_df)
print ("Student Count:", student_count)
print ("Updated Student Count:", updated_student_count)


#updated_student_count = updated_school_data_complete_df["Student ID"].count()
#print ("Updated Student Count", updated_student_count)


# askbcs
#new_student_count = student_count-ths_fresh_df
#print ("New Student Count", new_student_count)
```

    Thomas High School Freshman 461
    Student Count 39170
    Updated Student Count 38709
    


```python
# Calculate the passing rates using the "clean_student_data".
passing_math_count = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)].count()["student_name"]
passing_reading_count = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)].count()["student_name"]

print ("Students Passing Math:", passing_math_count)
print ("Students Passing Reading:", passing_reading_count, "\n")

passing_math_percentage=passing_math_count / float(student_count) * 100
passing_reading_percentage=passing_reading_count / float(student_count) *100

print ("Students Passing Math Percentage:", passing_math_percentage)
print ("Students Passing Reading Percentage:", passing_reading_percentage)

```

    Students Passing Math: 29370
    Students Passing Reading: 33610 
    
    Students Passing Math Percentage: 74.9808526933878
    Students Passing Reading Percentage: 85.80546336482001
    


```python
# Step 3. Calculate the passing percentages with the new total student count.
updated_passing_math_count = updated_school_data_complete_df[(updated_school_data_complete_df["math_score"] >= 70)].count()["student_name"]
updated_passing_reading_count = updated_school_data_complete_df[(updated_school_data_complete_df["reading_score"] >= 70)].count()["student_name"]

print ("Students Passing Math:", updated_passing_math_count)
print ("Students Passing Reading:", updated_passing_reading_count, "\n")

updated_passing_math_percentage=updated_passing_math_count / float(updated_student_count) * 100
updated_passing_reading_percentage=updated_passing_reading_count / float(updated_student_count) *100

print ("Updated Students Passing Math Percentage:", updated_passing_math_percentage)
print ("Updated Students Passing Reading Percentage:", updated_passing_reading_percentage)

# askbcs
#passing_math_percentage=passing_math_count / float(new_student_count) * 100
#passing_reading_percentage=passing_reading_count / float(new_student_count) * 100
```

    Students Passing Math: 28939
    Students Passing Reading: 33158 
    
    Updated Students Passing Math Percentage: 74.76039164018704
    Updated Students Passing Reading Percentage: 85.6596657108166
    


```python
# Calculate the students who passed both reading and math.
passing_math_reading = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)
                                             & (school_data_complete_df["reading_score"] >= 70)]

# Calculate the number of students that passed both reading and math.
overall_passing_math_reading_count = passing_math_reading["student_name"].count()
overall_passing_percentage = overall_passing_math_reading_count / student_count * 100

print ("Passing Both Math and Reading:", overall_passing_math_reading_count)
print ("Passing Percentage...:" ,overall_passing_percentage)
```

    Passing Both Math and Reading 25528
    Passing Percentage... 65.17232575950983
    


```python
# Step 4.Calculate the overall passing percentage with new total student count.
# Calculate the students who passed both reading and math.
updated_passing_math_reading = updated_school_data_complete_df[(updated_school_data_complete_df["math_score"] >= 70)
                                                             & (updated_school_data_complete_df["reading_score"] >= 70)]

# Calculate the number of students that passed both reading and math.
updated_overall_passing_math_reading_count = updated_passing_math_reading["student_name"].count()
updated_overall_passing_percentage = updated_overall_passing_math_reading_count / updated_student_count * 100

print ("Updated Passing Both Math and Reading:", updated_overall_passing_math_reading_count)
print ("Updated Passing Percentage...:", updated_overall_passing_percentage)
# askbcs
#overall_passing_percentage=overall_passing_math_reading_count / new_student_count * 100
```

    Updated Passing Both Math and Reading 25105
    Updated Passing Percentage... 64.85571830840374
    


```python
# Create a DataFrame
district_summary_df = pd.DataFrame(
          [{"Analysis Type": "BenchMark",
          "Total Schools": school_count, 
          "Total Students": student_count, 
          "Total Budget": total_budget,
          "Average Math Score": average_math_score, 
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
          "% Passing Reading": passing_reading_percentage,
          "% Overall Passing": overall_passing_percentage}])

# Format the "Total Students" to have the comma for a thousands separator.
district_summary_df["Total Students"] = district_summary_df["Total Students"].map("{:,}".format)

# Format the "Total Budget" to have the comma for a thousands separator, a decimal separator and a "$".
district_summary_df["Total Budget"] = district_summary_df["Total Budget"].map("${:,.2f}".format)

# Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)
district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)
district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.1f}".format)
district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.1f}".format)
district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.1f}".format)

# Display the data frame
district_summary_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Analysis Type</th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BenchMark</td>
      <td>15</td>
      <td>39,170</td>
      <td>$24,649,428.00</td>
      <td>79.0</td>
      <td>81.9</td>
      <td>75.0</td>
      <td>85.8</td>
      <td>65.2</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create a DataFrame
district_summary2_df = pd.DataFrame(
          [{"Analysis Type": "Adjusted",
          "Total Schools": school_count, 
          "Total Students": updated_student_count, 
          "Total Budget": total_budget,
          "Average Math Score": updated_average_math_score, 
          "Average Reading Score": updated_average_reading_score,
          "% Passing Math": updated_passing_math_percentage,
          "% Passing Reading": updated_passing_reading_percentage,
          "% Overall Passing": updated_overall_passing_percentage}])

# Format the "Total Students" to have the comma for a thousands separator.
district_summary2_df["Total Students"] = district_summary2_df["Total Students"].map("{:,}".format)

# Format the "Total Budget" to have the comma for a thousands separator, a decimal separator and a "$".
district_summary2_df["Total Budget"] = district_summary2_df["Total Budget"].map("${:,.2f}".format)

# Format the columns.
district_summary2_df["Average Math Score"] = district_summary2_df["Average Math Score"].map("{:.1f}".format)
district_summary2_df["Average Reading Score"] = district_summary2_df["Average Reading Score"].map("{:.1f}".format)
district_summary2_df["% Passing Math"] = district_summary2_df["% Passing Math"].map("{:.1f}".format)
district_summary2_df["% Passing Reading"] = district_summary2_df["% Passing Reading"].map("{:.1f}".format)
district_summary2_df["% Overall Passing"] = district_summary2_df["% Overall Passing"].map("{:.1f}".format)

# Display the data frame
district_summary2_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Analysis Type</th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Adjusted</td>
      <td>15</td>
      <td>38,709</td>
      <td>$24,649,428.00</td>
      <td>78.9</td>
      <td>81.9</td>
      <td>74.8</td>
      <td>85.7</td>
      <td>64.9</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Final DataFrame
final_district_summary_df = pd.concat([district_summary_df, district_summary2_df])
final_district_summary_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Analysis Type</th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BenchMark</td>
      <td>15</td>
      <td>39,170</td>
      <td>$24,649,428.00</td>
      <td>79.0</td>
      <td>81.9</td>
      <td>75.0</td>
      <td>85.8</td>
      <td>65.2</td>
    </tr>
    <tr>
      <th>0</th>
      <td>Adjusted</td>
      <td>15</td>
      <td>38,709</td>
      <td>$24,649,428.00</td>
      <td>78.9</td>
      <td>81.9</td>
      <td>74.8</td>
      <td>85.7</td>
      <td>64.9</td>
    </tr>
  </tbody>
</table>
</div>



##  School Summary


```python
# Determine the School Type
per_school_types = school_data_df.set_index(["school_name"])["type"]

# Calculate the total student count.
per_school_counts = school_data_complete_df["school_name"].value_counts()
updated_per_school_counts = updated_school_data_complete_df["school_name"].value_counts()

# Calculate the total school budget and per capita spending
per_school_budget = school_data_complete_df.groupby(["school_name"]).mean()["budget"]
updated_per_school_budget = updated_school_data_complete_df.groupby(["school_name"]).mean()["budget"]

# Calculate the per capita spending.
per_school_capita = per_school_budget / per_school_counts
updated_per_school_capita = updated_per_school_budget / updated_per_school_counts

# Calculate the average test scores.
per_school_math = school_data_complete_df.groupby(["school_name"]).mean()["math_score"]
per_school_reading = school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]

updated_per_school_math = updated_school_data_complete_df.groupby(["school_name"]).mean()["math_score"]
updated_per_school_reading = updated_school_data_complete_df.groupby(["school_name"]).mean()["reading_score"]

# Calculate the passing scores by creating a filtered DataFrame.
per_school_passing_math = school_data_complete_df[(school_data_complete_df["math_score"] >= 70)]
per_school_passing_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)]

updated_per_school_passing_math = updated_school_data_complete_df[(updated_school_data_complete_df["math_score"] >= 70)]
updated_per_school_passing_reading = updated_school_data_complete_df[(updated_school_data_complete_df["reading_score"] >= 70)]

# Calculate the number of students passing math and passing reading by school.
per_school_passing_math = per_school_passing_math.groupby(["school_name"]).count()["student_name"]
per_school_passing_reading = per_school_passing_reading.groupby(["school_name"]).count()["student_name"]

updated_per_school_passing_math = updated_per_school_passing_math.groupby(["school_name"]).count()["student_name"]
updated_per_school_passing_reading = updated_per_school_passing_reading.groupby(["school_name"]).count()["student_name"]

# Calculate the percentage of passing math and reading scores per school.
per_school_passing_math = per_school_passing_math / per_school_counts * 100
per_school_passing_reading = per_school_passing_reading / per_school_counts * 100

updated_per_school_passing_math = updated_per_school_passing_math / updated_per_school_counts * 100
updated_per_school_passing_reading = updated_per_school_passing_reading / updated_per_school_counts * 100

# Calculate the students who passed both reading and math.
per_passing_math_reading = school_data_complete_df[(school_data_complete_df["reading_score"] >= 70)
                                               & (school_data_complete_df["math_score"] >= 70)]

updated_per_passing_math_reading = updated_school_data_complete_df[(updated_school_data_complete_df["reading_score"] >= 70)
                                               & (updated_school_data_complete_df["math_score"] >= 70)]

# Calculate the number of students passing math and passing reading by school.
per_passing_math_reading = per_passing_math_reading.groupby(["school_name"]).count()["student_name"]

updated_per_passing_math_reading = updated_per_passing_math_reading.groupby(["school_name"]).count()["student_name"]

# Calculate the percentage of passing math and reading scores per school.
per_overall_passing_percentage = per_passing_math_reading / per_school_counts * 100

updated_per_overall_passing_percentage = updated_per_passing_math_reading / updated_per_school_counts * 100
```


```python
# Create the DataFrame 1
per_school_summary_df = pd.DataFrame({
    "Analysis Type": "BenchMark",
    "School Type": per_school_types,
    "Total Students": per_school_counts,
    "Total School Budget": per_school_budget,
    "Per Student Budget": per_school_capita,
    "Average Math Score": per_school_math,
    "Average Reading Score": per_school_reading,
    "% Passing Math": per_school_passing_math,
    "% Passing Reading": per_school_passing_reading,
    "% Overall Passing": per_overall_passing_percentage})
per_school_summary_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Analysis Type</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>BenchMark</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928.0</td>
      <td>628.0</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>66.680064</td>
      <td>81.933280</td>
      <td>54.642283</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>BenchMark</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356.0</td>
      <td>582.0</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>94.133477</td>
      <td>97.039828</td>
      <td>91.334769</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>BenchMark</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411.0</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>53.204476</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>BenchMark</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916.0</td>
      <td>644.0</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>68.309602</td>
      <td>79.299014</td>
      <td>54.289887</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>BenchMark</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500.0</td>
      <td>625.0</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>90.599455</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create the DataFrame 2
per_school_summary2_df = pd.DataFrame({
    "Analysis Type": "Adjusted",
    "School Type": per_school_types,
    "Total Students": updated_per_school_counts,
    "Total School Budget": updated_per_school_budget,
    "Per Student Budget": updated_per_school_capita,
    "Average Math Score": updated_per_school_math,
    "Average Reading Score": updated_per_school_reading,
    "% Passing Math": updated_per_school_passing_math,
    "% Passing Reading": updated_per_school_passing_reading,
    "% Overall Passing": updated_per_overall_passing_percentage})
per_school_summary2_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Analysis Type</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928.0</td>
      <td>628.0</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>66.680064</td>
      <td>81.933280</td>
      <td>54.642283</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356.0</td>
      <td>582.0</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>94.133477</td>
      <td>97.039828</td>
      <td>91.334769</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411.0</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>53.204476</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916.0</td>
      <td>644.0</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>68.309602</td>
      <td>79.299014</td>
      <td>54.289887</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500.0</td>
      <td>625.0</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>90.599455</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Final DataFrame
#final_school_summary_df = ([per_school_summary_df, per_school_summary2_df])
final_school_summary_df = per_school_summary_df.append(per_school_summary2_df, ignore_index=False)
### maybe use this higher up to create index_ column?
final_school_summary_df["index_"] = range(1,len(final_school_summary_df)+1)


### i've created a new index- but i don't want to loose the school names....
#final_school_summary_df.set_index("index_", inplace=True)

# Format the Total School Budget and the Per Student Budget
final_school_summary_df["Total School Budget"] = final_school_summary_df["Total School Budget"].map("${:,.2f}".format)
final_school_summary_df["Per Student Budget"] = final_school_summary_df["Per Student Budget"].map("${:,.2f}".format)

#per_school_summary2_df["Total School Budget"] = per_school_summary2_df["Total School Budget"].map("${:,.2f}".format)
#per_school_summary2_df["Per Student Budget"] = per_school_summary2_df["Per Student Budget"].map("${:,.2f}".format)



# Display the data frame
final_school_summary_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Analysis Type</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
      <th>index_</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>BenchMark</td>
      <td>District</td>
      <td>4976</td>
      <td>$3,124,928.00</td>
      <td>$628.00</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>66.680064</td>
      <td>81.933280</td>
      <td>54.642283</td>
      <td>1</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>BenchMark</td>
      <td>Charter</td>
      <td>1858</td>
      <td>$1,081,356.00</td>
      <td>$582.00</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>94.133477</td>
      <td>97.039828</td>
      <td>91.334769</td>
      <td>2</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>BenchMark</td>
      <td>District</td>
      <td>2949</td>
      <td>$1,884,411.00</td>
      <td>$639.00</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>53.204476</td>
      <td>3</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>BenchMark</td>
      <td>District</td>
      <td>2739</td>
      <td>$1,763,916.00</td>
      <td>$644.00</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>68.309602</td>
      <td>79.299014</td>
      <td>54.289887</td>
      <td>4</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>BenchMark</td>
      <td>Charter</td>
      <td>1468</td>
      <td>$917,500.00</td>
      <td>$625.00</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>90.599455</td>
      <td>5</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>BenchMark</td>
      <td>District</td>
      <td>4635</td>
      <td>$3,022,020.00</td>
      <td>$652.00</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>66.752967</td>
      <td>80.862999</td>
      <td>53.527508</td>
      <td>6</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>BenchMark</td>
      <td>Charter</td>
      <td>427</td>
      <td>$248,087.00</td>
      <td>$581.00</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>92.505855</td>
      <td>96.252927</td>
      <td>89.227166</td>
      <td>7</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>BenchMark</td>
      <td>District</td>
      <td>2917</td>
      <td>$1,910,635.00</td>
      <td>$655.00</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>65.683922</td>
      <td>81.316421</td>
      <td>53.513884</td>
      <td>8</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>BenchMark</td>
      <td>District</td>
      <td>4761</td>
      <td>$3,094,650.00</td>
      <td>$650.00</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>66.057551</td>
      <td>81.222432</td>
      <td>53.539172</td>
      <td>9</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>BenchMark</td>
      <td>Charter</td>
      <td>962</td>
      <td>$585,858.00</td>
      <td>$609.00</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>94.594595</td>
      <td>95.945946</td>
      <td>90.540541</td>
      <td>10</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>BenchMark</td>
      <td>District</td>
      <td>3999</td>
      <td>$2,547,363.00</td>
      <td>$637.00</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>66.366592</td>
      <td>80.220055</td>
      <td>52.988247</td>
      <td>11</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>BenchMark</td>
      <td>Charter</td>
      <td>1761</td>
      <td>$1,056,600.00</td>
      <td>$600.00</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>93.867121</td>
      <td>95.854628</td>
      <td>89.892107</td>
      <td>12</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>BenchMark</td>
      <td>Charter</td>
      <td>1635</td>
      <td>$1,043,130.00</td>
      <td>$638.00</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>93.272171</td>
      <td>97.308869</td>
      <td>90.948012</td>
      <td>13</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>BenchMark</td>
      <td>Charter</td>
      <td>2283</td>
      <td>$1,319,574.00</td>
      <td>$578.00</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>93.867718</td>
      <td>96.539641</td>
      <td>90.582567</td>
      <td>14</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>BenchMark</td>
      <td>Charter</td>
      <td>1800</td>
      <td>$1,049,400.00</td>
      <td>$583.00</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>93.333333</td>
      <td>96.611111</td>
      <td>90.333333</td>
      <td>15</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>4976</td>
      <td>$3,124,928.00</td>
      <td>$628.00</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>66.680064</td>
      <td>81.933280</td>
      <td>54.642283</td>
      <td>16</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1858</td>
      <td>$1,081,356.00</td>
      <td>$582.00</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>94.133477</td>
      <td>97.039828</td>
      <td>91.334769</td>
      <td>17</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>2949</td>
      <td>$1,884,411.00</td>
      <td>$639.00</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>53.204476</td>
      <td>18</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>2739</td>
      <td>$1,763,916.00</td>
      <td>$644.00</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>68.309602</td>
      <td>79.299014</td>
      <td>54.289887</td>
      <td>19</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1468</td>
      <td>$917,500.00</td>
      <td>$625.00</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>90.599455</td>
      <td>20</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>4635</td>
      <td>$3,022,020.00</td>
      <td>$652.00</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>66.752967</td>
      <td>80.862999</td>
      <td>53.527508</td>
      <td>21</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>427</td>
      <td>$248,087.00</td>
      <td>$581.00</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>92.505855</td>
      <td>96.252927</td>
      <td>89.227166</td>
      <td>22</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>2917</td>
      <td>$1,910,635.00</td>
      <td>$655.00</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>65.683922</td>
      <td>81.316421</td>
      <td>53.513884</td>
      <td>23</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>4761</td>
      <td>$3,094,650.00</td>
      <td>$650.00</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>66.057551</td>
      <td>81.222432</td>
      <td>53.539172</td>
      <td>24</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>962</td>
      <td>$585,858.00</td>
      <td>$609.00</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>94.594595</td>
      <td>95.945946</td>
      <td>90.540541</td>
      <td>25</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>3999</td>
      <td>$2,547,363.00</td>
      <td>$637.00</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>66.366592</td>
      <td>80.220055</td>
      <td>52.988247</td>
      <td>26</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1761</td>
      <td>$1,056,600.00</td>
      <td>$600.00</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>93.867121</td>
      <td>95.854628</td>
      <td>89.892107</td>
      <td>27</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1174</td>
      <td>$1,043,130.00</td>
      <td>$888.53</td>
      <td>83.350937</td>
      <td>83.896082</td>
      <td>93.185690</td>
      <td>97.018739</td>
      <td>90.630324</td>
      <td>28</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>2283</td>
      <td>$1,319,574.00</td>
      <td>$578.00</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>93.867718</td>
      <td>96.539641</td>
      <td>90.582567</td>
      <td>29</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1800</td>
      <td>$1,049,400.00</td>
      <td>$583.00</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>93.333333</td>
      <td>96.611111</td>
      <td>90.333333</td>
      <td>30</td>
    </tr>
  </tbody>
</table>
</div>




```python
updated_school_data_complete_df.loc[(updated_school_data_complete_df["school_name"] == "Thomas High School")
                                         & (updated_school_data_complete_df["grade"] != "9th"), "Student ID"].count() 
```




    1174




```python
# Step 5.  Get the number of 10th-12th graders from Thomas High School (THS).
print ("Number of 10th-12th graders from Thomas High School (THS):",
      updated_school_data_complete_df.loc[(updated_school_data_complete_df["school_name"] == "Thomas High School")
                                         &((updated_school_data_complete_df["grade"] == "10th") 
                                            | (updated_school_data_complete_df["grade"] == "11th")
                                            | (updated_school_data_complete_df["grade"] == "12th")), "Student ID"].count() )

ths_student_count =       updated_school_data_complete_df.loc[(updated_school_data_complete_df["school_name"] == "Thomas High School")
                                         &((updated_school_data_complete_df["grade"] == "10th") 
                                            | (updated_school_data_complete_df["grade"] == "11th")
                                            | (updated_school_data_complete_df["grade"] == "12th")), "Student ID"].count() 
```

    Number of 10th-12th graders from Thomas High School (THS): 1174
    


```python
# Step 6. Get all the students passing math from THS
print ("Number of students passing math from Thomas High School (THS):", 
      updated_school_data_complete_df.loc[(updated_school_data_complete_df["school_name"] == "Thomas High School")
                                         &(updated_school_data_complete_df["math_score"] >= 70), "Student ID"].count() )
```

    Number of students passing math from Thomas High School (THS): 1094
    


```python
# Step 7. Get all the students passing reading from THS
print ("Number of students passing reading from Thomas High School (THS):", 
      updated_school_data_complete_df.loc[(updated_school_data_complete_df["school_name"] == "Thomas High School")
                                         &(updated_school_data_complete_df["reading_score"] >= 70), "Student ID"].count() )
```

    Number of students passing reading from Thomas High School (THS): 1139
    


```python
# Step 8. Get all the students passing math and reading from THS
print ("Number of students passing math and reading from Thomas High School (THS):", 
      updated_school_data_complete_df.loc[(updated_school_data_complete_df["school_name"] == "Thomas High School")
                                         &(updated_school_data_complete_df["math_score"] >= 70)
                                         &(updated_school_data_complete_df["reading_score"] >= 70), "Student ID"].count() )
```

    Number of students passing math and reading from Thomas High School (THS): 1064
    


```python
# Step 9. Calculate the percentage of 10th-12th grade students passing math from Thomas High School. 
print ("Percentage of students passing math from Thomas High School (THS):", 
      updated_school_data_complete_df.loc[(updated_school_data_complete_df["school_name"] == "Thomas High School")
                                         &(updated_school_data_complete_df["math_score"] >= 70), "Student ID"].count() / ths_student_count * 100)
```

    Percentage of students passing math from Thomas High School (THS): 93.18568994889267
    


```python
# Step 10. Calculate the percentage of 10th-12th grade students passing reading from Thomas High School.
print ("Percentage of students passing reading from Thomas High School (THS):", 
      updated_school_data_complete_df.loc[(updated_school_data_complete_df["school_name"] == "Thomas High School")
                                         &(updated_school_data_complete_df["reading_score"] >= 70), "Student ID"].count() / ths_student_count * 100)
```

    Percentage of students passing reading from Thomas High School (THS): 97.01873935264055
    


```python
# Step 11. Calculate the overall passing percentage of 10th-12th grade from Thomas High School. 
print ("Overall passing percentage from Thomas High School (THS):", 
      updated_school_data_complete_df.loc[(updated_school_data_complete_df["school_name"] == "Thomas High School")
                                         &(updated_school_data_complete_df["math_score"] >= 70)
                                         &(updated_school_data_complete_df["reading_score"] >= 70), "Student ID"].count() / ths_student_count * 100)
```

    Overall passing percentage from Thomas High School (THS): 90.63032367972743
    


```python
# Step 12. Replace the passing math percent for Thomas High School in the per_school_summary_df.
# this is no longer necessary; I've already created a df for adjusted values
```


```python
# Step 13. Replace the passing reading percentage for Thomas High School in the per_school_summary_df.
# this is no longer necessary; I've already created a df for adjusted values
```


```python
# Step 14. Replace the overall passing percentage for Thomas High School in the per_school_summary_df.
# this is no longer necessary;  I've already created a df for adjusted values
```


```python
# per_school_summary_df
per_school_summary2_df.sort_values(by="% Overall Passing", ascending=False, ignore_index=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Analysis Type</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Cabrera High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356.0</td>
      <td>582.000000</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>94.133477</td>
      <td>97.039828</td>
      <td>91.334769</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1174</td>
      <td>1043130.0</td>
      <td>888.526405</td>
      <td>83.350937</td>
      <td>83.896082</td>
      <td>93.185690</td>
      <td>97.018739</td>
      <td>90.630324</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500.0</td>
      <td>625.000000</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>90.599455</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574.0</td>
      <td>578.000000</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>93.867718</td>
      <td>96.539641</td>
      <td>90.582567</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858.0</td>
      <td>609.000000</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>94.594595</td>
      <td>95.945946</td>
      <td>90.540541</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400.0</td>
      <td>583.000000</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>93.333333</td>
      <td>96.611111</td>
      <td>90.333333</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600.0</td>
      <td>600.000000</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>93.867121</td>
      <td>95.854628</td>
      <td>89.892107</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087.0</td>
      <td>581.000000</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>92.505855</td>
      <td>96.252927</td>
      <td>89.227166</td>
    </tr>
    <tr>
      <th>Bailey High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928.0</td>
      <td>628.000000</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>66.680064</td>
      <td>81.933280</td>
      <td>54.642283</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916.0</td>
      <td>644.000000</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>68.309602</td>
      <td>79.299014</td>
      <td>54.289887</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650.0</td>
      <td>650.000000</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>66.057551</td>
      <td>81.222432</td>
      <td>53.539172</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020.0</td>
      <td>652.000000</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>66.752967</td>
      <td>80.862999</td>
      <td>53.527508</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635.0</td>
      <td>655.000000</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>65.683922</td>
      <td>81.316421</td>
      <td>53.513884</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411.0</td>
      <td>639.000000</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>53.204476</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363.0</td>
      <td>637.000000</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>66.366592</td>
      <td>80.220055</td>
      <td>52.988247</td>
    </tr>
  </tbody>
</table>
</div>



## High and Low Performing Schools 


```python
# Sort and show top five schools.
#final_school_summary_df

print("BenchMark Analysis")
rslt_df = per_school_summary_df.sort_values(by="% Overall Passing", ascending=False, ignore_index=False)
print("Top 5 Schools:",  list(rslt_df.index[:5]), "\n")

print("Adjusted Analysis")
rslt_df = per_school_summary2_df.sort_values(by="% Overall Passing", ascending=False, ignore_index=False)
print("Top 5 Schools:",  list(rslt_df.index[:5]))
```

    BenchMark Analysis
    Top 5 Schools: ['Cabrera High School', 'Thomas High School', 'Griffin High School', 'Wilson High School', 'Pena High School'] 
    
    Adjusted Analysis
    Top 5 Schools: ['Cabrera High School', 'Thomas High School', 'Griffin High School', 'Wilson High School', 'Pena High School']
    


```python
# Sort and show bottom five schools.

print("BenchMark Analysis")
rslt_df = per_school_summary_df.sort_values(by="% Overall Passing", ascending=True, ignore_index=False)
print ("Bottom 5 Schools:", list(rslt_df.index[:5]), "\n")

print("Adjusted Analysis")
rslt_df = per_school_summary2_df.sort_values(by="% Overall Passing", ascending=True, ignore_index=False)
print ("Bottom 5 Schools:", list(rslt_df.index[:5]))
```

    BenchMark Analysis
    Bottom 5 Schools: ['Rodriguez High School', 'Figueroa High School', 'Huang High School', 'Hernandez High School', 'Johnson High School'] 
    
    Adjusted Analysis
    Bottom 5 Schools: ['Rodriguez High School', 'Figueroa High School', 'Huang High School', 'Hernandez High School', 'Johnson High School']
    

## Math and Reading Scores by Grade


```python
# Create a DataFrame of scores by grade level using conditionals.
bench_frosh = school_data_complete_df[(school_data_complete_df["grade"] == "9th")]
bench_soph  = school_data_complete_df[(school_data_complete_df["grade"] == "10th")]
bench_jun   = school_data_complete_df[(school_data_complete_df["grade"] == "11th")]
bench_sen   = school_data_complete_df[(school_data_complete_df["grade"] == "12th")]

updated_frosh = updated_school_data_complete_df[(updated_school_data_complete_df["grade"] == "9th")]
updated_soph  = updated_school_data_complete_df[(updated_school_data_complete_df["grade"] == "10th")]
updated_jun   = updated_school_data_complete_df[(updated_school_data_complete_df["grade"] == "11th")]
updated_sen   = updated_school_data_complete_df[(updated_school_data_complete_df["grade"] == "12th")]

# Group each grade level DataFrame by the school name for the average math score.
bench_frosh_math_scores = bench_frosh.groupby(["school_name"]).mean()["math_score"]
bench_soph_math_scores  = bench_soph.groupby(["school_name"]).mean()["math_score"]
bench_jun_math_scores   = bench_jun.groupby(["school_name"]).mean()["math_score"]
bench_sen_math_scores   = bench_sen.groupby(["school_name"]).mean()["math_score"]

updated_frosh_math_scores = updated_frosh.groupby(["school_name"]).mean()["math_score"]
updated_soph_math_scores  = updated_soph.groupby(["school_name"]).mean()["math_score"]
updated_jun_math_scores   = updated_jun.groupby(["school_name"]).mean()["math_score"]
updated_sen_math_scores   = updated_sen.groupby(["school_name"]).mean()["math_score"]

# Group each grade level DataFrame by the school name for the average reading score.
bench_frosh_reading_scores = bench_frosh.groupby(["school_name"]).mean()["reading_score"]
bench_soph_reading_scores  = bench_soph.groupby(["school_name"]).mean()["reading_score"]
bench_jun_reading_scores   = bench_jun.groupby(["school_name"]).mean()["reading_score"]
bench_sen_reading_scores   = bench_sen.groupby(["school_name"]).mean()["reading_score"]

updated_frosh_reading_scores = updated_frosh.groupby(["school_name"]).mean()["reading_score"]
updated_soph_reading_scores  = updated_soph.groupby(["school_name"]).mean()["reading_score"]
updated_jun_reading_scores   = updated_jun.groupby(["school_name"]).mean()["reading_score"]
updated_sen_reading_scores   = updated_sen.groupby(["school_name"]).mean()["reading_score"]

```


```python
# Combine each grade level Series for average math scores into a single DataFrame.
math_scores_by_grade = pd.DataFrame({
               "9th BenchMark":  bench_frosh_math_scores,
               "10th BenchMark": bench_soph_math_scores,
               "11th BenchMark": bench_jun_math_scores,
               "12th BenchMark": bench_sen_math_scores,
    
               "9th Adjusted":  updated_frosh_math_scores,
               "10th Adjusted": updated_soph_math_scores,
               "11th Adjusted": updated_jun_math_scores,
               "12th Adjusted": updated_sen_math_scores})

math_scores_by_grade
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>9th BenchMark</th>
      <th>10th BenchMark</th>
      <th>11th BenchMark</th>
      <th>12th BenchMark</th>
      <th>9th Adjusted</th>
      <th>10th Adjusted</th>
      <th>11th Adjusted</th>
      <th>12th Adjusted</th>
    </tr>
    <tr>
      <th>school_name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.083676</td>
      <td>76.996772</td>
      <td>77.515588</td>
      <td>76.492218</td>
      <td>77.083676</td>
      <td>76.996772</td>
      <td>77.515588</td>
      <td>76.492218</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.094697</td>
      <td>83.154506</td>
      <td>82.765560</td>
      <td>83.277487</td>
      <td>83.094697</td>
      <td>83.154506</td>
      <td>82.765560</td>
      <td>83.277487</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.403037</td>
      <td>76.539974</td>
      <td>76.884344</td>
      <td>77.151369</td>
      <td>76.403037</td>
      <td>76.539974</td>
      <td>76.884344</td>
      <td>77.151369</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.361345</td>
      <td>77.672316</td>
      <td>76.918058</td>
      <td>76.179963</td>
      <td>77.361345</td>
      <td>77.672316</td>
      <td>76.918058</td>
      <td>76.179963</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>82.044010</td>
      <td>84.229064</td>
      <td>83.842105</td>
      <td>83.356164</td>
      <td>82.044010</td>
      <td>84.229064</td>
      <td>83.842105</td>
      <td>83.356164</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.438495</td>
      <td>77.337408</td>
      <td>77.136029</td>
      <td>77.186567</td>
      <td>77.438495</td>
      <td>77.337408</td>
      <td>77.136029</td>
      <td>77.186567</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.787402</td>
      <td>83.429825</td>
      <td>85.000000</td>
      <td>82.855422</td>
      <td>83.787402</td>
      <td>83.429825</td>
      <td>85.000000</td>
      <td>82.855422</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.027251</td>
      <td>75.908735</td>
      <td>76.446602</td>
      <td>77.225641</td>
      <td>77.027251</td>
      <td>75.908735</td>
      <td>76.446602</td>
      <td>77.225641</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.187857</td>
      <td>76.691117</td>
      <td>77.491653</td>
      <td>76.863248</td>
      <td>77.187857</td>
      <td>76.691117</td>
      <td>77.491653</td>
      <td>76.863248</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.625455</td>
      <td>83.372000</td>
      <td>84.328125</td>
      <td>84.121547</td>
      <td>83.625455</td>
      <td>83.372000</td>
      <td>84.328125</td>
      <td>84.121547</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.859966</td>
      <td>76.612500</td>
      <td>76.395626</td>
      <td>77.690748</td>
      <td>76.859966</td>
      <td>76.612500</td>
      <td>76.395626</td>
      <td>77.690748</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.420755</td>
      <td>82.917411</td>
      <td>83.383495</td>
      <td>83.778976</td>
      <td>83.420755</td>
      <td>82.917411</td>
      <td>83.383495</td>
      <td>83.778976</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.590022</td>
      <td>83.087886</td>
      <td>83.498795</td>
      <td>83.497041</td>
      <td>NaN</td>
      <td>83.087886</td>
      <td>83.498795</td>
      <td>83.497041</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.085578</td>
      <td>83.724422</td>
      <td>83.195326</td>
      <td>83.035794</td>
      <td>83.085578</td>
      <td>83.724422</td>
      <td>83.195326</td>
      <td>83.035794</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.264706</td>
      <td>84.010288</td>
      <td>83.836782</td>
      <td>83.644986</td>
      <td>83.264706</td>
      <td>84.010288</td>
      <td>83.836782</td>
      <td>83.644986</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Combine each grade level Series for average reading scores into a single DataFrame.
reading_scores_by_grade = pd.DataFrame({
               "9th BenchMark":  bench_frosh_reading_scores,
               "10th BenchMark": bench_soph_reading_scores,
               "11th BenchMark": bench_jun_reading_scores,
               "12th BenchMark": bench_sen_reading_scores,
    
               "9th Adjusted":  updated_frosh_reading_scores,
               "10th Adjusted": updated_soph_reading_scores,
               "11th Adjusted": updated_jun_reading_scores,
               "12th Adjusted": updated_sen_reading_scores})

reading_scores_by_grade
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>9th BenchMark</th>
      <th>10th BenchMark</th>
      <th>11th BenchMark</th>
      <th>12th BenchMark</th>
      <th>9th Adjusted</th>
      <th>10th Adjusted</th>
      <th>11th Adjusted</th>
      <th>12th Adjusted</th>
    </tr>
    <tr>
      <th>school_name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>81.303155</td>
      <td>80.907183</td>
      <td>80.945643</td>
      <td>80.912451</td>
      <td>81.303155</td>
      <td>80.907183</td>
      <td>80.945643</td>
      <td>80.912451</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.676136</td>
      <td>84.253219</td>
      <td>83.788382</td>
      <td>84.287958</td>
      <td>83.676136</td>
      <td>84.253219</td>
      <td>83.788382</td>
      <td>84.287958</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.198598</td>
      <td>81.408912</td>
      <td>80.640339</td>
      <td>81.384863</td>
      <td>81.198598</td>
      <td>81.408912</td>
      <td>80.640339</td>
      <td>81.384863</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>80.632653</td>
      <td>81.262712</td>
      <td>80.403642</td>
      <td>80.662338</td>
      <td>80.632653</td>
      <td>81.262712</td>
      <td>80.403642</td>
      <td>80.662338</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.369193</td>
      <td>83.706897</td>
      <td>84.288089</td>
      <td>84.013699</td>
      <td>83.369193</td>
      <td>83.706897</td>
      <td>84.288089</td>
      <td>84.013699</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.866860</td>
      <td>80.660147</td>
      <td>81.396140</td>
      <td>80.857143</td>
      <td>80.866860</td>
      <td>80.660147</td>
      <td>81.396140</td>
      <td>80.857143</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.677165</td>
      <td>83.324561</td>
      <td>83.815534</td>
      <td>84.698795</td>
      <td>83.677165</td>
      <td>83.324561</td>
      <td>83.815534</td>
      <td>84.698795</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.290284</td>
      <td>81.512386</td>
      <td>81.417476</td>
      <td>80.305983</td>
      <td>81.290284</td>
      <td>81.512386</td>
      <td>81.417476</td>
      <td>80.305983</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>81.260714</td>
      <td>80.773431</td>
      <td>80.616027</td>
      <td>81.227564</td>
      <td>81.260714</td>
      <td>80.773431</td>
      <td>80.616027</td>
      <td>81.227564</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.807273</td>
      <td>83.612000</td>
      <td>84.335938</td>
      <td>84.591160</td>
      <td>83.807273</td>
      <td>83.612000</td>
      <td>84.335938</td>
      <td>84.591160</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>80.993127</td>
      <td>80.629808</td>
      <td>80.864811</td>
      <td>80.376426</td>
      <td>80.993127</td>
      <td>80.629808</td>
      <td>80.864811</td>
      <td>80.376426</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>84.122642</td>
      <td>83.441964</td>
      <td>84.373786</td>
      <td>82.781671</td>
      <td>84.122642</td>
      <td>83.441964</td>
      <td>84.373786</td>
      <td>82.781671</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.728850</td>
      <td>84.254157</td>
      <td>83.585542</td>
      <td>83.831361</td>
      <td>NaN</td>
      <td>84.254157</td>
      <td>83.585542</td>
      <td>83.831361</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.939778</td>
      <td>84.021452</td>
      <td>83.764608</td>
      <td>84.317673</td>
      <td>83.939778</td>
      <td>84.021452</td>
      <td>83.764608</td>
      <td>84.317673</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.833333</td>
      <td>83.812757</td>
      <td>84.156322</td>
      <td>84.073171</td>
      <td>83.833333</td>
      <td>83.812757</td>
      <td>84.156322</td>
      <td>84.073171</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Format each grade column.
math_scores_by_grade["9th BenchMark"]     = math_scores_by_grade["9th BenchMark"].map("{:,.1f}".format)
math_scores_by_grade["10th BenchMark"]    = math_scores_by_grade["10th BenchMark"].map("{:,.1f}".format)
math_scores_by_grade["11th BenchMark"]    = math_scores_by_grade["11th BenchMark"].map("{:,.1f}".format)
math_scores_by_grade["12th BenchMark"]    = math_scores_by_grade["12th BenchMark"].map("{:,.1f}".format)
reading_scores_by_grade["9th BenchMark"]  = reading_scores_by_grade["9th BenchMark"].map("{:,.1f}".format)
reading_scores_by_grade["10th BenchMark"] = reading_scores_by_grade["10th BenchMark"].map("{:,.1f}".format)
reading_scores_by_grade["11th BenchMark"] = reading_scores_by_grade["11th BenchMark"].map("{:,.1f}".format)
reading_scores_by_grade["12th BenchMark"] = reading_scores_by_grade["12th BenchMark"].map("{:,.1f}".format)

math_scores_by_grade["9th Adjusted"]     = math_scores_by_grade["9th Adjusted"].map("{:,.1f}".format)
math_scores_by_grade["10th Adjusted"]    = math_scores_by_grade["10th Adjusted"].map("{:,.1f}".format)
math_scores_by_grade["11th Adjusted"]    = math_scores_by_grade["11th Adjusted"].map("{:,.1f}".format)
math_scores_by_grade["12th Adjusted"]    = math_scores_by_grade["12th Adjusted"].map("{:,.1f}".format)
reading_scores_by_grade["9th Adjusted"]  = reading_scores_by_grade["9th Adjusted"].map("{:,.1f}".format)
reading_scores_by_grade["10th Adjusted"] = reading_scores_by_grade["10th Adjusted"].map("{:,.1f}".format)
reading_scores_by_grade["11th Adjusted"] = reading_scores_by_grade["11th Adjusted"].map("{:,.1f}".format)
reading_scores_by_grade["12th Adjusted"] = reading_scores_by_grade["12th Adjusted"].map("{:,.1f}".format)
```


```python
# Remove the index.
math_scores_by_grade.index.name = None

# Display the data frame
math_scores_by_grade
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>9th BenchMark</th>
      <th>10th BenchMark</th>
      <th>11th BenchMark</th>
      <th>12th BenchMark</th>
      <th>9th Adjusted</th>
      <th>10th Adjusted</th>
      <th>11th Adjusted</th>
      <th>12th Adjusted</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>77.1</td>
      <td>77.0</td>
      <td>77.5</td>
      <td>76.5</td>
      <td>77.1</td>
      <td>77.0</td>
      <td>77.5</td>
      <td>76.5</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.1</td>
      <td>83.2</td>
      <td>82.8</td>
      <td>83.3</td>
      <td>83.1</td>
      <td>83.2</td>
      <td>82.8</td>
      <td>83.3</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>76.4</td>
      <td>76.5</td>
      <td>76.9</td>
      <td>77.2</td>
      <td>76.4</td>
      <td>76.5</td>
      <td>76.9</td>
      <td>77.2</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>77.4</td>
      <td>77.7</td>
      <td>76.9</td>
      <td>76.2</td>
      <td>77.4</td>
      <td>77.7</td>
      <td>76.9</td>
      <td>76.2</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>82.0</td>
      <td>84.2</td>
      <td>83.8</td>
      <td>83.4</td>
      <td>82.0</td>
      <td>84.2</td>
      <td>83.8</td>
      <td>83.4</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>77.4</td>
      <td>77.3</td>
      <td>77.1</td>
      <td>77.2</td>
      <td>77.4</td>
      <td>77.3</td>
      <td>77.1</td>
      <td>77.2</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.8</td>
      <td>83.4</td>
      <td>85.0</td>
      <td>82.9</td>
      <td>83.8</td>
      <td>83.4</td>
      <td>85.0</td>
      <td>82.9</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>77.0</td>
      <td>75.9</td>
      <td>76.4</td>
      <td>77.2</td>
      <td>77.0</td>
      <td>75.9</td>
      <td>76.4</td>
      <td>77.2</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>77.2</td>
      <td>76.7</td>
      <td>77.5</td>
      <td>76.9</td>
      <td>77.2</td>
      <td>76.7</td>
      <td>77.5</td>
      <td>76.9</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.6</td>
      <td>83.4</td>
      <td>84.3</td>
      <td>84.1</td>
      <td>83.6</td>
      <td>83.4</td>
      <td>84.3</td>
      <td>84.1</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>76.9</td>
      <td>76.6</td>
      <td>76.4</td>
      <td>77.7</td>
      <td>76.9</td>
      <td>76.6</td>
      <td>76.4</td>
      <td>77.7</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>83.4</td>
      <td>82.9</td>
      <td>83.4</td>
      <td>83.8</td>
      <td>83.4</td>
      <td>82.9</td>
      <td>83.4</td>
      <td>83.8</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.6</td>
      <td>83.1</td>
      <td>83.5</td>
      <td>83.5</td>
      <td>nan</td>
      <td>83.1</td>
      <td>83.5</td>
      <td>83.5</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.1</td>
      <td>83.7</td>
      <td>83.2</td>
      <td>83.0</td>
      <td>83.1</td>
      <td>83.7</td>
      <td>83.2</td>
      <td>83.0</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.3</td>
      <td>84.0</td>
      <td>83.8</td>
      <td>83.6</td>
      <td>83.3</td>
      <td>84.0</td>
      <td>83.8</td>
      <td>83.6</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Remove the index.
reading_scores_by_grade.index.name = None

# Display the data frame
reading_scores_by_grade
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>9th BenchMark</th>
      <th>10th BenchMark</th>
      <th>11th BenchMark</th>
      <th>12th BenchMark</th>
      <th>9th Adjusted</th>
      <th>10th Adjusted</th>
      <th>11th Adjusted</th>
      <th>12th Adjusted</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>81.3</td>
      <td>80.9</td>
      <td>80.9</td>
      <td>80.9</td>
      <td>81.3</td>
      <td>80.9</td>
      <td>80.9</td>
      <td>80.9</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>83.7</td>
      <td>84.3</td>
      <td>83.8</td>
      <td>84.3</td>
      <td>83.7</td>
      <td>84.3</td>
      <td>83.8</td>
      <td>84.3</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>81.2</td>
      <td>81.4</td>
      <td>80.6</td>
      <td>81.4</td>
      <td>81.2</td>
      <td>81.4</td>
      <td>80.6</td>
      <td>81.4</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>80.6</td>
      <td>81.3</td>
      <td>80.4</td>
      <td>80.7</td>
      <td>80.6</td>
      <td>81.3</td>
      <td>80.4</td>
      <td>80.7</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>83.4</td>
      <td>83.7</td>
      <td>84.3</td>
      <td>84.0</td>
      <td>83.4</td>
      <td>83.7</td>
      <td>84.3</td>
      <td>84.0</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>80.9</td>
      <td>80.7</td>
      <td>81.4</td>
      <td>80.9</td>
      <td>80.9</td>
      <td>80.7</td>
      <td>81.4</td>
      <td>80.9</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>83.7</td>
      <td>83.3</td>
      <td>83.8</td>
      <td>84.7</td>
      <td>83.7</td>
      <td>83.3</td>
      <td>83.8</td>
      <td>84.7</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>81.3</td>
      <td>81.5</td>
      <td>81.4</td>
      <td>80.3</td>
      <td>81.3</td>
      <td>81.5</td>
      <td>81.4</td>
      <td>80.3</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>81.3</td>
      <td>80.8</td>
      <td>80.6</td>
      <td>81.2</td>
      <td>81.3</td>
      <td>80.8</td>
      <td>80.6</td>
      <td>81.2</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>83.8</td>
      <td>83.6</td>
      <td>84.3</td>
      <td>84.6</td>
      <td>83.8</td>
      <td>83.6</td>
      <td>84.3</td>
      <td>84.6</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>81.0</td>
      <td>80.6</td>
      <td>80.9</td>
      <td>80.4</td>
      <td>81.0</td>
      <td>80.6</td>
      <td>80.9</td>
      <td>80.4</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>84.1</td>
      <td>83.4</td>
      <td>84.4</td>
      <td>82.8</td>
      <td>84.1</td>
      <td>83.4</td>
      <td>84.4</td>
      <td>82.8</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>83.7</td>
      <td>84.3</td>
      <td>83.6</td>
      <td>83.8</td>
      <td>nan</td>
      <td>84.3</td>
      <td>83.6</td>
      <td>83.8</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>83.9</td>
      <td>84.0</td>
      <td>83.8</td>
      <td>84.3</td>
      <td>83.9</td>
      <td>84.0</td>
      <td>83.8</td>
      <td>84.3</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>83.8</td>
      <td>83.8</td>
      <td>84.2</td>
      <td>84.1</td>
      <td>83.8</td>
      <td>83.8</td>
      <td>84.2</td>
      <td>84.1</td>
    </tr>
  </tbody>
</table>
</div>



## Scores by School Spending


```python
# Establish the spending bins and group names.

###  ...print(min_views)
###  interval = round((max_views-min_views)/10)
###  print(interval)
###  import numpy as np
###  bins = np.arange(min_views, max_views, interval).tolist()
###  bins

###  min_ = per_school_summary2_df["Per Student Budget"].min()
###  max_ = per_school_summary2_df["Per Student Budget"].max()
###  interval_ = round((max_ - min_)/5)

###  print(min_)
###  print(max_)
###  print(interval_)
###  bin_spend = np.arange(min_, max_, interval_).tolist
###  bin_name = bin_spend.map("${:,.2f}".format)

spending_bins = [0, 585, 630, 645, 675]
group_names = ["<$584", "$585-629", "$630-644", "$645-675"]

# Categorize spending based on the bins.
per_school_summary2_df["Spending Ranges (Per Student)"] = pd.cut(per_school_capita, spending_bins, labels=group_names)
per_school_summary2_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Analysis Type</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
      <th>Spending Ranges (Per Student)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928.0</td>
      <td>628.000000</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>66.680064</td>
      <td>81.933280</td>
      <td>54.642283</td>
      <td>$585-629</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356.0</td>
      <td>582.000000</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>94.133477</td>
      <td>97.039828</td>
      <td>91.334769</td>
      <td>&lt;$584</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411.0</td>
      <td>639.000000</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>53.204476</td>
      <td>$630-644</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916.0</td>
      <td>644.000000</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>68.309602</td>
      <td>79.299014</td>
      <td>54.289887</td>
      <td>$630-644</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500.0</td>
      <td>625.000000</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>90.599455</td>
      <td>$585-629</td>
    </tr>
    <tr>
      <th>Hernandez High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020.0</td>
      <td>652.000000</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>66.752967</td>
      <td>80.862999</td>
      <td>53.527508</td>
      <td>$645-675</td>
    </tr>
    <tr>
      <th>Holden High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>427</td>
      <td>248087.0</td>
      <td>581.000000</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>92.505855</td>
      <td>96.252927</td>
      <td>89.227166</td>
      <td>&lt;$584</td>
    </tr>
    <tr>
      <th>Huang High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635.0</td>
      <td>655.000000</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>65.683922</td>
      <td>81.316421</td>
      <td>53.513884</td>
      <td>$645-675</td>
    </tr>
    <tr>
      <th>Johnson High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>4761</td>
      <td>3094650.0</td>
      <td>650.000000</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>66.057551</td>
      <td>81.222432</td>
      <td>53.539172</td>
      <td>$645-675</td>
    </tr>
    <tr>
      <th>Pena High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>962</td>
      <td>585858.0</td>
      <td>609.000000</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>94.594595</td>
      <td>95.945946</td>
      <td>90.540541</td>
      <td>$585-629</td>
    </tr>
    <tr>
      <th>Rodriguez High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>3999</td>
      <td>2547363.0</td>
      <td>637.000000</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>66.366592</td>
      <td>80.220055</td>
      <td>52.988247</td>
      <td>$630-644</td>
    </tr>
    <tr>
      <th>Shelton High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600.0</td>
      <td>600.000000</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>93.867121</td>
      <td>95.854628</td>
      <td>89.892107</td>
      <td>$585-629</td>
    </tr>
    <tr>
      <th>Thomas High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1174</td>
      <td>1043130.0</td>
      <td>888.526405</td>
      <td>83.350937</td>
      <td>83.896082</td>
      <td>93.185690</td>
      <td>97.018739</td>
      <td>90.630324</td>
      <td>$630-644</td>
    </tr>
    <tr>
      <th>Wilson High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574.0</td>
      <td>578.000000</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>93.867718</td>
      <td>96.539641</td>
      <td>90.582567</td>
      <td>&lt;$584</td>
    </tr>
    <tr>
      <th>Wright High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400.0</td>
      <td>583.000000</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>93.333333</td>
      <td>96.611111</td>
      <td>90.333333</td>
      <td>&lt;$584</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Calculate averages for the desired columns. 
spending_math_scores     = per_school_summary2_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Math Score"]
spending_reading_scores  = per_school_summary2_df.groupby(["Spending Ranges (Per Student)"]).mean()["Average Reading Score"]
spending_passing_math    = per_school_summary2_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Math"]
spending_passing_reading = per_school_summary2_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Passing Reading"]
overall_passing_spending = per_school_summary2_df.groupby(["Spending Ranges (Per Student)"]).mean()["% Overall Passing"]
```


```python
# Create the DataFrame
updated_spending_summary_df = pd.DataFrame({
          "Average Math Score" : spending_math_scores,
          "Average Reading Score": spending_reading_scores,
          "% Passing Math": spending_passing_math,
          "% Passing Reading": spending_passing_reading,
          "% Overall Passing": overall_passing_spending})

updated_spending_summary_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>Spending Ranges (Per Student)</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;$584</th>
      <td>83.455399</td>
      <td>83.933814</td>
      <td>93.460096</td>
      <td>96.610877</td>
      <td>90.369459</td>
    </tr>
    <tr>
      <th>$585-629</th>
      <td>81.899826</td>
      <td>83.155286</td>
      <td>87.133538</td>
      <td>92.718205</td>
      <td>81.418596</td>
    </tr>
    <tr>
      <th>$630-644</th>
      <td>78.502002</td>
      <td>81.636261</td>
      <td>73.462589</td>
      <td>84.319261</td>
      <td>62.778233</td>
    </tr>
    <tr>
      <th>$645-675</th>
      <td>76.997210</td>
      <td>81.027843</td>
      <td>66.164813</td>
      <td>81.133951</td>
      <td>53.526855</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Format the DataFrame 
updated_spending_summary_df["Average Math Score"]    = updated_spending_summary_df["Average Math Score"].map("{:.1f}".format)
updated_spending_summary_df["Average Reading Score"] = updated_spending_summary_df["Average Reading Score"].map("{:.1f}".format)
updated_spending_summary_df["% Passing Math"]        = updated_spending_summary_df["% Passing Math"].map("{:.0f}".format)
updated_spending_summary_df["% Passing Reading"]     = updated_spending_summary_df["% Passing Reading"].map("{:.0f}".format)
updated_spending_summary_df["% Overall Passing"]     = updated_spending_summary_df["% Overall Passing"].map("{:.0f}".format)

updated_spending_summary_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>Spending Ranges (Per Student)</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;$584</th>
      <td>83.5</td>
      <td>83.9</td>
      <td>93</td>
      <td>97</td>
      <td>90</td>
    </tr>
    <tr>
      <th>$585-629</th>
      <td>81.9</td>
      <td>83.2</td>
      <td>87</td>
      <td>93</td>
      <td>81</td>
    </tr>
    <tr>
      <th>$630-644</th>
      <td>78.5</td>
      <td>81.6</td>
      <td>73</td>
      <td>84</td>
      <td>63</td>
    </tr>
    <tr>
      <th>$645-675</th>
      <td>77.0</td>
      <td>81.0</td>
      <td>66</td>
      <td>81</td>
      <td>54</td>
    </tr>
  </tbody>
</table>
</div>



## Scores by School Size


```python
# Establish the bins.
size_bins = [0, 1000, 2000, 5000]
group_names = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

# Categorize spending based on the bins.
per_school_summary2_df["School Size"] = pd.cut(per_school_summary2_df["Total Students"], size_bins, labels=group_names)

per_school_summary2_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Analysis Type</th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
      <th>Spending Ranges (Per Student)</th>
      <th>School Size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Bailey High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>4976</td>
      <td>3124928.0</td>
      <td>628.0</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>66.680064</td>
      <td>81.933280</td>
      <td>54.642283</td>
      <td>$585-629</td>
      <td>Large (2000-5000)</td>
    </tr>
    <tr>
      <th>Cabrera High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356.0</td>
      <td>582.0</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>94.133477</td>
      <td>97.039828</td>
      <td>91.334769</td>
      <td>&lt;$584</td>
      <td>Medium (1000-2000)</td>
    </tr>
    <tr>
      <th>Figueroa High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411.0</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>65.988471</td>
      <td>80.739234</td>
      <td>53.204476</td>
      <td>$630-644</td>
      <td>Large (2000-5000)</td>
    </tr>
    <tr>
      <th>Ford High School</th>
      <td>Adjusted</td>
      <td>District</td>
      <td>2739</td>
      <td>1763916.0</td>
      <td>644.0</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>68.309602</td>
      <td>79.299014</td>
      <td>54.289887</td>
      <td>$630-644</td>
      <td>Large (2000-5000)</td>
    </tr>
    <tr>
      <th>Griffin High School</th>
      <td>Adjusted</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500.0</td>
      <td>625.0</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>93.392371</td>
      <td>97.138965</td>
      <td>90.599455</td>
      <td>$585-629</td>
      <td>Medium (1000-2000)</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Calculate averages for the desired columns. 
size_math_scores     = per_school_summary2_df.groupby(["School Size"]).mean()["Average Math Score"]
size_reading_scores  = per_school_summary2_df.groupby(["School Size"]).mean()["Average Reading Score"]
size_passing_math    = per_school_summary2_df.groupby(["School Size"]).mean()["% Passing Math"]
size_passing_reading = per_school_summary2_df.groupby(["School Size"]).mean()["% Passing Reading"]
size_overall_passing = per_school_summary2_df.groupby(["School Size"]).mean()["% Overall Passing"]
```


```python
# Assemble into DataFrame. 
updated_size_summary_df = pd.DataFrame({
          "Average Math Score" : size_math_scores,
          "Average Reading Score": size_reading_scores,
          "% Passing Math": size_passing_math,
          "% Passing Reading": size_passing_reading,
          "% Overall Passing": size_overall_passing})

updated_size_summary_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>School Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small (&lt;1000)</th>
      <td>83.821598</td>
      <td>83.929843</td>
      <td>93.550225</td>
      <td>96.099437</td>
      <td>89.883853</td>
    </tr>
    <tr>
      <th>Medium (1000-2000)</th>
      <td>83.361201</td>
      <td>83.873869</td>
      <td>93.582398</td>
      <td>96.732654</td>
      <td>90.557997</td>
    </tr>
    <tr>
      <th>Large (2000-5000)</th>
      <td>77.746417</td>
      <td>81.344493</td>
      <td>69.963361</td>
      <td>82.766634</td>
      <td>58.286003</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Format the DataFrame  
updated_size_summary_df["Average Math Score"]    = updated_size_summary_df["Average Math Score"].map("{:.1f}".format)
updated_size_summary_df["Average Reading Score"] = updated_size_summary_df["Average Reading Score"].map("{:.1f}".format)
updated_size_summary_df["% Passing Math"]        = updated_size_summary_df["% Passing Math"].map("{:.0f}".format)
updated_size_summary_df["% Passing Reading"]     = updated_size_summary_df["% Passing Reading"].map("{:.0f}".format)
updated_size_summary_df["% Overall Passing"]     = updated_size_summary_df["% Overall Passing"].map("{:.0f}".format)

updated_size_summary_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>School Size</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Small (&lt;1000)</th>
      <td>83.8</td>
      <td>83.9</td>
      <td>94</td>
      <td>96</td>
      <td>90</td>
    </tr>
    <tr>
      <th>Medium (1000-2000)</th>
      <td>83.4</td>
      <td>83.9</td>
      <td>94</td>
      <td>97</td>
      <td>91</td>
    </tr>
    <tr>
      <th>Large (2000-5000)</th>
      <td>77.7</td>
      <td>81.3</td>
      <td>70</td>
      <td>83</td>
      <td>58</td>
    </tr>
  </tbody>
</table>
</div>



## Scores by School Type


```python
# Calculate averages for the desired columns. 
type_math_scores     = per_school_summary2_df.groupby(["School Type"]).mean()["Average Math Score"]
type_reading_scores  = per_school_summary2_df.groupby(["School Type"]).mean()["Average Reading Score"]
type_passing_math    = per_school_summary2_df.groupby(["School Type"]).mean()["% Passing Math"]
type_passing_reading = per_school_summary2_df.groupby(["School Type"]).mean()["% Passing Reading"]
type_overall_passing = per_school_summary2_df.groupby(["School Type"]).mean()["% Overall Passing"]
```


```python
# Assemble into DataFrame. 
updated_type_summary_df = pd.DataFrame({
          "Average Math Score" : type_math_scores,
          "Average Reading Score": type_reading_scores,
          "% Passing Math": type_passing_math,
          "% Passing Reading": type_passing_reading,
          "% Overall Passing": type_overall_passing})

updated_type_summary_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>School Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>83.465425</td>
      <td>83.902315</td>
      <td>93.610020</td>
      <td>96.550223</td>
      <td>90.392533</td>
    </tr>
    <tr>
      <th>District</th>
      <td>76.956733</td>
      <td>80.966636</td>
      <td>66.548453</td>
      <td>80.799062</td>
      <td>53.672208</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Format the DataFrame 
updated_type_summary_df["Average Math Score"]    = updated_type_summary_df["Average Math Score"].map("{:.1f}".format)
updated_type_summary_df["Average Reading Score"] = updated_type_summary_df["Average Reading Score"].map("{:.1f}".format)
updated_type_summary_df["% Passing Math"]        = updated_type_summary_df["% Passing Math"].map("{:.0f}".format)
updated_type_summary_df["% Passing Reading"]     = updated_type_summary_df["% Passing Reading"].map("{:.0f}".format)
updated_type_summary_df["% Overall Passing"]     = updated_type_summary_df["% Overall Passing"].map("{:.0f}".format)

updated_type_summary_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing</th>
    </tr>
    <tr>
      <th>School Type</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Charter</th>
      <td>83.5</td>
      <td>83.9</td>
      <td>94</td>
      <td>97</td>
      <td>90</td>
    </tr>
    <tr>
      <th>District</th>
      <td>77.0</td>
      <td>81.0</td>
      <td>67</td>
      <td>81</td>
      <td>54</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
