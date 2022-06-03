import statcore
import numpy as np

def test_linear_ols():
	model = statcore.LinearRegressor()
	X = np.random.random((1000, 10))
	A = np.random.random(10)
	Y = X.dot(A)
	model.fit(X, Y)

	assert np.allclose(A, model.A)

	Y = X.dot(A) + np.random.random(1000) * 0.2
	model.fit(X, Y)
	assert np.allclose(A, model.A, atol=0.03, rtol=0.05)
