import os
import tensorflow as tf
tf.compat.v1.disable_eager_execution()

trained_checkpoint_prefix = '/Users/mollyejones/Music/TaPIR_lab_2022_23/tensorflow-wavenet-v2/logdir/train/final_models/accordion/345000/model.ckpt-345000'
export_dir = os.path.join('/Users/mollyejones/Music/TaPIR_lab_2022_23/tensorflow-wavenet-v2/logdir/train/final_models/accordion/pb', '345000')

graph = tf.Graph()
with tf.compat.v1.Session(graph=graph) as sess:
    # Restore from checkpoint
    loader = tf.compat.v1.train.import_meta_graph(trained_checkpoint_prefix + '.meta')
    loader.restore(sess, trained_checkpoint_prefix)

    # Export checkpoint to SavedModel
    builder = tf.compat.v1.saved_model.builder.SavedModelBuilder(export_dir)
    builder.add_meta_graph_and_variables(sess,
                                         [tf.saved_model.TRAINING, tf.saved_model.SERVING],
                                         strip_default_attrs=True)
    builder.save()  