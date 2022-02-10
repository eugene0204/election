from gensim.models import Word2Vec
from reader.large_file_reader import BigSentences
import os
import logging
import multiprocessing
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

cpu_count = multiprocessing.cpu_count()

train_data_path = "../data/ready_for_train/"
sentences = BigSentences(train_data_path)

model_path = "./models/"
model_name = "2022_election_w2v_model"

model = Word2Vec(sentences=sentences,
                 vector_size=300,
                 min_count=1,
                 workers=cpu_count)

model.save(model_path + model_name)







