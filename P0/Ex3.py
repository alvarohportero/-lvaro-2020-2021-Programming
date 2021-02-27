import seq_0

GENE_FOLDER = "./sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]

print("-----| Exercise 3 |------")

for gene in gene_list:
    # "./sequence/U5
    sequence = seq_0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    print("gene" + gene + " -----> length:" + str(seq_0.seq_len(sequence)))
