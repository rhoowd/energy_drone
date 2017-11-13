#!/usr/bin/env python
#coding=utf8
import sys
import extract_data as ed
from keras.models import model_from_json
import graph


model_file = (sys.argv[1]).split('.')[0]
data_file = sys.argv[2]
print "Load file:", model_file, "Data file", data_file

# Load data file

n_h = int(model_file.split('-')[2])
f_n = (data_file.split('/')[2])

print "Load model from ", model_file
print "Load data from ", f_n

xy = ed.extract_data_speed(n_history=n_h, filename=f_n)
x_data = xy[:, 0:-1]
y_data = xy[:, [-1]]

print "x_shape: " + str(x_data.shape) + ", y_shape:" + str(y_data.shape)

# load json and create model
json_file = open(model_file+".json", 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights(model_file+".h5")
print("Loaded model from disk")

# evaluate loaded model on test data
# loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
loaded_model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_squared_error'])
score = loaded_model.evaluate(x_data, y_data, verbose=0)
print "MSE: " + str(score[1])

est = loaded_model.predict(x_data)
graph.draw_graph(x_data[:, -1], y_data, est)