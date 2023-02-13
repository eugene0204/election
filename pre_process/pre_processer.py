from tokenization.soy_tokenizer import SoyNlpTokenizer
from reader.text_reader import TextReader
from tqdm import tqdm
from reader.json_reader import JsonReader
import csv

def write_file(sentences: list, name):
    path = "../data/ready_for_train/" + name
    with open(path, 'w') as f:
        writer = csv.writer(f)

        for sent in sentences:
            writer.writerow([sent])



class PreProcesser:
    def get_noun_sentences(self, sentences, nouns) -> list:
        noun_sentences = []

        nouns_ = set(nouns)
        for sent in tqdm(sentences, desc="making noun sentences"):
            sent_ = set(sent.split())
            commons = sent_ & nouns_

            if commons and len(commons) > 1:
                noun_sentences.append(" ".join(commons))

        noun_sentences = list(set(noun_sentences))

        return noun_sentences


if __name__ == "__main__":
    raw_path = "../data/raw_data/"
    nouns_path = "../tokenization/data/nouns/nouns.csv"

    data_reader = TextReader()
    sentences = data_reader.read_data(raw_path)

    tokenizer = SoyNlpTokenizer()
    nouns = tokenizer.read_noun_dict(nouns_path)

    pre = PreProcesser()
    noun_sentences = pre.get_noun_sentences(sentences, nouns)

    file_name = "0302_to_0308.csv"
    write_file(noun_sentences, file_name)
