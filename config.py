import tensorflow as tf

flags = tf.flags

# flags for setting
flags.DEFINE_integer("n_s", -1, "Number of sample (-1: read all data from file)")
flags.DEFINE_integer("n_h", 30, "Number of histroy we are interesed in from data")
flags.DEFINE_integer("n_e", 100, "Number of epoch for training")
flags.DEFINE_integer("b_s", 10, "Size of batch for each training epoch")
flags.DEFINE_string("f_n", "test2.dat", "filename of data file")


# For flexible model
flags.DEFINE_integer("depth", 3, "Depth of network (>1)")
flags.DEFINE_integer("h_size", 20, "Hidden node size")

# For data split for cross validation
flags.DEFINE_integer("seed", 1, "Random seed for split data set")
flags.DEFINE_float("test_size", 0.33, "Test data size")


flags.DEFINE_integer("verbose", 1, "Print during fit (1) or not (0)")
flags.DEFINE_integer("graph", 1, "Save graph (1) or not (0)")
