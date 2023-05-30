import csv

file_1 = './VCTK-all_base_en/13_04_checkpoint-18300/ALL_speakers.csv'
# file_2 = './VCTK-p287_base_en/17_04_checkpoint-3500/ALL_speakers.csv'
file_2 = './VCTK-p254_base_en/17_04_checkpoint-5400/ALL_speakers.csv'

csv_file_1 = open(file_1)
csv_file_2 = open(file_2)

row_count = 0
results = {}
for rows_1 in csv.reader(csv_file_1):
    if row_count == 0:
        row_count += 1
        continue
    else:
        results[rows_1[0]] = {'wer_ev': float(rows_1[1]), 'cer_ev': float(rows_1[2]), 'wer_my': float(rows_1[3]), 'cer_my': float(rows_1[4])}
row_count = 0
for rows_2 in csv.reader(csv_file_2):
    if row_count == 0:
        row_count += 1
        continue
    else:
        try:
            results[rows_2[0]]['wer_ev'] -= float(rows_2[1])
            results[rows_2[0]]['cer_ev'] -= float(rows_2[2])
            results[rows_2[0]]['wer_my'] -= float(rows_2[3])
            results[rows_2[0]]['cer_my'] -= float(rows_2[4])
        except:
            continue
results_wer_ev = {}
results_cer_ev = {}
results_wer_my = {}
results_cer_my = {}
for speaker in results:
    results_wer_ev[speaker] = results[speaker]['wer_ev']
    results_cer_ev[speaker] = results[speaker]['cer_ev']
    results_wer_my[speaker] = results[speaker]['wer_my']
    results_cer_my[speaker] = results[speaker]['cer_my']
    a = 0
results_wer_ev_sorted = sorted(results_wer_ev.items(), key=lambda x:x[1], reverse=True)
results_cer_ev_sorted = sorted(results_cer_ev.items(), key=lambda x:x[1], reverse=True)
results_wer_my_sorted = sorted(results_wer_my.items(), key=lambda x:x[1], reverse=True)
results_cer_my_sorted = sorted(results_cer_my.items(), key=lambda x:x[1], reverse=True)
#TODO skaits kuri ir + un kuri -
print("----- WER EV ----- ")
print("BEST: ", results_wer_ev_sorted[:5])
print("WORST: ", results_wer_ev_sorted[-5:])

print("----- CER EV ----- ")
print("BEST: ", results_cer_ev_sorted[:5])
print("WORST: ", results_cer_ev_sorted[-5:])

print("----- WER MY ----- ")
print("BEST: ", results_wer_my_sorted[:5])
print("WORST: ", results_wer_my_sorted[-5:])

print("----- CER MY ----- ")
print("BEST: ", results_cer_my_sorted[:5])
print("WORST: ", results_cer_my_sorted[-5:])





