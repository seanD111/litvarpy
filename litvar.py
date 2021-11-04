import urllib
import certifi
from enum import Enum

def make_request(href, post_body):
    with urllib.request.urlopen(href, data=post_body, cafile=certifi.where()) as response:
        compressed_bytes = io.BytesIO()
        compressed_bytes.write(response.read())
        compressed_bytes.seek(0)
        self.compressed[href] = compressed_bytes

class Concept(Enum):
    NONE = 0
    VARIANT = 1
    DISEASE = 2
    GENE = 3
    CHEMICAL = 4

class Link:
    def __init__(self, name, url):
        self.name = name
        self.url = url

class Model:
    def __init__(self, **kwargs):
        model_attributes = {'uid', 'name', 'concept', 'id', 'db', 'weight', 'rsid', 'hgvs', 'data', 'links'}
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in model_attributes)


class Disambiguation:
    def __init__(self, ):


# Disambiguations
def variation_disambiguation(query):


def variation_information(var_id):

# Publications
def pmids_by_varids(var_ids):

def pmids_by_rsids_get(rs_ids):

def pmids_by_rsids_post(rs_ids):

# Relations
def publications_by_varids_post(query):
