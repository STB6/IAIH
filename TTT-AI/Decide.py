# 实现decide方法
# 用于解码基因和实现AI决策
# neural_network(...)   神经网络的前向传播
# decode_gene(gene)     解码基因以获取神经网络的权重和偏置
# decide(gene, board)   根据神经网络的输出和当前棋盘状态决定落子优先级
import numpy as np


INPUT_NODES = 9
HIDDEN_NODES1 = 9
HIDDEN_NODES2 = 9
OUTPUT_NODES = 9


def ReLU(x):
    return np.maximum(0, x)


# 神经网络的前向传播
def neural_network(input, weights1, biases1, weights2, biases2, output_weights, output_biases):
    # 隐藏层1
    hidden_layer1_input = np.dot(input, weights1) + biases1
    hidden_layer1_output = ReLU(hidden_layer1_input)
    # 隐藏层2
    hidden_layer2_input = np.dot(hidden_layer1_output, weights2) + biases2
    hidden_layer2_output = ReLU(hidden_layer2_input)
    # 输出层
    output_layer_input = np.dot(hidden_layer2_output, output_weights) + output_biases
    output_layer_output = ReLU(output_layer_input)
    return output_layer_output


# 解码权重和偏置
def decode_gene(gene):
    # 隐藏层1
    weights1 = np.array(gene[: INPUT_NODES * HIDDEN_NODES1]).reshape(INPUT_NODES, HIDDEN_NODES1)
    biases1 = np.array(gene[INPUT_NODES * HIDDEN_NODES1 : INPUT_NODES * HIDDEN_NODES1 + HIDDEN_NODES1])
    # 隐藏层2
    weights2 = np.array(gene[INPUT_NODES * HIDDEN_NODES1 + HIDDEN_NODES1 : INPUT_NODES * HIDDEN_NODES1 + HIDDEN_NODES1 + HIDDEN_NODES1 * HIDDEN_NODES2]).reshape(HIDDEN_NODES1, HIDDEN_NODES2)
    biases2 = np.array(gene[INPUT_NODES * HIDDEN_NODES1 + HIDDEN_NODES1 + HIDDEN_NODES1 * HIDDEN_NODES2 : INPUT_NODES * HIDDEN_NODES1 + HIDDEN_NODES1 + HIDDEN_NODES1 * HIDDEN_NODES2 + HIDDEN_NODES2])
    # 输出层
    output_weights = np.array(gene[INPUT_NODES * HIDDEN_NODES1 + HIDDEN_NODES1 + HIDDEN_NODES1 * HIDDEN_NODES2 + HIDDEN_NODES2 : INPUT_NODES * HIDDEN_NODES1 + HIDDEN_NODES1 + HIDDEN_NODES1 * HIDDEN_NODES2 + HIDDEN_NODES2 + HIDDEN_NODES2 * OUTPUT_NODES]).reshape(HIDDEN_NODES2, OUTPUT_NODES)
    output_biases = np.array(gene[INPUT_NODES * HIDDEN_NODES1 + HIDDEN_NODES1 + HIDDEN_NODES1 * HIDDEN_NODES2 + HIDDEN_NODES2 + HIDDEN_NODES2 * OUTPUT_NODES :])
    return weights1, biases1, weights2, biases2, output_weights, output_biases


# 根据神经网络的输出和当前棋盘状态决定落子优先级
def decide(gene, board):
    weights1, biases1, weights2, biases2, output_weights, output_biases = decode_gene(gene)
    output = neural_network(np.array(board), weights1, biases1, weights2, biases2, output_weights, output_biases)
    # 将输出转换为一维数组,并获取降序排序的索引
    sorted_indices = np.argsort(output.flatten())[::-1]
    return sorted_indices.tolist()
