

# Greedy Method 贪心算法

Greedy algorithm does **NOT** always return the best solution

贪心算法**并不是**每次都返回最优解

E位Edge的数量，V为Vertex的数量

对于拥有m条边，n个顶点，连接所有的点需要消除m-(n-1)条线，也就是需要m - n + 1；或需要保留n-1条线

## Minimum Spanning tree (MST) 最小生成树

– Given an undirected connected graph G. 给定一个无向连通图G

​	• The edges are labelled by weight. 边缘按重量标记

– Spanning tree of G. G的生成树

​	• a tree containing all vertices in G. 包含 G 中所有顶点的树

– Minimum spanning tree. 最小生成树 (Minimum Spanning Tree)

​	• a spanning tree of G with minimum weight. 具有最小权重的 G 的生成树

<img src="img/Week5/img1.png" style="zoom:33%;" />

## Prim Algorithm 普利姆算法 O(|E|*log|V|) 

prim算法基于贪心，我们每次总是选出一个离生成树距离最小的点去加入生成树，最后实现最小生成树（不做证明，理解思想即可） 

这个算法需要维护点的初始集合S和点的最终集合T
初始时T为空，S为所有节点，将任意一节点从S移入T

1. 计算初始集合S上的所有节点到最终集合T上的所有节点的边的距离
2. 在所有上述边中选择距离最小的,将这条边的节点从初始集合S移到最终集合T,
3. 重复上述步骤直到结果图中包含了所有节点

<img src="https://img-blog.csdnimg.cn/70aee6f7b8e4490e9bf8d607bb76313a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAdGltZXJfY2F0Y2g=,size_20,color_FFFFFF,t_70,g_se,x_16" alt="img" style="zoom: 33%;" />

- 现在我们构建两个集合S（红色的点），V（蓝色的点），S集合中存放的是已近加入最小生成树的点，V集合中存放的是还没有加入最小生成树的点。显然刚开始时所有的点都在V集合中。
- 然后们先将任意一个点加入集合S中（默认为点1），并且初始化所有点（除了点1）到集合S的距离是无穷大。

<img src="https://img-blog.csdnimg.cn/1a3fb634db4345f18b428c103cb4f1ec.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAdGltZXJfY2F0Y2g=,size_20,color_FFFFFF,t_70,g_se,x_16" alt="img" style="zoom:33%;" />

<img src="https://img-blog.csdnimg.cn/6d2e36e13f16485caba4d78f7f07416a.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAdGltZXJfY2F0Y2g=,size_20,color_FFFFFF,t_70,g_se,x_16" alt="img" style="zoom:25%;" />

- 用一个变量res存放最小生成树所有边权值的和。我们每次都选择离S集合最近的点加入S集合中，并且用新加入的点去更新dist数组，因为只有一个新的点加入到集合S中，到集合S的距离才有可能更新（**贪心，每次都选最小的**）。
- 更新就是看一下能否通过新加入的点使到达集合的距离变小（看下面dist数组的变化）。
- 我们开始在加入点1后开始第一次更新。

<img src="https://img-blog.csdnimg.cn/5ba01475ba0741c3981dc3478936898b.gif" alt="img" style="zoom:25%;" />

- 现在集合S={1}，集合V={2，3，4，5，6，7}，根据贪心策略，我们选择离集合S最近的点加入 ，即点2，并把这一条边的权值加到res中

<img src="https://img-blog.csdnimg.cn/5441772b60ca41cdbc9292d084e84b81.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAdGltZXJfY2F0Y2g=,size_20,color_FFFFFF,t_70,g_se,x_16" alt="img" style="zoom:33%;" />

- 集合更新为S={1，2}，V={3，4，5，6，7}，并用点2去更新dist数组，我们发现点3和点7都可以都可以通过边2-3，2-7缩短到集合S得距离。

<img src="https://img-blog.csdnimg.cn/803ff94572c3453280ca34d9768a9cb0.gif" alt="img" style="zoom: 25%;" />

<img src="https://img-blog.csdnimg.cn/7464321fbb874507be1743a0c5021ec4.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAdGltZXJfY2F0Y2g=,size_20,color_FFFFFF,t_70,g_se,x_16" alt="img" style="zoom:33%;" />

<img src="https://img-blog.csdnimg.cn/3e51900f0d9c4d50af184d96936f693c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAdGltZXJfY2F0Y2g=,size_20,color_FFFFFF,t_70,g_se,x_16" alt="img" style="zoom:25%;" />

