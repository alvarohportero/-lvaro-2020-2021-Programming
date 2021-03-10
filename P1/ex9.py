from Seq1 import Seq


def print_result(i, sequence):
    print("Sequence" + str(i) + ":(length" + str(sequence.len()) + ")" + str(sequence))
    print("Bases:", sequence.count())
    print("Rev:", sequence.reverse())
    print("Comp:", sequence.complement())


print("-------Exercise 9-------")
s1 = Seq()
s1.seq_read_fasta("ADA.txt")
print_result("", s1)

