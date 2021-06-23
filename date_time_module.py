'''
1. Datetime module is divided in two category a) aware datetime and b) naive datetime. This categorization
depends on weather the data contains the information about the timezone or not

2. naive datetime objects are easy to work with but at the cost of some aspects of reality

3. The minimum year allowed in a datetime module is 1 and the maximum year allowed is 9999. They can be obtained by
datetime.MINYEAR and datetime.MAXYEAR

4.The smallest difference between two timedelta objects is 1 microseconds

'''

import datetime

# from datetime import timedelta
# delta = timedelta(days=50,seconds=27,microseconds=10,milliseconds=29000,minutes=5,hours=8,weeks=2)
# Normalization is taking place here eg. 1 week is normalised to 7 days
# print(delta)


