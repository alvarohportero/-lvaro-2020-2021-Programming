from seq import Seq


def print_counting_the_bases(s):
    for base in Seq.CORRECT_BASES:
        print(f"{base}: {s.count_base(base)} ", end="")
    print()


print("-------Exercise 5-------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
sequences = [s1, s2, s3]
for i, sequence in enumerate(sequences):
    print(f"Sequence {i}: (Length: {sequence.len()}) {sequence}")
    print_counting_the_bases(sequence)
