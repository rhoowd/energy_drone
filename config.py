import tensorflow as tf

flags = tf.flags

# flags for setting
flags.DEFINE_integer("n_s", -1, "Number of sample (-1: read all data from file)")
flags.DEFINE_integer("n_h", 30, "Number of histroy we are interesed in from data")
flags.DEFINE_string("f_n", "test2.dat", "filename of data file")
