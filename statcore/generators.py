import random as stdrandom

from .tensor import Tensor


def nested_lists_from_shape(shape):
	if len(shape) == 1:
		return [0] * shape[0]
	else:
		return [nested_lists_from_shape(shape[1:])] * shape[0]

def zeros(shape):
	return Tensor(nested_lists_from_shape(shape))

def random(shape):
	tensor = zeros(shape)
	for k in tensor.all_coords():
		tensor[k]= stdrandom.random()
	return tensor
