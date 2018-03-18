---
title: cuckoo沙箱问题列表
date: 2018-01-10 20:07:00
tags: 
- cuckoo
- Python
- Security
categories:
- PC应用检测
copyright: true
password: 666
---
-------------
## 前言
{% note info %} cuckoo sandbox是近年来一款非常好的动态检测开源工具，然而最新版本不支持py3，对中文不友好等问题凸显，以下是使用cuckoo沙箱遇到的问题汇总 {% endnote %}
<!--more-->
## 解决中文适配问题
- 如下文件需指定编码 : `#coding:utf-8`
    - `.cuckoo->analyzer->windows->analyzer.py`
    - `.cuckoo->analyzer->windows->lib->common->abstracts.py`
    - `.cuckoo->analyzer->windows->mudules->auxilary->[all]`
    - `.cuckoo->analyzer->windows->modules->packages->[all]`
    - 其他涉及打印、日志、执行包含中文路径文件
- 如下文件修改：
    -  `.cuckoo->analyzer->windows->lib->common->abstracts.py`中 `path = path.decode('utf-8')`
    -  `.cuckoo->analyzer->windows->mudules->auxilary->human.py`中指定需要识别中文
    - 其他涉及打印、日志、执行包含中文路径文件中中文字符串
- `sudo cuckoo submit --package sp -o path="C://Program Files//Notepad加加//notepad++.exe" test.bat `
## 其他
- mongodb在重启后，需要重新建立启动文件夹
    
    - sudo rm -rf /data
    - sudo mkdir -p /data/db
    - sudo mongod
    - (另一终端)sudo mongo