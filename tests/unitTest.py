from network import Network
import mnist_loader

print("coucou")


net = Network([784, 100, 10])

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()

sample = list(training_data)[0]

print("here")
# print(sample)

delta_biases, delta_weights = net.backprop(sample[0], sample[1])

print("weights {}".format(delta_weights))


#backprop: use ".transpose()" to do the calculus: so it mulitplies all biases with the corresponding previous delta to get the new delta



# print("biases {}".format(delta_biases))