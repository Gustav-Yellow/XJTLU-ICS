## Lab 2

Note that there is only one set of data (inputs + target output) for each problem because we are only going to train the perceptron. Of course, in a real world problem, you would want to use at least two data sets — one for training, and one for testing. If you look at t1 and t2, you will see that in each problem there are two classes.

请注意，每个问题仅有一组数据（输入+目标输出），因为我们仅需训练感知机。当然，在实际问题中，通常至少需要两个数据集，一个用于训练，另一个用于测试。观察t1和t2可知，每个问题均包含两个类别。

Plot the training examples using different colours or symbols for each class, e.g., 

使用不同颜色或符号为每个类别的训练样本绘制图形，例如，

```matlab
>> plot (p1(1,1:50), p1(2,1:50), ’b+’, p1(1,51:100), p1(2,51:100), ’ro’)
```

> `p1` 是一个 **2×100** 的矩阵：每一列是一条二维样本（x、y），然后有 100 个样本
>
> `p1(1,1:50)`：前 50 个样本的 **x 坐标**；`p1(2,1:50)`：对应的 **y 坐标**
>  → 用 `'b+'`（蓝色加号）画出来。
>
> `p1(1,51:100)` 与 `p1(2,51:100)`：后 50 个样本的 x、y
>  → 用 `'ro'`（红色空心圆）画出来。

The function **newp** from neural network toolbox requires an argument which specifies the expected range for each of the inputs in the input vector. The function **minmax** can be used for this purpose, as follows:

神经网络工具箱中的 **newp** 函数需要一个参数，该参数用于指定输入向量中每个输入值的预期范围。为此，可使用 **minmax** 函数，具体使用方法如下：

```matlab
>> mm = minmax(p1);
>> net = newp(mm,1);
```

> - `minmax(p1)`：计算 **每个输入维度**（这里是两维）在整个数据集上的最小值与最大值，得到一个 **2×2** 的范围矩阵（每一行对应一个维度：`[min max]`）。
>    这相当于告诉网络“输入大致会落在哪个范围内”。
> - `newp(mm,1)`：按给定输入范围 `mm`，创建一个**单输出**的感知器（Perceptron）。
>    感知器结构：输入权重 `IW{1}`（1×2）、偏置 `b{1}`（标量），激活函数是阶跃函数（hardlim）。

The above steps will automatically work out the correct range for each input, and then create a new perceptron with one neuron (and therefore one output).

上述步骤将自动计算每个输入的正确范围，随后创建一个包含一个神经元（因此仅有一个输出）的新感知器。

Now train the perceptron using the provided m-function **trainp_sh** as follows:

使用提供的m函数 **trainp_sh** 训练感知器的方法如下：

```matlab
% trainp_sh 代码
function net = trainp_sh(net, p, t, neps)
% net = trainp_sh(net, p, t, neps)
% Trains a perceptron with two inputs and shows the decision
% boundary after each epoch.
% Input
%  net  - perceptron
%  p    - Two-dimensional input vectors
%  t    - One dimensional target vectors (0 or 1)
%  neps - number of epochs to train, optional DEFAULT = 100
% Return
%  net - the trained perceptron

%nargin returns the number of arguments input when the function is called.
if nargin<4 
  neps = 100;
end

plotpv(p, t); % 把样本点按标签画在平面上（和你那句 plot 类似）
h = plotpc(net.IW{1}, net.b{1}); % 画出当前感知器的“决策边界”直线
e = 1; 
ep = 0;
while sum(abs(e))>0 & ep<neps, % while error still exists and the number of epochs not reached
  [net, y, e, pf, af, ar] = adapt(net, p, t); % 执行感知器学习规则进行一轮权重更新，并返回
  h = plotpc(net.IW{1},net.b{1}, h); % 用新的 w,b 更新那条分类线
  drawnow;							 % 立即刷新图像
  ep = ep + 1;
end
```

引用训练

```matlab
>> net = trainp_sh(net, p1, t1, 1);
```

The last argument to trainp_sh, the number of epochs (training steps) should be set to

trainp_sh 函数的最后一个参数，即训练轮数（训练步数），应设为一个比较大的值才能更直观地感受到分割线变化

1. This function will also update the graphical display, showing the decision line as well as the training examples.

   此函数还将更新图形显示，呈现决策线及训练样本。

For each of the two classification problems, plot the training examples and create a new perceptron, as described above. Then, do successive calls to trainp_sh and study the graph (resize the Matlab window so that you can watch the graph at the same time). 

对于两个分类问题中的每一个，绘制训练样本并创建一个新的感知器，如上所述。随后，连续调用trainp_sh函数，同时观察图形变化（调整Matlab窗口大小以便实时查看图形）。

Once you get the general idea of what’s happening, you can set the number of epochs to a higher number so that things go a little faster.

一旦你大致理解了当前情况，便可将训练周期数设定得更高，以加快进程。

Consider the following question (for both data sets): 

请思考以下问题（适用于两个数据集）：

[1] Is the perceptron able to classify all training vectors correctly after training? If not, why?

感知机训练后能否正确分类所有训练向量？如若不能，原因何在？



## Exercise 2

Design a perceptron with one output to decide if a digit represented by binary pattern is even or odd. 

设计一个具有单一输出的感知器，用于判断以二进制模式表示的数字是偶数还是奇数。

The 10 digits from 0 to 9 with the corresponding binary pattern is shown as the vectors below:

0至9这十个数字对应的二进制模式以如下向量形式展示：

<img src="D:\Applications\BaiduNetdisk\BaiduSyncdisk\Y4_S1\INT301-Bio_Computation\Notes\imgs\week2\img1.png" style="zoom:75%;" />

1. Use the vectors given in above table as the training data, together with their corresponding targets (0 for odd and 1 for even), train a perceptron by applying the Matlab Neural Network Toolbox.

   使用上表中给定的向量作为训练数据，以及它们对应的目标值（奇数为0，偶数为1），通过应用Matlab神经网络工具箱训练一个感知器。

2. Note the performance of training error within 10 epochs;

   请注意训练误差在10个周期内的表现。

3. After the training complete, test the following two patterns to see if the perceptron’s outputs are correct.

   训练完成后，请测试以下两种模式以验证感知器的输出是否正确。

```matlab
ptest = [1 1 1 1 0 1 1 0 1 1 0 1 1 0 1;
		1 1 0 0 1 0 0 1 1 0 1 0 1 1 1];
```



## 补充知识

在 MATLAB 的 **感知器工具箱**里，约定是这样的：

- **输入矩阵 P**：
  - 大小是 **R × Q**
  - **R** = 输入向量的维数（每个样本有多少个特征）
  - **Q** = 样本的个数（总共有多少个样本）
- **目标矩阵 T**：
  - 大小是 **S × Q**
  - **S** = 输出维数（这里是单一输出 → S=1）
  - **Q** = 样本的个数（必须和输入的样本数一致）

P(:, 1) 代表第 1 个样本的输入向量（数字 0 的 15 维模式）所以按照上面 P = 15 ✕ 10 的格式来说，P(:, 1)就是代表整个第一列的数据

