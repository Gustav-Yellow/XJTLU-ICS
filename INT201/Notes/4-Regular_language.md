# Regular language 正则语言

## Definition 定义

Previous: A language is regular if it is recognized by some **DFA**

上一篇： 如果一种语言被某些 **DFA 识别** ，则该语言是常规的

Now: A language is regular if and only if some **NFA** recognizes it.

现在：当且仅当某些 **NFA** 识别出一种语言时，它才是常规的

Some operations on languages: Union, Concatenation and Kleene star

对语言的一些操作：Union、Concatenation 和 Kleene star

## Closed under operation

A collection S of objects is **closed** under operation *f* if applying *f* to members of S always returns an object still in S.

如果对 S 的成员应用 *f* 总是返回仍在 S 中的对象，则对象的集合 S 在操作 *f* 下是 **关闭的**。

Regular languages are indeed closed under the regular operations (e.g. union, concatenation, star …)

常规语言在常规操作下确实是封闭的（例如 union、concatenation、star ...）

## Regular Languages Closed Under Union

**The set of regular languages is closed under the union operation.**

常规语言集在 union 操作下关闭。

- i.e. A and B are regular languages over the same alphabet Σ, then A∪B is also a regular language.

  即 A 和 B 是同一字母 Σ 上的常规语言，那幺 A∪B 也是一种常规语言。

Proof:

- Since A and B are regular languages, there are finite automata M1 = (*Q<sub>1</sub>* *,* Σ*, δ<sub>1</sub>* *,q<sub>1</sub>* *, F<sub>1</sub>* ) and M2 = (*Q<sub>2</sub>* *,* Σ*, δ<sub>2</sub>* *, q<sub>2</sub>* *, F<sub>2</sub>* ) that accept A and B, respectively.

  由于 A 和 B 是常规语言，因此存在有限自动机 M1 = （*Q<sub>1</sub>* *，* Σ*， δ<sub>1</sub>* *，q<sub>1</sub>* *， F<sub>1</sub>* ） 和 M2 = （*Q<sub>2</sub>* *，* Σ*， δ<sub>2</sub>* *、q<sub>2</sub>* *、F<sub>2</sub>* ），分别接受 A 和 B。

- In order to prove that A ∪ B is regular, we have to construct a finite automaton M that accepts A ∪ B. In other words, M must have the property that for every string w ∈ Σ* :

  为了证明 A ∪ B 是正则的，我们必须构造一个接受 A ∪ B 的有限自动机 M。换句话说， M 必须具有对于每个字符串 w ∈ Σ* 的属性：

Continue to proof

Given M1 and M2 that A = L(M1 ) and B = L(M2 ), we can define M = (*Q,* Σ*, δ, q, F*):

给定 M1 和 M2 ，其中 A = L（M1 ） 和 B = L（M2 ），我们可以定义 M = （*Q，* Σ*， δ， q， F*）：

- *Q = Q<sub>1</sub>* × *Q<sub>2</sub>* *=* {(*q<sub>1</sub>,* *q<sub>2</sub>* ): *q<sub>1</sub>*∈ *Q<sub>1</sub>* and *q<sub>2</sub>* ∈ *Q<sub>2</sub>* }
- Σ is same as the alphabet of A and B
- *q =* (*q<sub>1</sub>,* *q<sub>2</sub>* )
- *F =* {(*q<sub>1</sub>,* *q<sub>2</sub>* ): *q<sub>1</sub>*∈ *Q<sub>1</sub>* or *q<sub>2</sub>* ∈ *Q<sub>2</sub>* }

- *δ* : *Q* × Σ → *Q*

  *δ*((*q<sub>1</sub>,* *q<sub>2</sub>* ), *a*) = (*δ*(*q<sub>1</sub>* , *a*) , *δ*(*q<sub>2</sub>* , *a*)), *a* ∈ Σ

Continue to proof

- *δ* * ((*q<sub>1</sub>,* *q<sub>2</sub>* ), *w*) = (*δ* * (*q<sub>1</sub>* , *w*) , *δ* * (*q<sub>2</sub>* , *w*))

- *δ* * ((q<sub>1</sub>, q<sub>2</sub> ), *w*) ∈ *F* ⇔ *δ* * (*q<sub>1</sub>* , *w*) ∈ *F<sub>1</sub>* or *δ* * (*q<sub>2</sub>* , *w*) ∈ *F<sub>2</sub>*

