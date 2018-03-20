---
title: App场景分析与建模识别方法
date: 2018-03-20 16:31:51
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
提取出APP的UI信息，如控件的名字、坐标、尺寸、类名、内存，以及控件的树状层级关系，寻找方法通过这些UI信息得到APP当前的场景和动作，建立模型，输入为UIInfo(e.g.[[UIApp keyWindow] recursiveDescription])，输出为APPScene(e.g.发送搜索请求)。
{% endnote %}
<!--more-->
# 前言

提取出APP的UI信息，如控件的名字、坐标、尺寸、类名、内存，以及控件的树状层级关系，寻找方法通过这些UI信息得到APP当前的场景和动作，建立模型，输入为UIInfo(e.g.[[UIApp keyWindow] recursiveDescription])，输出为APPScene(e.g.发送搜索请求)。

app场景识别 App scene recognition
基于文本的app场景识别 Text-based App scene recognition

# 场景识别(机器学习)

## 介绍

[计算机视觉和场景识别的前世今生](http://www.donews.com/idonews/article/6446.shtm)

[场景识别论文阅读感想（初步）](http://blog.csdn.net/qq_35395045/article/details/77618836)

[MIT Scene Recognition Demo识别图片是在室内还是室外](http://places.csail.mit.edu/demo.html)

## 参考文献

[面向事件关系检测的特征分析与场景推理方法研究](http://xueshu.baidu.com.cn/s?wd=paperuri%3A%2830bcbd311c2a49113338f6b4ce03b067%29&filter=sc_long_sign&sc_ks_para=q%3D%E9%9D%A2%E5%90%91%E4%BA%8B%E4%BB%B6%E5%85%B3%E7%B3%BB%E6%A3%80%E6%B5%8B%E7%9A%84%E7%89%B9%E5%BE%81%E5%88%86%E6%9E%90%E4%B8%8E%E5%9C%BA%E6%99%AF%E6%8E%A8%E7%90%86%E6%96%B9%E6%B3%95%E7%A0%94%E7%A9%B6&sc_us=9160209492333156453&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8)

[Multi-spectral SIFT for scene category recognition](http://xueshu.baidu.com.cn/s?wd=paperuri%3A%282c3436e553512e233b7ca1ce1abca471%29&filter=sc_long_sign&sc_ks_para=q%3DMulti-spectral%20SIFT%20for%20scene%20category%20recognition&sc_us=11192796055788375713&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8)

[Convolutional Network Features for Scene Recognition](http://xueshu.baidu.com.cn/s?wd=paperuri%3A%28dabb94ad8359f7f82fd45dd96ee00d72%29&filter=sc_long_sign&sc_ks_para=q%3DConvolutional%20Network%20Features%20for%20Scene%20Recognition&sc_us=7184478976350537527&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8)

[SUN database: Large-scale scene recognition from abbey to zoo](http://xueshu.baidu.com.cn/s?wd=paperuri%3A%28ce62e8cc4b394c2361ff1bde7962f4fa%29&filter=sc_long_sign&sc_ks_para=q%3DSUN%20database%3A%20Large-scale%20scene%20recognition%20from%20abbey%20to%20zoo&sc_us=8683530613023129470&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8)

[Learning deep features for scene recognition using places database](http://xueshu.baidu.com.cn/s?wd=paperuri%3A%2811ca23fe4e8823cc24984d40393ee3fa%29&filter=sc_long_sign&sc_ks_para=q%3DLearning%20deep%20features%20for%20scene%20recognition%20using%20places%20database&sc_us=10700903575524642872&tn=SE_baiduxueshu_c1gjeupa&ie=utf-8)

[Scene Recognition with CNNs: Objects, Scales and Dataset Bias](http://xueshu.baidu.com.cn/s?wd=Scene+recognition+with+CNNs%3A+objects%2C+scales+and+dataset+bias&tn=SE_baiduxueshu_c1gjeupa&cl=3&ie=utf-8&bs=scene+recognition&f=8&rsv_bp=1&rsv_sug2=1&sc_f_para=sc_tasktype%3D%7BfirstSimpleSearch%7D&rsv_n=2)

[机器学习和深度学习引用量最高的20篇论文（2014-2017）](https://www.chainnews.com/articles/947306427039.htm)
