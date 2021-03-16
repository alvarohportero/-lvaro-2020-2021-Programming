from seq import Seq
import operator
print("-------Exercise 10-------")
FASTA_GENE_SEQ = ["U5.txt", "FRAT1.txt", "FXN.txt", "RNU6_269P.txt","ADA.txt"]
for fasta in FASTA_GENE_SEQ:
    s = Seq()
    s.read_fasta_format(fasta)
    var = s.count()
    max_key = max(var, key=var.get)
    print(max_key)

















