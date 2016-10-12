# Main file for the project. Calls other files based on user input. 

#=====================================================================================================================
## IMPORTS ##

import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import os, json
from gensim import matutils
import numpy as np
from datetime import datetime

from set_paths import user_home, ROOT_DIR, DATA_DIR, MODEL_DIR, RESULTS_DIR

#=====================================================================================================================
## USER INPUT ##

print ("Enter 'yes' to load a model and 'no' to train a new model: ")
load = raw_input()
if load == 'yes':
  import load_model
else:
  import make_model

#=====================================================================================================================
## IMPORTS ##

import query