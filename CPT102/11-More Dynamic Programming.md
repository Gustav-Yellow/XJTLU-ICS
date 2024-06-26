# 更多的动态规划问题

1. 求小问题
2. dynamic programming 公式
3. 基本情况(需要提前初始化)

## 1-dimensional DP 一维动态规划问题

### Example 1: 目标和的加法算式数量

例题：求出所有由1，3，4组成的和为5加法算式（如：1+1+3=5）的数量

大问题：在数组[a1,a2…am]中寻找和为n的加法算式有多少
*如：1+1+1+1+1，1+1+3，1+3+1，3+1+1，1 +4，4 +1*

Define subproblems: 定义一个微观问题

- Let D<sub>n</sub> be the number of ways to write n as the sum of 1, 3, 4 

  设 D<sub>n</sub> 是为1，3，4这三个数字组成的加法算式之和为n的算式数量

Find the recurrence: 求出递归

- Consider one possible solution n = x<sub>1</sub> + x<sub>2</sub> + ····· + x<sub>m</sub>

  考虑一种解 n = x<sub>1</sub> + x<sub>2</sub> + ····· + x<sub>m</sub>

- if x<sub>m</sub> = 1, the rest of the terms must sum to n-1

  如果x<sub>m</sub>=1，其余项的总和必须为n-1

- Thus, the number of sums that end with x<sub>m</sub> = 1 is equal to D<sub>n - 1</sub>

  因此，以x<sub>m</sub> = 1结尾的加法算式的个数等于D<sub>n - 1</sub>，也就是1，2，3组成和为5-1=4的加法算式的数量

- Take other cases into account (x<sub>m</sub> = 3, x<sub>m</sub> =4)

  在将剩下的算式放入递归计算

Recurrence is then

- **D<sub>n</sub> = D<sub>n-1</sub> +  D<sub>n-3</sub> + D<sub>n-4</sub>**

Solve the cases

dp自底部向上求解，算法维护一个数组，记录不同和的情况下加法式子的数量，和的值将从0逐渐迭代到大问题中的n（i会逐渐增加到n），D[n]即为问题答案

(基本情况base case：前 **数组长度+1** 个dp值需要先自己算)

- D<sub>0</sub> = 1
- D<sub>n</sub> = 0 for all negative n
- Alternatively, can set D<sub>0</sub> = D<sub>1</sub> = D<sub>2</sub> = 1 and D<sub>3</sub> = 2

实现:

```C
D[0] = D[1] = D[2] = 1;
D[3] = 2; 
for(i = 4;i <= n;i++) 
 D[i] = D[i-1] + D[i-3] + D[i-4];
```

### Example 2 完美覆盖问题

**Problem:** Given n, find the number of ways to fill a 3 × n boardwith dominoes. (boardwith dominoes are  1 * 2)

**问题：** 用2*1的小砖块填满3*你的区域

Here is one possible solution for n = 12: 下面是n=12的可能解

<img src="https://img-blog.csdnimg.cn/20210530092048161.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3Nhbm11c2VuX3d1,size_16,color_FFFFFF,t_70" alt="在这里插入图片描述" style="zoom:50%;" />

问题以二维表述，但仍然是一个一维的dp问题。要点主要在于大问题和小问题之间的衔接过程

算法维护两个一维的数据，分别记录两种情况下的小瓷砖排列情况。大问题正好摆放n列，小问题是正好摆放n-1列

思路1：

设f(n)为需要填充的区域长为n时填充的方法数量

首先确定，n为奇数情况下，无法密铺区域，只需要考虑偶数情况，于是考虑f(n)和f(n-2)的关系，如果填充区域向右增加2个单位，有以下三种方法填满新增的小区域:

<img src="img/Week11/img1.png" style="zoom:50%;" />

因此f(n)与f(n-2)的关系中，至少会有一项3f(n-2)；(3代表3种方式)

本题有意思的地方在于，f(n)不仅仅和f(n-2)有关系，如下

<img src="img/Week11/img2.png" style="zoom:50%;" />

这种铺法的话就需要4个单位，并存在垂直方向对称铺法，于是需要填充的区域向右拓展2个单位时，我们可以选择不铺，继续等待下次再拓展两个单位，也就是等到拓展了4个单位的时候再用以上的这种铺法填充区域，因为图形f(n)和f(n-4)有关系，经过实现观察还可以发现，想要铺满宽大于2的空间（长为偶数），有且仅有形如上面的铺法，也就是两种铺法，那么f(n)和f(n-4)的关系中至少会有一项2f(n-4)，推广到所有情况，其实4,6,8都是一样的，也就是说f(n)其实和2(f(n-4)+f(n-6)+f(n-8)+.... +f(2)+f(0))有关系。

那么至此就可以写出状态转移方程:

f(n) = 3 * f(n-2) + 2 * (f(n-4) + f(n-6) + ... + f(0))

## 2-dimensional DP 二维动态规划问题

**LCS (Longest common subsequence) Problem**

week9讲过了，可以看出dp是以二维table的形式体现。

### Interval DP Example 间隔DP

**Problem:** given a string x = x1 .. n, find the minimum number of characters that need to be inserted to make it a palindrome

给定一字符串，添加最少的字符，使字符串变成对称的回文字符串 (palindrome 正数倒数都一样)

