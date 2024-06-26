# Dynamic Programming Knapsack 动态背包客问题

The goal is to **maximize the value of a knapsack** that can hold at most W units (i.e., lbs or kg) worth of goods from a list of items I0, I1, … In-1. 

我们的目标是**最大化背包的价值**，它可以容纳最多W个单位(即磅或公斤)的货物，从物品清单I0, I1，…In-1。**背包客问题是NP问题**

Each item has 2 attributes:

1. Value – let this be v<sub>i</sub> for item I<sub>i</sub>

   value价值，

2. Weight – let this be w<sub>i</sub> for item I<sub>i</sub>

   weight重量

## Brute Force 暴力解法

The naïve way to solve this problem is to cycle through all **2<sup>n</sup>** subsets of the n items and pick the subset with a legal weight that maximizes the value of the knapsack.

解决这个问题的naïve方法是循环遍历n个项目的所有**2<sup>n</sup>**个子集，并选择具有合法权重的子集，使背包的价值最大化。

## DP 动态规划解法

将问题拆分成sub-problems

我们的第一个尝试可能是将子问题描述如下:

Let Sk be the optimal subset of elements from {I0, I1, …, Ik}. 

设Sk为{I0, I1，…，Ik}中元素的最优子集。

- What we find is that the optimal subset from the elements {I0, I1, …, Ik+1} may not correspond to the optimal subset of elements from {I0, I1, …, Ik} in any regular pattern.

  我们发现元素{I0, I1，…，Ik+1}的最优子集可能不对应于任何正则模式下元素{I0, I1，…，Ik}的最优子集。

- Basically, the solution to the optimization problem for Sk+1 might NOT contain the optimal solution from problem Sk

  基本上，Sk+1的优化问题的解可能不包含问题Sk的最优解

举一个例子:

| Item          | Weight | Value |
| ------------- | ------ | ----- |
| I<sub>0</sub> | 3      | 10    |
| I<sub>1</sub> | 8      | 4     |
| I<sub>2</sub> | 9      | 9     |
| I<sub>3</sub> | 8      | 11    |

这个背包的**最大承重是20公斤**。

The best set of items from {I0, I1, I2} is {I0, I1, I2} 

BUT the best set of items from {I0, I1, I2, I3} is {I0, I2, I3}. 

- In this example, note that this optimal solution, {I0, I2, I3}, does NOT build upon the previous optimal solution, {I0, I1, I2}. 

  在这个例子中，请注意，这个最优解{I0, I2, I3}并不是建立在之前的最优解{I0, I1, I2}之上的。

  - (相反，在这个子集中并不包含I1，因此与{I0, I1, I2}相关的最优子集只能是{I0, I2}

所以这个时候需要改进我们对于子问题的划分:

- Let **B[k, w]** represent the maximum total value of a subset Sk with weight w. 

  设**B[k, w]**表示子集Sk的最大value以及对应的weight w

- 我们的目标是找到**B[n, W]**，其中n是物品的总数，W是背包可以携带的最大重量

那么子问题的递归公式：

**B[k, w] = B[k - 1,w],   if w<sub>k</sub>> w**

​	  **= max { B[k - 1, w], B[k - 1,w - w<sub>k</sub>] + v<sub>k</sub>}, otherwise**

这意味着Sk的最佳子集有总权重w为:

1. 总权值为w的最佳子集Sk-1，或者

2) Sk-1为最佳子集，其总权重为w-w<sub>k</sub>加上item k

The best subset of Sk that has the total weight w, either contains item k or not.

总权值为w的最佳子集Sk，要么包含item k，要么不包含。w<sub>k</sub>代表item k的weight

- 第一种情况（w<sub>k</sub> > w）: item k不能成为解决方案的一部分!如果是一部分那么总重量就会> w，这是不可接受的。
- 第二种情况（w<sub>k</sub> < w）: item k 可以出现在解中此时总重量仍然不会超过最大重量，我们选择数值较大的情况。

```C
for w = 0 to W { // Initialize 1st row to 0’s
	B[0,w] = 0
}
for i = 1 to n { // Initialize 1st column to 0’s
	B[i,0] = 0
}
for i = 1 to n {
	for w = 0 to W {
		if wi <= w { //item i can be in the solution
			if vi + B[i-1,w-wi] > B[i-1,w]
				B[i,w] = vi + B[i-1,w- wi]
			else
				B[i,w] = B[i-1,w]
		}
		else B[i,w] = B[i-1,w] // wi > w
	}
}
```

### 测试

- n = 4 (# of elements)

- W = 5 (max weight)

- Elements (weight, value): (2,3), (3,4), (4,5), (5,6)

| i / w | 0    | 1    | 2    | 3    | 4    | 5    |
| ----- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0     | 0    | 0    | 0    | 0    | 0    | 0    |
| 1     | 0    |      |      |      |      |      |
| 2     | 0    |      |      |      |      |      |
| 3     | 0    |      |      |      |      |      |
| 4     | 0    |      |      |      |      |      |

初始化基本用例

for w = 0 to W

​	B[0,w] = 0

for i = 1 to n

​	B[i,0] = 0

<img src="img/Week11/img3.png" style="zoom:50%;" />

<img src="img/Week11/img4.png" style="zoom:50%;" />

<img src="img/Week11/img5.png" style="zoom:50%;" />

<img src="img/Week11/img6.png" style="zoom:50%;" />

<img src="img/Week11/img7.png" style="zoom:50%;" />

<img src="img/Week11/img8.png" style="zoom:50%;" />

<img src="img/Week11/img9.png" style="zoom:50%;" />

<img src="img/week11/img10.png" style="zoom:50%;" />

<img src="img/Week11/img11.png" style="zoom:50%;" />

<img src="img/Week11/img12.png" style="zoom:50%;" />

<img src="img/Week11/img13.png" style="zoom:50%;" />

<img src="img/Week11/img14.png" style="zoom:50%;" />

<img src="img/Week11/img15.png" style="zoom:50%;" />

<img src="img/Week11/img16.png" style="zoom:50%;" />

<img src="img/Week11/img17.png" style="zoom:50%;" />

<img src="img/Week11/img18.png" style="zoom:50%;" />

该算法只寻找背包中可以携带的最大可能值， The value in B[n,W]

要了解使该值达到最大值的项，我们需要追溯整个表。

```
Let i = n and k = W

if B[i, k] ≠ B[i-1, k] then

	mark the ith item as in the knapsack

	i = i-1, k = k-wi

else

	i = i-1 // Assume the ith item is not in the knapsack

			// Could it be in the optimally packed knapsack?
```

<img src="img/Week11/img19.png" style="zoom:50%;" />

<img src="img/Week11/img20.png" style="zoom:50%;" />

<img src="img/Week11/img21.png" style="zoom:50%;" />

<img src="img/Week11/img22.png" style="zoom:50%;" />

**时间复杂度:**

<img src="img/Week11/img23.png" style="zoom:50%;" />
