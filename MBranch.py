from MCSV import CSV

url_a = 'Filiale_A.csv'
url_b = 'Filiale_B.csv'
url_c = 'Filiale_C.csv'

class Branch:
    def __init__(self):
        self.day = ''
        self.revenue = 0.0
        self.revenue_url = ''

list_store_a = []
list_store_b = []
list_store_c = []

def config_list_revenue(revenue):
    cur_list = []
    for value in revenue:
        cur_list.append(float((value.replace('.', '').replace(',', '.').replace('€', ''))))
    return cur_list

def init_stores():
    csv = CSV()

    store_a = Branch()
    store_a.revenue_url = url_a
    store_b = Branch()
    store_b.revenue_url = url_b
    store_c = Branch()
    store_c.revenue_url = url_c
    stores = [store_a, store_b, store_c]

    for store in stores:
        data = csv.read_csv(store.revenue_url)
        cur_revenues = data[1]
        cur_revenues = config_list_revenue(cur_revenues)
        cur_days = data[0]
        for i in range(len(cur_revenues)):
            cur_branch = Branch()
            cur_branch.revenue = cur_revenues[i]
            cur_branch.day = cur_days[i]
            decide_list(store.revenue_url, cur_branch)

def decide_list(string, branch):
    if string == url_a:
        list_store_a.append(branch)
    elif string == url_b:
        list_store_b.append(branch)
    elif string == url_c:
        list_store_c.append(branch)
