# 1. 简介
> subprocess模块主要用于创建子进程，并连接它们的输入、输出和错误管道，获取它们的返回状态。
>
> 通俗地说就是通过这个模块，你可以在Python的代码里执行操作系统级别的命令，比如“ipconfig”、“du -sh”等等。

subprocess模块替代了一些老的模块和函数，比如: 

+ os.system   
+ os.spawn*   

> subprocess过去版本中的***call()，check_call()***和***check_output()***已经被***run()***方法取代了。**run()**方法为3.5版本新增。

大多数情况下，推荐使用***run()***方法调用子进程，执行操作系统命令。

在更高级的使用场景，你还可以使用***Popen***接口。其实***run()***方法在底层调用的就是***Popen***接口。

# 2. 使用说明
```python
subprocess.run(args, *, 
               stdin=None, 
               input=None, 
               stdout=None, 
               stderr=None, 
               shell=False, 
               timeout=None, 
               check=False, 
               encoding=None,
               errors=None)
```

功能：执行args参数所表示的命令，等待命令结束，并返回一个***CompletedProcess***类型对象。

## 2.1 各参数说明

1. <u>**args**</u>：表示要执行的命令。必须是一个字符串，字符串参数列表。   
2. stdin、stdout和stderr：子进程的标准输入、输出和错误。其值可以是*subprocess.PIPE、subprocess.DEVNULL、一个已经存在的文件描述符、已经打开的文件对象或者None*。*subprocess.PIPE *表示为子进程创建新的管道。*subprocess.DEVNULL* 表示使用os.devnull。默认使用的是None，表示什么都不做。另外，stderr可以合并到stdout里一起输出。   
3. <u>**timeout**</u>：设置命令超时时间。如果命令执行时间超时，子进程将被杀死，并弹出TimeoutExpired异常。   
4. check：如果该参数设置为True，并且进程退出状态码不是0，则弹出CalledProcessError异常。   
5. <u>**encoding**</u>:如果指定了该参数，则stdin、stdout和stderr可以接收字符串数据，并以该编码方式编码。否则只接收bytes类型的数据。   
6. <u>**shell**</u>：如果该参数为True，将通过操作系统的shell执行指定的命令。   

## 2.2 CompletedProcess类

***run()***方法的返回值，表示一个进程结束了。`CompletedProcess`类有下面这些属性：

- args 启动进程的参数，通常是个列表或字符串。
- returncode 进程结束状态返回码。0表示成功状态。
- stdout 获取子进程的stdout。通常为bytes类型序列，None表示没有捕获值。如果你在调用run()方法时，设置了参数`stderr=subprocess.STDOUT`，则错误信息会和stdout一起输出，此时stderr的值是None。
- stderr 获取子进程的错误信息。通常为bytes类型序列，None表示没有捕获值。
- check_returncode() 用于检查返回码。如果返回状态码不为零，弹出`CalledProcessError`异常。

**subprocess.DEVNULL**

一个特殊值，用于传递给stdout、stdin和stderr参数。表示使用`os.devnull`作为参数值。

**subprocess.PIPE**

管道，可传递给stdout、stdin和stderr参数。

**subprocess.STDOUT**

特殊值，可传递给stderr参数，表示stdout和stderr合并输出。

## args与shell参数   

Linux中，当args是个字符串是，请设置shell=True，当args是个列表的时候，shell保持默认的False。

# 3. 获取执行结果    

# 4. 交互式输入

