模块 -- 一个个.py文件
	使用模块: import sys
	安装第三方模块： pip install Pillow
	pip： python包管理工具，提供对python包的查找、下载、安装、卸载
	
面向对象编程
	数据封装、继承和多态是面向对象的三大特点
	1。 类和实例
	类是抽象的模板，实例是根据类创建出来的一个个具体的对象
	定义类关键字:class
	创建实例：类名+() eg： bart=Student()
	可以自由的给一个实例变量邦定属性，eg： bart.name="Bob"
	把必须绑定的属性强制写进去用特殊方法__init__, __init__方法的第一个参数必须是self，表示创建实例的本身
	
	数据封装
	在类内部定义访问数据的函数，这些封装数据的函数，我们称之为类的方法
	要定义一个方法，除了第一个参数是self外，其他和普通函数一样
	
	小结
	类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
	方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
	通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
	和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同
	
	2。 访问限制
	如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__；不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量，强烈建议不要这么干
	在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
	有些时候，会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
	
	3。 继承和多态
	继承好处:最大的好处是子类获得了父类的全部功能；多态
	多态“开闭原则”：对扩展开放：允许新增Animal子类； 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
	静态语言 vs 动态语言：
	对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
	对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
	
	小结
	继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
	动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
	
	4。 获取对象信息
	判断对象类型： type()  //type(123)
	判断class的类型: isinstance()  //isinstance(d, Dog)
	获得一个对象的所有属性和方法: dir()  //dir('ABC')
	直接操作一个对象的状态:  getattr()、setattr()、hasattr()  //hasattr(obj, 'x') # 有属性'x'吗？
	
	5。 实例属性和类属性
	由于Python是动态语言，根据类创建的实例可以任意绑定属性；给实例绑定属性的方法是通过实例变量，或者通过self变量
	Student类本身需要绑定一个属性，可以直接在class中定义属性，这种属性是类属性，归Student类所有
	/*class Student(object):
		name = 'Student'  */
	del s.name # 如果删除实例的name属性
	
面向对象高级编程
	高级特性包括多重继承、定制类、元类等概念
	1。 使用__slots____
	正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
	//s.name = 'Michael' # 动态给实例绑定一个属性
	//s.set_age = MethodType(set_age, s) # 给实例绑定一个方法,只是s这个实例可以使用set_age这个方法
	//Student.set_score = set_score//class绑定方法后，所有实例均可调用
	
	限制实例的属性： 特殊的__slots__变量  //只允许对Student实例添加name和age属性  __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
	__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
	
	2。 使用@property
	@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性
	Python内置的@property装饰器就是负责把一个方法变成属性调用的
	使用: 把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
	
	3. 多重继承
	继承是面向对象编程的一个重要的方式，因为通过继承，子类就可以扩展父类的功能
	多重继承，一个子类就可以同时获得多个父类的所有功能
	MixIn设计: 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
	//class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
	
	小结
	由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
	只允许单一继承的语言（如Java）不能使用MixIn的设计。
	
	4。定制类
	看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的
	Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类
	__str__， __repr__ ： __str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
	__iter__： 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
	__getitem__： 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
	__getattr__： 除了__init__可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性
	__call__： 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
	
	5。 枚举类
	Enum类： 枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例
	#from enum import Enum
	#Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
	
	6。 元类
	type()： type()函数可以查看一个类型或变量的类型，type()函数既可以返回一个对象的类型，又可以创建出新的类型
	通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class
	metaclass： 直译为元类， 当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例

错误调试和测试
	1。 错误处理
	try...except...finally...的错误处理机制
	当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕
	抛出错误： 用raise语句抛出一个错误的实例
	
	2。 调试
	print： 第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看
	
	assert： 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
	#assert n != 0, 'n is zero!'    assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错
	
	logging： 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件
	
	pdb： Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态
	#python -m pdb err.py
	#输入命令l来查看代码；输入命令n可以单步执行代码；任何时候都可以输入命令p 变量名来查看变量；输入命令q结束调试，退出程序
	
	pdb.set_trace()： 我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点
	#可以用命令p查看变量，或者用命令c继续运行
	IDE： 如果要比较爽地设置断点、单步执行，就需要一个支持调试功能的IDE。Visual Studio Code， PyCharm
	
	小结
	写程序最痛苦的事情莫过于调试，程序往往会以你意想不到的流程来运行，你期待执行的语句其实根本没有执行，这时候，就需要调试了。
	虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。
	
	3。 单元测试
	单元测试： 是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作
	setUp与tearDown： 这两个方法会分别在每调用一个测试方法的前后分别被执行
	
	4。 文档测试
	
