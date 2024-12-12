from MCSV import CSV

class Store:
    def __init__(self):
        self.days = None
        self.revenues = None
        self.name = ''
        self.highscore = 0

class StoreDatas:
    def __init__(self):
        self.dictionary_path = ''
        self.store_path = ''

def config_list_revenue(revenue):
    cur_list = []
    for value in revenue:
        cur_list.append(float((value.replace('.', '').replace(',', '.').replace('€', ''))))
    return cur_list #gibt eine Formatierte liste zurück

def get_store_path(dictionary):
    csv = CSV()
    temp_list = csv.get_all_data_paths(dictionary)
    return temp_list

def get_store_datas(list_paths):
    csv = CSV()
    temp_list = []
    for path in list_paths:
        plane_store = csv.read_csv(path)
        temp_list.append(plane_store)
    return temp_list
