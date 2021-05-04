from pathlib import Path


class Seq:
    CORRECT_BASES = ["A", "T", "C", "G"]
    BASES_COMPLEMENTS = {"A": "T", "T": "A", "C": "G", "G": "C"}

    def __init__(self, bases="NULL"):
        if bases == "NULL":
            print("NULL sequence created!")
            self.bases = bases
            return

        for d in bases:
            if d not in Seq.CORRECT_BASES:
                self.bases = "ERROR"
                print("INVALID sequence created!")
                return
        self.bases = bases
        print("New sequence created!")

    def __str__(self):
        return self.bases

    def len(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        else:
            return len(self.bases)

    def count_base(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return self.bases.count(base)

    def count(self):
        bases_dict = {}
        for base in Seq.CORRECT_BASES:
            bases_dict[base] = self.count_base(base)
        return bases_dict

    def reverse_mode(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases
        return self.bases[::-1]

    def complementary(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases
        result = ""
        for base in self.bases:
            result += Seq.BASES_COMPLEMENTS[base]
        return result

    def percentage_base(self, base):
        if self.bases == "NULL" or self.bases == "ERROR":
            return 0
        return (self.count_base(base) * 100) / self.len()

    def read_fasta_format(self, filename):
        file_content = Path(filename).read_text()  # contenido del fichero
        file_content_without_end_of_line_character = file_content.splitlines()  # sin salto de linea
        self.bases = ""
        for line in file_content_without_end_of_line_character[1:]:  # el
            self.bases += line

    def info(self):
        result = f"Sequence: {self} \n"
        result += f"Total length:{self.len()}\n"
        bases_count = self.count()
        for base, count in bases_count.items():
            if count == 0:
                result += f"{base} : {count} (0%) \n"
            else:
                result += f"{base}: {count} ({'{:.1f}'.format((count * 100) / self.len())}%)\n"
                return result

    def complement(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases

        result = ""
        complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
        for base in self.bases:
            result += complements[base]
        return result

    def reverse(self):
        if self.bases == "NULL" or self.bases == "ERROR":
            return self.bases
        return self.bases[::-1]


class Gene(Seq):
    def __init__(self, bases, name=""):
        super().__init__(bases)
        self.name = name
        print("New sequence created")
