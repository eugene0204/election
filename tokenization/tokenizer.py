from reader.text_reader import TextReader
from soynlp.noun import LRNounExtractor_v2


class SoyNlpTokenizer:
    def __init__(self):
        self.noun_extractor = LRNounExtractor_v2(verbose=True, extract_compound=True)

    def extract(self, sents):
        self.noun_extractor.train(sents)
        return self.noun_extractor.extract()


if __name__ == "__main__":
    path = "../raw_data/"

    soy = SoyNlpTokenizer()