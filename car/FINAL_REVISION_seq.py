from pathlib import Path


class Seq:
    BASES_ALLOWED = ["A", "C", "G", "T"]

    """A class for representing sequences"""
    def __init__(self, strbases="NULL"):
        if strbases == "NULL":
            print("NULL Sequence created!")
            self.strbases = strbases
            return

        for c in strbases:
            if c not in Seq.BASES_ALLOWED:
                self.strbases = "ERROR"
                print("INCORRECT Sequence detected!")
                return
        self.strbases = strbases
        print("New Sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        return len(self.strbases)

    def count_base(self, base):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return 0
        return self.strbases.count(base)

    def read_fasta(self, filename):
        file_contents = Path(filename).read_text()
        body = file_contents.splitlines()[1:]
        self.strbases = ""
        for line in body:
            self.strbases += line

    def count(self):
        result = {}
        bases = ["A", "T", "C", "G"]
        for base in bases:
            result[base] = self.count_base(base)
        return result

    def reverse(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases
        return self.strbases[::-1]

    def complement(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return self.strbases

        result = ""
        complements = {"A": "T", "T": "A", "C": "G", "G": "C"}
        for base in self.strbases:
            result += complements[base]
        return result

    def most_frequent_base(self):
        if self.strbases == "NULL" or self.strbases == "ERROR":
            return None

        bases_freq = self.count()
        base_result = None
        freq_result = 0
        for base, freq in bases_freq.items():
            if freq > freq_result:
                base_result = base
                freq_result = freq
        return base_result

    def info(self):
        result = f"Sequence: {self}\n"
        result += f"Total length: {self.len()}\n"
        bases_count = self.count()
        for base, count in bases_count.items():
            if count == 0:
                result += f"{base}: {count} (0%)\n"
            else:
                result += f"{base}: {count} ({'{:.1f}'.format((count * 100) / self.len())}%)\n"
        return result