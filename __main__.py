from .litvar import Disambiguation

if __name__ == "__main__":
    d1 = Disambiguation(query="VHL")
    d2 = Disambiguation(var_id='rs28940298##')
    print(d1.model)
