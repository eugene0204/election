import os


class BigCorpora:
    def __init__(self, path):
        self.path = path

    def __iter__(self):
        files = os.listdir(self.path)
        for file in files:
            with open(os.path.join(self.path, file)) as f:
                for line in f:
                    yield line.split()


if __name__ == "__main__":
    path = "../data/ready_for_train"
    sentences = BigCorpora(path)

    for sent in sentences:
        pass
