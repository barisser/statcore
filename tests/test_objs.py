import statcore



def test_array():
	ar = statcore.Array([1,4,6])
	assert len(ar) == 3
	assert ar == ar
	ar2 = statcore.Array([7,8,9])
	assert ar + ar2 == statcore.Array([8, 12, 15])
	assert ar2 - ar == statcore.Array([6, 4, 3])
	assert ar * ar2 == statcore.Array([7, 32, 54])
	assert ar2 / ar == statcore.Array([7, 2, 1.5])
	assert ar2 % ar == statcore.Array([0, 0, 3])
#	import pdb;pdb.set_trace()