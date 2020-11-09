import tensorflow as tf

x = tf.constant([[1.],[4.],[7.]])
y = tf.constant([[1.,1.,1.]])

print('shape:{} {}'.format(x.get_shape(), y.get_shape()))

subXY = tf.subtract(x,y)
sess = tf.Session()
result = sess.run(subXY)
print(result)
