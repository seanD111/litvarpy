from urllib import request, parse
import certifi
import json
import io
from enum import Enum

def make_request(href, post_body):
    return_data = None
    href = parse.quote(href, safe="/:")
    if post_body is None:
        with request.urlopen(href, data=post_body, cafile=certifi.where()) as response:
            in_buffer = io.BytesIO()
            in_buffer.write(response.read())
            in_buffer.seek(0)
            text_buffer = io.TextIOWrapper(in_buffer, encoding='utf-8')
            return_data = text_buffer.read()
    return json.loads(return_data)


class Concept(Enum):
    variant = 1
    disease = 2
    gene = 3
    chemical = 4


class Link:
    def __init__(self, name, url):
        self.name = name
        self.url = url


class Model:
    def __init__(self, **kwargs):
        model_attributes = {'_id', 'name', 'concept', 'id', 'db', 'weight', 'rsid', 'hgvs', 'data', 'links'}
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in model_attributes)


class Disambiguation:
    SEARCH_URL = "https://www.ncbi.nlm.nih.gov/research/bionlp/litvar/api/v1/entity/search/"
    INFO_URL = "https://www.ncbi.nlm.nih.gov/research/bionlp/litvar/api/v1/entity/litvar/"

    def __init__(self, query=None, var_id=None):
        self.query = query
        self.var_id = var_id
        self.models = []

        if query is not None:
            self.variation_search(query)
        elif var_id is not None:
            self.variation_information(var_id)

    def variation_search(self, query):
        results = make_request(self.SEARCH_URL + query, None)
        for result in results:
            new_model = Model(**result)
            self.models.append(new_model)

    def variation_information(self, var_id):
        results = make_request(self.INFO_URL + var_id, None)
        if not isinstance(results, list):
            results = [results]
        for result in results:
            new_model = Model(**result)
            self.models.append(new_model)

class Publications:
    OCCURANCE_URL = "https://www.ncbi.nlm.nih.gov/research/bionlp/litvar/api/v1/public/pmids"
    PMIDS_URL = "https://www.ncbi.nlm.nih.gov/research/bionlp/litvar/api/v1/public/rsids2pmids"

    def __init__(self):

    def pmids_by_cooccur_varids(self, var_ids):

    def pmids_by_rsids_get(self, rs_ids):

    def pmids_by_rsids_post(self, rs_ids):

# Relations
def publications_by_varids_post(query):
