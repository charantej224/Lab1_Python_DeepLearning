'''
a sample code to clean the output files. so as to facilitate a new run.
'''

import os

os.remove("lem_output.txt")
os.remove("token_output.txt")
os.remove("trigrams_output.txt")
os.remove("trigram_repetition_output.txt")
