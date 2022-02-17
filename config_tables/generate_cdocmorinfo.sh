#!/bin/bash

activity_id=$1
experiment_id=$2
realization_id=$3
drs_root=$4
parent_directory=$5

output_path=${parent_directory}/${activity_id}/${experiment_id}/${realization_id}
mkdir -p $output_path
echo $output_path
cat << EOF > ${output_path}/cdocmorinfo_${activity_id}_${experiment_id}_${realization_id}
mip_era="CMIP6"

source="MPI-ESM1.2-LR (2017): \naerosol: none, prescribed MACv2-SP\natmos: ECHAM6.3 (spectral T63; 192 x 96 longitude/latitude; 47 levels; top level 0.01 hPa)\natmosChem: none\nland: JSBACH3.20\nlandIce: none/prescribed\nocean: MPIOM1.63 (bipolar GR1.5, approximately 1.5deg; 256 x 220 longitude/latitude; 40 levels; top grid cell 0-12 m)\nocnBgchem: HAMOCC6\nseaIce: unnamed (thermodynamic (Semtner zero-layer) dynamic (Hibler 79) sea ice model)"
source_id="MPI-ESM1-2-LR"

institution_id="MPI-M"
institution="Max Planck Institute for Meteorology, Hamburg 20146, Germany"

license="CMIP6 model data produced by MPI-M is licensed under a Creative Commons Attribution ShareAlike 4.0 International License (https://creativecommons.org/licenses). Consult https://pcmdi.llnl.gov/CMIP6/TermsOfUse for terms of use governing CMIP6 output, including citation requirements and proper acknowledgment. Further information about this data, including some limitations, can be found via the further_info_url (recorded as a global attribute in this file) and contact (recorded as a global attribute in this file). The data producers and data providers make no warranty, either express or implied, including, but not limited to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from the supply of the information (including any liability arising in negligence) are excluded to the fullest extent permitted by law."
calendar="proleptic_gregorian"
contact="cmip6-mpiesm1@dkrz.de"

activity_id=${activity_id}

experiment_id=${experiment_id}

experiment=${experiment_id}

parent_experiment_id="no parent"
sub_experiment_id="none"
sub_experiment="none"

nominal_resolution="100 km"
grid="gn"
grid_label="gn"
source_type="AOGCM"

realization_index=${realization_id}
physics_index=1
forcing_index=1
initialization_index=1
version_date="v20220217"

drs_root="${drs_root}"
EOF
