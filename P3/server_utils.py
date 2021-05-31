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


def get(list_sequences, seq_number):
    context = {
        'number': seq_number,
        'sequence': list_sequences[int(seq_number)]
    }
    contents = read_template_html_file('./html/get.html').render(context=context)
    return contents


def info(cs, sequence):
    print_colored("INFO", "green")
    seq = Seq(sequence)
    response = seq.percentage_base()  # -- We have created a new function in Seq1.py to print A: number (percentage)%
    final_response = "Sequence: " + sequence + "\n" + "Total Length: " + str(seq.len()) + "\n" + response
    print(final_response)
    cs.send(str(final_response).encode())


def comp(cs, argument):
    print_colored("COMP", "green")
    seq = Seq(argument)
    complement = seq.complement()
    print(complement)
    cs.send(complement.encode())


def rev(cs, argument):
    print_colored("REV", "green")
    seq = Seq(argument)
    reverse = seq.reverse()
    print(reverse)
    cs.send(reverse.encode())


def gene(seq_name):
    PATH = "./projects/" + seq_name + ".txt"
    s1 = Seq()
    s1.seq_read_fasta(PATH)
    context = {
        'gene_name': seq_name,
        'gene_contents': s1.bases
    }
    contents = read_html_file('./html/gene.html').render(context=context)
    return contents
