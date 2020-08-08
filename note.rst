from: |  http://neuralnetworksanddeeplearning.com/chap1.html

execute:

.. code-block:: bash
 
 > python3 #python prompt

.. code-block:: python

 import mnist_loader
 import network
 
 training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
 

 net = network.Network([784, 30, 10])
 #net = network.Network([784, 30, 10], True) to use the minibatch computation improvement
 net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
