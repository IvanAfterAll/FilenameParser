##Import Required Packages
import os
import csv
import intake
import pandas as pd
import glob
import parse
#import fnmatch, re

#Find All Files in Newspaper Articles Folder/Subfolder - **INSERT RELEVANT FILEPATH HERE**
filepath = 'INSERTHERE'
files = glob.glob(filepath + '*\*.*', recursive=True)
dir_list = os.listdir(filepath)

#Add Files to Pandas Dataframe - Maybe Unnecessary Now?
s = pd.DataFrame(data=dir_list)

print(s)
print(files)

#Compile List of Matching Files
from parse import compile
c = compile("Newspaper {State} - {Year} {Month} {Day} {Fileblurb}.*")
values = s
print(values)
print(c.named_fields)
print(c)

#Parse Filenames
from parse import parse
parse_func = parse
pattern = "Newspaper{State}-{Year:4d}{Month:3w}{Day:2w}{Fileblurb}.pdf"
export = [parse_func(pattern, f) for f in dir_list if parse(pattern, f) is not None]
print(export)
parse_func

#Export to CSV in Project Directory
with open('export.csv', 'w', newline='') as csvfile:
    for item in export:
        fields = item.named
#        csvreader = csv.DictReader(export)
        csvwriter = csv.writer(csvfile)
#        csvwriter.writerow(fields)
    for item in export:
        csvwriter.writerow([item.named.get(f) for f in fields])

csvfile