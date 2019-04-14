#协程
    -实现协程比较好的包有asyncio,tornado,gevent
    -定义：协程 是为非抢占式多任务产生子程序的计算机程序组件，协程允许不同入口点在不同位置暂停或开始执行程序”。
    -从技术角度讲，协程就是一个你可以暂停执行的函数，
    -实现
        -yield返回
        -send调用
    #协程的四个状态

    inspect.getgeneratorstate(…) 函数确定，该函数会返回下述字符串中的一个：
    GEN_CREATED：等待开始执行
    GEN_RUNNING：解释器正在执行
    GEN_SUSPENED：在yield表达式处暂停
    GEN_CLOSED：执行结束
    next预激（prime)
    代码案例v2
    协程终止

    -协程中未处理的异常会向上冒泡，传给 next 函数或 send 方法的调用方（即触发协程的对象）
    -止协程的一种方式：发送某个哨符值，让协程退出。内置的 None 和Ellipsis 等常量经常用作哨符值==。
    #yield from

    调用协程为了得到返回值，协程必须正常终止
    生成器正常终止会发出StopIteration异常，异常对象的vlaue属性保存返回值
    yield from从内部捕获StopIteration异常
    案例v03
    #委派生成器
    包含yield from表达式的生成器函数
    委派生成器在yield from表达式出暂停，调用方可以直接把数据发给子生成器
    子生成器在把产出的值发给调用方
    子生成器在最后，解释器会抛出StopIteration，并且把返回值附加到异常对象上
    案例v04
#可迭代(Iterable):直接作用于for循环的变量
-迭代器(Iterator):不但可以作用于for循环，还可以被next调用
-list是典型的可迭代对象，但不是迭代器
-通过isinstance判断
-iterable和iterator可以转换
-通过iter函数
#生成器
-generator:一边循环一边计算下一个元素的机制/算法
-需要满足三个条件：
    -每次调用都生产出for循环需要的下一个元素或者
    -如果打到最后一个，爆出stopinteration异常
    -可以被next函数调用
-如何升成一个生成器
-直接使用
-如果函数中包含yield,则这个函数就叫生成器
    -next调用函数，遇到yield返回

#asyncio
    -python3.4开始引入的标准库,内置了对移步io的支持
    -asyncio本身是一个消息循环,
    -步骤
    -创建消息循环
    -把协程导入
    -关闭
    -案例08
    -案例09-两个tasks
    -案例v10-得到多个网站
#async and await
    -为了更好的表示异步io
    -python3.5引入
    -使用上，可以简单的进行替换
        -用async替换@asyncio.coroutine
        -await替换yield from
#aiohttp
-asyncio实现单线程的并发io，在客户端用户不大
-在服务器端可以asyncio+coroutine配合，因为http是io操作
-asyncio实现了tcp、udp、ssl等协议
-aiohttp是给与asyncio实现的http框架
-pip install aiohttp
        
#concurrent.futures
-python3新增的库
-类似其他语言的线程池
-此模块利用multiprocessiong实现真正的平行计算

-核心原理是：concurrent.futures会以子进程的形式，平行的运行多个python解释器，从而令python程序可以利用多核CPU来提升执行速度。 由于子进程与主解释器相分离，所以他们的全局解释器锁也是相互独立的。每个子进程都能够完整的使用一个CPU内核。

--concurrent.futures.Executor

-ThreadPoolExecutor
-ProcessPoolExecutor
-submit(fn, args, kwargs)

fn:异步执行的函数

args,kwargs:参数

   # 官方死锁案例
  import time
  def wait_on_b():
      time.sleep(5)
      print(b.result())  #b不会完成，他一直在等待a的return结果
      return 5

  def wait_on_a():
      time.sleep(5)
      print(a.result())  #同理a也不会完成，他也是在等待b的结果
      return 6


  executor = ThreadPoolExecutor(max_workers=2)
  a = executor.submit(wait_on_b)
  b = executor.submit(wait_on_a)
  
#map(fn, *iterables, timeout=None)

跟map函数类似

函数需要异步执行

timeout: 超时时间

起执行结果是list,数据需要从list中取出来

  with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
      print(list(executor.map(sleeper, x)))
submit和map根据需要选一个即可
#Future

未来需要完成的任务
future 实例由Excutor.submit创建