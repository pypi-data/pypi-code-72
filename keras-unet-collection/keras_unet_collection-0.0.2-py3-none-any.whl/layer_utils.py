
from __future__ import absolute_import

from tensorflow.keras.layers import Conv2D, MaxPooling2D, UpSampling2D, Conv2DTranspose
from tensorflow.keras.layers import BatchNormalization, Activation, concatenate, multiply, add
from tensorflow.keras.layers import ReLU, LeakyReLU, PReLU, ELU, Softmax


def stride_conv(X, channel, pool_size=2, 
                activation='ReLU', 
                batch_norm=False, name='stride_conv'):
    '''
    stride convolutional layer --> batch normalization --> Activation
    *Proposed to replace max- and average-pooling layers 
    
    Input
    ----------
        X: input tensor
        channel: number of convolution filters
        pool_size: number of stride
        activation: one of the `tensorflow.keras.layers` interface, e.g., ReLU
        batch_norm: True for batch normalization, False otherwise.
        name: name of the created keras layers
    Output
    ----------
        X: output tensor
    '''
    
    bias_flag = ~batch_norm
    
    # linear convolution with strides
    X = Conv2D(channel, pool_size, strides=(pool_size, pool_size), 
                            padding='valid', use_bias=bias_flag, name='{}_stride_conv'.format(name))(X)
    
    # batch normalization
    if batch_norm:
        X = BatchNormalization(axis=3, name='{}_bn'.format(name))(X)
    
    # activation
    activation_func = eval(activation)
    X = activation_func(name='{}_activation'.format(name))(X)
    
    return X

def attention_gate(X, g, channel,  
                   activation='ReLU', 
                   attention='add', name='att'):
    '''
    Additive attention gate as in Oktay et al. 2018
    
    Input
    ----------
        X: input tensor, i.e., upsampled tensor)
        g: gated tensor. Downsampled for coarser level, and have not concatenated with X
        channel: number of intermediate channel.
                 Oktay et al. (2018) did not specify (denoted as F_int).
                 intermediate channel is expected to be smaller than the input channel.
        
        activation: a nonlinear attnetion activation.
                    The `sigma_1` in Oktay et al. 2018. Default is ReLU
                    
        attention: 'add' for additive attention. 'multiply' for multiplicative attention.
                   Oktay et al. 2018 applied additive attention.
    Output
    ----------
        X_att: output tensor
    
    '''
    activation_func = eval(activation)
    attention_func = eval(attention)
    
    # mapping the input tensor to the intermediate channel
    theta_att = Conv2D(channel, 1, use_bias=True, name='{}_theta_x'.format(name))(X)
    
    # mapping the gate tensor
    phi_g = Conv2D(channel, 1, use_bias=True, name='{}_phi_g'.format(name))(g)
    
    # ----- attention learning ----- #
    query = attention_func([theta_att, phi_g], name='{}_add'.format(name))
    
    # nonlinear activation
    f = activation_func(name='{}_activation'.format(name))(query)
    
    # linear transformation
    psi_f = Conv2D(1, 1, use_bias=True, name='{}_psi_f'.format(name))(f)
    # ------------------------------ #
    
    # sigmoid activation as attention coefficients
    coef_att = Activation('sigmoid', name='{}_sigmoid'.format(name))(psi_f)
    
    # multiplicative attention masking
    X_att = multiply([X, coef_att], name='{}_masking'.format(name))
    
    return X_att

def CONV_stack(X, channel, kernel_size=3, stack_num=2, 
               activation='ReLU', 
               batch_norm=False, name='conv_stack'):
    '''
    Stacked convolutional layer:
    ----------
    (Convolutional layer --> batch normalization --> Activation)*stack_num
    
    Input
    ----------
        X: input tensor
        channel: number of convolution filters
        kernel_size: size of 2-d convolution kernels
        
        stack_num: number of stacked Conv2D-BN-Activation layers
        activation: one of the `tensorflow.keras.layers` interface, e.g., ReLU
        batch_norm: True for batch normalization, False otherwise.
        name: name of the created keras layers
    Output
    ----------
        X: output tensor
        
    '''
    
    bias_flag = ~batch_norm
    
    # stacking Convolutional layers
    for i in range(stack_num):
        
        activation_func = eval(activation)
        
        # linear convolution
        X = Conv2D(channel, kernel_size, padding='same', use_bias=bias_flag, name='{}_{}'.format(name, i))(X)
        
        # batch normalization
        if batch_norm:
            X = BatchNormalization(axis=3, name='{}_{}_bn'.format(name, i))(X)
        
        # activation
        activation_func = eval(activation)
        X = activation_func(name='{}_{}_activation'.format(name, i))(X)
        
    return X

