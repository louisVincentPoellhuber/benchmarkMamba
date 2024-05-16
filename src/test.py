import shelve
import dotenv
import os
from tqdm import tqdm

dotenv.load_dotenv()
DATA_PATH = os.getenv("LOCAL_DATA_PATH")


if __name__ == "__main__":
    corpus_path = os.path.join(DATA_PATH, "default_corpus")
    default_corpus = shelve.open(corpus_path)

    print("======================= D1650436 =======================")
    print(default_corpus["D1650436"])
    print("======================= D1460407 =======================")
    print(default_corpus["D1460407"])
    print("======================= D782169 =======================")
    print(default_corpus["D782169"])
