import seq_0
FOLDER = "./sequences/"   # 2 points means we are going back two folders
ID = "ADA.txt"
print(FOLDER)
u5_seq = seq_0.seq_read_fasta(FOLDER + ID)
print("The first 20 bases are:", u5_seq[0:20])
