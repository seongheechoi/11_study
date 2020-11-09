import tensorflow as tf

a = tf.add(1, 3, name='a_add')
b = tf.multiply(a, 3, name='b_multiply')

tf.summary.FileWriter('./my_graph', graph=tf.get_default_graph())
