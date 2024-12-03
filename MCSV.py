import csv

class CSV:


    def read_csv(self, url):
        with open(url) as file:
            csv_data = csv.reader(file, delimiter=';')
            return list(csv_data)


    def get_branch_data(self, url):
        self.read_csv(url)
        self.config_list_revenue()
