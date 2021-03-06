#!/bin/bash

module use /g/data/v10/public/modules/modulefiles
module use /g/data/v10/private/modules/modulefiles

module load h5-compression-filters/20200612

module load dea

SSPATH=$PWD/../

# so it uses the dev scene select
#echo $PYTHONPATH
[[ ":$PYTHONPATH:" != *":$SSPATH:"* ]] && PYTHONPATH="$SSPATH:${PYTHONPATH}"
#echo $PYTHONPATH

#pytest -s test_check_ancillary.py #-k 'test_definitive_ancillary_files_local'
pytest -s test_check_ancillary.py #-k 'test_ancillaryfiles_water'
#./timing_check_ancillary.py