<img src="https://img-blog.csdnimg.cn/7cbd2143c8e640dcbd49d80bb5225593.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAdGltZXJfY2F0Y2g=,size_20,color_FFFFFF,t_70,g_se,x_16" alt="img" style="zoom:33%;" />

<img src="https://img-blog.csdnimg.cn/590b2c3219374c9eab5413e4b25ad585.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAdGltZXJfY2F0Y2g=,size_20,color_FFFFFF,t_70,g_se,x_16" alt="img" style="zoom:25%;" />

- 此时到达节点4的权值已经在更新到节点7的时候被填入9了，而3如果更新到节点4的权值只能更改为15，大于9，因此节点3无法更改任何的权值，所以返回上一个节点7

<img src="https://img-blog.csdnimg.cn/7326e90bf1c04ef680501d08b0dc5c2f.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAdGltZXJfY2F0Y2g=,size_20,color_FFFFFF,t_70,g_se,x_16" alt="img" style="zoom:33%;" />

<img src="https://img-blog.csdnimg.cn/8b0bcc887cb5419b9b66be05b1b2a3b3.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAdGltZXJfY2F0Y2g=,size_20,color_FFFFFF,t_70,g_se,x_16" alt="img" style="zoom:25%;" />

<img src="https://img-blog.csdnimg.cn/bbc4960ced2946d7b448b13b3d11d48c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAdGltZXJfY2F0Y2g=,size_20,color_FFFFFF,t_70,g_se,x_16" alt="img" style="zoom:33%;" />

<img src="https://img-blog.csdnimg.cn/6be2bd08b46840958d8e996a7c1b1d37.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAdGltZXJfY2F0Y2g=,size_20,color_FFFFFF,t_70,g_se,x_16" alt="img" style="zoom:25%;" />

<img src="https://img-blog.csdnimg.cn/477b503532864a138fd01b0a8fb42c21.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAdGltZXJfY2F0Y2g=,size_20,color_FFFFFF,t_70,g_se,x_16" alt="img" style="zoom:33%;" />

- 这样一颗最小生成树就构建完成了，权值和是57。

解释2：

图 G=（V,E）是一个无向连通带权图，如下图所示



<img src="https://img-blog.csdnimg.cn/cbd9d6dca6ad471bbc93d5cbeb4a584a.png" alt="img" style="zoom: 50%;" />

1 初始化，令集合 U={u0}，u0 属于 V，并初始化数组 closest[]、lowcost[]和s[]。

2 在集合 V-U 中找 lowcost 值最小的节点t，即 lowcost[t]=min{lowcost[j]},j 属于 V-U，满足该公式的节点 t 就是集合 V-U 中连接 U 的最邻近点。

3 将节点 t 加入集合 U 中。

4 如果集合 V - U 为空，则算法结束，否则转向步骤 5。

5 对集合 V-U 中的所有节点 j 都更新其 lowcost[] 和 closest[]。if(C[t] [j]<lowcost[j]){lowcost[j]=C[t] [j];closest[j]=t;},转向步骤2。

图解：

