---
title: lldb+debugserver速查表
date: 2018-02-07 11:59:48
tags: 
- Security
- tool
- iOS
categories: 
- iOS逆向
copyright: true
---
--------------
{% note info %}
lldb+debugserver是iOS逆向的一个重要的工具，用于动态调试，包括寻找有用api、寻找有用信息等等，结合IDA构成iOS逆向的大半江山。以下是我的速查表。
{% endnote %}
<!--more-->
>   #### 一、准备阶段


- #### iPhone端开启监听
```
debugserver 192.168.3.242:8888 -a "SpringBoard"

debugserver -x backboard 192.168.3.242:8888 /Applications/AppStore.app/AppStore
```
- #### lldb连接iPhone
```    
process connect connect://192.168.3.235:8888
```
- #### cycript连接
```
ps -e | grep /Applications(位置)查看当前可执行程序

cycript -p 可执行程序
```

-------
>   #### 二、寻找思路

- #### 列出当前镜像
```
image list -o -f
```
- #### 列出调用栈信息
```
thread backtrace

bt [all]

sbt
```
- #### 找到view对应的controller
```
首先找到view界面的地址（easy），通过调用
[#0x17f92890 nextResponder]找到controller的名字
通过lldb po [controller名 _ivarDescription]和[controller名 _shortMethodDescription]
看方法和属性
对方法和属性所在内存下断点
读取寄存器信息，获取寄存器存放的对象
```

- #### 下断点(通过help br查看)
```
b function

br s -a address

br s -a ASLR+offset

......
```
- #### 调试下一步
```
br l（断点列表）

br dis 序号（不加为全）

br en 序号

br del 序号

c(下一个断点)

s   源码级别单步执行，遇到子函数则进入

si  单步执行，遇到子函数则进入

n 源码级别单步执行，遇到子函数不进入，直接步过

ni 单步执行，遇到子函数不进入，直接步过

finish/f  退出子函数

br com add 序号
（执行这条命令后，LLDB会要求我们设置一系列
指令，以“DONE”结束，）
```
- #### 寄存器
```
reg r -a/-A...

register read -a/-A...

register write 寄存器 值 （将寄存器赋值）reg w

```

- #### 关于打印
```

po或p $寄存器        （打印寄存器的值）

po [$寄存器 或类名  _shortMethodDescription]

po [$寄存器 或类名  _ivarDescription]
然后通过cycript进行调用，或者lldb本身可以调用：
po [$寄存器 或类名 method]

po [view subviews]

po [view superviews]

po [$r0（寄存器、地址） detailTextLabel]

po [$r2 propertyForKey:@"set"]拿到setter方法

po [$r2 propertyForKey:@"get"]拿到getter方法

po[$r2 allTargets]拿到调用者，用于写在函数前面
拿到了调用者也相当于拿到了类，可以用method或class-dump定位方法和属性，用ida定位方法，进入方法内部作进一步分析，结合lldb再做断点调试，看寄存器的method，看target和寄存器存放的形参。

po [button allControlEvents]拿到部分形参

[button actionsForTarget:#0x14609d00
forControlEvent:64]
```



> 通过help ..查看详细



>   “函数的前4个参数存放在R0到R3中，其他参数
存放在栈中；返回值放在R0中。”


> ```
> debugserver -x backboard 192.168.3.183:8888 /var/containers/Bundle/Application/A910BD37-4684-49A6-97A7-924891F98D90/WYParking.app/WYParking
> ```