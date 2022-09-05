import utils.file as fu
import json
import pandas as pd

file_list = fu.read_json()

for file in file_list:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data = pd.DataFrame(data)
    data.to_excel(fu.out_excel() + '/' + fu.get_file_name(file) + '.xlsx', index=None)
