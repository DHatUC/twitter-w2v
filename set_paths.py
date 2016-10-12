# A program to define file paths used frequently. 

'''
Variables set in this file:
user_home
ROOT_DIR
DATA_DIR
MODEL_DIR
RESULTS_DIR
'''

#=====================================================================================================================
## IMPORTS ##

# import modules & set up logging
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
import os, json


#=====================================================================================================================
## USER INPUT ##

user_home = os.environ['HOME']

correct_input = False 

while not correct_input:
  # ROOT DIRECTORY # 
  print ("Your home directory is: " + str(user_home))
  print ("Enter root directory for this project beginning with the directory inside the home directory (e.g. " + user_home + "/my_project): ")
  ROOT_DIR = os.path.abspath(os.path.join(user_home, raw_input()))
  print ("Your project root directory has been set as: " + str(ROOT_DIR))
  print (str(ROOT_DIR) + " should contain folders for data, models, and results.")
  
  # DATA DIRECTORY #
  print ("Enter the name of the directory where data can be found (Note: all data files should be directly in this folder, not in subfolders): ")
  data_dir_name = raw_input()
  DATA_DIR = os.path.join(ROOT_DIR, data_dir_name)
  
  # MODEL DIRECTORY #
  print ("Enter the name of the directory where models can be found: ")
  model_dir_name = raw_input()
  MODEL_DIR = os.path.join(ROOT_DIR, model_dir_name)
  
  # RESULTS DIRECTORY #
  print ("Enter the name of the directory where results can be found: ")
  results_dir_name = raw_input()
  RESULTS_DIR = os.path.join(ROOT_DIR, results_dir_name)
  
  print ("Data directory: " + str(DATA_DIR) + "\nModel directory: " + str(MODEL_DIR) + "\nResults directory: " + str(RESULTS_DIR))
  print ("Is this correct_input? y/n")
  correct = raw_input()
  if correct == 'y':
    correct_input = True
  
print ("Done")