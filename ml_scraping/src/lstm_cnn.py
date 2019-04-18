# LSTM for sequence classification in the IMDB dataset
import os
import numpy as np
from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Conv1D
from tensorflow.keras.layers import MaxPooling1D
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.callbacks import ModelCheckpoint
from sklearn.metrics import classification_report


def save_best_model(epoch, dir_path, num_ext, ext):
    tmp_file_name = os.listdir(dir_path)
    test = []
    num_element = -num_ext

    for x in range(0, len(tmp_file_name)):
        test.append(tmp_file_name[x][:num_element])
        float(test[x])

    highest = max(test)

    return dir_path + '/' + str(highest) + ext


# fix random seed for reproducibility
# np.random.seed(7)

# load the dataset but only keep the top n words, zero the rest
top_words = 5000
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words=top_words)
print(X_train.shape)
print(X_train.shape)
print(X_train.shape)
print(X_train.shape)
print(X_train.shape)
print(imdb.)


# truncate and pad input sequences
max_review_length = 500
X_train = sequence.pad_sequences(X_train, maxlen=max_review_length)
X_test = sequence.pad_sequences(X_test, maxlen=max_review_length)

# create the model

embedding_vecor_length = 32
model = Sequential()
model.add(Embedding(top_words, embedding_vecor_length, input_length=max_review_length))
model.add(Conv1D(filters=32, kernel_size=3, padding='same', activation='relu'))
model.add(MaxPooling1D(pool_size=2))
model.add(Dropout(0.2))
model.add(LSTM(100))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())

checkpoint = ModelCheckpoint('output/lstm_cnn/{val_acc:.4f}.hdf5', monitor='val_acc', verbose=1, save_best_only=True,
                             mode='auto')

#model.fit(
#    X_train,
#    y_train,
#    epochs=5,
#    batch_size=64,
#    verbose=1,
#    validation_data=(X_test, y_test),
#    callbacks=[checkpoint]
#)

best = save_best_model(10, "output/lstm_cnn", 5, ".hdf5")

model.load_weights(best)

model.save("output/lstm_cnn/best.hdf5")

# Final evaluation of the model
scores = model.evaluate(X_test, y_test, verbose=0)
print("Accuracy: %.2f%%" % (scores[1] * 100))
print(classification_report(y_test, np.round(model.predict(X_test))))
