from pathlib import Path


class Seq:
    CORRECT_BASES = ["A", "T", "C", "G"]
    BASES_COMPLEMENTS = {"A": "T", "T": "A", "C": "G", "G": "C"}


    def __init__(self, bases="NULL"):
        if bases == "NULL":
            print("NULL sequence created!")
        else:
            for base in bases:
                if base not in Seq.CORRECT_BASES:
                    print("INVALID sequence created!")
                    self.bases = "ERROR"
                    return

            print("New sequence created!")

        self.bases = bases

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
            bases_dict[base] = self.count_base(
                base)  # en el dic bases_dict, le estoy poniendo de clave:base y valor : self..
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

    def read_fasta_format(self, filename):
        file_content = Path(filename).read_text()  # contenido del fichero
        file_content_without_end_of_line_character = file_content.splitlines()  # sin salto de linea
        self.bases = ""
        for line in file_content_without_end_of_line_character[1:]:  # el
            self.bases += line


class Gene(Seq):
    def __init__(self, bases, name=""):
        super().__init__(bases)
        self.name = name
        print("New sequence created")
