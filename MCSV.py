import csv
import glob

class CSV:
    def read_csv(self, url):
        with open(url) as file:
            csv_data = csv.reader(file, delimiter=';')
            print(glob.glob('Umsätze/*.csv'))
            return list(csv_data)
