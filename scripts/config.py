import numpy as np
import json

CV_path = "../MIP_tables/CMIP6_CV.json"

with open(CV_path) as file:
    CV_dict = json.load(file)

print(CV_dict)
