from sklearn.manifold import TSNE
from gensim.models import KeyedVectors
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from collections import namedtuple


plt.rc('font', family='NanumBarunGothic')
def show_tsne(name, vectors_show, vocab_show):
    tsne = TSNE(n_components=2, perplexity=35)
    X = tsne.fit_transform(vectors_show)
    df = pd.DataFrame(X, index=vocab_show, columns=['x', 'y'])
    fig = plt.figure()
    fig.set_size_inches(30, 20)
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(df['x'], df['y'])

    for word, pos in df.iterrows():
        ax.annotate(word, pos, fontsize=12)

    plt.xlabel(name, fontsize=20)
    plt.show()


if __name__ == "__main__":
    model_name = "../model/models/2022_election_w2v_model_2"
    model = KeyedVectors.load(model_name, mmap='r')

    test_list = ('이재명', '윤석열', '안철수', '심상정')

    Candi = namedtuple("Candi", ["name", "words"])

    topics = []
    candis = []
    for name in test_list:
        print(name)
        topics.clear()
        result = model.wv.most_similar(name, topn=100)
        for topic in result:
            topics.append(topic[0])

        candis.append(Candi(name, topics.copy()))

    for candi in candis:
        vocab = candi.words
        name = candi.name
        try:
            vectors = list(model.wv[vocab])
        except KeyError:
            pass
        show_tsne(name, vectors, vocab)





