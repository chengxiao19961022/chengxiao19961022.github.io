---
title: 字符串的模式匹配-BF和KMP算法
date: 2018-03-20 12:08:05
tags:
- C++
- algorithm
categories:
- 数据结构与算法
copyright: true
---
-----------------------
{% note info %}
母串匹配子串的常用算法，定义Tag为主串，Ptn为子串（模式串），如果在主串Tag的第pos个位置后存在与子串Ptn相同的子串，返回它在主串Tag中第pos个字符后第一次出现的位置，否则返回-1。BF算法为暴力回溯求解算法，KMP算法相对优化。
{% endnote %}
<!--more-->

# BF算法

## 思路

定义两个索引值i和j分别为Tag和Ptn的带匹配字符，匹配则自增，不匹配则i回溯为i-j+1，j回溯为0，当二者有其一索引至尾端则跳出循环，若跳出循环后j索引完了Ptn则返回i-length（Ptn），否则返回-1。

## 代码

```cpp
/*
返回子串Ptn在主串Tag的第pos个字符后(含第pos个位置)第一次出现的位置，若不存在，则返回-1
采用BF算法，这里的位置全部以从0开始计算为准，其中T非空，0<=pos<=Tlen
*/
int index(const string &Tag,const string &Ptn,int pos)
{
    int i = pos;  //主串当前正待比较的位置，初始为pos
    int j = 0;   //子串当前正待比较的位置，初始为0
    int Tlen = Tag.size();  //主串长度
    int Plen = Ptn.size();  //子串长度

    while(i<Tlen && j<Plen)
    {
        if(Tag[i] == Ptn[j])   //如果当前字符相同，则继续向下比较
        {
            i++;
            j++;
        }
        else   //如果当前字符不同，则i和j回退，重新进行匹配
        {
            //用now_pos表示每次重新进行匹配时开始比较的位置，则
            //i=now_pos+后移量，j=0+后移量
            //则i-j+1=now_pos+1,即为Tag中下一轮开始比较的位置
            i = i-j+1;
            //Ptn退回到子串开始处
            j = 0;
        }
    }

    if(j >= Plen)
        return i - Plen;
    else
        return -1;
}
```

## 验证

```cpp
int main()
{
    char ch;
    do{
        string Tag,Ptn;
        int pos;
        cout<<"输入主串：";
        cin>>Tag;
        cout<<"输入子串：";
        cin>>Ptn;
        cout<<"输入主串中开始进行匹配的位置（首字符位置为0）：";
        cin>>pos;

        int result = index(Tag,Ptn,pos);
        if(result != -1)
            cout<<"主串与子串在主串的第"<<result<<"个字符（首字符的位置为0）处首次匹配"<<endl;
        else
            cout<<"无匹配子串"<<endl;

        cout<<"是否继续测试（输入y或Y继续，任意其他键结束）：";
        cin>>ch;
    }while(ch == 'y' || ch == 'Y');
    return 0;
}
```

# KMP算法

## 思路

- 回溯的方法不同，一旦失配，i不回溯，j回溯到一个特殊的位置，采用next[length(Ptn)]记录元素失配后回溯到的下一位置。
- 关键在与next数组的求解，下面举例。key：next数组是针对子串的，和母串没关。

> next数组理解的举例

- 对于子串“ABCDABD”，对应的next数组为“-1 0 0 0 0 1 2”，下面解释next数组怎么来的。
- 当匹配到第六位的“B”时，如果发生了失配，j将回到1即第二位开始配，因为失配位的前一位是A，而A在子串的最开头出现过，所以j没必要回溯到0再开始匹配了。
- 当匹配到第七位的“D”时，如果发生了失配，j将回到2即第三位开始配，因为失配位的前两位是AB，而AB在子串的最开头出现过，所以j没必要回溯到0再开始匹配了，直接从第三位开始匹配。
- 所以next数组记录的是，当前位置元素往前看，比如D往前看，出现的连续字符满足和从头开始数连续字符相等的数量。比如从D往前看为AB，所以D对应2。

## 代码