- M accepts *w* ⇔ *δ* * (*q<sub>1</sub>* , *w*) ∈ *F<sub>1</sub>* or *δ* * (*q<sub>2</sub>* , *w*) ∈ F2

- M accepts *w* ⇔ M<sub>1</sub> accepts *w* or M<sub>2</sub> accepts *w*

Proved



**Example:**

Consider the following DFAs and languages over Σ = {*a*, *b*}:

DFA M<sub>1</sub> recognizes A<sub>1</sub> = L(M<sub>1</sub>)

DFA M<sub>2</sub> recognizes A<sub>2</sub> = L(M<sub>2</sub>)

<img src="imgs/week4/img1.png" style="zoom:50%;" />

**DFA M for A1∪ A2 ?**

Example2:



**How to prove this from the perspective of NFA?**

**如何从 NFA 的角度证明这一点？**

Proof

Consider the following NFAs:

NFA M1 = (*Q<sub>1</sub>* *,* Σ*, δ<sub>1</sub>* *, q<sub>1</sub>* *, F<sub>1</sub>* ) recognizes A<sub>1</sub> = L(M<sub>1</sub>)

NFA M2 = (*Q<sub>2</sub>* *,* Σ*, δ<sub>2</sub>* *, q<sub>2</sub>* *, F<sub>2</sub>* ) recognizes A<sub>2</sub> = L(M<sub>2</sub>)

We will construct an NFA M = (*Q,* Σ*, δ, q, F*)

- *Q =* {*q<sub>0</sub>* }∪ *Q<sub>1</sub>* ∪ *Q<sub>2</sub>*
- *q<sub>0</sub>* is the start state of M
- *F* = *F<sub>1</sub>* ∪ *F<sub>2</sub>*
- *δ* : *Q* × Σϵ → *P*(*Q*) is defined as: For any *r* ∈ *Q* and for any *a* ∈ Σϵ

<img src="imgs/week4/img2.png" style="zoom:50%;" />

Proof:





## Regular Languages Closed Under Concatenation

The concatenation of A1 and A2 is defined as:

A1 和 A2 中的串联定义为：

- A<sub>1</sub> A<sub>2</sub> = {*ww′* : *w* ∈ A<sub>1</sub> and *w′* ∈ A<sub>2</sub> }

Proof

Consider the following NFAs:

NFA M1 = (*Q<sub>1</sub>* *,* Σ*, δ<sub>1</sub>* *, q<sub>1</sub>* *, F<sub>1</sub>* ) recognizes A<sub>1</sub> = L(M<sub>1</sub>)

NFA M2 = (*Q<sub>2</sub>* *,* Σ*, δ<sub>2</sub>* *, q<sub>2</sub>* *, F<sub>2</sub>* ) recognizes A<sub>2</sub> = L(M<sub>2</sub>)

We will construct an NFA M = (*Q,* Σ*, δ, q, F*) for A<sub>1</sub> A<sub>2</sub>

- *Q = Q<sub>1</sub>* ∪ *Q<sub>2</sub>*
- M has the same start state as M<sub>1</sub> : *q<sub>1</sub>*
- Set of accept states of M is same as M<sub>2</sub> : *F<sub>2</sub>*
- *δ* : *Q* × Σϵ → *P*(*Q*) is defined as: For any *r* ∈ *Q* and for any *a* ∈ Σ<sub>ε</sub>

<img src="imgs/week4/img3.png" style="zoom:50%;" />

Proof:





## Regular Languages Closed Under Kleene star

The star of A is defined as:

- A * = {*u<sub>1</sub>* *u<sub>2</sub>* . . . *u<sub>k</sub>* : *k* ≥ *0* and *u<sub>i</sub>* ∈ **A** for all *i = 1, 2, . . . , k*}

Proof:

Consider the following NFA:

NFA M1 = (*Q<sub>1</sub>* *,* Σ*, δ<sub>1</sub>* *, q<sub>1</sub>*, F<sub>1</sub>* ) recognizes A = L(M<sub>1</sub>)

We will construct an NFA M = (*Q,* Σ*, δ, q, F*) for A*

- *Q =* {*q<sub>0</sub>* }∪ *Q<sub>1</sub>*

- *q<sub>0</sub>* is the start state of M

- *F =* {*q<sub>0</sub>* }∪ *F<sub>1</sub>*

- *δ* : *Q* × Σϵ → *P*(*Q*) is defined as: For any *r* ∈ *Q* and for any *a* ∈ Σϵ