1. 初始化。假设 u0=1，令集合 U={1},集合 V-U={2,3,4,5,6,7},s[1]=true，初始化数组 closest[]：除了节点1，其余节点均为1，表示集合 V-U 中的节点到集合 U 的最邻近点均为1.lowcost[]:节点1到集合 V-U 中节点的边值。closest[] 和 lowcost[] 如下图所示。
   ![img](https://img-blog.csdnimg.cn/ac08c55bc8a3461c97c82f3ae17b9ad6.png)





<img src="https://img-blog.csdnimg.cn/c27704f5fff74b29b246aef8623931c1.png" alt="img" style="zoom: 50%;" />

2. 找 lowcost 最小的节点，对应的 t=2，选中的边和节点如下图。

   <img src="https://img-blog.csdnimg.cn/6f01eedbbf5347fdace314cf1c0c1dcf.png" alt="img" style="zoom: 50%;" />

3. 加入集合U中。将节点 t 加入集合 U 中，U={1,2}，同时更新 V-U={3,4,5,6,7}

4.  更新。对 t 在集合 V-U 中的每一个邻接点 j,都可以借助 t 更新。节点 2 的邻接点是节点 3 和节点7。

```
C[2][3]=20<lowcost[3]=无穷大，更新最邻近距离 lowcost[3]=20,最邻近点 closest[3]=2;

C[2][7]=1<lowcost[7]=36，更新最邻近距离 lowcost[7]=1,最邻近点 closest[7]=2;
```

![img](https://img-blog.csdnimg.cn/7c436aeb2933457cb84e4d5d3bc61e5f.png)

<img src="https://img-blog.csdnimg.cn/c9d9c27965d24386bdb291fd2f02eed7.png" alt="img" style="zoom:50%;" />

5.  找 lowcost 最小的节点，对应的 t=7，选中的边和节点如下图。

<img src="https://img-blog.csdnimg.cn/433a2cf91304496c9dbaa4180af4d162.png" alt="img" style="zoom:50%;" />

6. 加入集合U中。将节点 t 加入集合 U 中，U={1,2,7}，同时更新 V-U={3,4,5,6}

7. 更新。对 t 在集合 V-U 中的每一个邻接点 j,都可以借助 t 更新。节点 7 的邻接点是节点 3、4、5、6

```
C[7][3]=4<lowcost[3]=20，更新最邻近距离 lowcost[3]=4,最邻近点 closest[3]=7;

C[7][4]=4<lowcost[4]=无穷大，更新最邻近距离 lowcost[3]=9,最邻近点 closest[4]=7;

C[7][5]=4<lowcost[5]=无穷大，更新最邻近距离 lowcost[3]=16,最邻近点 closest[5]=7;

C[7][6]=4<lowcost[6]=28，更新最邻近距离 lowcost[3]=25,最邻近点 closest[6]=7;
```



![img](https://img-blog.csdnimg.cn/88b544f8bdcc488a98260856ce7ca757.png)

8. 找 lowcost 最小的节点，对应的 t=3，选中的边和节点如下图

<img src="https://img-blog.csdnimg.cn/c7c537959d8a4cf29f20802a4dd29bb5.png" alt="img" style="zoom: 50%;" />

9.  加入集合U中。将节点 t 加入集合 U 中，U={1,2,3,7}，同时更新 V-U={4,5,6}

10.  更新。对 t 在集合 V-U 中的每一个邻接点 j,都可以借助 t 更新。节点 3 的邻接点是节点 4。

```
C[3][4]=15>lowcost[4]=9，不更新
```

11.  找 lowcost 最小的节点，对应的 t=4，选中的边和节点如下图

<img src="https://img-blog.csdnimg.cn/37d6a4b294694ffcab3989d78297aa3d.png" alt="img" style="zoom:50%;" />

12. 加入集合U中。将节点 t 加入集合 U 中，U={1,2,3,4,7}，同时更新 V-U={5,6}

13.  更新。对 t 在集合 V-U 中的每一个邻接点 j,都可以借助 t 更新。节点 4 的邻接点是节点 5。

```
C[4][5]=3<lowcost[5]=16，更新最邻近距离 lowcost[5]=3,最邻近点 closest[5]=4;
```

![img](https://img-blog.csdnimg.cn/48e038931ad343c396bdeb89e53aa539.png)

14 找 lowcost 最小的节点，对应的 t=5，选中的边和节点如下图。

<img src="https://img-blog.csdnimg.cn/22973ce5ac364003963d6409e695592b.png" alt="img" style="zoom:50%;" />

15. 加入集合U中。将节点 t 加入集合 U 中，U={1,2,3,4,5,7}，同时更新 V-U={6}

16. 更新。对 t 在集合 V-U 中的每一个邻接点 j,都可以借助 t 更新。节点 5 的邻接点是节点 6

```
C[5][6]=17<lowcost[6]=25，更新最邻近距离 lowcost[6]=17,最邻近点 closest[6]=5;
```

17.  找 lowcost 最小的节点，对应的 t=6，选中的边和节点如下图。

<img src="https://img-blog.csdnimg.cn/fa904b1f0bd24990b11e86c6f4babf19.png" alt="img" style="zoom:50%;" />

18.  加入集合U中。将节点 t 加入集合 U 中，U={1,2,3,4,5,6,7}，同时更新 V-U={}

19. 更新。对 t 在集合 V-U 中的每一个邻接点 j,都可以借助 t 更新。节点 6 在集合 V-U 中无邻接点。不用更新 closest[] 和 lowcost[] 。

20.  得到的最小生成树如下。最小生成树的权值之和为 57.


<img src="https://img-blog.csdnimg.cn/df002f23a86d4afa82a289df700ee3ec.png" alt="img" style="zoom:50%;" />

## Kruskal’s algorithm Kruskal算法 O(|E|*log|V|)

这个算法维护一个**已确定的边**的集合T，
起始时图上所有边初始化为未确定状态，集合T为空

1. 选择未选择状态中最短的边w
2. 如果边w加入集合T，集合T中不会形成回路，则将边w加入集合T
3. 否则，在图中删除边w
4. 重复上述步骤直到集合T中包含所有节点

<img src="img/Week5/img2.png" style="zoom: 25%;" />

<img src="img/Week5/img3.png" style="zoom: 25%;" />

<img src="img/Week5/img4.png" style="zoom: 25%;" />

<img src="img/Week5/img5.png" style="zoom: 25%;" />

<img src="img/Week5/img6.png" style="zoom: 25%;" />

<img src="img/Week5/img7.png" style="zoom: 25%;" />

<img src="img/Week5/img8.png" style="zoom: 25%;" />

<img src="img/Week5/img9.png" style="zoom: 25%;" />

<img src="img/Week5/img10.png" style="zoom: 25%;" />

<img src="img/Week5/img11.png" style="zoom: 25%;" />

<img src="img/Week5/img12.png" style="zoom:25%;" />

<img src="img/Week5/img13.png" style="zoom:25%;" />

## Dijkstra’s algorithm O(|E|*log|V|)  迪克斯特拉算法应用于有向图

针对于边权值非负的图，寻求从起点开始到**其他各个节点**的最短距离。注意计算的是从源结点S到其他每一个节点的最短路径，而上面无向图计算的是连接所有节点的最短路径是什么。

Dijkstra算法找不到最小生成树，因为其主要判断的还是每个节点距离所选择源点S的最短距离

MST计算的是走完所有的点需要的最短路径（无向图），shortest paths代表的是找到每个节点距离原点最近的距离（有向图）

• **Input:** A directed connected weighted graph G and a source vertex **s**

有向连通加权图 G 和源顶点 s

• **Output:** For every vertex **v** in G, find the shortest path from **s** to **v**

输出：G中每个顶点**v**，求从**s**到**v**的最短路径

• **Dijkstra’s algorithm** runs in iterations:

​	– in the i-th iteration, the vertex which is the i-th closest to **s** is found,

​		在第 i 次迭代中，找到最接近 **S** 的第 i 次顶点，

​	– for every remaining vertices, the current shortest path to **s** found so far (this shortest path will be updated as the algorithm 	runs)

​		对于每个剩余的顶点，到目前为止找到的当前最短路径（此最短路径将随着算法的运行而更新）

解释：

这个算法中每个点都有距离值，初始化为无穷，代表从起点到该点的最短距离。

算法需要维护已确定的点的集合True和一个已探明的集合Light，其余点均未探明。集合T中的点已经确定最小距离值，集合L中的点已被

探知但未确定最小距离值。（可以想象为这是一个矿工在探索漆黑矿洞的过程，有些矿洞已走进去过，有些矿洞没进去过但是在路牌上见过，有些矿洞见都还没见着）

步骤：

起始时只有起点在确定集合T中，与起点直接相连的点在探知集合L中，这些点的距离值为它们到起点的边长。

- 在集合L中挑选距离值最少的点m，移入集合T
- 在图中检查所有从点m出发相连的点p，
- 点p的距离值=m的距离值加上m和p它俩间的距离
- 如果点p在已探明集合L中，再检查p的新距离值是否小于原来记录的距离值，如果小于就更新距离值，同时记录下是从点m这儿发现更短的路的。
- 如果点p未探明，恭喜，你在黑暗中解锁了一个新矿洞，将p和其距离值加入集合L，同时记录下是从点m这儿探知到的。
- 如果点p在已确定集合T中，则其新距离值一定大于已记录的距离值。因为这个算法会将当前L中距离值最小的点加入T，又因为边权非负，意味着加入T的时间越靠前，其距离值必定越小。
- 重复上述步骤直到集合T包含所有节点

<img src="img/Week5/img14.png" style="zoom:33%;" />

<img src="img/Week5/img15.png" style="zoom:33%;" />

<img src="img/Week5/img16.png" style="zoom:33%;" />

<img src="img/Week5/img17.png" style="zoom:33%;" />

<img src="img/Week5/img18.png" style="zoom:33%;" />

Prim算法中每个顶点的局部最优解不一定能直接代表这个结果就是全局最优解，因为prim算法是贪心算法，只会根据当前选择的顶点来决定最优的边加入生成树，因此如果想要通过Prim算法来查找全局最优解，可能需要考虑从所有可能的初始顶点开始进行搜索测试，并比对最后得到的权值来觉得从哪个顶点开始才是全局最优解

Kruskal算法由于直接根据最小权值的边来决定生成树，且避免形成回路，因此在一开始得到的结果就可以代表全局最优解。

Kruskal算法相对于Prim算法的缺点就是Kruskal算法需要知道所有边的权值才能进行运算，而Prim是根据一点一点地推进来获取下一层边的权值。

