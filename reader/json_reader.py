import json
import os
import re

class JsonReader:
    def read_file(self, path) -> list:
        files = os.listdir(path)

        sentences = []
        for file in files:
            with open(os.path.join(path, file), 'r') as f:
                for tweet in f:
                    try:
                        json_data = json.loads(tweet)
                        text = json_data['text']
                        hangul = re.findall(u'[\uAC00-\uD7A3]+', text)
                        hangul = ' '.join(hangul)
                        if len(hangul) > 1:
                            sentences.append(hangul)
                    except KeyError as e:
                        pass

        sentences = list(set(sentences))

        return sentences


if __name__ == "__main__":
    path = "../data/raw_data/"
    reader = JsonReader()
    sents = reader.read_file(path)
    print(sents)





