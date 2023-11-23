# 实现decide方法
# 用于解码基因和实现AI决策
# activation(x)         ReLU激活函数
# neural_network(...)   神经网络的前向传播
# decode_gene(gene)     解码基因以获取神经网络的权重和偏置
# decide(gene, board)   根据神经网络的输出和当前棋盘状态决定落子优先级
import numpy as np


def activation(x):
    # ReLU激活函数
    return np.maximum(0, x)


def neural_network(input, weights1, biases1, weights2, biases2, output_weights, output_biases):
    # 神经网络的前向传播
    # 隐藏层1
    hidden_layer1_input = np.dot(input, weights1) + biases1
    hidden_layer1_output = activation(hidden_layer1_input)
    # 隐藏层2
    hidden_layer2_input = np.dot(hidden_layer1_output, weights2) + biases2
    hidden_layer2_output = activation(hidden_layer2_input)
    # 输出层
    output_layer_input = np.dot(hidden_layer2_output, output_weights) + output_biases
    output_layer_output = activation(output_layer_input)
    return output_layer_output


def decode_gene(gene):
    # 解码得到权重和偏置
    # 隐藏层1
    weights1 = np.array(gene[:450]).reshape((9, 50))
    biases1 = np.array(gene[450:500])
    # 隐藏层2
    weights2 = np.array(gene[500:3000]).reshape((50, 50))
    biases2 = np.array(gene[3000:3050])
    # 输出层
    output_weights = np.array(gene[3050:3500]).reshape((50, 9))
    output_biases = np.array(gene[3500:3509])
    return weights1, biases1, weights2, biases2, output_weights, output_biases


def decide(gene, board):
    # 根据神经网络的输出和当前棋盘状态决定落子优先级
    weights1, biases1, weights2, biases2, output_weights, output_biases = decode_gene(gene)
    output = neural_network(np.array(board), weights1, biases1, weights2, biases2, output_weights, output_biases)
    # 直接将输出转换为一维数组,并获取降序排序的索引
    sorted_indices = np.argsort(output.flatten())[::-1]
    return sorted_indices.tolist()
