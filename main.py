from string import punctuation

import nltk
from nltk.corpus.europarl_raw import english

from logger import Logger
log = Logger.get_logs("main")
import sys
import os
import string
import nltk
from nltk.corpus import stopwords
# nltk.download('punkt_tab')
# nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
import re
class NLP_PIPELINE:
    def __init__(self):
        try:
            self.data = '.\\data'
        except Exception:
            exc_type, exc_msg, exc_line = sys.exc_info()
            log.error(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")
    def collect_data(self):
        try:
            if os.path.exists(self.data):
                for i in os.listdir(self.data):
                    main_file = os.path.join(self.data, i)
                    file_load = open(main_file, 'r')
                    lines = file_load.readlines()
                    if lines:
                        log.info(f"Data is loaded from the file-{i}")
                        self.sentence_token(lines, i)
                    if file_load:
                        file_load.close()
        except Exception:
            exc_type, exc_msg, exc_line = sys.exc_info()
            log.error(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")
    def sentence_token(self, text, file_name):
        try:
            log.info("Sentence tokenization is running.......")
            final_string = f"""{" ".join(text)}"""
            final_string = re.sub(r"[\[\]\(\)\{\}]", " ", final_string)
            final_string = re.sub(r"\s+", " ", final_string)
            sentence = sent_tokenize(final_string)
            if sentence:
                log.info("Sentence_token is done...")
            log.info(f"The file {file_name} contains {len(sentence)} sentences.")
            log.info(sentence)
            self.word_token(sentence, file_name)
        except Exception:
            exc_type, exc_msg, exc_line = sys.exc_info()
            log.error(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")
    def word_token(self, sentence, file):
        try:
            log.info("Word Tokenization has started..............")
            word = []
            for i in sentence:
                words = word_tokenize(i)
                word.extend(words)
            log.info(f"The file {file} contain {len(word)} words.")
            log.info(word)
            self.check_punctuations(word, file)
        except Exception:
            exc_type, exc_msg, exc_line = sys.exc_info()
            log.error(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")
    def check_punctuations(self, words, file_name_p):
        try:
            log.info("Punctuations checking has started........")
            punctuation_data = [i for i in words if i.lower().isalpha()]
            log.info(f"In the file {file_name_p} removed the punctuations\n{len(punctuation_data)}")
            log.info(punctuation_data)
            log.info("By using the string function checking the punctutations......")
            punctuation_data2 = [i for i in words if i not in string.punctuation]
            log.info(f"In the file {file_name_p} removed the punctuations\n{len(punctuation_data)} by using the string module.")
            log.info(punctuation_data2)
            self.stop_words_removing(punctuation_data2, file_name_p)
        except Exception:
            exc_type, exc_msg, exc_line = sys.exc_info()
            log.error(f"{exc_type} at {exc_line.tb_lineno} as {exc_msg}")

    def stop_words_removing(self, words_stop, file_stop):
        try:
            english_words = stopwords.words('english')
            stop_words = [i for i in words_stop if i.lower() not in english_words]

            log.info(f"In the file {file_stop} we have removed stopwords and now it contains {len(stop_words)} words.")
            os.makedirs("./cleaned_data", exist_ok=True)
            cleaned_file_path = f"./cleaned_data/{file_stop}_cleaned.txt"

            if not os.path.exists(cleaned_file_path):
                with open(cleaned_file_path, "w", encoding="utf-8", errors="ignore") as f:
                    f.write(" ".join(stop_words))

                log.info(f"Created cleaned file: {cleaned_file_path}")

            else:
                log.info(f"Cleaned file already exists: {cleaned_file_path}")

        except Exception as e:
            exc_type, exc_msg, exc_tb = sys.exc_info()
            log.error(f"{exc_type} at line {exc_tb.tb_lineno}: {exc_msg}")


if __name__ == "__main__":
    obj = NLP_PIPELINE()
    obj.collect_data()