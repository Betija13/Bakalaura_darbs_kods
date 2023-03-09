import os

path_to_generated_transcript = ''
path_to_true_transcript = ''

generated_ts = open(path_to_generated_transcript, "r")
true_ts = open(path_to_true_transcript, "r")

lines_generated = generated_ts.readlines()
lines_true = true_ts.readlines()



generated_ts.close()
true_ts.close()
