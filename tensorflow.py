import tensorflow as tf

# criar uma constante no TensorFlow

hello = tf.constant('hello world')

# iniciar  sessão

sess = tf.Session()

# executar operação

print(sess.run(hello))