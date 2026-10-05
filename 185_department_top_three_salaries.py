import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # print(employee)
    # print(department.columns)
    department = department.rename(columns={'id':'departmentId', 'name': 'departmentName'})
    print(department)
    all_df = pd.merge(employee, department, on=['departmentId'], how="inner", validate="many_to_many")
    print(all_df)
    groups = all_df.groupby(['departmentId'])
    for group in groups.groups.keys():
        print(group)
        tf = groups.get_group(group)
        list = 
        
    all_df = all_df.sort_values('salary',ascending=False).groupby(['departmentId', 'salary']).head(3)
    print(all_df)

def top_in_groups(df: pd.DataFrame, num) -> pd.DataFrame:

    groups = df.groupby('salary')
    rank_list = [group for group in groups.groups.keys()]
    rank_list.sort(reverse=True)
    res = rank_list[:num]
    return res


if __name__ == "__main__":
    df1 = pd.read_csv('185.Department Top Three Salaries.csv')
    df2 = pd.read_csv('185.Department Top Three Salaries 2.csv')
    a = top_three_salaries(employee=df1, department=df2)