# Question 1：Car Loan Monthly Payment Application

题目给出 3 个输入：
 Cost of car：1000 到 200000
 Loan period：1 到 10 years
 Interest rate：0.01 到 0.2

Boundary Value Testing 的核心思想是选择每个变量的 **min, min+, nominal, max-, max**；Normal BVT 使用单故障假设，所以测试数量是 `4n + 1`。Robust BVT 在此基础上加入 `min-` 和 `max+`，测试数量是 `6n + 1`。Worst-case BVT 使用所有变量边界值的笛卡尔积，数量是 `5^n`；Robust worst-case 使用 7 个值的笛卡尔积，数量是 `7^n`。

## Boundary values

| Input         | min- | min  | min+ | nominal | max-   | max    | max+   |
| ------------- | ---- | ---- | ---- | ------- | ------ | ------ | ------ |
| Cost          | 999  | 1000 | 1001 | 100000  | 199999 | 200000 | 200001 |
| Loan period   | 0    | 1    | 2    | 5       | 9      | 10     | 11     |
| Interest rate | 0    | 0.01 | 0.02 | 0.10    | 0.19   | 0.20   | 0.21   |

这里我将 nominal cost 设为 **100000**，虽然严格中点是 100500，但 Tutorial Answer 里使用的是 100000，所以考试中也可以沿用这个值。

------

## a. Normal Boundary Value Test Cases

`n = 3`
 Number of test cases = `4n + 1 = 4(3) + 1 = 13`

| Case | Cost   | Loan period | Interest rate | Expected result                  |
| ---- | ------ | ----------- | ------------- | -------------------------------- |
| 1    | 100000 | 5           | 0.01          | Valid, calculate monthly payment |
| 2    | 100000 | 5           | 0.02          | Valid, calculate monthly payment |
| 3    | 100000 | 5           | 0.10          | Valid, calculate monthly payment |
| 4    | 100000 | 5           | 0.19          | Valid, calculate monthly payment |
| 5    | 100000 | 5           | 0.20          | Valid, calculate monthly payment |
| 6    | 100000 | 1           | 0.10          | Valid, calculate monthly payment |
| 7    | 100000 | 2           | 0.10          | Valid, calculate monthly payment |
| 8    | 100000 | 9           | 0.10          | Valid, calculate monthly payment |
| 9    | 100000 | 10          | 0.10          | Valid, calculate monthly payment |
| 10   | 1000   | 5           | 0.10          | Valid, calculate monthly payment |
| 11   | 1001   | 5           | 0.10          | Valid, calculate monthly payment |
| 12   | 199999 | 5           | 0.10          | Valid, calculate monthly payment |
| 13   | 200000 | 5           | 0.10          | Valid, calculate monthly payment |

------

## b. Robust Boundary Value Test Cases

`n = 3`
 Number of test cases = `6n + 1 = 6(3) + 1 = 19`

Robust BVT 会额外测试 slightly below minimum 和 slightly above maximum，主要是为了检查 exception handling。

| Case | Cost   | Loan period | Interest rate | Expected result       |
| ---- | ------ | ----------- | ------------- | --------------------- |
| 1    | 100000 | 5           | 0             | Invalid interest rate |
| 2    | 100000 | 5           | 0.01          | Valid                 |
| 3    | 100000 | 5           | 0.02          | Valid                 |
| 4    | 100000 | 5           | 0.10          | Valid                 |
| 5    | 100000 | 5           | 0.19          | Valid                 |
| 6    | 100000 | 5           | 0.20          | Valid                 |
| 7    | 100000 | 5           | 0.21          | Invalid interest rate |
| 8    | 100000 | 0           | 0.10          | Invalid loan period   |
| 9    | 100000 | 1           | 0.10          | Valid                 |
| 10   | 100000 | 2           | 0.10          | Valid                 |
| 11   | 100000 | 9           | 0.10          | Valid                 |
| 12   | 100000 | 10          | 0.10          | Valid                 |
| 13   | 100000 | 11          | 0.10          | Invalid loan period   |
| 14   | 999    | 5           | 0.10          | Invalid cost          |
| 15   | 1000   | 5           | 0.10          | Valid                 |
| 16   | 1001   | 5           | 0.10          | Valid                 |
| 17   | 199999 | 5           | 0.10          | Valid                 |
| 18   | 200000 | 5           | 0.10          | Valid                 |
| 19   | 200001 | 5           | 0.10          | Invalid cost          |

------

## c. Worst-case Boundary Value Test Cases

Worst-case BVT 不再使用 single fault assumption，而是假设多个变量可以同时取边界值，所以要做笛卡尔积。

每个变量使用 5 个 normal boundary values：

Cost set:

```
C = {1000, 1001, 100000, 199999, 200000}
```

Loan period set:

```
L = {1, 2, 5, 9, 10}
```

Interest rate set:

```
R = {0.01, 0.02, 0.10, 0.19, 0.20}
```

Test suite:

```
T = C × L × R
```

Number of test cases:

```
5^3 = 125
```

所以测试用例就是所有 `(Cost, Loan period, Interest rate)` 的组合，例如：

