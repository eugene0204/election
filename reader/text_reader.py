import os
import re
from tqdm import tqdm


class TextReader:
    def read_data(self, path):
        sentences = []
        files = os.listdir(path)
        for file in tqdm(files, desc="text reader"):
            with open(os.path.join(path, file), 'r') as f:
                for sent in f:
                    korean = re.findall(u'[\uAC00-\uD7A3]+', sent)
                    korean = ' '.join(korean)
                    if len(korean) > 1:
                        sentences.append(korean)

        sentences = list(set(sentences))

        return sentences


if __name__ == "__main__":
    path = "../data/raw_data/"
    reader = TextReader()

    sentences = reader.read_data(path)
    print(len(sentences))


