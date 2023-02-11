# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tensorflow as tf

if __name__=='__main__':

    # In tensorflow version
    print(tf.__version__)
    
# =============================================================================
#     Constant: Không thay đổi trong quá trình chạy chương trình
# =============================================================================
    x1 = tf.constant(1)
    print(x1)
    
    x2 = tf.constant(2 , dtype=('int32') , shape=(2) , name=('constant_x2'))
    print(x2)
    
    x3 = tf.constant([3,5] , dtype=('int32') , shape=(2) , name=('constant_x3'))
    print(x3)
    
    x4 = tf.constant(3)
    
    y = x1 * x4
# =============================================================================
#    Session trong tensorflow 
# =============================================================================
    sess = tf.compat.v1.Session()
    print(sess.run(y))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    