| Case | Cost   | Loan period | Interest rate | Expected result |
| ---- | ------ | ----------- | ------------- | --------------- |
| 1    | 1000   | 1           | 0.01          | Valid           |
| 2    | 1000   | 1           | 0.02          | Valid           |
| 3    | 1000   | 1           | 0.10          | Valid           |
| 4    | 1000   | 1           | 0.19          | Valid           |
| 5    | 1000   | 1           | 0.20          | Valid           |
| ...  | ...    | ...         | ...           | ...             |
| 125  | 200000 | 10          | 0.20          | Valid           |

考试里不一定需要手写 125 行，通常写清楚 **Cartesian product** 和数量即可。

------

## d. Robust Worst-case Boundary Value Test Cases

每个变量使用 7 个 robust boundary values：

Cost set:

```
C' = {999, 1000, 1001, 100000, 199999, 200000, 200001}
```

Loan period set:

```
L' = {0, 1, 2, 5, 9, 10, 11}
```

Interest rate set:

```
R' = {0, 0.01, 0.02, 0.10, 0.19, 0.20, 0.21}
```

Test suite:

```
T = C' × L' × R'
```

Number of test cases:

```
7^3 = 343
```

Expected result：只要任意一个输入超出合法范围，就应该返回 invalid input / error message；只有三个输入都在合法范围内，才计算 monthly payment。

------

# Question 2：Equivalence Class Testing

题目给出的有效范围是：

```
1000 <= x1 <= 10000
10-year <= x2 <= 50-year
```

有效等价类：

```
x1:
V1 = [1000, 5000]
V2 = [5001, 10000]

x2:
V3 = [10, 19]
V4 = [20, 29]
V5 = [30, 50]
```

课件中说明，等价类测试通过从每个 equivalence class 中选择一个代表值来减少冗余测试；Weak Normal 的目标是让每个等价类至少被覆盖一次，不要求覆盖所有组合。最少测试数量等于分区数量最多的那个变量的等价类数量。

------

## a. Weak Normal Equivalence Class Testing

x1 有 2 个有效等价类，x2 有 3 个有效等价类。
 所以最少测试用例数量：

```
max(2, 3) = 3
```

可以选择代表值：

```
V1: x1 = 3000
V2: x1 = 7500

V3: x2 = 15
V4: x2 = 25
V5: x2 = 40
```

为了让每个 class 至少出现一次，可以设计：

| Test case | x1 class | x1 value | x2 class | x2 value |
| --------- | -------- | -------- | -------- | -------- |
| TC1       | V1       | 3000     | V3       | 15       |
| TC2       | V2       | 7500     | V4       | 25       |
| TC3       | V1       | 3000     | V5       | 40       |

Graphical representation 可以理解为：

```
          x2
          ↑
V5 [30-50]        ● TC3
V4 [20-29]              ● TC2
V3 [10-19]        ● TC1
          └────────────────→ x1
              V1          V2
          [1000-5000] [5001-10000]
```

注意：Weak Normal 不需要覆盖所有组合，所以不是 2 × 3 = 6 个测试，而是只要 3 个就能覆盖所有等价类。

------

## b. Why Strong Normal generates more test cases?

Strong Normal Equivalence Class Testing 会生成更多测试用例，因为它要求测试 **所有有效等价类组合**，也就是使用笛卡尔积。

Weak Normal 只要求每个等价类至少出现一次：

```
Number = max(number of classes per variable)
```

Strong Normal 要求所有组合都被测试：

```
Number = number of x1 classes × number of x2 classes
       = 2 × 3
       = 6
```

所以 Strong Normal 的测试用例是：

| Test case | x1 class | x2 class |
| --------- | -------- | -------- |
| TC1       | V1       | V3       |
| TC2       | V1       | V4       |
| TC3       | V1       | V5       |
| TC4       | V2       | V3       |
| TC5       | V2       | V4       |
| TC6       | V2       | V5       |

简单来说，Weak Normal 是“每个 class 至少出现一次”，Strong Normal 是“每个 class 的组合都要出现”。

------

## c. Robustness Testing Equivalence Classes

Robust equivalence class testing 要加入无效等价类，也就是低于最小值和高于最大值的输入。课件中说明，Robust Equivalence Class Testing 会在 normal equivalence classes 外额外加入 out-of-range classes。

对于 x1：

| Class | Range               | Type    |
| ----- | ------------------- | ------- |
| I1    | x1 < 1000           | Invalid |
| V1    | 1000 <= x1 <= 5000  | Valid   |
| V2    | 5001 <= x1 <= 10000 | Valid   |
| I2    | x1 > 10000          | Invalid |

对于 x2：

| Class | Range          | Type    |
| ----- | -------------- | ------- |
| I3    | x2 < 10        | Invalid |
| V3    | 10 <= x2 <= 19 | Valid   |
| V4    | 20 <= x2 <= 29 | Valid   |
| V5    | 30 <= x2 <= 50 | Valid   |
| I4    | x2 > 50        | Invalid |

------

## d. Weak Robust Equivalence Class Testing

