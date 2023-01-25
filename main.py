from ActiveDirectoryWrite import ActiveDirectoryWrite


def main():
    file = ActiveDirectoryWrite("HostnameList.csv", "ITInventory.csv")
    file.update_list()


main()
