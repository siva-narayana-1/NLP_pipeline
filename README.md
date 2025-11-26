# 🧠 NLP Preprocessing Pipeline

A complete end-to-end **NLP preprocessing pipeline** built in Python using NLTK. This project automates the process of cleaning raw text files, tokenizing them, removing noise, and saving processed output in a structured format.

---

## 📁 Project Overview

This project demonstrates a production-style NLP pipeline that processes text files stored in a folder and applies multiple preprocessing steps including:

* Sentence tokenization
* Word tokenization
* Punctuation removal (two methods)
* Stopword removal
* Regex normalization
* Cleaned data export
* Logging and error handling

---

## 📂 Project Structure

```
NLP-Pipeline/
│
├── data/                     # Raw input text files
├── cleaned_data/             # Output cleaned text files (auto-created)
├── logger.py                 # Custom logger handler
├── main.py                   # Main NLP pipeline code
└── README.md                 # Project documentation
```

---

## ⚙️ Features Explained (Based on Code)

Below is a detailed explanation of **every component** in your code.

### ### 1️⃣ Class Initialization

```python
self.data = '.\\data'
```

* Sets the directory where raw text files are stored.
* Ensures the pipeline dynamically reads all files inside the folder.

---

### 2️⃣ Data Collection

```python
for i in os.listdir(self.data):
    main_file = os.path.join(self.data, i)
```

* Iterates through every file inside the `data/` folder.
* Opens each file with UTF-8 support.
* Reads all lines for further processing.
* Sends text to the sentence tokenizer.

Key operations:

* File handling
* Line-by-line reading
* Error logging

---

### 3️⃣ Sentence Tokenization

```python
final_string = " ".join(text)
sentence = sent_tokenize(final_string)
```

Steps applied:

* Joins all lines into a single string.
* Removes brackets `()[]{}` using regex.
* Normalizes multiple whitespaces to a single space.
* Tokenizes text into sentences.
* Logs total number of sentences.

Output:

* A **list of cleaned sentences**.

---

### 4️⃣ Word Tokenization

```python
for i in sentence:
    words = word_tokenize(i)
```

Actions performed:

* Each sentence is tokenized into words using NLTK.
* All tokens are added into a master list.
* Logs total number of words.

This stage prepares the data for deeper cleaning.

---

### 5️⃣ Punctuation Removal (Two Methods)

Your pipeline uses *two different techniques*.

#### ✔ Method 1: Using `.isalpha()`

```python
punctuation_data = [i for i in words if i.lower().isalpha()]
```

* Keeps tokens containing only alphabetic characters.
* Removes numbers, symbols, emojis, emoticons.

#### ✔ Method 2: Using `string.punctuation`

```python
punctuation_data2 = [i for i in words if i not in string.punctuation]
```

* Removes standard punctuation symbols like `. , ! ? :` etc.

Both logs recorded:

* Number of tokens remaining after punctuation cleaning.

---

### 6️⃣ Stopword Removal

```python
english_words = stopwords.words('english')
stop_words = [i for i in words_stop if i.lower() not in english_words]
```

* Uses NLTK stopword list.
* Removes common words like: *the, is, at, which, on*.
* Converts words to lowercase before matching.
* Logs total remaining words.

---

### 7️⃣ Export Cleaned Data

```python
os.makedirs("./cleaned_data", exist_ok=True)
```

* Automatically creates `cleaned_data/` folder if it doesn't exist.
* Saves cleaned output into:

```
cleaned_data/<filename>_cleaned.txt
```

* Uses UTF-8 encoding and ignores unsupported characters.

---

### 8️⃣ Logging System

Every stage logs:

* Execution status
* Number of sentences
* Number of words
* Success and failure messages
* File paths

This makes debugging easier and resembles real ML pipelines in production.

---

## 📌 Workflow Summary

```
RAW TEXT → Sentence Tokenization → Word Tokenization → Punctuation Cleanup → Stopword Removal → Save Cleaned Output
```

---

## ▶️ How to Run the Project

1. Place your raw `.txt` files inside the **data/** folder.
2. Run:

```
python main.py
```

3. Cleaned files will appear inside:

```
cleaned_data/
```

---

## 🛠️ Requirements

```
pip install nltk
```

Download necessary nltk data:

```python
nltk.download('punkt')
nltk.download('stopwords')
```

---

## 🚀 Future Enhancements

* Add lemmatization or stemming
* Add Unicode normalization
* Add spell correction
* Integrate vectorization / embeddings
* Add unit tests
* Build a GUI around the pipeline

---

## 🤝 Contributing

Feel free to fork this repository, raise issues, or submit pull requests.

---

## 📬 Contact

Created by **Siva Narayana Surya Chandra**.
For collaboration or queries, feel free to reach out on LinkedIn
