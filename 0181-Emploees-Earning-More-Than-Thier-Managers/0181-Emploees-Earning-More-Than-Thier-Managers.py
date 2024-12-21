import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    result = []
    id_to_index = {row['id']: idx for idx, row in employee.iterrows()}

    for i in range(len(employee)):
        curr_manager_id = employee.iloc[i, 3]
        if pd.notna(curr_manager_id) and curr_manager_id in id_to_index:
            curr_manager_index = id_to_index[curr_manager_id]
            if employee.iloc[i, 2] > employee.iloc[curr_manager_index, 2]:
                result.append(employee.iloc[i, 1])
    return pd.DataFrame(result, columns = ['Employee'])
