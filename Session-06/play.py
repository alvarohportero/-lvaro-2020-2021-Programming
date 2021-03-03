import seq_0


class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):
        self.strbases = strbases
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if self.is_valid_sequence_2(strbases):
            print("New sequence created")
            self.strbases = strbases
        else:
            self.strbases = "Error"
            print("Incorrect seqeunce detected")
    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            print("Sequence", i, ":Length:",list_sequences[i].len(),  3, ")",list_sequences[i] )

    @staticmethod # if we use a static method, we call the class, for instance seq.doc  / if we use the self, we call the instance s1.doc
    def is_valid_sequence_2(bases):
        for c in bases:
            if c != "A" and c != "C" and c != "T" and c != "G":
                return False
        return True

    # @staticmethod
    # def static_function():
    #   print(text)

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)


class Gene(Seq):
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class
    """
    pass


# --- Main program
s1 = Seq("AGTACACTGGT")
g = Gene("CGTAAC")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Gene: {g}")
print(f"  Length: {g.len()}")