<img src="imgs/week4/img4.png" style="zoom:50%;" />

Proof





## Regular Languages Closed Under Complement and Interaction

The set of regular languages is closed under the complement and interaction operations:

常规语言集在 complement 和 interaction 操作下是封闭的：

- If A is a regular language over the alphabet Σ, then the complement:
  - <img src="imgs/week4/img5.png" style="zoom:50%;" />  is also a regular language.

- If A1 and A2 are regular languages over the same alphabet Σ, then the interaction:

  如果 A1 和 A2 是同一字母 Σ 上的常规语言，则交互作用：

  - A<sub>1</sub> ∩ A<sub>2</sub> = {*w* ∈ Σ<sup>∗</sup>: *w* ∈ A<sub>1</sub> and *w* ∈ A<sub>2</sub> }  is also a regular language.

## Regular expression

Regular expressions are means to describe certain languages.

正则表达式是描述某些语言的手段。

**Example:**

Consider the expression:

- (0∪1)01<sup>*</sup>

The language described by this expression is the set of all binary strings satisfy:

此表达式描述的语言是满足以下条件的所有二进制字符串的集合：

- that start with either 0 or 1 (this is indicated by (0 ∪ 1) ),

  以 0 或 1 开头（由 （0 ∪ 1） 表示），

- for which the second symbol is 0 (this is indicated by 0),

  第二个符号为 0（用 0 表示），

- that end with zero or more 1s (this is indicated by 1<sup>∗</sup>).

  以零个或多个 1 结尾（用 1∗ 表示）。

Further examples:

- The language {*w* : *w* contains exactly two 0s} is described by the expression:

  语言 {*w* ： *w* 正好包含两个 0} 由表达式描述：

- The language {*w* : *w* contains at least two 0s} is described by the expression:

  语言 {*w* ： *w* 包含至少两个 0} 由表达式描述：

- The language {*w* : 1011 is a substring of *w*} is described by the expression:

  语言 {*w* ： 1011 是 *w*} 的子字符串，由表达式描述：

### Formal Definition of regular expression

Let Σ be a non-empty alphabet.

设 Σ 为非空字母表。

1. *ϵ* is a regular expression.
2. ∅ is a regular expression.
3. For each *a* ∈ Σ, *a* is a regular expression.
4. If *R<sub>1</sub>* and *R<sub>2</sub>* are regular expressions, then *R<sub>1</sub>* *R<sub>2</sub>* is a regular expression.
5. If *R<sub>1</sub>* and *R<sub>2</sub>* are regular expressions, then *R<sub>1</sub>* *R<sub>2</sub>* is a regular expression.
6. If *R* is a regular expression, then R<sup>∗</sup> is a regular expression.

### Exercise:

Given (0∪1)<sup>\*</sup>101(0∪1)<sup>\*</sup>, prove it is a regular expression (note: Σ={0, 1}).

Further Definition:

If *R* is a regular expression, then L(*R*) is the **language** generated (or described or defined) by *R*.

如果 *R* 是一个正则表达式，那幺 L（*R*） 是由 *R* 生成（或描述或定义）的 **语言**。

**Formal Definition of regular expressions **正则表达式的正式定义

Let Σ be a non-empty alphabet. 

设 Σ 为非空字母表。

1. The regular expression *ϵ* describes the language {*ϵ*}. 
2. The regular expression ∅ describes the language ∅. 
3. For each *a* ∈ Σ, the regular expression a describes the language {*a*}. 
4. Let *R<sub>1</sub>* and *R<sub>2</sub>* be regular expressions and let L1 and L2 be the languages described by them, respectively. The regular expression *R<sub>1</sub>* ∪ *R<sub>2</sub>* describes the language L1 ∪ L2 . 

5. Let *R<sub>1</sub>* and *R<sub>2</sub>* be regular expressions and let L1 and L2 be the languages described by them, respectively. The regular expression R<sub>1</sub>R<sub>2</sub> describes the language L1L2 . 

6. Let R be a regular expression and let L be the language described by it. The regular expression R<sup>∗</sup> describes the language L∗.

Example；

Given a regular expression (0∪ *ϵ*) 1<sup>*</sup>, it describes the language:

<img src="imgs/week4/img6.png" style="zoom:50%;" />

- Observe that this language is also described by the regular expression 01<sup>\*</sup> ∪ 1<sup>\*</sup>