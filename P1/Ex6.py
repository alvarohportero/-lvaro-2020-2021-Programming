from seq import Seq

print("-------Exercise 6-------")
s1 = Seq()
s2 = Seq("ACTGA")
s3 = Seq("Invalid sequence")
sequences = [s1, s2, s3]
for i, sequence in enumerate(sequences):
    print(f"Sequence {i}: (Length: {sequence.len()}) {sequence}")
    print(f"Bases:{sequence.count()}")
