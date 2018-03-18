---
title: iOS逆向工具
date: 2018-02-07 13:04:02
tags:
- Security
- tool
- iOS
categories: 
- iOS逆向
copyright: true
---
-----------------------
{% note info %}
iOS逆向常用的一些小工具
{% endnote %}
<!--more-->

## 砸壳工具dumpdecrypted的使用
- 将`~/HackTools/dumpdecrypted-master/dumpdecrypted.dyli`b拷贝到TargetApp的`Documents`目录下
- 开始砸壳
    ```cpp
    DYLD_INSERT_LIBRARIES=/path/to/dumpdecrypted.dylib /path/to/executable
    ```

## class-dump的使用
- 在Terminal中进入App所在的目录，并用Xcode自带的plutil工具查看Info.plist中的“CFBundleExecutable”字段：
    ```
    plutil -p Info.plist | grep CFBundleExecutable
    ```
- 将头文件dump到指定文件夹下,且内容按名字排序
    ```
    class-dump -S -s -H 可执行文件 -o 文件夹
    ```