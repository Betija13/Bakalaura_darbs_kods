import os
from tqdm import tqdm
import re, string
import time

#p326
def calculate_WER(true_ts, generated_ts):
    if true_ts == generated_ts or true_ts.lower() == generated_ts.lower():
        return 0, 0
    true_tx_punc = true_ts.lower().split(" ")
    generated_tx_punc = generated_ts.lower().split(" ")
    true_tx = []
    generated_tx = []
    for i in true_tx_punc:
        true_tx.append(re.split('[?.,!]', i)[0])
    for i in generated_tx_punc:
        generated_tx.append(re.split('[?.,!]', i)[0])
    sub_error = 0
    ins_error = 0
    del_error = 0
    sub_error_1 = 0
    ins_error_1 = 0
    del_error_1 = 0
    true_tx_ar = []
    gen_text_ar = []
    j = 0
    k = 0
    start_time = time.time()

    while False in [b in true_tx_ar for b in true_tx] or False in [n in gen_text_ar for n in generated_tx]:
        process_time = time.time() - start_time
        if process_time > 5:
            print("ERROR")
            print("True: ", true_ts)
            print("Generated:", generated_ts)
            print("True arr:", true_tx_ar)
            print("Gen arr: ", gen_text_ar)
            return 0, 0
        if k >= len(true_tx) and j < len(generated_tx):
            for i in range(len(generated_tx) - j):
                true_tx_ar.append('')
                gen_text_ar.append(generated_tx[j+i])
                ins_error_1 += 1
        elif j >= len(generated_tx) and k < len(true_tx):
            for i in range(len(true_tx) - k):
                true_tx_ar.append(true_tx[i+k])
                gen_text_ar.append('')
                del_error_1 += 1
        elif true_tx[k] == generated_tx[j]:
            true_tx_ar.append(true_tx[k])
            gen_text_ar.append(generated_tx[j])
            k += 1
            j += 1

        elif true_tx[k] in generated_tx:
            if true_tx[k] == generated_tx[j-1]:
                pass
            if j + 1 < len(generated_tx):
                if true_tx[k] == generated_tx[j+1]:
                    true_tx_ar.append('')
                    gen_text_ar.append(generated_tx[j])
                    ins_error_1 += 1
                    j += 1
                    continue

            if j + 1 < len(generated_tx) and k + 1 < len(true_tx):
                if true_tx[k + 1] == generated_tx[j + 1]:
                    true_tx_ar.append(true_tx[k])
                    gen_text_ar.append(generated_tx[j])
                    sub_error_1 += 1
                    j += 1
                    k += 1
                    continue
                if j < generated_tx.index(true_tx[k]) + 1 < len(generated_tx) and len(generated_tx) - len(true_tx) >= generated_tx.index(true_tx[k]) - k :
                    if true_tx[k + 1] == generated_tx[generated_tx.index(true_tx[k]) + 1]:
                        for i in range(generated_tx.index(true_tx[k]) - k):
                            true_tx_ar.append('')
                            gen_text_ar.append(generated_tx[j])
                            ins_error_1 += 1
                            j += 1
                        continue
                if k + 2 < len(true_tx):
                    if true_tx[k + 2] == generated_tx[j + 1]:
                        true_tx_ar.append(true_tx[k])
                        true_tx_ar.append(true_tx[k+1])
                        gen_text_ar.append(generated_tx[j])
                        gen_text_ar.append('')
                        sub_error_1 += 1
                        del_error_1 += 1
                        j += 1
                        k += 2
                        continue

            true_tx_ar.append(true_tx[k])
            gen_text_ar.append(generated_tx[j])
            sub_error_1 += 1
            k += 1
            j += 1
            continue

        elif true_tx[k] not in generated_tx:
            if j+1 < len(generated_tx) and k+1 < len(true_tx):
                # checks if the next words are both the same, if yes => substitution error
                if true_tx[k+1] == generated_tx[j+1]:
                    true_tx_ar.append(true_tx[k])
                    gen_text_ar.append(generated_tx[j])
                    sub_error_1 +=1
                    j+=1
                    k+=1
                    continue
                if k + 2 < len(true_tx):
                    if true_tx[k + 2] == generated_tx[j + 1]:
                        true_tx_ar.append(true_tx[k])
                        true_tx_ar.append(true_tx[k+1])
                        gen_text_ar.append(generated_tx[j])
                        gen_text_ar.append('')
                        sub_error_1 += 1
                        del_error_1 += 1
                        j += 1
                        k += 2
                        continue
                else:
                    true_tx_ar.append(true_tx[k])
                    gen_text_ar.append(generated_tx[j])
                    sub_error_1 += 1
                    k += 1
                    j += 1
                    continue
            true_tx_ar.append(true_tx[k])
            gen_text_ar.append(generated_tx[j])
            sub_error_1 += 1
            k += 1
            j += 1

    for i in range(len(true_tx_ar)):
        if true_tx_ar[i]==gen_text_ar[i]:
            continue
        elif true_tx_ar[i]=='':
            ins_error +=1
        elif gen_text_ar[i]=='':
            del_error += 1
        else:
            sub_error += 1

    word_error_rate = (sub_error + ins_error + del_error) / len(true_tx)
    word_error_rate_1 = (sub_error_1 + ins_error_1 + del_error_1) / len(true_tx_ar)
    if word_error_rate > 0.5 or word_error_rate_1 > 0.5:
        print(f"HIGH WER! WER: {word_error_rate}, WER_!: {word_error_rate_1}")
        print("TRUE: \t", true_tx_ar)
        print("GEN:  \t", gen_text_ar)

    return word_error_rate, word_error_rate_1

#p283
def calculate_CER(true_ts, generated_ts):
    if true_ts == generated_ts:
        return 0

    a = 0
    return 0

if __name__ == '__main__':
    # 326, 283, 266
    path_to_generated_transcript = 'p304_transcripts_VCTK_original__W_medium_no-fine-tuning.txt'
    path_to_true_transcript = '../datasets/VCTK-Corpus-0.92/txt/'

    generated_ts = open(path_to_generated_transcript, "r")
    lines_generated = generated_ts.readlines()
    nr_of_files = 0
    total_WER = 0
    total_WER_1 = 0
    for i in tqdm(lines_generated):
        file, generated_transcript = i.split('|')
        generated_transcript = generated_transcript.rstrip('\n').strip()
        speaker, audio_nr, _ = file.split('_')

        true_ts = open(f"{path_to_true_transcript}{speaker}/{speaker}_{audio_nr}.txt", "r")
        true_transcript = true_ts.readlines()[0].rstrip('\n').strip()

        WER, WER_1 = calculate_WER(true_ts=true_transcript, generated_ts=generated_transcript)
        CER = calculate_CER(true_ts=true_transcript, generated_ts=generated_transcript)
        # print("WER: ", WER, "\t WER_1: ", WER_1)
        # print(CER)
        total_WER += WER
        total_WER_1 += WER_1
        nr_of_files += 1
        #TODO ieraksta rezultātus failā
        true_ts.close()
    print("Total WER: ", total_WER/nr_of_files * 100, " Total WER_1: ", total_WER_1/nr_of_files * 100)

    generated_ts.close()

