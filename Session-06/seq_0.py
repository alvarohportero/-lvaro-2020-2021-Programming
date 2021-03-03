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

    return {"A": a, "C": c, "G": g, "T": t}


# gene_dict = {"A": 0, "C":0..

def seq_count_base(seq, base):
    return seq.count(base)


def seq_reverse(seq):
    return seq[::-1]


def seq_complement(seq):
    list = []
    for gene in seq:
        if gene == "A":
            list.append("T")
        elif gene == "T":
            list.append("C")
        elif gene == "C":
            list.append("T")
        else:
            list.append("G")
    convert = "".join(list)
    return convert


class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases
        # Initialize the sequence with the value
        # passed as argument when creating the object
        if self.is_valid_sequence_2(strbases):
            print("New sequence created")
            self.strbases = strbases
        else:
            self.strbases = "Error"
            print("Incorrect seqeunce detected")

    @staticmethod  # if we use a static method, we call the class, for instance seq.doc  / if we use the self, we call the instance s1.doc
    def is_valid_sequence_2(bases):
        for c in bases:
            if c != "A" and c != "C" and c != "T" and c != "G":
                return False
        return True
    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = "Sequence" + str(i) + ":(length" + str(list_sequences[i]. len() + ")" + str(list_sequences[i]))
            termcolor.cprint(text, "yellow")

    # @staticmethod
    # def static_function():
    #   print(text)

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)
def generate_seqs(pattern, number):
    # A, 3
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq


