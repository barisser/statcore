import statcore



def test_matrices():
	mat1 = statcore.Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
	assert mat1.shape == (3, 3)
	mat2 = statcore.Matrix([[10, 20, 30], [100, 200, 300], [3000, 4000, 5000]])

	mat3 = mat1 + mat2
	mat4 = mat1 * 3 + 1
	mat5 = mat1 ** 2
	mat6 = mat3 - mat2
	assert mat6 == mat1
	assert mat3[0][1] == 22
