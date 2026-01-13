
############################### Python Dates

# A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects.

import datetime

x = datetime.datetime.now()
print(x)
print("Year",x.year)
print("Month in number",x.month)
print("Month name",x.strftime("%B"))
print("Day",x.strftime("%A"))
print("time",x.time())
print("Hour",x.hour)
print("minute",x.minute)
print("Second",x.second)
# 2025-06-01 14:18:39.535659
# The date contains year, month, day, hour, minute, second, and microsecond.
# The datetime module has many methods to return information about the date object.


# Crate your own date
import datetime
y = datetime.datetime(2020, 5, 17)
print(x)

# On that date which day is
import datetime
z = datetime.datetime(2018, 6, 1)
print("The day on 2018-06-01",z.strftime("%A"))

########################################## Calculating Years, Months, Days, Hours, Seconds and Microseconds

# from datetime import datetime
# from dateutil.relativedelta import relativedelta  # needs installation

# We required libary for that
# relativedelta is part of the python-dateutil package. Install it if not already:
# pip install python-dateutil

# ✅ Step 1: Import Required Modules
from datetime import datetime
from dateutil.relativedelta import relativedelta  # needs installation

# ✅ Step 2: Define Your Dates
start_date = datetime(1996, 6, 7, 8, 0, 0)  # Jan 15, 2020 at 8:00 AM
print("Start Date",start_date)
end_date = datetime.now()  # Current date and time
print("End date",end_date)


# ✅ Step 3: Calculate Time Differences
# 🔹 A. Using relativedelta – Most accurate for Y/M/D
diff = relativedelta(end_date, start_date)

# Years calculate
print(f"Years  : {diff.years}")

# Months calculate
print(f"Months : {diff.months}")

# Days calculate
print(f"Days   : {diff.days}")

# Hours calculate
print(f"Hours  : {diff.hours}")

# Minutes calculate
print(f"Minutes: {diff.minutes}")

# Seconds calculate
print(f"Seconds: {diff.seconds}")



delta = end_date - start_date

total_days = delta.days
total_seconds = delta.total_seconds()
total_hours = total_seconds // 3600

print(f"Total Days  : {total_days}")
print(f"Total Hours : {total_hours}")


# 💡 Bonus: From String Dates
# If your dates come from a string:
date1 = datetime.strptime("2020-01-15 08:00", "%Y-%m-%d %H:%M")
date2 = datetime.strptime("2025-06-01 10:15", "%Y-%m-%d %H:%M")

