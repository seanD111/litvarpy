import core


class TestCore:
    def test_variation_search(self):
        for model in core.variation_search("VHL"):
            assert isinstance(model, core.Model)

    def test_variation_information(self):
        for model in core.variation_information('rs28940298##'):
            assert isinstance(model, core.Model)

    def test_pmids_by_cooccur_varids(self):
        for model in core.pmids_by_cooccur_varids(["litvar@rs28940298##", "litvar@rs5030821##"]):
            assert isinstance(model, core.Model)

    def test_pmids_by_rsids(self):
        for reqtype in ["GET", "POST"]:
            for model in core.pmids_by_rsids(['rs123', 'rs126', 'rs129'], method=reqtype):
                assert isinstance(model, core.Model)

    def test_publications_by_varids(self):
        for model in core.publications_by_varids(["litvar@rs121913527##"], True):
            assert isinstance(model, core.Model)
