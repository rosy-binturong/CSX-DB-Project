import pandas as pd

# This is my practice so far for pandas. I left off on the section "selecting a subset."

def lines():
  return "\n" + '_____ _____ _____ _____ _____' + "\n"

df = pd.DataFrame(
  {
    "Name": [
      "Braund, Mr. Owen Harris",
      "Allen, Mr. William Henry",
      "Bonnell, Miss. Elizabeth",
    ],
    "Age": [22, 35, 58],
    "Sex": ["male", "male", "female"],
  }
)
print(str(df) + lines())

# column "Age"
print(str(df["Age"]) + lines())
print(str(df["Age"].max()) + lines())

# basic statistics of each number
print(str(df.describe()) +lines())

# ----- ----- ----- ----- -----

nums = pd.Series([1, 2, 3], name="Number")
print(str(nums) + lines())
print(str(nums.max()) + lines())

# ----- ----- ----- ----- -----

titanic = pd.read_csv("data/titanic.csv")
print(str(titanic) + lines())

# first 8 rows & last 8 rows
print(str(titanic.head(8)) + lines())
print(str(titanic.tail(8)) + lines())

# data types
print(str(titanic.dtypes) + lines())

# technical summary
print(str(titanic.info()) + lines())
print(str(type(titanic["Age"])) + lines())

# number of rows
print(str(titanic["Age"].shape) + lines())

# selects multiple columns & their first 5 rows
age_sex = titanic[["Age", "Sex"]]
print(str(age_sex.head()) + lines())

# selects ages above 35 & their first 5 rows
above_35 = titanic[titanic["Age"] > 35]
print(str(above_35.head()) + lines())

# shows True or False depending on if Age is over 35
print(str(titanic["Age"] > 35) + lines())

# number of rows where Age is over 35
print(str(above_35.shape) + lines())

# shows first 5 rows of cabin classes 2 and 3
class_23 = titanic[titanic["Pclass"].isin([2, 3])]
print(str(class_23.head()) + lines())