import seq_0

FOLDER = "./sequences/"
ID = "U5.txt"

u5_seq = seq_0.seq_read_fasta(FOLDER + ID)
print("------| Exercise 6 |------")
print("Gene U5:","\n", "Frag:", u5_seq[0:20], "\n", "Rev:", seq_0.seq_reverse(u5_seq[0:20]))