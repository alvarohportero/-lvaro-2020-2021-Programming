def read_from_file(filename):
    with open(filename, "r") as f:
        dna = f.read()
        dna.replace("\n", "")
        return dna


def correct_sequence(dna):
    for c in dna:
        if c != "A" and c != "G" and c != "C" and c != "T":
            return False
    return True


def count_bases(dna):
    a, c, g, t = 0, 0, 0, 0
    for h in dna:
        if h == "A":
            a += 1
        elif h == "C":
            c += 1
        elif h == "G":
            g += 1
        elif h == "T":
            t += 1
    return a, c, g, t


dna = read_from_file("dna.txt")
correct_dna = correct_sequence(dna)
if correct_dna:
    print("Total length:", len(dna))
    a, c, g, t = count_bases(dna)
    print("A", a)
    print("C", c)
    print("T", t)
    print("G", g)
else:
    print('Not VALID SEQUENCE')
