from datetime import date
import tweepy
import csv

access_token = "810489185861824512-sa6J6p1RAaolOFcLh1TOPmuOP9XHmDM"
access_token_secret = "zczOpmqn2vpzIg68XuKhXQgXzE4nMhuJGTu1gGugyV6Mv"
consumer_key = "mYh1sti2PMGKmiU0C8pPLbGGl"
consumer_secret = "0Kf8DNw8HklsHnINLGOPRryZMo3EvSCJvIL0Edh9JKS6ShCfx1"


def write_file(tweet):
    today = date.today()
    current_date = today.strftime("%Y_%m_%d")
    path = "../data/downloading_data/" + "election_" + current_date + ".txt"

    with open(path, 'a') as f:
        f.write(tweet.text)
        f.write('\n')


class MyStreamListener(tweepy.Stream):
    def on_status(self, tweet):
        write_file(tweet)

    def on_exception(self, exception):
        print(f"Exception:{exception}")

    def on_connection_error(self):
        print("connection error")

    def on_connect(self):
        print("on connect")


def get_filter_words(path):

    with open(path, "r") as file:
        csv_reader = csv.reader(file)
        filter_words = [word[0] for word in csv_reader]

    return filter_words


if __name__ == "__main__":
    filter_path = "./filter_file/2022_election_filter_words.csv"
    filter_words = get_filter_words(filter_path)

    stream = MyStreamListener(consumer_key, consumer_secret, access_token, access_token_secret)
    stream.filter(track=filter_words, threaded=True)

