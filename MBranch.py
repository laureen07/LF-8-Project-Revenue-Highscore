from MCSV import CSV

data_path = 'Umsätze/*.csv'

class Branch:
    def __init__(self):
        self.days = None
        self.revenues = None

stores = []

def config_list_revenue(revenue):
    cur_list = []
    for value in revenue:
        cur_list.append(float((value.replace('.', '').replace(',', '.').replace('€', ''))))
    return cur_list #gibt eine Formatierte liste zurück

def init_stores():
    csv = CSV()
    data_paths = csv.get_all_data(data_path)

    for path in data_paths:
        store_data = csv.read_csv(path)
        cur_days = store_data[0]
        cur_plane_revenues = store_data[1]
        cur_revenues = config_list_revenue(cur_plane_revenues)
        cur_store = Branch()
        cur_store.days = cur_days
        cur_store.revenues = cur_revenues
        stores.append(cur_store)