Weak Robust 和 Weak Normal 类似，但还要让每个 invalid class 至少被覆盖一次。并且通常一次只让一个变量无效，另一个变量保持有效，这样可以更清楚地判断错误来源。

有效类最少覆盖：

| Test case | x1   | x2   | Covered classes |
| --------- | ---- | ---- | --------------- |
| TC1       | 3000 | 15   | V1, V3          |
| TC2       | 7500 | 25   | V2, V4          |
| TC3       | 3000 | 40   | V1, V5          |

加入 invalid class：

| Test case | x1    | x2   | Covered classes | Expected result |
| --------- | ----- | ---- | --------------- | --------------- |
| TC4       | 999   | 25   | I1, V4          | Invalid x1      |
| TC5       | 10001 | 25   | I2, V4          | Invalid x1      |
| TC6       | 3000  | 9    | V1, I3          | Invalid x2      |
| TC7       | 3000  | 51   | V1, I4          | Invalid x2      |

所以 Weak Robust 最少可以设计为 **7 个测试用例**：

```
3 valid coverage cases + 4 invalid coverage cases = 7
```

Graphical representation：

```
                  x2
                  ↑
I4  x2>50          ● TC7
V5  [30-50]        ● TC3
V4  [20-29]   ● TC4     ● TC2     ● TC5
V3  [10-19]        ● TC1
I3  x2<10          ● TC6
                  └────────────────────────→ x1
                    I1      V1       V2      I2
                  <1000  [1000-5000] [5001-10000] >10000
```

------

# Question 3：Decision Table Based Testing

题目要求为 shipping cost 系统创建 decision table。课件中说明，Decision Table 可以精确并且紧凑地表达复杂逻辑，它可以把多个 independent conditions 和多个 actions 组合起来，也容易检查是否覆盖了所有可能情况。

这里有 3 个条件：

```
Item type: Fragile / Non-Fragile
Shipping method: Standard / Express / Overnight
Order price: Below $50 / $50-$100 / Above $100
```

理论组合数量：

```
2 × 3 × 3 = 18 rules
```

但是因为 **Above $100 always gets free shipping regardless of item type or shipping method**，所以可以压缩成一个规则。下面给出 compact decision table。

## Decision Table

| Rule | Item type   | Shipping method | Order price | Base shipping | Handling fee | Total shipping cost |
| ---- | ----------- | --------------- | ----------- | ------------- | ------------ | ------------------- |
| R1   | Non-Fragile | Standard        | Below $50   | 5             | 5            | 10                  |
| R2   | Fragile     | Standard        | Below $50   | 10            | 5            | 15                  |
| R3   | Non-Fragile | Express         | Below $50   | 10            | 5            | 15                  |
| R4   | Fragile     | Express         | Below $50   | 15            | 5            | 20                  |
| R5   | Non-Fragile | Overnight       | Below $50   | 20            | 5            | 25                  |
| R6   | Fragile     | Overnight       | Below $50   | 25            | 5            | 30                  |
| R7   | Non-Fragile | Standard        | $50-$100    | 5             | 0            | 5                   |
| R8   | Fragile     | Standard        | $50-$100    | 10            | 0            | 10                  |
| R9   | Non-Fragile | Express         | $50-$100    | 10            | 0            | 10                  |
| R10  | Fragile     | Express         | $50-$100    | 15            | 0            | 15                  |
| R11  | Non-Fragile | Overnight       | $50-$100    | 20            | 0            | 20                  |
| R12  | Fragile     | Overnight       | $50-$100    | 25            | 0            | 25                  |
| R13  | Any         | Any             | Above $100  | 0             | 0            | 0                   |

------

## How to convert this decision table into test cases

每一列 / 每一条 rule 都可以转换成一个 test case。也就是说，每个 test case 选择一个具体输入组合，然后检查系统输出的 shipping cost 是否等于 expected total。

例如：

| Test case | Item type   | Shipping method | Order price | Expected output |
| --------- | ----------- | --------------- | ----------- | --------------- |
| TC1       | Non-Fragile | Standard        | 40          | 10              |
| TC2       | Fragile     | Standard        | 40          | 15              |
| TC3       | Non-Fragile | Express         | 40          | 15              |
| TC4       | Fragile     | Express         | 40          | 20              |
| TC5       | Non-Fragile | Overnight       | 40          | 25              |
| TC6       | Fragile     | Overnight       | 40          | 30              |
| TC7       | Non-Fragile | Standard        | 75          | 5               |
| TC8       | Fragile     | Standard        | 75          | 10              |
| TC9       | Non-Fragile | Express         | 75          | 10              |
| TC10      | Fragile     | Express         | 75          | 15              |
| TC11      | Non-Fragile | Overnight       | 75          | 20              |
| TC12      | Fragile     | Overnight       | 75          | 25              |
| TC13      | Fragile     | Overnight       | 120         | 0               |
| TC14      | Non-Fragile | Standard        | 120         | 0               |

这里 TC13 和 TC14 是为了确认 “Above $100 free shipping regardless of item type or shipping method” 真的生效。严格来说 R13 可以只用一个测试用例，但考试里多给一个不同 item type / method 的例子，会让答案更完整。