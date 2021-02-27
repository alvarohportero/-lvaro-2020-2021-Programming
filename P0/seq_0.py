from pathlib import Path

def seq_ping():
    print("OK")

def read_all(seq):
    for e in range(len(seq)):
        print(e)
    return seq

def take_out_first_line(seq):
    return seq[seq.find("\n") + 1:].replace("\n", "")

def seq_read_fasta(filename):
    sequence = take_out_first_line(Path(filename).read_text())
    return sequence

def seq_len(seq):
    return len(seq)

def seq_count(seq):
    a, c, g, t = 0, 0, 0, 0
    for d in seq:
        if c == "A":
            a += 1
        elif d == "C":
            c += 1
        elif d == "T":
            t += 1
        else:
            g += 1

    return  {"A": a, "C": c, "G":g, "T": t}

# gene_dict = {"A": 0, "C":0..

def seq_count_base(seq, base):
    return seq.count(base)

