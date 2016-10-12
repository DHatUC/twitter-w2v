# An interactive program to query a model. 

#=====================================================================================================================
## IMPORTS ##

import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

import os, json
from gensim import matutils
import numpy as np
from datetime import datetime

from set_paths import user_home, ROOT_DIR, DATA_DIR, MODEL_DIR, RESULTS_DIR
from make_model import my_model
from load_model import my_model



print ("Enter the name for your results file: ")
results_name = raw_input() + ".txt"
results_path = os.path.join(RESULTS_DIR, results_name)
print ("Your results will be saved at: " + str(results_path))

f = open(results_path, "a+")

timestamp = datetime.today()
print timestamp
f.write(str(timestamp) + "\n\n")


#=====================================================================================================================
## USER INPUT ##

print("Model " + str(MODEL_DIR) + " has been loaded.")
print("This program will allow you to: ") 
print("1. View the vocabulary")
print("2. Find the top n terms that are similar to one set of terms and different from another set of terms")
print("3. Find the cosine similarity between two sets of terms")
print("You will be given the option to write these results to an output file that you can view later.")
print("N.B.: all queries must be made using words that are contained in the vocabulary.")


## PRINT VOCABULARY ## 
print ("\n1. Hit \"y\" to see the vocabulary, \"s\" to see a sample, and \"n\" to move on to step 2.") 
vocab = raw_input()
if vocab == "y":
  for word in my_model.vocab:
    print word
    #print my_model[word]
  print ("Hit \"y\" to write this to the output file and \"n\" to move on.")
  output = raw_input()
  if output == "y":
    f.write("Full vocabulary: \n")
    for word in my_model.vocab:
      f.write(word + "\n")
elif vocab == "s":
  i = 0
  for word in my_model.vocab:
    if i%5 == 0:
      print word
    i+=1
  print ("Hit \"y\" to write this to the output file and \"n\" to move on.")
  output = raw_input()
  if output == "y":
    f.write("Sample of vocabulary: \n")
    i = 0
  for word in my_model.vocab:
    if i%5 == 0:
      f.write(word + "\n")
    i+=1
else:
  print("Moving on...\n")


## QUERIES ##
query = "y"
while query == "y":
  print ("2. Hit \"y\" to enter a query and \"n\" to move on to step 3.") 
  query = raw_input()
  if query == "y":
    print ("Enter the number of top terms you would like to see: ") 
    q_num = int(raw_input())
    print ("Enter the positively correlated words separated by spaces") 
    pos_words = set(raw_input().split())
    #pos_words = set('neighborhood. #stlouis #ferguson'.split())
    print ("Enter the negatively correlated words separated by spaces") 
    neg_words = set(raw_input().split())
    #neg_words = set(''.split())
    context = ("Top " + str(q_num) + " most similar words when " + str(pos_words) + " is positive and " + str(neg_words) + " is negative.")
    result = my_model.most_similar(positive=pos_words, negative=neg_words, topn=q_num)
    print context + str(result)
    print ("Hit \"y\" to write this to the output file and \"n\" to move on.")
    output = raw_input()
    if output == "y":
      f.write("\n" + context + str(result) + "\n")
  else:
    print("Moving on...\n")
    

## SIMILARITIES ##
sim = "y"
while sim == "y":
  print ("3. Hit \"y\" to enter a similarity and \"n\" to finish.") 
  sim = raw_input()
  if sim == "y":
    print ("Enter the first set of words separated by spaces: ") 
    ws1 = set(raw_input().split())
    print ("Enter the second set of words separated by spaces: ") 
    ws2 = set(raw_input().split())
    context = ("Cosine similarity of " + str(ws1) + " and " + str(ws2) + ":")
    result = my_model.n_similarity(ws1, ws2)
    print context + str(result)
    print ("Hit \"y\" to write this to the output file and \"n\" to move on.")
    output = raw_input()
    if output == "y":
      f.write("\n" + context + str(result) + "\n")

f.write("\n\n\n")
print ("Done.")
print ("Your results can be found at " + results_path)