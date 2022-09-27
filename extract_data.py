# importing necessary libraries
import pandas as pd
import json
import torch
import torch.nn as nn
from torch import optim
import torch.nn.functional as F

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Reading the first file (Data for dec 2019)
with open("16119_webhose_2019_12_db21c91a1ab47385bb13773ed8238c31_0000001.json", "r", encoding="utf8") as file1:
  json_data1 = [json.loads(line) for line in file1]
len(json_data1)

# Reading the second json (Data for jan 2020)
with open("16119_webhose_2020_01_db21c91a1ab47385bb13773ed8238c31_0000001.json", "r", encoding="utf8") as file2:
  json_data2 = [json.loads(line) for line in file2]
len(json_data2)

# Extracting the value of the text key and title key from the 2 jsons and putting them in the dataset and target lists respectively  
dataset = []
target = []
for dict1 in json_data1:
  text1 = dict1.get("text")
  dataset.append(text1)
  title1 = dict1.get("title")
  target.append(title1)
    
for dict2 in json_data2:
  text2 = dict2.get("text")
  dataset.append(text1)
  title2 = dict2.get("title")
  target.append(title2)

print("The length of dataset is:", len(dataset))
print("The length of dataset is:", len(target))
