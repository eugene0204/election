from gensim.models import KeyedVectors

model_name = "./models/2022_election_w2v_model_0303_0308"
model = KeyedVectors.load(model_name, mmap='r')


test_list = ('이재명', '윤석열', '안철수', '심상정', "문재인", "김건희", "이준석")

for name in test_list:
    print(name)
    print(model.wv.most_similar(name, topn=50))
