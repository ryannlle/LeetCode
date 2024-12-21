import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    salaries = employee['salary'].drop_duplicates()

    if len(salaries) > 1:
        second_highest = salaries.nlargest(2).iloc[-1]
    else:
        second_highest = None
    return pd.DataFrame([[second_highest]], columns = ['SecondHighestSalary'])