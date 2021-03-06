import argparse, codecs


parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str)
parser.add_argument("--output", type=str)
args = parser.parse_args()

# https://universaldependencies.org/format.html
with codecs.open(args.input, 'r', encoding='utf-8') as fin, codecs.open(args.output, 'w', encoding='utf-8') as fout:
    for line_num, line in enumerate(fin):
        if line_num == 10000: break 
        info = line.strip().split()
        for token_num, token in enumerate(info):
            data = ["_" for _ in range(10)]
            data[0] = str(token_num + 1) # rram added + 1 to avoid 0
            data[1] = token
            data[2] = token
            data[3] = 'PUNCT'
            data[4] = str(1) # rram 
            # data[5] = str(5) # rram 
            # data[6] = 'punct' # rram
            data[6] = str(5) # rram
            data[7] = 'punct' # rram 
            # data[8] = 'punct'
            if token_num == len(info) - 1: fout.write( "\t".join(data) + "\n\n") # rram - double new line
            else: fout.write( "\t".join(data) + "\n")
