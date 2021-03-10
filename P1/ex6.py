from Seq1 import Seq, test_sequences


def print_result(i, sequence):
    print("Sequence" + str(i) + ":(length" + str(sequence.len()) + ")" + str(sequence))
    print("Bases:", sequence.count())


print("-------Exercise 6-------")
# we create the test sequence
list_sequences = list(test_sequences())
for i in range(0, len(list_sequences)):
    print_result(i, list_sequences[i])
