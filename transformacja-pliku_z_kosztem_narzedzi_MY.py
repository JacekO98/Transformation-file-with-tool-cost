import pandas as pd


file_path = 'C:\\Users\\jacuu\\PycharmProjects\\projekt\\Analiza_danych\\Transrofmacja_pliku_z_kosztem_narzędzi\\generated_pattern_v2.xlsx'

file = pd.read_excel(file_path, sheet_name='Sheet1', header=None)
print(file.head(10))
file = file.fillna('').map(lambda x: str(x)).map(lambda x: x.replace(',', '.'))
file = file.drop([1,2], axis=1)
print(file.head(10))
SAP_number = file.iloc[:, 0]
tool_amount = file.iloc[:, 1]
tool_cost = file.iloc[:, 1]

i = 5
SAP_list=[]
tool_list=[]
tool_cost_list=[]
tool_value_list=[]

for i in range(i, len(SAP_number)-2, 4):
    SAP_number1 = SAP_number[i]
    SAP_list.append(SAP_number1)

    tool_amount1 = tool_amount[i+1]
    tool_amount2 = float(tool_amount1) if tool_amount1 != '' else 0.0
    tool_list.append(tool_amount2)

    tool_cost1 = tool_cost[i + 2]
    tool_cost1 = float(tool_cost1) if tool_cost1 != '' else 0.0
    tool_cost_list.append(tool_cost1)

    tool_value = tool_cost1 / tool_amount2 if tool_amount2 != 0 else 0
    tool_value_list.append(tool_value)

tabela = pd.DataFrame({
    "Numer SAP": SAP_list,
    "koszt na sztukę": tool_value_list
})

tabela.to_excel('C:\\Users\\jacuu\\PycharmProjects\\projekt\\Analiza_danych\\Transrofmacja_pliku_z_kosztem_narzędzi\\nowy.xlsx', index=False)
