---
title: Mac系统10.11之后/usr/bin 拷贝权限禁止解决方案
date: 2018-02-07 12:11:56
tags:
- tips
- unix
categories: 
- Mac
copyright: true
---
------------
{% note info %}
Mac系统10.11之后/usr/bin 拷贝权限是禁止的，此时自定义的基础功能二进制文件使用困难，以下是比较好的解决方案，亲测有效！
{% endnote %}
<!--more-->

### Mac系统10.11之后/usr/bin 拷贝权限禁止解决方案
---------
- Step1：
在当前用户根目录下创建一个bin目录；
    - 命令：`mkdir ~/bin`
    
    
- Step2：
把要拷贝 **实现基础功能的二进制** 如`class-dump`给拷贝到这个目录里，并赋予其可执行权限;
    - 命令一: `sudo cp /.../class-dump ~/bin`    
       (/.../class-dump是指的class-dump的完整路径)
 
    - 命令二: `chmod +x ~/bin/class-dump`
        
        
- Step3：打开~/.bash_profile文件，配置环境变量
    - 命令一: `vi ~/.bash_profile`
    - 命令二: 按 `i` 键进入编辑模式，写入下面一行代码， `export PATH=$HOME/bin/:$PATH`    按ESC然后输入冒号(shift+;),然后输入`wq`,退出即可。

- Step4：在Terminal中执行source命令(每次开机后都要重新source)
    - 命令:`source ~/.bash_profile`
完成以上步骤，在terminal中执行class-dump实验一下，应该就可以了。


- ### 其他方案：修改系统权限
    - 关闭 Rootless。重启按住 `Command+R`，进入恢复模式，打开Terminal。

        `csrutil disable`

        重启即可。如果要恢复默认，那么

        `csrutil enable`

    - 附录:
    
        csrutil命令参数格式：
    
            csrutil enable [--without kext | fs | debug | dtrace | nvram][--no-internal]
    
        禁用：`csrutil disable`
    
        （等同于`csrutil enable --without kext --without fs --without debug --without dtrace --without nvram`）
        
        其中各个开关，意义如下：
    
        `B0: [kext]` 
        
        允许加载不受信任的kext（与已被废除的kext-dev-mode=1等效）
        
        `B1: [fs]` 解锁文件系统限制
        
        `B2: [debug]` 允许task_for_pid()调用
        B3: [n/a] 允许内核调试 （官方的csrutil工具无法设置此位）
        
        `B4: [internal]` Apple内部保留位（csrutil默认会设置此位，实际不会起作用。设置与否均可）
        
        `B5: [dtrace]` 解锁dtrace限制
        
        `B6: [nvram]`
        解锁NVRAM限制
        
        `B7: [n/a]`
        允许设备配置（新增，具体作用暂时未确定）
