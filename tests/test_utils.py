from src.litvar import utils
from src.litvar import core


class TestUtils:
	def test_publications_from_query(self):
		var_pmids = utils.publications_from_query("VHL")
		assert all([isinstance(var_pmid, core.Model) for var_pmid in var_pmids])
