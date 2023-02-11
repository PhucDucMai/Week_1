# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 09:49:22 2023

@author: maidu
"""

import tensorflow as tf
import warnings
warnings.filterwarnings('ignore')

if __name__ == '__main__':
    # =============================================================================
    #     Phiên bản của tensorflow
    # =============================================================================
    print(tf.__version__)

# =============================================================================
#     Constant: Không thay đổi trong suốt quá trình chạy
# =============================================================================
    x1 = tf.constant(2, dtype='int32', name=('const_x1'))
    print(x1)

    x2 = tf.constant(3, dtype=('int32'), name=('const_x2'))
    print(x2)

    x3 = x1*x2

# =============================================================================
#     Session: Khởi tạo session để tính toán với Tensorflow
# =============================================================================
    sess = tf.compat.v1.Session()
    print(sess.run(x3))
    print(sess.run(x1))

# =========================================================================================
#     Tensor có thể là số thực , số nguyên , ma trận 1D , 2D , 3D , ma trận nhiều chiều
# =========================================================================================
    v1 = tf.constant([[1, 2, 3], [3, 5, -1]], dtype=('int32'), name=('v1_2D'))
    print("Ma trận v1: ", sess.run(v1))

    v2 = tf.constant([[2, -1, 3], [1, 1, -2]], name=('v2_2D'))
    print("Ma trận v2: ", sess.run(v2))

# =============================================================================
#     Tính toán trên Tensorflow:
    # 1. Phải cùng dtype
# =============================================================================

    v12 = v1 + v2
    print("Tổng 2 ma trận v1 và v2: ", sess.run(v12))


# =============================================================================
#     Placeholder: load dữ liệu đầu vào
# =============================================================================
    p1 = tf.compat.v1.placeholder(dtype=tf.float32)
    p2 = tf.compat.v1.placeholder(dtype=tf.float32)

    o_add = p1 + p2
    o_mul = p1 * p2
    o_denta = pow(p1, 2) - pow(p2, 2)
    print(o_add)

# =============================================================================
#     Feed Value for Placeholder: load dữ liệu đầu vào
# =============================================================================
    d_values = {
        p1: 20,
        p2: 10
    }
    print("Tổng của 2 placeholder: ",sess.run(o_add, feed_dict=d_values))
    
    # Tính 1 lúc nhiều giá trị của placeholder
    print("Giá trị của các placeholder lần lượt là: ",sess.run([o_add , o_mul , o_denta] , feed_dict=d_values))
    
# =============================================================================
#     Variables: Tham số
    # Cần phải khởi tạo biến(variable) trước khi đưa vào tính toán trên session
# =============================================================================

    var_1 = tf.Variable(name=('var_1') , initial_value = 10)
    var_2 = tf.Variable(name=('var_2') , initial_value = 20)
    
    # Tạo ra dòng chạy global cho variable trong session
    tf.compat.v1.global_variables_initializer().run(session=sess)
    
    # Chạy biến var_1
    print("Giá trị của var_1: ",sess.run(var_1))
    
    
    
    
    
    
    
    
