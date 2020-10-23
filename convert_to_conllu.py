import argparse, codecs


parser = argparse.ArgumentParser()
parser.add_argument("--input", type=str)
parser.add_argument("--output", type=str)
args = parser.parse_args()

with codecs.open(args.input, 'r', encoding='utf-8') as fin, codecs.open(args.output, 'w', encoding='utf-8') as fout:
    for line in fin:
        info = line.strip().split()
        for token_num, token in enumerate(info):
            data = ["_" for _ in range(10)]
            data[0] = str(token_num)
            data[1] = token
            data[2] = token
            data[3] = 'PUNCT'
            data[5] = 5 # rram 
            data[6] = punct # rram
            data[8] = 'punct'
            fout.write( "\t".join(data) + "\n")
