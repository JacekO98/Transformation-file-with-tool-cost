import pandas as pd
from pathlib import Path


def load_data(input_path: Path) -> pd.DataFrame:
    """
    Load raw exel file
    """
    return pd.read_excel(input_path, sheet_name='Sheet1', header=None)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans DF:
    1. Replane NaN with empty string
    2. Normalizes coma
    3. Drops unnecessary columns
    """
    df = df.fillna('').astype(str)
    df.iloc[:, 3] = df.iloc[:, 3].str.replace(',', '.')
    df = df.drop([1, 2], axis=1)
    return df

def analyze_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze raw data and return output data
    """
    SAP_number = df.iloc[:, 0]
    tool_amount = df.iloc[:, 1]
    tool_cost = df.iloc[:, 1]

    i = 5
    SAP_list = []
    tool_list = []
    tool_cost_list = []
    tool_value_list = []

    for i in range(i, len(SAP_number) - 2, 4):
        SAP_number1 = float(SAP_number[i])
        SAP_list.append(SAP_number1)

        tool_amount1 = tool_amount[i + 1]
        tool_amount2 = float(tool_amount1) if tool_amount1 != '' else 0.0
        tool_list.append(tool_amount2)

        tool_cost1 = tool_cost[i + 2]
        tool_cost1 = float(tool_cost1) if tool_cost1 != '' else 0.0
        tool_cost_list.append(tool_cost1)

        tool_value = tool_cost1 / tool_amount2 if tool_amount2 != 0 else 0
        tool_value = round(tool_value, 2)
        tool_value_list.append(tool_value)

    table = pd.DataFrame({
        "SAP Number": SAP_list,
        "Cost per piece": tool_value_list})
    return table


def save_file(input_path: Path, output_path: Path) -> None:
    """
        Full transformation pipeline.
    """
    df_raw = load_data(input_path)
    df_clean = clean_data(df_raw)
    result = analyze_data(df_clean)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    result.to_excel(output_path, index=False)


if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent

    input_file = BASE_DIR / "data" / "data_input.xlsx"
    output_file = BASE_DIR / "output" / "tool_cost.xlsx"

    save_file(input_file, output_file)



















