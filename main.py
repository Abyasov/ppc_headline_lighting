import pandas as pd

# переменные на время разработки
free_format_xls_file_path = '/test_data/free_format_file.xlsx'
free_format_csv_file_path = 'test_data/free_format_file.csv'

# data_xls = pd.read_excel(free_format_xls_file_path)
# data_xls

data_csv = pd.read_csv(free_format_csv_file_path)
print(data_csv)