IO编程
	1。 文件读写
	读文件： open()，read()，close()
	#f = open('/Users/michael/test.txt', 'r')
	#f.read()。调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
	#另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
	#f.close()
	with 结构： 和try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法
	#with open('/path/to/file', 'r') as f:
    #	print(f.read())
	写文件： open()，write()，close()
	#f = open('/Users/michael/test.txt', 'w')  以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入
	#f.write('Hello, world!')
	#f.close()
	with 结构： 
	#with open('/Users/michael/test.txt', 'w') as f:
    #	f.write('Hello, world!')
	
	2： StringIO和BytesIO
	StringIO： 顾名思义就是在内存中读写str
	写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入
	getvalue()方法用于获得写入后的str
	要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取
	
	BytesIO： StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO
	
	3。 操作文件和目录
	os: Python内置的os模块也可以直接调用操作系统提供的接口函数
	#os.name # 操作系统类型 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
	#os.uname() 详细的系统信息
	
	操作文件和目录： 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
	#os.path.abspath('.')   查看当前目录的绝对路径:
	#os.path.join('/Users/michael', 'testdir')  在某个目录下创建一个新目录，首先把新目录的完整路径表示出来
	#os.mkdir('/Users/michael/testdir')  然后创建一个目录:
	#os.rmdir('/Users/michael/testdir')  删掉一个目录
	#os.path.split('/Users/michael/testdir/file.txt')  把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
	复制文件的函数居然在os模块中不存在，原因是复制文件并非由操作系统提供的系统调用
	幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充
	
	4。 序列化
	我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等
	序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上
	反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling
	pickle模块： 
	存储在变量中: pickle.dumps(dic)
	#dic = {'age': 23, 'job': 'student'}
	#byte_data = pickle.dumps(dic)   //dumps(): 把序列化对象储存在变量中
	#obj = pickle.loads(byte_data)   //loads(): 读取数据
	#print(obj)
	存储在文件中: pickle.dump(dic, f)
	#with open('abc.pkl', 'wb') as f:
    #	dic = {'age': 23, 'job': 'student'}
    #pickle.dump(dic, f)    //dump(): 把序列化对象储存在文件中
	#with open('abc.pkl', 'rb') as f:
    #	aa = pickle.load(f)    //loads(): 读取数据
    #	print(aa)
	JSON： 要把序列化搞得更通用、更符合Web标准
	Python3 中可以使用 json 模块来对 JSON 数据进行编解码
    json.dumps(): 对数据进行编码。
    json.loads(): 对数据进行解码。
	#d = dict(name='Bob', age=20, score=88)
	#json.dumps(d)  对数据进行编码成{}
	#json_str = '{"age": 20, "score": 88, "name": "Bob"}'
	#json.loads(json_str)  对数据进行解码成dict
	
