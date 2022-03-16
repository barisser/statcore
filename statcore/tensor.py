import copy
import itertools

def get_shape_from_lists(data):
	shape = []

	size = len(data)
	shape.append(size)

	while True:
		if not data:
			break
		if isinstance(data[0], int) or isinstance(data[0], float):
			break
		else:
			if not all([isinstance(x, list) for x in data]):
				raise ValueError("all elements must be a list")
			sizes = [len(x) for x in data]
			if not len(set(sizes)) == 1:
				raise ValueError("All entries must be the same length.")
			shape.append(len(data[0]))
			data = data[0] # we are not doing multi-level checks to determine if sizes are consistent
			# above should be fixed eventually.  Current check only goes to depth=1.
	return tuple(shape)

def get_shape_from_keys(keys):
	dims = len(next(iter(keys)))
	shape = [0] * dims
	for k in keys:
		for i in range(len(k)):
			shape[i] = max(shape[i], k[i] + 1)
	return tuple(shape)


def nested_list_lookup(llist, coords):
	if len(coords) == 1:
		return llist[coords[0]]
	return nested_list_lookup(llist[coords[0]], coords[1:])


class Tensor(object):
	def __init__(self, values=None):
		if not isinstance(values, list):
			raise ValueError("Values must be a list")

		if values is None:
			values = []
		self.shape = get_shape_from_lists(values)
		self.values = values
#		self.values_map = tensor_list_to_dict(values, self.shape)

	def check_shape_with_other(self, other):
		if not self.shape == other.shape:
			raise ValueError("Shapes of tensors aren't equal: {} vs {}".format(
				self.shape, other.shape))

	def all_coords(self): # todo make this return an iterable
		coord_count = 1
		for x in self.shape:
			coord_count *= x

		coords = []
		dims = len(self.shape) # number of dimensions
		for i in range(coord_count):
			# convert the integer to a coord in the space
			coord = []
			j = copy.copy(i)
			for dim_size in self.shape:
				if dim_size == 0:
					break
				coord.append(int(j%dim_size))
				j -= j%dim_size
				j /= dim_size

			coords.append(tuple(coord))
		return coords

	def __add__(self, other):
		"""Add to another tensor or scalar value"""
		if isinstance(other, Tensor):
			self.check_shape_with_other(other)
			newtensor = copy.deepcopy(self)
			for k in self.all_coords():
				newtensor[k] = v1 + other[k]
		elif isinstance(other, int) or isinstance(other, float):
			for k in self.all_coords():
				self[k] = other + self[k]
		return newtensor

	def __radd__(self, other):
		return self + other

	def __getitem__(self, k):
		if isinstance(k, int):
			return self.values[k]
		elif isinstance(k, tuple):
			return nested_list_lookup(self.values, k)

#	def __setitem__(self, k, v):
#		if len(k) == len(self.shape):
