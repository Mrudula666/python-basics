import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('darkgrid')
sns.set(font_scale=1.5)
import warnings
warnings.filterwarnings('ignore')

# Read in TN middle school dataset from GitHub
df = pd.read_csv('https://raw.githubusercontent.com/LearnDataSci/article-resources/master/Essential%20Statistics/middle_tn_schools.csv')
#netflix_data = pd.read_csv('netflix.csv')

#print(netflix_data.describe())
df.describe()
#print(netflix_data[['ratingdescription','user_rating_score']].groupby(['user_rating_score']).describe())
#print(netflix_data[['ratingdescription','user_rating_score']].corr())
df[['reduced_lunch', 'school_rating']].groupby(['school_rating']).describe()
df[['reduced_lunch', 'school_rating']].corr()

#fig, ax = plt.subplots(figsize=(14,8))

#ax.set_ylabel('user_rating_score')
fig, ax = plt.subplots(figsize=(14,8))

print(fig)
print(ax)
ax.set_ylabel('school_rating')

# boxplot with only these two variables
_ = df[['reduced_lunch', 'school_rating']].boxplot(by='school_rating', figsize=(13,8), vert=False, sym='b.', ax=ax)

# boxplot with only these two variables
#_ = netflix_data[['ratingdescription','user_rating_score']].boxplot(by='user_rating_score', figsize=(13,8), vert=False, sym='b.', ax=ax)

plt.show()