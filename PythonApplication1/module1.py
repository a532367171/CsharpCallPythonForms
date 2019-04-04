import tensorflow as tf
# 创建两个常量节点

def TFadd(a,b):
    node1 = tf.constant(a)
    node2 = tf.constant(b)
    adder = node1 + node2
    #print(adder)
    sess = tf.Session()
    return sess.run(adder)