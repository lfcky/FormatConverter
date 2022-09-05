import os


def read_files(file_path, suffix):
    li = os.listdir(file_path)
    new_li = []
    for item in li:
        if suffix and os.path.splitext(item)[1] != ('.' + suffix):
            continue
        item = file_path + '/' + item
        new_li.append(item)
    return new_li


def read_excel():
    return read_files('excel', 'xlsx')


def read_json():
    return read_files('json', 'json')


def out_excel():
    return 'json/result'


def out_json():
    return 'excel/result'


def get_file_name(path):
    name = os.path.basename(path)
    name = os.path.splitext(name)[0]
    return name
