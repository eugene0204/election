from gensim.models import Word2Vec
from reader.gen_reader import BigCorpora
import logging
import multiprocessing
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

cpu_count = multiprocessing.cpu_count()

train_data_path = "../data/ready_for_train/"
sentences = BigCorpora(train_data_path)

for sent in sentences:
    pass

model_path = "./models/"
model_name = "2022_election_w2v_model_0303_0308"

model = Word2Vec(sentences=sentences,
                 vector_size=300,
                 min_count=1,
                 workers=cpu_count)

model.save(model_path + model_name)







