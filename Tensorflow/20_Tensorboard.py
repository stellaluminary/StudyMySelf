import tensorflow as tf

a = tf.constant(2.0, name="a")
b = tf.constant(3.0, name="b")
c = tf.constant(4.0, name="c")

# name_scope는 영역을 의미한다.
# Graph에서는 그룹 박스로 표시된다.
with tf.name_scope("large_op"):
    with tf.name_scope("mini_op"):
        addop = tf.add(a, b, name="add_op")
    mulop = tf.multiply(addop, c, name="mul_op")

# step 1 : scalars 기록할 node 선택
tf.summary.scalar("mul_result", mulop)

# step 2 : summary 통합
merged = tf.summary.merge_all()

with tf.Session() as sess:
    # step 3: writer 생성
    writer = tf.summary.FileWriter("./tmp/tensorboard/group",
                                   sess.graph)
    # step 4: 그래프 실행, summary 정보 로그 추가
    summary = sess.run(merged)
    writer.add_summary(summary)

print("Done")