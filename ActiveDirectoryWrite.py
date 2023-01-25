import csv
from App import App


class ActiveDirectoryWrite:

    ad_list = []

    def __init__(self, hostname_csv, inventory_csv):
        app = App(hostname_csv, inventory_csv)
        self.ad_list = app.create_ad_list()

    def update_list(self):
        with open("UPDATED_HostnameList.csv", mode='w') as csvfile:
            fieldnames = ["Name", "Type", "Description"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for a in self.ad_list:
                writer.writerow({"Name": a[0], "Type": a[1], "Description": a[2]})
