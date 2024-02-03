# This is a python script to categorize an age continous variable to different categories for analysis

# this method using the pandas cut()

# create a new column in our dataset called age_group
# categories age into 3 categories
# 10 to 13 yrs: (9, 13], 9 is excluded and 13 is included
# 14 to 16 yrs: (13, 16], 13 is excluded and 16 is included
# 17 to 19 yrs: (16, 19], 16 is excluded and 19 is included.

import pandas as pd

students= pd.read_csv("filepath")

students['Age_group'] = pd.cut(x=students['Age'], bins=[9, 13, 16, 19], labels=['10 to 13 yrs','14 to 16 yrs','17 to 19 yrs'])

