from neuron_individual import Neuron

my_neuron = Neuron(nb_inputs=3, weights=[3, -5, 2], bias=3.1415926)

print(my_neuron.evaluate_neuron([47, 12, 42]))
