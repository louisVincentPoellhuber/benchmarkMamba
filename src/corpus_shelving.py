import shelve
import dotenv
import os
from tqdm import tqdm

dotenv.load_dotenv()
DATA_PATH = os.getenv("LOCAL_DATA_PATH")

if __name__ == "__main__":
    corpus_path = os.path.join(DATA_PATH, "default_corpus")
    default_corpus = shelve.open(corpus_path)

    collection_path = os.path.join(DATA_PATH, "collection.tsv")
    with open(collection_path, 'r') as fin:
        for line in tqdm(fin, desc="loading collection..."):
            pid, passage = line.strip().split("\t")
            
            default_corpus[pid] = passage

    default_corpus.close() 