def RES_CONV_stack(X, channel, kernel_size=3, stack_num=2, res_num=2, activation='ReLU', batch_norm=False, name='res'):
    '''
    Stacked convolutional layer with residual path.
    
    Input
    ----------
        X: input tensor
        channel: number of convolution filters
        kernel_size: size of 2-d convolution kernels
        
        stack_num: number of stacked residual blocks
        res_num: number of convolutional layers per residual path
        
        activation: one of the `tensorflow.keras.layers` interface, e.g., ReLU
        batch_norm: True for batch normalization, False otherwise.
        name: name of the created keras layers
        
    Output
    ----------
        X: output tensor
        
    '''
    
    activation_func = eval(activation)
    
    layer_skip = Conv2D(channel, 1, name='{}_conv'.format(name))(X)
    layer_main = layer_skip
    
    for i in range(stack_num):

        layer_res = Conv2D(channel, kernel_size, padding='same', name='{}_conv{}'.format(name, i))(layer_main)
        
        if batch_norm:
            layer_res = BatchNormalization(name='{}_bn{}'.format(name, i))(layer_res)
        layer_res = activation_func(name='{}_activation{}'.format(name, i))(layer_res)
            
        for j in range(res_num):
            
            layer_add = add([layer_res, layer_main], name='{}_add{}_{}'.format(name, i, j))
            layer_res = Conv2D(channel, kernel_size, padding='same', name='{}_conv{}_{}'.format(name, i, j))(layer_add)
            
            if batch_norm:
                layer_res = BatchNormalization(name='{}_bn{}_{}'.format(name, i, j))(layer_res)
                
            layer_res = activation_func(name='{}_activation{}_{}'.format(name, i, j))(layer_res)
            
        layer_main = layer_res

    out_layer = add([layer_main, layer_skip], name='{}_add{}'.format(name, i))
    
    return out_layer

def CONV_output(X, n_labels, kernel_size=1, 
                activation='Softmax', 
                name='conv_output'):
    '''
    Convolutional layer with output activation
    
    Input
    ----------
        X: input tensor
        n_labels: number of classification labels (larger than two)
        kernel_size: size of 2-d convolution kernels. Default option is 1-by-1
        activation: one of the `tensorflow.keras.layers` interface. Default option is Softmax
                    if None is received, then linear activation is applied, that said, not activation.
        name: name of the created keras layers
    Output
    ----------
        X: output tensor
        
    '''
    
    X = Conv2D(n_labels, kernel_size, padding='same', use_bias=True, name=name)(X)
    
    if activation:
        activation_func = eval(activation)
        X = activation_func(name='{}_activation'.format(name))(X)
    
    return X

def UNET_left(X, channel, kernel_size=3, 
              stack_num=2, activation='ReLU', 
              pool=True, batch_norm=False, name='left0'):
    '''
    Encoder block of UNet (downsampling --> stacked Conv2D)
    
    Input
    ----------
        X: input tensor
        channel: number of convolution filters
        kernel_size: size of 2-d convolution kernels
        stack_num: number of convolutional layers
        activation: one of the `tensorflow.keras.layers` interface, e.g., ReLU
        pool: True for maxpooling, False for strided convolutional layers
        batch_norm: True for batch normalization, False otherwise.
        name: name of the created keras layers
    Output
    ----------
        X: output tensor
    
    *downsampling is fixed to 2-by-2, e.g., reducing feature map sizes from 64-by-64 to 32-by-32
    '''
    pool_size = 2
    
    # maxpooling layer vs strided convolutional layers
    if pool:
        X = MaxPooling2D(pool_size=(pool_size, pool_size), name='{}_pool'.format(name))(X)
    else:
        X = stride_conv(X, channel, pool_size, activation=activation, batch_norm=batch_norm, name=name)
    
    # stack linear convolutional layers
    X = CONV_stack(X, channel, kernel_size, stack_num=stack_num, activation=activation, batch_norm=batch_norm, name=name)
    
    return X

