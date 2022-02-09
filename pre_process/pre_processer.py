from tokenization.soy_tokenizer import SoyNlpTokenizer
from reader.text_reader import TextReader
from reader.json_reader import JsonReader
import csv

def write_file(sentences: list):
    path = "../data/ready_for_train/"
    with open(path, 'w') as f:
        writer = csv.writer(f)

        for sent in sentences:
            writer.writerow(sent)


class PreProcesser:
    def get_noun_sentences(self, sentences, nouns) -> list:
        noun_sentences = []
        words = []

        for sent in sentences:
            split_words = sent.split()
            for word in split_words:
                if [word] in nouns:
                    words.append(word)

            noun_sentences.append(" ".join(words))
            words.clear()

        return noun_sentences


if __name__ == "__main__":
    raw_path = "../data/raw_data/"
    nouns_path = "../tokenization/data/nouns/nouns.csv"

    json_reader = JsonReader()
    sentences = json_reader.read_file(raw_path)

    tokenizer = SoyNlpTokenizer()
    nouns = tokenizer.read_noun_dict(nouns_path)

    pre = PreProcesser()
    noun_sentences = pre.get_noun_sentences(sentences, nouns)