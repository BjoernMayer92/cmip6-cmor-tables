"""


"""

import numpy as np  
import json
import subprocess
from pathlib import Path
import os
import argparse


parser = argparse.ArgumentParser()

parser.add_argument("--activity")
parser.add_argument("--experiment")

project_dir = Path.cwd().parents[0]


data_path = Path.cwd().parents[2]


CV_path = os.path.join(project_dir, "MIP_tables", "CMIP6_CV.json")
config_table_path = os.path.join(project_dir,"config_tables")
MIP_table_path = os.path.join(project_dir,"MIP_tables")
generate_cdocmorinfo_script_path = os.path.join(config_table_path,"generate_cdocmorinfo.sh")


MIP_table_filename = "CMIP6_Omon.json"
MIP_table_file = os.path.join(MIP_table_path,MIP_table_filename)


# In[31]:


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


# # 3 Load Json

# In[33]:


with open(CV_path) as file:
    CV_dict = json.load(file)


# # 4 Create cdocmorinfo

# In[34]:


for experiment_id in ["hist"]:#CV_dict["CV"]["experiment_id"]:
    activity_id = CV_dict["CV"]["experiment_id"][experiment_id]["activity_id"][0]
    
    year_min_id = year_min[activity_id][experiment_id]
    year_max_id = year_max[activity_id][experiment_id]
    
    
    for realization_id in realization[activity_id][experiment_id]:
        subprocess.Popen([generate_cdocmorinfo_script_path,str(activity_id),str(experiment_id),str(realization_id),str(data_path),str(config_table_path)])
        if activity_id=="GrandEnsemble":
            realization_str = "lkm"+str(realization_id).zfill(4)
        if activity_id=="LongRunMIP":
            realization_str = "mpiesm-1.2.00"


        input_data_path = os.path.join(data_path,activity_id,experiment_id, realization_str,"rho")
            
        cdocmorinfo_path = os.path.join(config_table_path,activity_id,experiment_id,str(realization_id))
        cdocmorinfo_filename = "_".join(["cdocmorinfo",activity_id,experiment_id,str(realization_id)])
        cdocmorinfo_file  = os.path.join(cdocmorinfo_path, cdocmorinfo_filename)


        
        for year_id in range(year_min_id, year_max_id+1):
            
            input_data_filename = "_".join([activity_id,experiment_id,realization_str,"rho",str(year_id)])+".nc"
            input_data_file = os.path.join(input_data_path, input_data_filename)

            
            #assert os.path.exists(MIP_table_file) & os.path.exists(cdocmorinfo_file) & os.path.exists(input_data_file)

            cmorization_string = "cdo cmor,{},i={} {}".format(MIP_table_file,cdocmorinfo_file, input_data_file)
            #print(cmorization_string)
            os.system(cmorization_string)


# In[14]:


os.path.exists(MIP_table_file)


# In[16]:


os.path.exists(cdocmorinfo_file)


# In[17]:


os.path.exists(input_data_file)


# In[18]:


input_data_file


# In[19]:


MIP_table_file


# In[20]:


cdocmorinfo_file


# In[21]:


cmorization_string


# In[ ]:




