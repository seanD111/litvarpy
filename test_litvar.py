import litvar


class TestLitvar:
    def test_variation_search(self):
        for model in litvar.variation_search("VHL"):
            assert isinstance(model, litvar.Model)

    def test_variation_information(self):
        for model in litvar.variation_information('rs28940298##'):
            assert isinstance(model, litvar.Model)

    def test_pmids_by_cooccur_varids(self):
        for model in litvar.pmids_by_cooccur_varids(["litvar@rs28940298##", "litvar@rs5030821##"]):
            assert isinstance(model, litvar.Model)

    def test_pmids_by_rsids(self):
        for reqtype in ["GET", "POST"]:
            for model in litvar.pmids_by_rsids(['rs123', 'rs126', 'rs129'], method=reqtype):
                assert isinstance(model, litvar.Model)

    def test_publications_by_varids(self):
        for model in litvar.publications_by_varids(["litvar@rs121913527##"], True):
            assert isinstance(model, litvar.Model)


# if __name__ == "__main__":
#     e = litvar.variation_search("VHL")
#     e = litvar.variation_information('rs28940298##')
#     e = litvar.pmids_by_cooccur_varids(["litvar@rs28940298##","litvar@rs5030821##"])
#     e = litvar.pmids_by_rsids(['rs123', 'rs126', 'rs129'], method="GET")
#     e = litvar.publications_by_varids(["litvar@rs121913527##"], True)
#     print(e)
