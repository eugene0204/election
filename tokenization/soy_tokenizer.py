from reader.text_reader import TextReader
from reader.json_reader import JsonReader
from soynlp.noun import LRNounExtractor_v2
import csv


class SoyNlpTokenizer:
    def __init__(self):
        self.noun_extractor = LRNounExtractor_v2(verbose=True, extract_compound=True)

    def train_extract(self, sents):
        return self.noun_extractor.train_extract(sents)

    def read_noun_dict(self, path):
        print("reading noun file")
        with open(path, 'r') as f:
            reader = csv.reader(f)
            nouns = [noun[0] for noun in reader]

        return nouns


def write_file(path, sents):
    with open(path, 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        for sent in sents:
            if len(sent) > 1:
                writer.writerow([sent])


if __name__ == "__main__":
    path = "./data/raw_data/"
    nouns_path = "./data/nouns/nouns.csv"

    data_reader = TextReader()
    sents = data_reader.read_data(path)


    soy = SoyNlpTokenizer()

    nouns = soy.train_extract(sents)
    write_file(nouns_path, nouns)
    print(nouns["이재명"])

    # test_list = ['이재명', '윤석열', '안철수', '심상정', '김건희']
    # write_file(test_list, nouns_path, noun_dict)
