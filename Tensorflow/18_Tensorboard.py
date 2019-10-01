import tensorflow as tf

a = tf.constant(3.0, name='a')
b = tf.constant(4.0, name='b')
c = tf.add(a, b, name='addnode')

# step 1. scalar 기록할 node 선택
tf.summary.scalar('add_result_c', c)

# step 2. summary 통합
mergeall = tf.summary.merge_all()

with tf.Session() as sess:
    print("c = ", sess.run(c))

    # step 3. writer 생성
    writer = tf.summary.FileWriter('./tmp/tensorboard/addnum')
    writer.add_graph(sess.graph)

    # step 4. summary 정보 로그 추가
    summary = sess.run(mergeall)
    writer.add_summary(summary)