def UNET_res_left(X, channel, kernel_size=3, 
                  stack_num=2, res_num=2, activation='ReLU', 
                  pool=True, batch_norm=False, name='left0'):
    '''
    Encoder block of resildual UNet (downsampling --> stacked residual blocks)
    
    Input
    ----------
        X: input tensor
        channel: number of convolution filters
        kernel_size: size of 2-d convolution kernels
        stack_num: number of stacked residual blocks
        res_num: number of convolutional layers per residual path
        activation: one of the `tensorflow.keras.layers` interface, e.g., ReLU
        pool: True for maxpooling, False for strided convolutional layers
        batch_norm: True for batch normalization, False otherwise.
        name: name of the created keras layers
    Output
    ----------
        X: output tensor
    
    *downsampling is fixed to 2-by-2, e.g., reducing feature map sizes from 64-by-64 to 32-by-32
    '''
    pool_size = 2
    
    # maxpooling layer vs strided convolutional layers
    if pool:
        X = MaxPooling2D(pool_size=(pool_size, pool_size), name='{}_pool'.format(name))(X)
    else:
        X = stride_conv(X, channel, pool_size, activation=activation, batch_norm=batch_norm, name=name)
    
    # stack linear convolutional layers
    X = RES_CONV_stack(X, channel, stack_num=stack_num, res_num=res_num, 
                      activation=activation, batch_norm=batch_norm, name=name)    
    return X

# def UNET_right(X, X_left, channel, kernel_size=3, 
#                stack_num=2, activation='ReLU',
#                unpool=True, batch_norm=False, name='right0'):
#     '''
#     Decoder block of UNet (upsampling --> stacked Conv2D)
    
#     Input
#     ----------
#         X: input tensor
#         X_left: the output of corresponded downsampling output tensor (the input tensor is upsampling input)
#         channel: number of convolution filters
#         kernel_size: size of 2-d convolution kernels
#         stack_num: number of convolutional layers
#         activation: one of the `tensorflow.keras.layers` interface, e.g., ReLU
#         unpool: True for unpooling (i.e., reflective padding), False for transpose convolutional layers
#         batch_norm: True for batch normalization, False otherwise.
#         name: name of the created keras layers
#     Output
#     ----------
#         X: output tensor
    
#     *upsampling is fixed to 2-by-2, e.g., reducing feature map sizes from 64-by-64 to 32-by-32
    
#     '''
    
#     pool_size = 2
    
#     if unpool:
#         X = UpSampling2D(size=(pool_size, pool_size), name='{}_unpool'.format(name))(X)
#     else:
#         # Transpose convolutional layer --> stacked linear convolutional layers
#         X = Conv2DTranspose(channel, kernel_size, strides=(pool_size, pool_size), 
#                                          padding='same', name='{}_trans_conv'.format(name))(X)
    
#     # linear convolutional layers before concatenation
#     X = CONV_stack(X, channel, kernel_size, stack_num=1, activation=activation, 
#                    batch_norm=batch_norm, name='{}_conv_before_concat'.format(name))
    
#     # Tensor concatenation
#     H = concatenate([X, X_left], axis=-1, name='{}_concat'.format(name))
    
#     # stacked linear convolutional layers after concatenation
#     H = CONV_stack(H, channel, kernel_size, stack_num=stack_num, activation=activation, 
#                    batch_norm=batch_norm, name='{}_conv_after_concat'.format(name))
    
#     return H

def UNET_right(X, X_list, channel, kernel_size=3, 
               stack_num=2, activation='ReLU',
               unpool=True, batch_norm=False, name='right0'):
    '''
    Decoder block of UNet
    
    Input
    ----------
        X: input tensor
        X_list: a list of other tensors that connected to the input tensor
        channel: number of convolution filters
        kernel_size: size of 2-d convolution kernels
        stack_num: number of convolutional layers
        activation: one of the `tensorflow.keras.layers` interface, e.g., ReLU
        unpool: True for unpooling (i.e., reflective padding), False for transpose convolutional layers
        batch_norm: True for batch normalization, False otherwise.
        name: name of the created keras layers
    Output
    ----------
        X: output tensor

    *upsampling is fixed to 2-by-2, e.g., reducing feature map sizes from 64-by-64 to 32-by-32
    
    '''
    
    pool_size = 2
    
    if unpool:
        X = UpSampling2D(size=(pool_size, pool_size), name='{}_unpool'.format(name))(X)
    else:
        # Transpose convolutional layer --> stacked linear convolutional layers
        X = Conv2DTranspose(channel, kernel_size, strides=(pool_size, pool_size), 
                                         padding='same', name='{}_trans_conv'.format(name))(X)
    
    # linear convolutional layers before concatenation
    X = CONV_stack(X, channel, kernel_size, stack_num=1, activation=activation, 
                   batch_norm=batch_norm, name='{}_conv_before_concat'.format(name))
    
    # <--- *stacked convolutional can be applied here
    X = concatenate([X,]+X_list, axis=3, name=name+'_concat')
    
    # Stacked convolutions after concatenation 
    X = CONV_stack(X, channel, kernel_size, stack_num=stack_num, activation=activation, 
                   batch_norm=batch_norm, name=name+'_conv_after_concat')
    
    return X

