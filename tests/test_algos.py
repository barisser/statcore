import numpy as np

import statcore


def test_kmeans_simple():
	ar = np.random.randint(0, 10, size=(1000, 10)) + 200
	ar2 = np.random.randint(0, 30, size=(500, 10)) - 300
	ar3 = np.concatenate((ar, ar2))

	model = statcore.KMeans(2)
	model.fit(ar3)
	assert np.allclose([*model.centroids.values()][0], np.zeros(10)-285, atol=1.0,rtol=0.01) or np.allclose([*model.centroids.values()][1], np.zeros(10)-285, atol=1.0,rtol=0.01)
	assert np.allclose([*model.centroids.values()][0], np.zeros(10)+205, atol=1.0,rtol=0.01) or np.allclose([*model.centroids.values()][1], np.zeros(10)+205, atol=1.0,rtol=0.01)

	p1 = model.predict(ar)
	p2 = model.predict(ar2)
	assert all([p1[i] != p2[i] for i in range(500)])


def test_kmeans_complex():
	ar = np.random.randint(0, 20, size=(1000, 20, 30)) + 20
	model = statcore.KMeans(4)
	model.fit(ar, n=5)
	resp = model.predict(ar)
	assert len(resp) == 1000
	assert max(resp) == 3
	assert min(resp) == 0
