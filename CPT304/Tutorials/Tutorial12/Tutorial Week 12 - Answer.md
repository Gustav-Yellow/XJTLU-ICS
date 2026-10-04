# 代码节点划分

我先按照题目图片中的编号，把程序划分成节点：

```
(1) 初始化变量：
    int bot, mid, top;
    index = -1;
    bot = 0;
    top = arraySize - 1;
    mid = (top + bot) / 2;

(2) if (array[mid] == searchKey)

(3) found = true;

(4) found = false;

(5) while (bot <= top && !found)

(6) mid = (top + bot) / 2;

(7) if (array[mid] == searchKey)

(8) found = true;
    index = mid;

(9) else if (array[mid] < searchKey)

(10) bot = mid + 1;

(11) top = mid - 1;

(12) end while body / loop back

(13) end function
```

------

# Question 1：Draw a Control Flow Graph

Control Flow Graph 可以画成下面这样。课件中说 CFG 是有向图，node 表示 statement 或 statement fragment，edge 表示 control flow。

```
                ┌──────────────┐
                │   (1) Init    │
                └──────┬───────┘
                       ↓
              ┌─────────────────┐
              │ (2) array[mid]  │
              │ == searchKey ?  │
              └──────┬──────┬───┘
                   T │      │ F
                     ↓      ↓
              ┌────────┐  ┌────────┐
              │(3)found│  │(4)found│
              │ = true │  │ = false│
              └────┬───┘  └────┬───┘
                   └──────┬────┘
                          ↓
              ┌────────────────────┐
              │ (5) bot <= top     │
              │     && !found ?    │
              └──────┬────────┬────┘
                   T │        │ F
                     ↓        ↓
              ┌────────┐   ┌────────┐
              │(6) mid │   │(13)End │
              │ update │   └────────┘
              └────┬───┘
                   ↓
              ┌─────────────────┐
              │ (7) array[mid]  │
              │ == searchKey ?  │
              └──────┬──────┬───┘
                   T │      │ F
                     ↓      ↓
              ┌────────┐  ┌─────────────────┐
              │(8)found│  │ (9) array[mid]  │
              │true,idx│  │ < searchKey ?   │
              └────┬───┘  └──────┬──────┬───┘
                   │           T │      │ F
                   │             ↓      ↓
                   │       ┌────────┐ ┌────────┐
                   │       │(10)bot │ │(11)top │
                   │       │=mid+1  │ │=mid-1  │
                   │       └────┬───┘ └────┬───┘
                   └────────────┴──────────┘
                                ↓
                           ┌────────┐
                           │ (12)   │
                           │ loop   │
                           └────┬───┘
                                │
                                └────────── back to (5)
```

用 edge list 表示就是：

```
1 → 2
2(T) → 3
2(F) → 4
3 → 5
4 → 5
5(T) → 6
5(F) → 13
6 → 7
7(T) → 8
7(F) → 9
8 → 12
9(T) → 10
9(F) → 11
10 → 12
11 → 12
12 → 5
```

------

# Question 2：Branch Testing Test Cases

Branch testing 的目标是让每个 decision 的 True / False branch 都至少执行一次。这里主要有 4 个 decision：

```
D1: (2) array[mid] == searchKey
D2: (5) bot <= top && !found
D3: (7) array[mid] == searchKey
D4: (9) array[mid] < searchKey
```

为了覆盖所有 branch，我们可以使用下面的测试用例。假设 array 是升序排列。

## Test Case Set for Branch Coverage

| Test case | array             | arraySize | searchKey | Expected found | Expected index | Covered branch                                            |
| --------- | ----------------- | --------- | --------- | -------------- | -------------- | --------------------------------------------------------- |
| TC1       | `[1, 3, 5, 7, 9]` | 5         | 5         | true           | 2              | (2) True, (5) False                                       |
| TC2       | `[1, 3, 5, 7, 9]` | 5         | 9         | true           | 4              | (2) False, (5) True, (7) False, (9) True, later (7) True  |
| TC3       | `[1, 3, 5, 7, 9]` | 5         | 1         | true           | 0              | (2) False, (5) True, (7) False, (9) False, later (7) True |
| TC4       | `[1, 3, 5, 7, 9]` | 5         | 4         | false          | -1             | unsuccessful search, loop exits because `bot > top`       |

