import os
import csv
import numpy as np
import pandas as pd

path = "folder_containing_files"
normallist = os.listdir(path)

class = 1 # if getting files from positive class during classification

for filename in filelist:
    if filename != ".ipynb_checkpoints":
        with open("train.csv", "a") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow([filename, class])
