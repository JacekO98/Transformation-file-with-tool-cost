# File transformation - Tool cost analysis
This project transforms SAP-generated `.xlsx` files into a structured format ready for analysis.

## Description

- Loads `.xlsx` file generated from SAP.
- Cleans raw data:
  - Replaces NaN values with empty strings
  - Normalizes decimal separators
  - Drops unnecessary columns
- Calculates cost per tool.
- Saves transformed data into a new Excel file.

## Technologies Used 
- Python
- Pandas
- Pathlib

## How to run
Make sure you have Python 3.10 or newer installed. You can check your version by running:

```bash
python --version
```
Install required dependencies:
`pip install pandas openpyxl`

Place your SAP-generated Excel file in the following location:
data/data_input.xlsx

Ensure that the Excel sheet name is: Sheet1

From the project root directory, run:
python main.py

After successful execution, the transformed file will be generated automatically in:
output/result.xlsx