## Explanation

TC1：一开始 `mid = 2`，`array[2] = 5`，刚好等于 `searchKey`，所以 `(2)` 为 True，`found = true`，while 不进入。

TC2：搜索 9。第一次中间值 5 小于 9，所以走 `(9)` True，更新 `bot = mid + 1`，之后找到 9。

TC3：搜索 1。第一次中间值 5 大于 1，所以 `(9)` False，更新 `top = mid - 1`，之后找到 1。

TC4：搜索 4。4 不在数组中，最后循环退出，`found = false`，`index = -1`。

------

# Question 3：Multiple-condition Testing Test Cases

Multiple-condition testing 要求对 compound predicate 中的每个 basic condition 的组合进行测试。课件中说明，如果一个 predicate 是 compound predicate，例如 `(A or B)`，就需要考虑所有可能 condition combination。

这里最重要的 compound condition 是：

```
(5) while (bot <= top && !found)
```

可以拆成：

```
A = bot <= top
B = !found
```

理论上 `A && B` 有 4 种组合：

| A: bot <= top | B: !found | while result |
| ------------- | --------- | ------------ |
| True          | True      | True         |
| True          | False     | False        |
| False         | True      | False        |
| False         | False     | False        |

但是在这个 binary search 程序中，`False, False` 基本是不可行的，因为当 `found = true` 时，通常是在当前合法搜索范围内找到元素，此时 `bot <= top` 仍然为 True。所以我们主要覆盖可行的 3 种组合。

## Multiple-condition Test Cases

| Test case | array             | searchKey | Important condition combination                              |
| --------- | ----------------- | --------- | ------------------------------------------------------------ |
| MC1       | `[1, 3, 5, 7, 9]` | 5         | 初始找到，while 中 `bot <= top = True`, `!found = False`     |
| MC2       | `[1, 3, 5, 7, 9]` | 4         | 未找到，循环中出现 `True, True`，最后退出时出现 `False, True` |
| MC3       | `[1, 3, 5, 7, 9]` | 9         | 覆盖 `array[mid] < searchKey` 为 True，并最终找到            |
| MC4       | `[1, 3, 5, 7, 9]` | 1         | 覆盖 `array[mid] < searchKey` 为 False，并最终找到           |

## Coverage explanation

```
MC1:
array[2] = 5, searchKey = 5
(2) True
found = true
while condition: bot <= top is True, !found is False

MC2:
searchKey = 4
进入 while 时: bot <= top is True, !found is True
最后找不到时: bot <= top is False, !found is True

MC3:
searchKey = 9
在 loop 内部:
array[mid] == searchKey 为 False
array[mid] < searchKey 为 True

MC4:
searchKey = 1
在 loop 内部:
array[mid] == searchKey 为 False
array[mid] < searchKey 为 False
```

所以这个 test set 可以覆盖：

```
(5) bot <= top && !found 的主要可行 condition combinations
(7) array[mid] == searchKey 的 True / False
(9) array[mid] < searchKey 的 True / False
```

------

# Question 4：Cyclomatic Complexity

课件中说明，McCabe’s Basis Path Testing 使用 cyclomatic complexity 来衡量程序逻辑复杂度，并用它指导 basis paths 的数量。公式为：

```
V(G) = e - n + 2p
```

其中：

```
e = number of edges
n = number of nodes
p = number of connected components
```

在这个 CFG 中：

```
n = 13
e = 16
p = 1
```

所以：

```
V(G) = e - n + 2p
     = 16 - 13 + 2(1)
     = 5
```

