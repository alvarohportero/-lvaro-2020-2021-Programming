from seq import Seq
import pathlib
import jinja2


def read_html_file(filename):
    contents = pathlib.Path(filename).read_text()
    return contents
def read_template_html_file(filename):
    contents = jinja2.Template(pathlib.Path(filename).read_text())
    return contents
def print_colored(message, color):
    import termcolor
    print(termcolor.colored(message, color))

def format_command(command):
    return command.replace("\n", "").replace("\r", "")

def ping(cs):
    print_colored("PING command!", "green")
    response = "OK!"
    print(response)
    cs.send(response.encode())

def get(list_sequences, number_sequence):
   context = {
       'number': number_sequence,
       'sequence': list_sequences[int(number_sequence)]
   }
   contents = read_template_html_file('./html/get.html').render(context=context)
   return contents


def info(sequence):
    seq = Seq(sequence)
    response = seq.percentage_base()  # -- We have created a new function in Seq1.py to print A: number (percentage)%
    final_response = "Sequence: " + sequence + "\n" + "Total Length: " + str(seq.len()) + "\n" + response
    return final_response


def comp(sequence):
    seq = Seq(sequence)
    complementary = seq.complement()
    return complementary

def rev(argument):
    seq = Seq(argument)
    reverse = seq.reverse()
    return reverse


def gene(seq_name):
    PATH = "./sequences/" + seq_name
    s1 = Seq()
    s1.read_fasta(PATH)
    context = {
        'gene_name': seq_name,
        'gene_contents': s1.bases
    }
    contents = read_template_html_file('./html/gene.html').render(context=context)
    return contents
def operation(sequence, operation):
    if operation == "Info":
        result = info(sequence)
    elif operation == "Rev":
        result = rev(sequence)
    elif operation == "Comp":
        result = comp(sequence)
    context={
        "sequence": sequence,
        "operation": operation,
        "result": result
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents

