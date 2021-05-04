from seq import Seq
import pathlib
import jinja2


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

def info(sequence):
    seq = Seq(sequence)
    result = f"Total length: {seq.len()}<br><br>"
    for base, count in seq.count().items():
        result += f"{base}: {count} ({seq.percentage_base(base)}%)<br><br>"
    context = {
        "sequence": seq,
        "operation": "info",
        "result": result
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents


def comp(sequence):
    seq = Seq(sequence)
    context = {
        "sequence": seq,
        "operation": "comp",
        "result": seq.complement()
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents


def rev(sequence):
    seq = Seq(sequence)
    context = {
        "sequence": seq,
        "operation": "rev",
        "result": seq.reverse()
    }
    contents = read_template_html_file("./html/operation.html").render(context=context)
    return contents

def gene(seq_name):
    path = "./sequences/" +seq_name + ".txt"
    seq = Seq()
    seq.read_fasta_format(path)
    context = {
        'gene_name': seq_name,
        'gene_contents': seq.bases
    }
    contents = read_template_html_file('./html/gene.html').render(context=context)
    return contents
