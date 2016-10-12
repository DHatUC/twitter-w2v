# README.md file for twitter-w2v
##### A program to build models on twitter data and run queries. 

###### __author__ Madeleine Hardt
###### __email__ hardtmad@grinnell.edu
###### __last_updated__ 2016.10.12


## Installation Instructions 
#### Starting from the terminal:

1. Clone repository from GitHub.
    * In the terminal window use cd and mkdir commands to switch to the root directory for the project.
    * In the terminal type: git clone https://github.com/<your-username>/twitter-w2v
    *  N.B.: Replace <your-username> with your username and do not include <> e.g. https://github.com/hardtmad/twitter-w2v
2.  Install Gensim package. 
    * In the terminal type: sudo easy_install -U gensim
    * Further instructions can be found at https://radimrehurek.com/gensim/install.html
3. Ensure you have downloaded the appropriate twitter data from http://archive.org/search.php?query=collection%3Atwitterstream&sort=-publicdate
    * Inside your project root directory there should be 3 directories: data, models, and results. Twitter data should be stored in .txt files named for the 
        minute inside two levels of folders named for hours and days (i.e. data/data-type/month/day/hour.txt) (data/aug2014/01/00/00.json would be the 
        relative path for the first minute of data in the first hour of the first day of the data collected for aug2014. The name aug2014 can be specifed 
        by the user as a way to remember what type of data is stored in the folder. 