```cpp
/*
返回子串Ptn在主串Tag的第pos个字符后(含第pos个位置)第一次出现的位置，若不存在，则返回-1
采用KMP算法，这里的位置全部以从0开始计算为准，其中T非空，0<=pos<=Tlen
*/
int kmp_index(const string &Tag,const string &Ptn,int pos)
{
    int i = pos;  //主串当前正待比较的位置，初始为pos
    int j = 0;   //子串当前正待比较的位置，初始为0
    int Tlen = Tag.size();  //主串长度
    int Plen = Ptn.size();  //子串长度

    //求next数组的值，并逐个输出
    int *next = (int *)malloc(Plen*sizeof(int));
    get_next(Ptn,next,Plen);
//  get_nextval(Ptn,next,Pln);
    int t;
    cout<<"子串的next数组中的各元素为：";
    for(t=0;t<Plen;t++)
        cout<<next[t]<<" ";
    cout<<endl;

    while(i<Tlen && j<Plen)
    {
        if(j==-1 || Tag[i] == Ptn[j])
        {   //如果当前字符相同，或者在子串的第一个字符处失配，则继续向下比较
            i++;
            j++;
        }
        else   //如果当前字符不同，则i保持不变，j变为下一个开始比较的位置
        {
            //next数组时KMP算法的关键，i不回退，
            //而是继续与子串中的nex[j]位置的字符进行比较
            j = next[j];
        }
    }

    if(j >= Plen)
        return i - Plen;
    else
        return -1;
}

/*
求next数组中各元素的值，保存在长为len的next数组中
*/
void get_next(const string &Ptn,int *next,int len)
{
    int j = 0;
    int k = -1;
    next[0] = -1;

    while(j<len-1)
    {
        if(k == -1 || Ptn[j] == Ptn[k])
        {   //如果满足上面分析的Pk = Pj的情况，则继续比较下一个字符，
            //并得next[j+1]=next[j]+1
            j++;
            k++;
            next[j] = k;
        }
        else
        {   //如果符合上面分析的第2种情况，则依据next[k]继续寻找下一个比较的位置
            k = next[k];
        }
    }
}


/*
求next数组的改进数组中各元素的值，保存在长为len的nextval数组中
*/
void get_nextval(const string &Ptn,int *nextval,int len)
{
    int j = 0;
    int k = -1;
    nextval[0] = -1;

    while(j<len-1)
    {
        if(k == -1 || Ptn[j] == Ptn[k])
        {   //如果满足上面分析的Pk = Pj的情况，则继续比较下一个字符，
            //并得next[j+1]=next[j]+1
            j++;
            k++;
            if(Ptn[j] != Ptn[k])
                nextval[j] = k;
            else  //Ptn[j]与Ptn[k]相等时，直接跳到netval[k]
                nextval[j] = nextval[k];
        }
        else
        {   //如果符合上面分析的第2种情况，则依据next[k]继续寻找下一个比较的位置
            k = nextval[k];
        }
    }
}
```

## 验证

```cpp
int main()
{
    char ch;
    do{
        string Tag,Ptn;
        int pos;
        cout<<"输入主串：";
        cin>>Tag;
        cout<<"输入子串：";
        cin>>Ptn;
        cout<<"输入主串中开始进行匹配的位置（首字符位置为0）：";
        cin>>pos;

        int result = kmp_index(Tag,Ptn,pos);
        if(result != -1)
            cout<<"主串与子串在主串的第"<<result<<"个字符（首字符的位置为0）处首次匹配"<<endl;
        else
            cout<<"无匹配子串"<<endl;

        cout<<"是否继续测试（输入y或Y继续，任意其他键结束）：";
        cin>>ch;
    }while(ch == 'y' || ch == 'Y');
    return 0;
}
```
# 参考链接

- [【数据结构与算法】模式匹配——从BF算法到KMP算法（附完整源码）](http://blog.csdn.net/ns_code/article/details/19286279)
- [从头到尾彻底理解KMP](http://blog.csdn.net/v_july_v/article/details/7041827)
