import os
import csv
##  takes a folder of text files and makes a metadata.csv file for the topic modeling tool


# look inside a folder
corpus_dir = 'poems/'

# get all the filenames
def all_files(folder_name):
    """given a directory, return the filenames in it"""
    texts = []
    for (root, _, files) in os.walk(folder_name):
        for fn in files:
            texts.append(fn)
    return texts

# make a new csv file
def write_the_csv(list_of_files):
    # given a list of files, write their filenames to a csv
    with open('metadata.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['filenames'])
        for fn in list_of_files:
            csvwriter.writerow([fn])

# spit out the filenames into the first column


files = all_files(corpus_dir)
write_the_csv(files)
