# !pip install transformers --quiet

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from wordcloud import WordCloud
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding, Dropout
from tensorflow.keras.callbacks import EarlyStopping
nltk.download("stopwords")

stop_words = set(stopwords.words("english"))
from google.colab import files
uploaded = files.upload()

# Example files you upload:
# train.txt, test.txt, val.txt
train_data = pd.read_csv("train.txt", sep=";", header=None, names=["Comment","Emotion"])
test_data = pd.read_csv("test.txt", sep=";", header=None, names=["Comment","Emotion"])
validation_data = pd.read_csv("val.txt", sep=";", header=None, names=["Comment","Emotion"])

print(train_data.shape, test_data.shape, validation_data.shape)
train_data["length"] = train_data["Comment"].apply(len)

plt.figure(figsize=(10,6))
sns.histplot(train_data["length"], kde=True)
plt.title("Sentence Length Distribution")
plt.show()
def words_cloud(df, emotion):
    text = " ".join(df[df["Emotion"] == emotion]["Comment"])
    wc = WordCloud(width=800, height=600).generate(text)

    plt.figure(figsize=(7,7))
    plt.imshow(wc)
    plt.axis("off")
    plt.title(f"{emotion} Word Cloud")
    plt.show()

for emotion in train_data["Emotion"].unique():
    words_cloud(train_data, emotion)
    lb = LabelEncoder()
train_data["Emotion"] = lb.fit_transform(train_data["Emotion"])
test_data["Emotion"] = lb.transform(test_data["Emotion"])
validation_data["Emotion"] = lb.transform(validation_data["Emotion"])
X_train = train_data["Comment"]
y_train = train_data["Emotion"]

X_test = test_data["Comment"]
y_test = test_data["Emotion"]

X_val = validation_data["Comment"]
y_val = validation_data["Emotion"]
vocabSize = 11000

from tensorflow.keras.preprocessing.text import one_hot

def text_cleaning(df_column):
    stemmer = PorterStemmer()
    corpus = []

    for text in df_column:
        text = re.sub("[^a-zA-Z]", " ", text)
        text = text.lower().split()
        text = [stemmer.stem(word) for word in text if word not in stop_words]
        text = " ".join(text)
        corpus.append(text)

    one_hot_words = [one_hot(word, vocabSize) for word in corpus]
    padded = pad_sequences(one_hot_words, maxlen=300, padding="pre")
    return padded

x_train = text_cleaning(X_train)
x_test = text_cleaning(X_test)
x_val = text_cleaning(X_val)

y_train = to_categorical(y_train)
y_test  = to_categorical(y_test)
y_val   = to_categorical(y_val)
model = Sequential()
model.add(Embedding(vocabSize, 150, input_length=300))
model.add(Dropout(0.2))
model.add(LSTM(128))
model.add(Dropout(0.2))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.2))
model.add(Dense(6, activation="softmax"))

model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])
model.summary()
callback = EarlyStopping(monitor="val_loss", patience=3, restore_best_weights=True)

history = model.fit(
    x_train, y_train,
    validation_data=(x_val, y_val),
    epochs=10,
    batch_size=64,
    callbacks=[callback],
    verbose=1
)
print("Validation accuracy:", model.evaluate(x_val, y_val, verbose=0))
print("Test accuracy:", model.evaluate(x_test, y_test, verbose=0))
acc = history.history["accuracy"]
val_acc = history.history["val_accuracy"]
loss = history.history["loss"]
val_loss = history.history["val_loss"]
epochs = range(len(acc))

plt.plot(epochs, acc, label="Training Accuracy")
plt.plot(epochs, val_acc, label="Validation Accuracy")
plt.legend()
plt.show()

plt.plot(epochs, loss, label="Training Loss")
plt.plot(epochs, val_loss, label="Validation Loss")
plt.legend()
plt.show()
def clean_sentence(sentence):
    stemmer = PorterStemmer()
    text = re.sub("[^a-zA-Z]", " ", sentence)
    text = text.lower().split()
    text = [stemmer.stem(word) for word in text if word not in stop_words]
    text = " ".join(text)

    seq = one_hot(text, vocabSize)
    padded = pad_sequences([seq], maxlen=300, padding="pre")
    return padded

def predict_emotion(sentence):
    processed = clean_sentence(sentence)
    pred = model.predict(processed)
    emotion = lb.classes_[np.argmax(pred)]
    print("Predicted Emotion:", emotion)

predict_emotion("I am very happy today!")