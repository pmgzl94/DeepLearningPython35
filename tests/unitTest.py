#!/bin/env python3
from network import Network
import mnist_loader
import numpy as np

import unittest

class TestNetwork(unittest.TestCase):
    """TEST ON UPDATE_MINIBATCH METHOD"""
    def test_update_mini_batch(self):

        net = Network([784, 100, 10])
        net2 = Network([784, 100, 10], True, net.get_biases(), net.get_weights())

        training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

        list_arr = list(training_data)

        eta = 0.1
        batch = list_arr[:10]
        batch2 = list_arr[:10]

        net.update_mini_batch(batch, eta) #original method

        weights1 = net.get_weights()
        biases1 = net.get_biases()

        net2.effectiv_update_mini_batch(batch2, eta) #updated method

        weights2 = net2.get_weights()
        biases2 = net2.get_biases()

        arr = [np.allclose(w, w2) for w, w2 in zip(weights1, weights2)]
        self.assertEqual(False in arr, False)

        arr = [np.allclose(b, b2) for b, b2 in zip(biases1, biases2)]    
        self.assertEqual(False in arr, False)
        # print(arr)

if __name__ == '__main__':
    unittest.main()

# """TEST ON BACKPROP METHOD"""
# sample = list_arr[0]

# delta_biases, delta_weights = net.backprop(sample[0], sample[1])

# print("weights {}".format(delta_weights))

# delta_biases, delta_weights = net.backprop(list_arr[1][0], list_arr[1][1])

# print("weights2 {}".format(delta_weights))
# print("shape {}".format(delta_weights[0].shape))
# print("type {}".format(type(delta_weights[0])))

# delta_biases, delta_weights = net.effectiv_backprop(list_arr[:2])
# print(delta_biases)
