import os
import re


class TextReader:
    def read_data(self, path):
        sentneces = []
        files = os.listdir(path)
        for file in files:
            with open(os.path.join(path, file), 'r') as f:
                for sent in f:
                    korean = re.findall(u'[\uAC00-\uD7A3]+', sent)
                    korean = ' '.join(korean)
                    sentneces.append(korean)

        return sentneces


if __name__ == "__main__":
    path = "../raw_data/"
    reader = TextReader()

    sentences = reader.read_data(path)


