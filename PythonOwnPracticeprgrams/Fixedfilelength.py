# This script used to write fixed length data into csv file
import re
space = re.compile(r"\s+")
fh = open("data.prn")
fho = open("csv177.txt","w")
count =0
while (True):
        record = fh.readline()
        if not record:
            break
        values = record.split()
        if count!=0:
            fho.write('"' + '","'.join(values) + '"\n')
        count = count + 1

fho.close()