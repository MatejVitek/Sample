import utils.do_stuff


class A:
	def __init__(self, val):
		self.val = 2 * val


class B:
	def __init__(self, val):
		self.val = val


if __name__ == '__main__':
	print(utils.do_stuff(A(1).val) == B(2).val)
