import codecs
import csv


class HostName:

    # output
    def get_hostname_list(self, csv_file):
        decoded = self.unicode_decoder(csv_file)
        tuple_list = self.create_tuple_list(decoded)
        hostname_list = self.create_list(tuple_list)
        return hostname_list

    # unicode decoder
    def unicode_decoder(self, csv_file):
        encoded_text = open(csv_file, 'rb').read()                # you should read in binary mode to get the BOM correctly
        bom = codecs.BOM_UTF16_LE                                 # print dir(codecs) for other encodings
        assert encoded_text.startswith(bom)                       # make sure the encoding is what you expect, otherwise you'll get wrong data
        encoded_text = encoded_text[len(bom):]                    # strip away the BOM
        decoded_text = encoded_text.decode('utf-16le')            # decode to unicode
        return decoded_text

    # convert decoded text to tuple list
    def create_tuple_list(self, decoded_text):
        out = []
        buff = []
        for c in decoded_text:
            if c == '\n':
                out.append(''.join(buff))
                buff = []
            else:
                buff.append(c)
        else:
            if buff:
                out.append(''.join(buff))
        return out

    # format tuple list, append to list
    def create_list(self, tuple_list):
        hostname_list = []
        for element in enumerate(tuple_list):
            x = element[1].split(',')
            x[0] = x[0].replace('\"', '')
            x.pop()
            x.pop()
            hostname_list.append(x)
        hostname_list.pop(0)
        return hostname_list


class Inventory:

    # output
    def get_inventory_list(self, csv_file):
        with open(csv_file, 'r') as file:
            csvreader = csv.reader(file)
            data = list(csvreader)
            data.pop(0)
            return data
