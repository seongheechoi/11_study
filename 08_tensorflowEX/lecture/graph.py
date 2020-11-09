import tensorflow as tf

print(tf.get_default_graph())

g= tf.Graph()
with g.as_default():
    a=tf.multiply(2,4)
    b=tf.add(a,5)
    c=tf.subtract(b,7)

sess = tf.Session(graph=g)
result = sess.run(c)
print(result)

print(a.graph is g)
sess2 = tf.Session(graph=tf.get_default_graph())