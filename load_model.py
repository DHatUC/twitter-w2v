# A program to load a previously made model.

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
print ("Enter the name of the model you would like to load from the model directory (e.g. 'aug2011-ferg'): ")
model_name = raw_input()
model_path = os.path.join(MODEL_DIR, model_name)

#=====================================================================================================================
## LOAD MODEL ##
my_model = gensim.models.Word2Vec.load(model_path)
my_model.init_sims(replace=True)