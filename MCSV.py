import csv

class CSV:
    def read_csv(self, url):
        with open(url) as file:
            csv_data = csv.reader(file, delimiter=';')
            return list(csv_data)