进程和线程
	线程是最小的执行单元，而进程由至少一个线程组成。如何调度进程和线程，完全由操作系统决定，程序自己不能决定什么时候执行，执行多长时间。
	多进程和多线程的程序涉及到同步、数据共享的问题，编写起来更复杂
	1。 多进程
	os模块: os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程
	子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID
	
	multiprocessing模块： 就是跨平台版本的多进程模块
	from multiprocessing import Process
	import os
	def run_proc(name):
		print('Run child process %s (%s)...' % (name, os.getpid()))
	if __name__=='__main__':
		print('Parent process %s.' % os.getpid())
		p = Process(target=run_proc, args=('test',))
		print('Child process will start.')
		p.start()
		p.join()
		print('Child process end.')
	创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
	join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
	
	Pool： 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
	对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
	请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行
	Pool的默认大小是CPU的核数
	
	子进程
	很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出
	subprocess模块： 可以让我们非常方便地启动一个子进程，然后控制其输入和输出
	import subprocess
	print('$ nslookup www.python.org')
	r = subprocess.call(['nslookup', 'www.python.org'])
	print('Exit code:', r)
	如果子进程还需要输入，则可以通过communicate()方法输入
	import subprocess
	print('$ nslookup')
	p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
	print(output.decode('utf-8'))
	print('Exit code:', p.returncode)
	
	进程间通信
	Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据
	Pipes:　单向，一段输入，另一端输出，先进先出FIFO。管道也是文件。管道大小4096字节。实际上，管道是一个固定大小的缓冲区
	Queue：　消息队列是先进先出FIFO原则
	
	2。 多线程
	线程是操作系统直接支持的执行单元，　进程是由若干线程组成的，一个进程至少有一个线程
	Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
	由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，它永远返回当前线程的实例
	
	Lock
	多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改。
	因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了
	由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突
	threading.Lock()： 创建一个锁
	balance = 0
	lock = threading.Lock()
	def run_thread(n):
		for i in range(100000):
			# 先要获取锁:
			lock.acquire()
			try:
				# 放心地改吧:
				change_it(n)
			finally:
				# 改完了一定要释放锁:
				lock.release()
	好处： 确保了某段关键代码只能由一个线程从头到尾完整地执行
	缺点： 首先是阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了
		 其次，由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止
	
	多核CPU
	启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。
	但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，4核就跑到400%，8核就跑到800%
	解释器执行代码时，有一个GIL锁
	这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核
	Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响
	
	小结
	多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
	Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。
	
	ThreadLocal
	一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题
	
	3。 进程 vs. 线程
	多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）著名的Apache最早就是采用多进程模式
	多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用fork调用还行，在Windows下创建进程开销巨大。另外，操作系统能同时运行的进程数也是有限的，在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题
	多线程模式通常比多进程快一点，但是也快不到哪去，而且，多线程模式致命的缺点就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存
	
	线程切换： 多任务一旦多到一个限度，就会消耗掉系统所有的资源，结果效率急剧下降，所有任务都做不好
	
	计算密集型 vs. IO密集型
	计算密集型任务的特点是要进行大量的计算，消耗CPU资源，比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力。这种计算密集型任务虽然也可以用多任务完成，但是任务越多，花在任务切换的时间就越多，CPU执行任务的效率就越低，所以，要最高效地利用CPU，计算密集型任务同时进行的数量应当等于CPU的核心数
	计算密集型任务由于主要消耗CPU资源，因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写
	第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成（因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用
	IO密集型任务执行期间，99%的时间都花在IO上，花在CPU上的时间很少。对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差。
	
	异步IO
	对应到Python语言，单线程的异步编程模型称为协程，有了协程的支持，就可以基于事件驱动编写高效的多任务程序
	
	5。 分布式进程
	在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上
	Python的分布式进程接口简单，封装良好，适合需要把繁重任务分布到多台机器的环境下。
	注意Queue的作用是用来传递任务和接收结果，每个任务的描述数据量要尽量小。比如发送一个处理日志文件的任务，就不要发送几百兆的日志文件本身，而是发送日志文件存放的完整路径，由Worker进程再去共享的磁盘上读取文件。
	
正则表达式
	1。 re模块
	Python提供re模块，包含所有正则表达式的功能
	re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
	match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None。 常用于密码判断
	
	2。 切分字符串
	用固定的字符： 'a b   c'.split(' ')
	用正则表达式： re.split(r'\s+', 'a b   c')
	
	3。 分组
	除了简单地判断是否匹配之外，正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
	
	4。 贪婪匹配
	正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符。
	>>> re.match(r'^(\d+)(0*)$', '102300').groups()
	('102300', '')
	加个?就可以让\d+采用非贪婪匹配
	>>> re.match(r'^(\d+?)(0*)$', '102300').groups()
	('1023', '00')
	
	
	
	
	
	
	
	
	
	