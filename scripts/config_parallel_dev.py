#!/usr/bin/env python
# coding: utf-8

# # 1 Import Packages

# In[68]:


import numpy as np  
import json
import subprocess
from pathlib import Path
import os
from subprocess import Popen, PIPE


# # 2 Metadata

# In[10]:


project_dir = Path.cwd().parents[0]


# In[11]:


data_path = Path.cwd().parents[2]


# In[12]:


CV_path = os.path.join(project_dir, "MIP_tables", "CMIP6_CV.json")
config_table_path = os.path.join(project_dir,"config_tables")
MIP_table_path = os.path.join(project_dir,"MIP_tables")
generate_cdocmorinfo_script_path = os.path.join(config_table_path,"generate_cdocmorinfo.sh")


# In[13]:


MIP_table_filename = "CMIP6_Omon.json"
MIP_table_file = os.path.join(MIP_table_path,MIP_table_filename)


# In[16]:


import config as config


# # 4 Create cdocmorinfo

# In[103]:


command_dictionary = {}
command_filenames = []

for experiment_id in config.CV_dict["CV"]["experiment_id"]:
    activity_id = config.CV_dict["CV"]["experiment_id"][experiment_id]["activity_id"][0]
    
    year_min_id = config.year_min[activity_id][experiment_id]
    year_max_id = config.year_max[activity_id][experiment_id]
    
    command_dictionary[experiment_id] = {"activity_id":activity_id,"realization_id":{}}
    
    for realization_id in config.realization[activity_id][experiment_id]:
        subprocess.Popen([generate_cdocmorinfo_script_path,str(activity_id),str(experiment_id),str(realization_id),str(data_path),str(config_table_path)])
        if activity_id=="GrandEnsemble":
            realization_str = "lkm"+str(realization_id).zfill(4)
        if activity_id=="LongRunMIP":
            realization_str = "mpiesm-1.2.00"

        command_dictionary[experiment_id][realization_id] = []
        input_data_path = os.path.join(data_path,activity_id,experiment_id, realization_str,"rho")
            
        cdocmorinfo_path = os.path.join(config_table_path,activity_id,experiment_id,str(realization_id))
        cdocmorinfo_filename = "_".join(["cdocmorinfo",activity_id,experiment_id,str(realization_id)])
        cdocmorinfo_file  = os.path.join(cdocmorinfo_path, cdocmorinfo_filename)
        
        command_dictionary[experiment_id]["realization_id"][realization_id] = []
        
        bash_filename = "_".join([activity_id, experiment_id, str(realization_id)])+".sh"
        command_filenames.append(bash_filename)
        
        with open(bash_filename,"w") as file:
            for year_id in range(year_min_id, year_max_id+1):

                input_data_filename = "_".join([activity_id,experiment_id,realization_str,"rho",str(year_id)])+".nc"
                input_data_file = os.path.join(input_data_path, input_data_filename)


                assert os.path.exists(MIP_table_file) & os.path.exists(cdocmorinfo_file) & os.path.exists(input_data_file)

                cmorization_string = "cdo cmor,{},i={} {}".format(MIP_table_file,cdocmorinfo_file, input_data_file)
                command_dictionary[experiment_id]["realization_id"][realization_id].append(cmorization_string)
                file.write(cmorization_string)
                file.write("\n")
        
        os.system("chmod +x "+bash_filename)

            #print(cmorization_string)
            #os.system(cmorization_string)


# # 5 Run in parallel

# In[99]:


processes = []

for command_filename in command_filenames:
    processes.append(subprocess.Popen(["bash",command_filename]))

return_codes = [p.wait() for p in processes]

