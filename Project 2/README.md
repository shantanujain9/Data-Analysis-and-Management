This is Python Project

Problem 2: German Credit Dataset (72 points)
Given a CSV data file as represented by the sample file GermanCredit.csv
(https://rutgers.instructure.com/courses/133454/files/20252574/download?download_frd=1) (1000 records),
load it into a Pandas DataFrame, and perform the following tasks on it.
Important: Your code should be applicable to any extension of this sample, so make sure you
don't hardcode anything that applies only to the values in this sample.
Preprocessing (31 pts)
1. [8 pts] Drop the 3 columns that contribute the least to the dataset. These would be the columns with
the highest number of non-zero 'none' values. Break ties by going left to right in columns. (Your code
should be generalizable to drop n columns, but for the rest of the analysis, you can call your code
for n=3.)
2. [4 pts] Certain values in some of the columns contain unnecessary apostrophes (‘). Remove the
apostrophes.
3. [5 pts] The checking_status column has values in 4 categories: 'no checking', '<0', '0<=X<200',
and '>=200'. Change these to 'No Checking', 'Low', 'Medium', and 'High' respectively.
4. [5 pts] The savings_status column has values in 4 categories: 'no known savings', '<100',
'100<=X<500', '500<=X<1000', and '>=1000'. Change these to 'No Savings', 'Low', 'Medium', 'High',
and 'High' respectively. (Yes, the last two are both 'High').
5. [4 pts] Change class column values from 'good' to '1' and 'bad' to '0'
6. [5 pts] Change the employment column value 'unemployed' to 'Unemployed', and for the others,
change to 'Amateur', 'Professional', 'Experienced' and 'Expert', depending on year range.
Analysis (17 pts)
For the following tasks, do preprocessing or changing of data types in the data frame as required.
1. [5 pts] Often we need to find correlations between categorical attributes, i.e. attributes that have
values that fall in one of several categories, such as "yes"/"no" for attr1, or "low","medium","high" for
attr2.
One such correlation is to find counts in combinations of categorial values across attributes, as in
how many instances are "yes" for attr1 and "low" for attr2. A good way to find such counts is to use

1/6/22, 12:26 PM Assignment 3
https://rutgers.instructure.com/courses/133454/assignments/1698128 4/6
the Pandas crosstab (https://pandas.pydata.org/pandasdocs/stable/reference/api/pandas.crosstab.html) function. Do this for the following two counts.
a. [3 pts] Get the count of each category of foreign workers (yes and no) for each class of credit
(good and bad).
b. [2 pts] Similarly, get the count of each category of employment for each category of
saving_status.
2. [4 pts] Find the average credit_amount of single males that have 4<=X<7 years of employment. You
can leave the raw result as is, no need for rounding.
3. [4 pts] Find the average credit duration for each of the job types. You can leave the raw result as is,
no need for rounding.
4. [4 pts] For the purpose 'education', what is the most common checking_status and savings_status?
Your code should print:
 Most common checking status: ...
 Most common savings status: ...
Visualization (24 pts)
1. [9 pts] Plot subplots of two histograms: one with savings_status on the x-axis and personal_status as
different colors, and another with checking_status on the x-axis and personal_status as different
colors.
2. [9 pts] For people having credit_amount more than 4000, plot a bar graph which maps
property_magnitude (x-axis) to the average customer age for that magnitude (y-axis).
3. [6 pts] For people with a "High" savings_status and age above 40, use subplots to plot the following
pie charts:
a. Personal status
b. Credit history
c. Job
