from seq import Seq

print("-----|  Exercise 9 |------")
s = Seq()
s.read_fasta_format('U5.txt')

print(f"Sequence: (Length: {s.len()}) {s}")
print(f"\tBases: {s.count()}")
print(f"\tRev: {s.reverse_mode()}")
print(f"\tComp: {s.complementary()}")
