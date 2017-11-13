import tensorflow as tf

flags = tf.flags

# flags for setting
flags.DEFINE_integer("n_s", -1, "Number of sample (-1: read all data from file)")
flags.DEFINE_integer("n_h", 30, "Number of histroy we are interesed in from data")
flags.DEFINE_integer("n_e", 100, "Number of epoch for training")
flags.DEFINE_integer("b_s", 10, "Size of batch for each training epoch")
flags.DEFINE_integer("verbose", 1, "Print during fit (1) or not (0)")
flags.DEFINE_integer("graph", 1, "Save graph (1) or not (0)")
flags.DEFINE_string("f_n", "test2.dat", "filename of data file")
