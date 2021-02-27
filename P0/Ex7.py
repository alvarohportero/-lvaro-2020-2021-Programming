import seq_0
FOLDER = "./sequences/"
ID = "ADA.txt"
u5_seq = seq_0.seq_read_fasta(FOLDER + ID)
print("-----| Exercise 7 |------")
print("Gene U5:","\n","Frag:",  u5_seq[0:20],"\n","Comp:", seq_0.seq_complement(u5_seq[0:20]))