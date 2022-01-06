**Problem Question:**

**German Credit Dataset** 

Given a CSV data file as represented by the sample file GermanCredit.csv load it into a Pandas DataFrame, and perform the following tasks on it.
Important: Your code should be applicable to any extension of this sample, so make sure you
don't hardcode anything that applies only to the values in this sample.

**Preprocessing**

1. Drop the 3 columns that contribute the least to the dataset. These would be the columns with
the highest number of non-zero 'none' values. Break ties by going left to right in columns. (Your code
should be generalizable to drop n columns, but for the rest of the analysis, you can call your code
for n=3.)
2. Certain values in some of the columns contain unnecessary apostrophes (‘). Remove the
apostrophes.
3. The checking_status column has values in 4 categories: 'no checking', '<0', '0<=X<200',
and '>=200'. Change these to 'No Checking', 'Low', 'Medium', and 'High' respectively.
4. The savings_status column has values in 4 categories: 'no known savings', '<100',
'100<=X<500', '500<=X<1000', and '>=1000'. Change these to 'No Savings', 'Low', 'Medium', 'High',
and 'High' respectively. (Yes, the last two are both 'High').
5. Change class column values from 'good' to '1' and 'bad' to '0'
6. Change the employment column value 'unemployed' to 'Unemployed', and for the others,
change to 'Amateur', 'Professional', 'Experienced' and 'Expert', depending on year range.

**Analysis**

For the following tasks, do preprocessing or changing of data types in the data frame as required.
1. Often we need to find correlations between categorical attributes, i.e. attributes that have
values that fall in one of several categories, such as "yes"/"no" for attr1, or "low","medium","high" for
attr2.
One such correlation is to find counts in combinations of categorial values across attributes, as in
how many instances are "yes" for attr1 and "low" for attr2. A good way to find such counts is to use the Pandas crosstab (https://pandas.pydata.org/pandasdocs/stable/reference/api/pandas.crosstab.html) function. Do this for the following two counts.
a. Get the count of each category of foreign workers (yes and no) for each class of credit
(good and bad).
b. Similarly, get the count of each category of employment for each category of
saving_status.
2. Find the average credit_amount of single males that have 4<=X<7 years of employment. You
can leave the raw result as is, no need for rounding.
3. Find the average credit duration for each of the job types. You can leave the raw result as is,
no need for rounding.
4. For the purpose 'education', what is the most common checking_status and savings_status?
Your code should print:
 Most common checking status: ...
 Most common savings status: ...

**Visualization** 

1. Plot subplots of two histograms: one with savings_status on the x-axis and personal_status as
different colors, and another with checking_status on the x-axis and personal_status as different
colors.
2. For people having credit_amount more than 4000, plot a bar graph which maps
property_magnitude (x-axis) to the average customer age for that magnitude (y-axis).
3. For people with a "High" savings_status and age above 40, use subplots to plot the following
pie charts:
a. Personal status
b. Credit history
c. Job
