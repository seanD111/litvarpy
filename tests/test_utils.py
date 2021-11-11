from src.litvar import utils
from src.litvar import core


class TestUtils:
	def test_publications_from_query(self):
		var_pmids = utils.publications_from_query("VHL")
		assert all([key.startswith("rs") for key, val in var_pmids.items()])
