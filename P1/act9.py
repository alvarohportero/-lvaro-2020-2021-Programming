from seq import Seq


print("------ | Exercise 9 |-------")
s = Seq

s.read_fasta("U5.txt")

print(f"Sequence : (Length: {s.len()}) {s}")
print(f"Bases:{s.count()}")
print(f"Rev:{s.reverse()}")
print(f"Ciomp: {s.complement()}")