Example:
– x: “Ab3bd”
– Can get “dAb3bAd” or “Adb3bdA” by inserting 2 characters (one ‘d’, one ‘A’)

将字符串看成滑块，左边界i和右边界j可以滑动。

大问题：字符串需要添加至少多少字符使之回文
子问题：左右边界同时向内移1的字符串需要添加至少多少字符使之回文

**Define subproblems:** 定义小问题

Let D<sub>i,j</sub> be the minimum number of characters that need to be inserted to make x<sub>i....j</sub> into a palindrome.

让 D<sub>i,j</sub> 成为使 x<sub>i....j</sub> 成为回文的最小字符数。

**Find the recurrence:**

- Consider a shortest palindrome y1...k containing xi...j 
- Either y<sub>1</sub> = x<sub>i</sub> or y<sub>k</sub> = x<sub>j</sub>
- y<sub>2...k-1</sub> is then an optimal solution for x<sub>i+1....j</sub> or x<sub>i...j-1</sub> or x<sub>i+1...j-1</sub>
  - last case possible only if y1 = yk = xi = xj
  - D<sub>i,j</sub> = max(**1+min(D<sub>i+1, j</sub>, D<sub>i, j-1</sub>) 当x<sub>i</sub> != x<sub>j</sub>**, **D<sub>i+1, j-1</sub> 当x<sub>i</sub> = x<sub>j</sub>**)

问题间关系：
如果内移掉的字符与另一侧内移掉的字符不同，则需要 一侧不移动的子问题的dp值 加上一个另一侧的内移掉的额外字符 使之回文，在两侧之间找最小。

如果内移掉的字符与另一侧内移掉的字符相同，代表该次dp不要添加字符，大问题与子问题dp值相同。
基本情况base case：dp<sub>i,i</sub>,dp<sub>i,i-1</sub>=0 for all i

## Tree DP

**Problem:** given a tree, color nodes black as many as possible without coloring two adjacent nodes

**问题：** 给定一棵树，在不给两个相邻节点着色的情况下，尽可能多地给节点涂上黑色

**Subproblem:**

- First, we arbitrarily decide the root node r 

  首先，我们任意确定根节点 r

- B<sub>v</sub>: the optimal solution for a subtree having v as the root, where we color v black
- W<sub>v</sub>:  the optimal solution for a subtree having v as the root, where we don’t color v
- Answer is max(B<sub>r</sub>, W<sub>r</sub>)

**Find the Recurrence:**

- Crucial observation: once v’s color is determined, subtrees can be solved independently

- If v is colored, its children must not be colored

  如果v是有色的，它的子元素不能是有色的
  $$
  B_v = 1 + \sum{W_i, u\in children(v)}
  $$

- If v is not colored, its children can have any color

  如果v没有颜色，它的子元素可以是任何颜色
  $$
  B_v = 1 + \sum{max(B_u, W_u), u\in children(v)}
  $$

v：根节点
B<sub>v</sub>：根节点为黑色，其子树的最大黑色数量
W<sub>v</sub>：根节点为白色，其子树的最大黑色数量

**Three step of dp**

1. Defining subproblems
2. Finding recurrences 
3. Solving the base cases

## Knapsack 0-1 Example 背包问题 

| Items | Weight | Value |
| ----- | ------ | ----- |
| I0    | 3      | 10    |
| I1    | 8      | 4     |
| I2    | 9      | 9     |
| I3    | 8      | 11    |

大问题：物品有重量和价值，给定一限重为20的背包，怎样挑选物品使背包内价值最大

dp思想大问题：物品有重量和价值，dp可供挑选的物品范围和限重从0到w的背包，求每次dp怎么在当前可选的物品范围挑选物品使物品价值最大

0-1 背包问题的特点之一在于，一个物品只有带或者不带两个状态，不存在带一部分的情况。

wi：当前dp背包限重
vt：当前dp预拿取物品的价值
dp<sub>i,w</sub>：当前dp背包最大价值
wt：当前dp预拿取物品的重量

子问题：背包限重缩小1，或者物品范围缩小1，或者物品范围缩小1同时背包限重缩小1

自底向上:

大问题与子问题的关系，随着背包的容量逐步上涨和物品范围的扩大，会出现两种情况：

1. 新的物品可以单独进背包，此时考虑拿还是不拿，二者选最大
   (例如，dp限重为10的时候物品范围新增了一个重量为10的物品，这时就要判断是维持限重为9时的配置还是单独拿重量为10的那一个物品）
   1. 拿的话为了使当前dp最优，应当按照拿取当前物品后**剩下来的重量**所在的dp值算当前dp，当前价值dp<sub>i,w</sub>应该等于dp<sub>i,w-wt</sub>+vt
      也就是与上次比物品范围变大，容量上涨，价值变动
   2. 不拿的话当前dp<sub>i,w</sub>=dp<sub>i-1,w</sub>
      也就是与上次比物品范围变大但是不拿，容量上涨，价值与上次一样
2. 新的物品压根塞不进背包，wt>wi，单个物品重量大于限重，此时dp<sub>i,w</sub>=dp<sub>i-1,w</sub>，
   也就是物品范围没法变大，容量上涨一格，价值与上次一样

![在这里插入图片描述](https://img-blog.csdnimg.cn/20210530103630940.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3Nhbm11c2VuX3d1,size_16,color_FFFFFF,t_70)

