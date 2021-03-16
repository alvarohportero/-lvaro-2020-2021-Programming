from seq import Seq

def print_count_bases(s):
    for base in Seq.BASES_VALID:
        print(f"{base}: {s.count_base(base)} ", end="")
    print()

print("-------Exercise 5-------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
sequences = [s1,s2,s3]
for index, sequence in enumerate(sequences):
    print(f"Sequence {index}: (Length: {sequence.len()}) {sequence}")
    print_count_bases(sequence)


