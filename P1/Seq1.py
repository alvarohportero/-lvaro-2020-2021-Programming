class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases="NULL"):#kind of a default value if we dont put anything the null is
        self.strbases = strbases
        # Initialize the sequence with the value
        # passed as argument when creating the object
        if strbases == "NULL":
            print("Null seq was created")
        else:
            if Seq.is_valid_sequence_2(strbases):
                print("New sequence created!")
                self.strbases = strbases
            else:
                self.strbases = "Error"
                print("Incorrect seqeunce detected")

    @staticmethod  # if we use a static method, we call the class, for instance seq.doc  / if we use the self, we call the instance s1.doc
    def is_valid_sequence_2(bases):
        for c in bases:
            if c != "A" and c != "C" and c != "T" and c != "G":
                return False
        return True
    @staticmethod
    def print_seqs(list_sequences):
        for i in range(0, len(list_sequences)):
            text = ("Sequence" + str(i) + ":(length" + str(list_sequences[i]. len() + ")" + str(list_sequences[i])))


    # @staticmethod)
    # def static_function():
    #   print(text)

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        if self.strbases == "NULL" or self.strbases == "Error":
            return 0

def generate_seqs(pattern, number):
    # A, 3
    list_seq = []
    for i in range(0, number):
        list_seq.append(Seq(pattern * (i + 1)))
    return list_seq


