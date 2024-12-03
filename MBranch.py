import csv

class MCSV:
    def __init__(self):
        self.csv_data = None
        self.data_url = None
        self.list_days = None
        self.list_revenue = None

    def config_list_revenue(self):
        cur_list = []
        for value in self.list_revenue:
            cur_list.append(float((value.replace('.', '').replace(',', '.').replace('€', ''))))
        self.list_revenue = cur_list

    def read_csv(self, url):
        with open(url) as file:
            _csvReader = csv.reader(file, delimiter=';')
            temp_list = list(_csvReader)
            self.list_days = temp_list[0]
            self.list_revenue = temp_list[1]

    def get_branch_data(self, url):
        self.read_csv(url)
        self.config_list_revenue()
class MBranch:
    def __init__(self):
        self.day = None
        self.revenue = None

branch_a = MCSV()
branch_a.data_url = 'Filiale_A.csv'
branch_a.get_branch_data(branch_a.data_url)

branch_b = MCSV()
branch_b.data_url = 'Filiale_B.csv'
branch_b.get_branch_data(branch_b.data_url)

branch_c = MCSV()
branch_c.data_url = 'Filiale_C.csv'
branch_c.get_branch_data(branch_c.data_url)
