import utils
from package2.baz import A


if __name__ == '__main__':
	for a in range(10):
		assert utils.do_stuff(a) == a
	assert A(10).val == 20
