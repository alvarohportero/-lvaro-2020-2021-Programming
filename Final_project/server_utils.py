from seq import Seq


def read_template_html_file(filename):
    import jinja2
    from pathlib import Path
    content = jinja2.Template(Path(filename).read_text())
    return content


SERVER = 'rest.ensembl.org'
OK = 200
BAD_REQUEST = 400


def list_species(limit=None):
    import http.client
    import json
    from pathlib import Path

    endpoint = '/info/species'
    params = '?content-type=application/json'
    url = endpoint + params

    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", url)
    response = conn.getresponse()
    status = OK
    if response.status == OK:
        data = json.loads(response.read().decode("utf-8"))
        print(data)
        try:
            species = data['species']

            context = {
                "total": len(species),
                "species": species,
                "limit": limit
            }
            contents = read_template_html_file("./html/species.html").render(context=context)
        except KeyError:
            status = BAD_REQUEST
            contents = Path("./html/error.html").read_text()
    else:
        status = BAD_REQUEST
        contents = Path("./html/error.html").read_text()
    return status, contents


def karyotype(specie):
    import http.client
    import json
    from pathlib import Path

    endpoint = '/info/assembly/'
    params = f'{specie}?content-type=application/json'
    url = endpoint + params

    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", url)
    response = conn.getresponse()
    status = OK
    if response.status == OK:
        data = json.loads(response.read().decode("utf-8"))
        try:
            karyotype = data['karyotype']

            context = {
                "karyotype": karyotype,
            }
            contents = read_template_html_file("./html/karyotype.html").render(context=context)
        except KeyError:
            status = BAD_REQUEST
            contents = Path("./html/error.html").read_text()
    else:
        status = BAD_REQUEST
        contents = Path("./html/error.html").read_text()
    return status, contents


def chromosome_length(specie, chromo):
    import http.client
    import json
    from pathlib import Path

    endpoint = '/info/assembly/'
    params = f'{specie}?content-type=application/json'
    url = endpoint + params

    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", url)
    response = conn.getresponse()
    status = OK
    if response.status == OK:
        data = json.loads(response.read().decode("utf-8"))
        try:
            top_level_region = data['top_level_region']
            length = 0
            for chromosome in top_level_region:
                if chromosome['name'] == chromo:
                    length = chromosome['length']
                    break

            context = {
                "length": length,
            }
            contents = read_template_html_file("./html/chromosome_length.html").render(context=context)
        except KeyError:
            status = BAD_REQUEST
            contents = Path("./html/error.html").read_text()
    else:
        status = BAD_REQUEST
        contents = Path("./html/error.html").read_text()
    return status, contents


def get_id(gene):
    import http.client
    import json

    endpoint = '/homology/symbol/human/'
    params = f'{gene}?content-type=application/json'
    url = endpoint + params

    conn = http.client.HTTPConnection(SERVER)
    conn.request("GET", url)
    response = conn.getresponse()
    ok = True
    id = None
    if response.status == OK:
        data = json.loads(response.read().decode("utf-8"))
        try:
            id = data['data'][0]['id']
        except (KeyError, ValueError):
            ok = False
    else:
        ok = False
    return ok, id


def gene_seq(gene):
    import http.client
    import json
    from pathlib import Path

    ok, id = get_id(gene)
    if ok:
        endpoint = '/sequence/id/'
        params = f'{id}?content-type=application/json'
        url = endpoint + params

        conn = http.client.HTTPConnection(SERVER)
        conn.request("GET", url)
        response = conn.getresponse()
        status = OK
        if response.status == OK:
            data = json.loads(response.read().decode("utf-8"))
            try:
                bases = data['seq']

                context = {
                    "gene": gene,
                    "bases": bases
                }
                contents = read_template_html_file("html/gene_seq.html").render(context=context)
            except KeyError:
                status = BAD_REQUEST
                contents = Path("./html/error.html").read_text()
        else:
            status = BAD_REQUEST
            contents = Path("./html/error.html").read_text()
    else:
        status = BAD_REQUEST
        contents = Path("./html/error.html").read_text()
    return status, contents


def gene_info(gene):
    import http.client
    import json
    from pathlib import Path

    ok, id = get_id(gene)
    if ok:
        endpoint = '/overlap/id/'
        params = f'{id}?feature=gene;content-type=application/json'
        url = endpoint + params

        conn = http.client.HTTPConnection(SERVER)
        conn.request("GET", url)
        response = conn.getresponse()
        status = OK
        if response.status == OK:
            data = json.loads(response.read().decode("utf-8"))
            try:
                start = data[0]['start']
                end = data[0]['end']
                length = end - start
                chromosome_name = data[0]['assembly_name']

                context = {
                    "gene": gene,
                    "start": start,
                    "end": end,
                    "id": id,
                    "length": length,
                    "chromosome_name": chromosome_name
                }
                contents = read_template_html_file("html/gene_info.html").render(context=context)
            except (KeyError, IndexError):
                status = BAD_REQUEST
                contents = Path("./html/error.html").read_text()
        else:
            status = BAD_REQUEST
            contents = Path("./html/error.html").read_text()
    else:
        status = BAD_REQUEST
        contents = Path("./html/error.html").read_text()
    return status, contents


def gene_calc(gene):
    import http.client
    import json
    from pathlib import Path

    ok, id = get_id(gene)
    if ok:
        endpoint = '/sequence/id/'
        params = f'{id}?content-type=application/json'
        url = endpoint + params

        conn = http.client.HTTPConnection(SERVER)
        conn.request("GET", url)
        response = conn.getresponse()
        status = OK
        if response.status == OK:
            data = json.loads(response.read().decode("utf-8"))
            try:
                bases = data['seq']
                seq = Seq(bases)
                context = {
                    "gene": gene,
                    "seq": seq
                }
                contents = read_template_html_file("html/gene_calc.html").render(context=context)
            except KeyError:
                status = BAD_REQUEST
                contents = Path("./html/error.html").read_text()
        else:
            status = BAD_REQUEST
            contents = Path("./html/error.html").read_text()
    else:
        status = BAD_REQUEST
        contents = Path("./html/error.html").read_text()
    return status, contents
