import statcore


def test_linear_ols():
	model = statcore.LinearRegressor()
	X = statcore.random((1000, 4))
	A = statcore.random((4,))
	Y = X.dot(A) + statcore.random((1000,)) * 0.1
	import pdb;pdb.set_trace()