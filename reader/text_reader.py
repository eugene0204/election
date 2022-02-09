import os
import re


class TextReader:
    def read_data(self, path):
        sentences = []
        words = []
        files = os.listdir(path)
        for file in files:
            with open(os.path.join(path, file), 'r') as f:
                words.clear()
                for sent in f:
                    korean = re.findall(u'[\uAC00-\uD7A3]+', sent)
                    korean = ' '.join(korean)
                    if len(korean) > 1:
                        words.append(korean)

                words = list(set(words))
                file = file.split(".")
                sentences.append((words, file[0]))

        return sentences


if __name__ == "__main__":
    path = "../data/raw_data/"
    reader = TextReader()

    sentences = reader.read_data(path)
    print(len(sentences))


