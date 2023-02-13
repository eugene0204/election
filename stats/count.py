from reader.gen_reader import BigCorpora

class Counter:

    def count(self, sentences):
        lee = "이재명"
        yoon = "윤석열"
        ahn = "안철수"
        shim = "심상정"

        num_lee = num_yoon = num_ahn = num_shim = 0

        for sent in sentences:
            if lee in sent:
                num_lee += 1
            if yoon in sent:
                num_yoon += 1

            # if ahn in sent:
            #     num_ahn += 1

            if shim in sent:
                num_shim += 1

        total = num_lee + num_yoon + num_ahn + num_shim

        print(f"이재명:{num_lee}, {num_lee/total}")
        print(f"윤석열:{num_yoon}, {num_yoon/total}")
        print(f"안철수:{num_ahn}, {num_ahn/total}")
        print(f"심상정:{num_shim}, {num_shim/total}")
        print(f"합계:{total}")

if __name__ == "__main__":
    path = "../data/ready_for_train"
    sentences = BigCorpora(path)

    counter = Counter()
    counter.count(sentences)