def UNET_res_right(X, X_list, channel, kernel_size=3, 
                   stack_num=2, res_num=2, activation='ReLU',
                   unpool=True, batch_norm=False, name='right0'):
    '''
    Decoder block of Residual UNet
    
    Input
    ----------
        X: input tensor
        X_list: a list of other tensors that connected to the input tensor
        channel: number of convolution filters
        kernel_size: size of 2-d convolution kernels
        stack_num: number of stacked residual blocks
        res_num: number of convolutional layers per residual path
        activation: one of the `tensorflow.keras.layers` interface, e.g., ReLU
        unpool: True for unpooling (i.e., reflective padding), False for transpose convolutional layers
        batch_norm: True for batch normalization, False otherwise.
        name: name of the created keras layers
    Output
    ----------
        X: output tensor

    *upsampling is fixed to 2-by-2, e.g., reducing feature map sizes from 64-by-64 to 32-by-32
    
    '''
    
    pool_size = 2
    
    if unpool:
        X = UpSampling2D(size=(pool_size, pool_size), name='{}_unpool'.format(name))(X)
    else:
        # Transpose convolutional layer --> stacked linear convolutional layers
        X = Conv2DTranspose(channel, kernel_size, strides=(pool_size, pool_size), 
                                         padding='same', name='{}_trans_conv'.format(name))(X)
    
    # linear convolutional layers before concatenation
    X = CONV_stack(X, channel, kernel_size, stack_num=1, activation=activation, 
                   batch_norm=batch_norm, name='{}_conv_before_concat'.format(name))
    
    # Tensor concatenation
    H = concatenate([X,]+X_list, axis=-1, name='{}_concat'.format(name))
    
    # stacked linear convolutional layers after concatenation
    H = RES_CONV_stack(H, channel, stack_num=stack_num, res_num=res_num, 
                      activation=activation, batch_norm=batch_norm, name=name)
    
    return H


def UNET_att_right(X, X_left, channel, att_channel, kernel_size=3, stack_num=2,
                   activation='ReLU', atten_activation='ReLU', attention='add',
                   unpool=True, batch_norm=False, name='right0'):
    '''
    Decoder block of Attention-UNet
    
    Input
    ----------
        X: input tensor
        X_left: the output of corresponded downsampling output tensor (the input tensor is upsampling input)
        channel: number of convolution filters
        att_channel: number of intermediate channel.        
        kernel_size: size of 2-d convolution kernels.
        stack_num: number of convolutional layers.
        activation: one of the `tensorflow.keras.layers` interface, e.g., ReLU
        atten_activation: a nonlinear attnetion activation.
                    The `sigma_1` in Oktay et al. 2018. Default is ReLU
        attention: 'add' for additive attention. 'multiply' for multiplicative attention.
                   Oktay et al. 2018 applied additive attention.
                   
        unpool: True for unpooling (i.e., reflective padding), False for transpose convolutional layers
        batch_norm: True for batch normalization, False otherwise.
        name: name of the created keras layers
    Output
    ----------
        X: output tensor

    *upsampling is fixed to 2-by-2, e.g., reducing feature map sizes from 64-by-64 to 32-by-32
    
    '''
    
    pool_size = 2
    
    if unpool:
        X = UpSampling2D(size=(pool_size, pool_size), name='{}_unpool'.format(name))(X)
    else:
        # Transpose convolutional layer --> stacked linear convolutional layers
        X = Conv2DTranspose(channel, kernel_size, strides=(pool_size, pool_size), 
                                         padding='same', name='{}_trans_conv'.format(name))(X)
        
    X_left = attention_gate(X=X_left, g=X, channel=att_channel, activation=atten_activation, 
                            attention=attention, name='{}_att'.format(name))
    
    # Tensor concatenation
    H = concatenate([X, X_left], axis=-1, name='{}_concat'.format(name))
    
    # stacked linear convolutional layers after concatenation
    H = CONV_stack(H, channel, kernel_size, stack_num=stack_num, activation=activation, 
                   batch_norm=batch_norm, name='{}_conv_after_concat'.format(name))
    
    return H



