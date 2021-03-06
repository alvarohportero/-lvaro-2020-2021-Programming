import seq_0

GENE_FOLDER = "./sequences/"

gene_list = ["U5", "ADA", "FRAT1", "FXN"]
base_list = ["A", "C", "T", "G"]

print("-----| Exercise 8 |------")
result = 0
for gene in gene_list:
    sequence = seq_0.seq_read_fasta(GENE_FOLDER + gene + ".txt")
    for base in base_list:
        counting = seq_0.seq_count_base(sequence, base)
        if counting >= result:
            result = counting
    print("Gene", gene, ":  Most frequent Base:", base)
