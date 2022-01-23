# PyCitySchools

## Deliverable 1: Replace the reading and math scores.
### Replace the 9th grade reading and math scores at Thomas High School with NaN.



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


We've completed our data-merge/left join the school and students. We've create 2 distinct d(ata) f(rames) in the process, to give us an opportunity to compare and contrast the output's and insure our data remains distinct and intact through the analysis process.

This also gives us an opportunity to later reuse this architecture to test other data abnormalities.
The checks below show us a 'before' and 'after' for what we've called in our analysis- the "BenchMark" and the "Adjusted" data sets.

The BenchMark data is the complete data set, unmolested and unmanipulated.
The Adjusted data is where we've replaced records with NaN based on unconfirmed suspiciouns of potential academic fraud.

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


This shows in summary our totals for the Adjusted df.


    Schools 15
    Students 39170
    Updated Students 38709
    Total Budget  24649428
    

"School Data Complete" is concurrent with our BenchMark data.
```python
# Calculate the Average Scores using the "clean_student_data".
average_reading_score = school_data_complete_df["reading_score"].mean()
average_math_score = school_data_complete_df["math_score"].mean()

print ("Average Reading Score:" , average_reading_score )
print ("Average Math Score:" , average_math_score )
```
This shows our Benchmark Values.
    Average Reading Score 81.87784018381414
    Average Math Score 78.98537145774827
    

"Updated School Data Complete" is concurrent with our Adjusted data.
```python
# Calculate the Average Scores using the "updated_student_data".
updated_average_reading_score = updated_school_data_complete_df["reading_score"].mean()
updated_average_math_score = updated_school_data_complete_df["math_score"].mean()

print ("Updated Average Reading Score:" , updated_average_reading_score )
print ("Updated Average Math Score:" , updated_average_math_score )
```
This shows our Adjusted Values.
    Updated Average Reading Score 81.85579580976001
    Updated Average Math Score 78.93053295099331
    


Our BenchMark Counts
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
BenchMark Data
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
Adjusted Data
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
BenchMark Data
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
Adjusted Data
    Updated Passing Both Math and Reading 25105
    Updated Passing Percentage... 64.85571830840374
    

BenchMark data
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


Adjusted data
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




Concated DF with both BenchMark and Adjusted Data sets
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

We've completed a similar analysis here, to mirror the comparatives in a similar manner as before.

BenchMark Data
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






Adjusted Data
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





Unioned data set from BenchMark and Adjusted
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




### Adjusted data Calculation outputs
    Number of 10th-12th graders from Thomas High School (THS): 1174
    Number of students passing math from Thomas High School (THS): 1094
    Number of students passing reading from Thomas High School (THS): 1139
    Number of students passing math and reading from Thomas High School (THS): 1064
    Percentage of students passing math from Thomas High School (THS): 93.18568994889267
    Percentage of students passing reading from Thomas High School (THS): 97.01873935264055
    Overall passing percentage from Thomas High School (THS): 90.63032367972743


Adjusted Data
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

### Outuputs for top/bottom [school] performers
    BenchMark Analysis
    Top 5 Schools: ['Cabrera High School', 'Thomas High School', 'Griffin High School', 'Wilson High School', 'Pena High School'] 
    
    Adjusted Analysis
    Top 5 Schools: ['Cabrera High School', 'Thomas High School', 'Griffin High School', 'Wilson High School', 'Pena High School']
    
    BenchMark Analysis
    Bottom 5 Schools: ['Rodriguez High School', 'Figueroa High School', 'Huang High School', 'Hernandez High School', 'Johnson High School'] 
    
    Adjusted Analysis
    Bottom 5 Schools: ['Rodriguez High School', 'Figueroa High School', 'Huang High School', 'Hernandez High School', 'Johnson High School']
    

## Math and Reading Scores by Grade

## Math Scores by Grade

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



## Reading Scores by Grade

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









### Spending Summary


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
