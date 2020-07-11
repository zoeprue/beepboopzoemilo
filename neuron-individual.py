#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:40:23 2020

@author: Zoe and Milo
"""


class neuron:
    def __init__(self, nb_inputs, weights=None, bias=0): # constructor empty calls default neuron
        if weights is not None:
            self.weights = weights
        else:
            self.weights = [1 for n in range(nb_inputs)]
        self.bias = bias
        self.nb_inputs = nb_inputs
        
    def evaluate_neuron(self, inputs):
        inputs_to_weights = [weight*inp for weight, inp in zip(self.weights, inputs)]
        return sum(inputs_to_weights) - self.bias