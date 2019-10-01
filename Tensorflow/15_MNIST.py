import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("./mnist/data/", one_hot=True)

# 신경망 모델 구성
X = tf.placeholder(tf.float32, [None, 28*28])
Y = tf.placeholder(tf.float32, [None, 10])

W1 = tf.Variable(tf.random_normal([784, 10], stddev=0.01))
model = tf.matmul(X, W1)

cost = tf.reduce_mean(
    tf.nn.softmax_cross_entropy_with_logits(logits=model, labels=Y))
# optimizer = tf.train.GradientDescentOptimizer(0.001).minimize(cost)
optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)
# optimizer = tf.train.RMSPropOptimizer(0.001).minimize(cost)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

batch_size = 100
total_batch = int(mnist.train.num_examples / batch_size)

for epoch in range(15):
    total_cost = 0

    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        _, cost_val = sess.run([optimizer, cost],
                               feed_dict={X:batch_xs, Y:batch_ys})
        total_cost += cost_val
    print('Epoch : ', '%04d' % (epoch+1),
          'Avg. Cost : ', '{:.3f}'.format(total_cost/total_batch))

print("학습 완료!!")

# 테스트 데이터로 검증하기
is_correct = tf.equal(tf.argmax(model, 1), tf.argmax(Y, 1))
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print("accuracy: ", sess.run(accuracy,
                             feed_dict={X:mnist.test.images,
                                        Y:mnist.test.labels}))





