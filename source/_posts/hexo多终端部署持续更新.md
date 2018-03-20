---
title: hexo多终端部署持续更新
date: 2018-03-18 19:45:41
tags:
- Hexo
- Git
categories:
- 杂七杂八
copyright: true
---
-----------------------
{% note info %}
使用hexo+git写博客十分简便高效，然而多终端的部署问题有很多坑，本博客将持续更新在多终端部署时遇到的坑。
{% endnote %}
<!--more-->

# 基本方法

## 安装git并设置关联

什么是Git ?简单来说Git是开源的分布式版本控制系统，用于敏捷高效地处理项目。我们网站在本地搭建好了，需要使用Git同步到GitHub上。如果想要了解Git的细节，参看廖雪峰老师的Git教程：Git教程 从Git官网下载：Git - Downloading Package 现在的机子基本都是64位的，选择64位的安装包，下载后安装，在命令行里输入git测试是否安装成功，若安装失败，参看其他详细的Git安装教程。安装成功后，将你的Git与GitHub帐号绑定，鼠标右击打开Git Bash

或者在菜单里搜索Git Bash，设置user.name和user.email配置信息：
`git config --global user.name "你的GitHub用户名"`
`git config --global user.email "你的GitHub注册邮箱"`

生成ssh密钥文件：
`ssh-keygen -t rsa -C "你的GitHub注册邮箱"`

然后直接三个回车即可，默认不需要设置密码然后找到生成的.ssh的文件夹中的id_rsa.pub密钥，将内容全部复制
打开GitHub_Settings_keys 页面，新建new SSH Key

Title为标题，任意填即可，将刚刚复制的id_rsa.pub内容粘贴进去，最后点击Add SSH key。在Git Bash中检测GitHub公钥设置是否成功，输入 ssh git@github.com ：

## 安装Node.js

Hexo基于Node.js，Node.js下载地址：Download | Node.js 下载安装包，注意安装Node.js会包含环境变量及npm的安装，安装后，检测Node.js是否安装成功，在命令行中输入 node -v :

检测npm是否安装成功，在命令行中输入npm -v :

到这了，安装Hexo的环境已经全部搭建完成。

## github设置

- 在yourname.github.io仓库内创建一个新的branch，如：hexo。
- 将该分支设置为默认分支
`settings -> branch -> Default branch -> update`



## 在本地建立git仓库

> 配置.gitignore文件。进入博客目录文件夹下，找到此文件，用sublime text 打开，在最后增加两行内容/.deploy_git和/public

- 进入blog文件夹，shift+右键打开终端
- `git init` Initialized empty Git repository初始化git仓库
- `git add -A` 添加本地所有文件
- `git commit -m "blog source files"` 提交到本地仓库
- `git branch hexo` 创建本地hexo分支

## 将本地仓库与远端关联

- `git remote add origin git@github.com:yourname/yourname.github.io.git` 添加远程仓库
- `git push origin hexo -f` 将本地仓库推到远端仓库(默认为hexo分支)

## 另一终端的所有操作

> 将远程clone至本地

`git clone -b hexo git@github.com:yourname/yourname.github.io.git`

> 进入clone下来的仓库以及__next主题文件夹__下执行安装(会根据package.json安装对应的依赖)

`npm install`

> 编辑本地文件后更新远程

`git add . ,git commit -m "update info"， git push origin hexo`

> 部署发布博客

`hexo clean hexo g -d`

# 踩坑记

暂无

