import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # print(employee)
    # employee.sort_values(by='salary',ascending=False, inplace=True)
    groups = employee.groupby('salary')
    rank_list = [group for group in groups.groups.keys()]
    rank_list.sort(reverse=True)
    if len(rank_list) <2:
        res =  np.nan
    else:
        res = rank_list[1]
    # print(rank_list)
    res_df = pd.DataFrame([res], columns=['SecondHighestSalary'])
    # res_df = res_df.replace({None, np.nan})
    return res_df
    
if __name__ == "__main__":
    input_list = [
        [100,200,100,300,300],
        [100]
    ]
    for item in input_list:
        df = pd.DataFrame(item,columns =['salary'])
        df['id'] = df.index
        a = second_highest_salary(employee=df)
        print(a)