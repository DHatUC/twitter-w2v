# A program to a train a model based on data.

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
## CLASS DECLARATION ##

# Object is the memory-friendly result of iterating through all files in dirname 
# and grabbing all values of fields with the key "text" 
# Grabs only fields that contain a filter term if filter_on == true
class MySentences(object):
    def __init__(self, dirname, filter_on, filter_terms):
        self.dirname = dirname
        self.filter_on = filter_on
        self.filter_terms = filter_terms
 
    def __iter__(self):
      for fname in os.listdir(self.dirname):
        i = 0
        with open(os.path.join(self.dirname, fname)) as fo:
          for line in fo:
            i += 1
            all_data = json.loads(line, "utf-8")
            for cur_data in all_data['nodes']:
              if 'text' in cur_data:
                if self.filter_on == "yes":
                  for term in self.filter_terms:
                    if term in cur_data['text']:
                      yield cur_data['text']
                else:
                  yield cur_data['text']
 
#=====================================================================================================================
## USER INPUT ##

print ("Enter the name of the model you would like to train (e.g. 'aug2011-ferg'): ")
model_name = raw_input()

print ("Enter \"yes\" if you would use filter terms and \"no\" if you would like to use the complete text: ")
filter_on = raw_input()

if filter_on == "yes":
  print ("Enter the terms you would like to filter by separated by spaces (e.g. Ferguson Brown) : ")
  filter_terms = raw_input()
else:
  filter_terms = ""

#=====================================================================================================================
## BUILD MODEL ##

sentences = MySentences(DATA_DIR, filter_on, filter_terms)

my_model = gensim.models.Word2Vec(sentences, size=100, window=5, min_count=3, workers=4)
my_model.init_sims(replace=True)

# Save model for reuse
model_path = os.path.join(MODEL_DIR, model_name)
my_model.save(model_path)