也可以用更简单的方法：

```
Cyclomatic Complexity = number of decision nodes + 1
```

Decision nodes 是：

```
(2) if array[mid] == searchKey
(5) while bot <= top && !found
(7) if array[mid] == searchKey
(9) else if array[mid] < searchKey
```

所以：

```
V(G) = 4 + 1 = 5
```

因此，这个函数的 **cyclomatic complexity = 5**。

这也意味着我们至少需要 **5 条 linearly independent basis paths**。

------

# Question 5：McCabe’s Basis Paths

McCabe’s Basis Path Method 的基本步骤是：先画 program graph，然后计算 cyclomatic complexity，再选择一组 basis paths，最后为每条 path 设计测试用例。

因为 Question 4 中算出：

```
V(G) = 5
```

所以我们需要设计 **5 条 basis paths**。

------

## Basis Path 1：Initial middle element found

```
P1: 1 → 2(T) → 3 → 5(F) → 13
```

对应测试用例：

| array             | searchKey | Expected                |
| ----------------- | --------- | ----------------------- |
| `[1, 3, 5, 7, 9]` | 5         | found = true, index = 2 |

说明：一开始就找到目标值，不进入 while loop。

------

## Basis Path 2：Go right, then found

```
P2: 1 → 2(F) → 4 → 5(T) → 6 → 7(F) → 9(T) → 10 → 12 → 5(T) → 6 → 7(T) → 8 → 12 → 5(F) → 13
```

对应测试用例：

| array             | searchKey | Expected                |
| ----------------- | --------- | ----------------------- |
| `[1, 3, 5, 7, 9]` | 9         | found = true, index = 4 |

说明：第一次中间值 5 小于 9，所以向右半部分搜索，最后找到 9。

------

## Basis Path 3：Go left, then found

```
P3: 1 → 2(F) → 4 → 5(T) → 6 → 7(F) → 9(F) → 11 → 12 → 5(T) → 6 → 7(T) → 8 → 12 → 5(F) → 13
```

对应测试用例：

| array             | searchKey | Expected                |
| ----------------- | --------- | ----------------------- |
| `[1, 3, 5, 7, 9]` | 1         | found = true, index = 0 |

说明：第一次中间值 5 大于 1，所以向左半部分搜索，最后找到 1。

------

## Basis Path 4：Go right, but not found

```
P4: 1 → 2(F) → 4 → 5(T) → 6 → 7(F) → 9(T) → 10 → 12 → 5(F) → 13
```

对应测试用例：

| array | searchKey | Expected                  |
| ----- | --------- | ------------------------- |
| `[5]` | 7         | found = false, index = -1 |

说明：数组只有一个元素 5，搜索 7。因为 5 < 7，所以 `bot = mid + 1`，之后 `bot > top`，循环退出。

------

## Basis Path 5：Go left, but not found

```
P5: 1 → 2(F) → 4 → 5(T) → 6 → 7(F) → 9(F) → 11 → 12 → 5(F) → 13
```

对应测试用例：

| array | searchKey | Expected                  |
| ----- | --------- | ------------------------- |
| `[5]` | 3         | found = false, index = -1 |

说明：数组只有一个元素 5，搜索 3。因为 5 > 3，所以 `top = mid - 1`，之后 `bot > top`，循环退出。

------

# Final Answer Summary

| Question | Answer                                                       |
| -------- | ------------------------------------------------------------ |
| Q1       | CFG 如上，包含 13 个节点和 16 条边                           |
| Q2       | Branch testing 至少使用 TC1–TC4 覆盖所有 True / False branch |
| Q3       | Multiple-condition testing 重点覆盖 `bot <= top && !found` 的可行组合，以及内部判断条件 |
| Q4       | Cyclomatic complexity = `16 - 13 + 2 = 5`                    |
| Q5       | 需要 5 条 McCabe basis paths，对应 P1–P5                     |