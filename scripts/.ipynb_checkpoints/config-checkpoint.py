import numpy as np
import json

CV_path = "../MIP_tables/CMIP6_CV.json"

with open(CV_path) as file:
    CV_dict = json.load(file)

print(CV_dict)


year_min = {
    "LongRunMIP":
    {
        "abrupt2xCO2":1850,
        "abrupt4xCO2":1850,
        "abrupt8xCO2":1850,
        "abrupt16xCO2":1850
    },
    "GrandEnsemble":
    {
    "hist":1850
    }
}

year_max = {
    "LongRunMIP":
    {
        "abrupt2xCO2":2849,
        "abrupt4xCO2":2849,
        "abrupt8xCO2":2849,
        "abrupt16xCO2":2849
    },
    "GrandEnsemble":
    {
    "hist":2005
    }
}


# In[32]:


realization = {
    "LongRunMIP":
    {
        "abrupt2xCO2":np.arange(1,2),
        "abrupt4xCO2":np.arange(1,2),
        "abrupt8xCO2":np.arange(1,2),
        "abrupt16xCO2": np.arange(1,2)
    },
    "GrandEnsemble":
    {
        "hist":np.arange(1,101)
    }
    }

