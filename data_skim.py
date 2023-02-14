import pandas as pd
import numpy as np
import os

BASE_DIRECTIORY = os.getcwd()
test1 = []
test2 = []
test3 = []

test_list = [ test1, test2, test3]

test1_file = []
test2_file = []
test3_file = []

test_file_list = [test1_file, test2_file, test3_file]

header = ["Test_Type","Number of clauses", "conflicts", "decisions", "Memory used", "CPU time"]

dirlist = [BASE_DIRECTIORY + "/tests/resolutions/", BASE_DIRECTIORY + "/tests_2/resolutions/", BASE_DIRECTIORY + "/tests_3/resolutions/"]

for i in range(3):
  for (dirpath, dirnames, filenames) in os.walk(dirlist[i]):
    for f in filenames:
      if "test" in str(f) or "hard" in str(f):
        test_file_list[i].append(os.path.join(str(dirpath), str(f)))

for i in range(3):
  for f in test_file_list[i]:
    file = open(f, 'r')
    output =[]
    
    output.append(f[-11:-4])
    
    for line in file:
      if header[1] in line:
        temp_line = line.split()
        output.append(temp_line[4])
      if header[2] in line:
        temp_line = line.split()
        output.append(temp_line[2])
      if header[3] in line:
        temp_line = line.split()
        output.append(temp_line[2])
      if header[4] in line:
        temp_line = line.split()
        output.append(temp_line[3])
      if header[5] in line:
        temp_line = line.split()
        output.append(temp_line[3])
    
    test_list[i].append(output)


data1 = pd.DataFrame(test_list[0], columns = header)
data2 = pd.DataFrame(test_list[1], columns = header)
data3 = pd.DataFrame(test_list[2], columns = header)

data1.to_csv(BASE_DIRECTIORY + "/stat/std_data.csv", index = False)
data2.to_csv(BASE_DIRECTIORY + "/stat/ET2_data.csv", index = False)
data3.to_csv(BASE_DIRECTIORY + "/stat/ET3_data.csv", index = False)
