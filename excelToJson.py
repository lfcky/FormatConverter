import utils.file as fu
import json
import pandas as pd

file_list = fu.read_excel()

for file in file_list:
    df = pd.read_excel(file)
    df.fillna('', inplace=True)
    col_list = [col_name for col_name in df.columns]
    json_list = []
    for row in df.itertuples():
        json_dict = {}
        for i in range(len(col_list)):
            json_dict[col_list[i]] = getattr(row, col_list[i])
        json_list.append(json_dict)
    with open(fu.out_json() + '/' + fu.get_file_name(file) + '.json', 'w', encoding='utf-8') as f:
        json.dump(json_list, f, ensure_ascii=False, indent=4)
