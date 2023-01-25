# Computer Hostname in our AD (Active Directory) exist but does not exist in our IT inventory
# Computer Hostname in our AD (Active Directory) exist but in our IT inventory, it is more than 3 years
# Computer Hostname in our AD (Active Directory) exist but in our IT inventory, it has status “broken, spoilt or others”
from datetime import date, datetime
from FileConversion import HostName, Inventory


class App:

    hostname = []
    inventory = []
    ad_description_list = []

    def __init__(self, hostname_csv, inventory_csv):
        h = HostName()
        self.hostname = h.get_hostname_list(hostname_csv)
        i = Inventory()
        self.inventory = i.get_inventory_list(inventory_csv)

    # def get_hostname(self):
    #     return self.hostname
    #
    # def get_inventory(self):
    #     return self.inventory
    #
    # def ad_toString(self):
    #     for ad in self.create_ad_list():
    #         print(ad)

    def create_ad_list(self):
        self.create_ad_description_list()
        ad_list = self.hostname
        for x in range(len(ad_list)):
            ad_list[x].append(self.ad_description_list[x])
        return ad_list

    def create_ad_description_list(self):
        self.ad_description_list = []
        for h in self.hostname:
            self.ad_description_list.append(self.ad_description_str(h[0]))
        return self.ad_description_list

    # add description to hostname
    def ad_description_str(self, host_str):
        ad = self.get_host_in_inventory(host_str)
        if ad is None:
            return "{name} in our AD exists but does not exist in our IT inventory.".format(name=host_str)
        elif self.directory_over_3yrs(ad):
            return "{name} in our AD exists in our IT inventory, it is over 3 years old.".format(name=host_str)
        else:
            return "{name} in our AD exists in our IT inventory, it's status is {status}.".format(name=host_str, status=self.get_directory_status(ad))

    def get_host_in_inventory(self, host_str):
        for i in self.inventory:
            if host_str == i[0]:
                return i
        return None

    def directory_over_3yrs(self, host_list):
        d = str(date.today()).split('-')
        d.append(d.pop(1))
        d.append(d.pop(0))
        current_date_str = "{day}/{month}/{year}".format(day=d[0], month=d[1], year=d[2])
        date_format = "%d/%m/%Y"
        host_date = datetime.strptime(host_list[13], date_format)
        current_date = datetime.strptime(current_date_str, date_format)
        delta = current_date - host_date
        return 3 < (delta.days/365)

    def get_directory_status(self, host_list):
        status_list = host_list[4].split(" > ")
        return "\"{status}\"".format(status=status_list[1].lower())

