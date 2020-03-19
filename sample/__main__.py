from utils import do_stuff
import package1.foo
from package2 import bar
import package2.subpackage.baz as baz


b = baz.B(bar.VAL)
if do_stuff(b.val) > 10:
	print(package1.foo.prefix(b.val))
else:
	print(package1.foo.prefix(-b.val))
