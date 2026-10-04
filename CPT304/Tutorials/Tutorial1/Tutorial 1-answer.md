# Tutorial – Week 1: Essence and Accidents of Software Engineering 

1. Categorize each as either an **Essential Difficulty** or an **Accidental Difficulty**, and provide a brief justification
   
   判断下面的案例是本质困难还是附属困难。
   
   - Determining the interlocking business rules for a cross-border tax calculation engine.
   
     确定跨境税务计算引擎的互锁业务规则。
   
     - **分类**: 本质困难 (Essential Difficulty)。
     - **理由**: 软件实体的本质正是由联锁概念（如数据集、关系、算法）构成的抽象结构 。处理复杂的业务逻辑属于梳理这些互锁概念的固有困难 。
   
   - Configuring the YAML files for a Kubernetes cluster to ensure high availability.
   
     配置Kubernetes集群的YAML文件以确保高可用性。
   
     - **分类**: 附属困难 (Accidental Difficulty)。
     - **理由**: 这是在表达和实现概念结构时所付出的劳动，并不是软件概念本身固有的困难 。它属于特定工具和格式（如语法）带来的附属复杂性 。
   
   - Resolving a "Segmentation Fault" caused by manual memory management in C++.
   
     解决 C++ 中手动内存管理引起的“段错误”
   
     - **分类**: 附属困难 (Accidental Difficulty)。
   
     - **理由**: 这涉及具体机器程序底层的关注点，例如位、寄存器、状态等 。使用更高级的语言本可以消除这种完全不属于程序本质的复杂性 。
   
   - Mapping out the conflicting requirements between three different stakeholders for a new hospital management system.
   
     梳理新医院管理系统中三个不同利益相关者之间冲突的需求
   
     - **分类**: 本质困难 (Essential Difficulty)。
     - **理由**: 构建软件系统最困难的部分就是确切地决定到底要构建什么 。确立详细的技术需求（包括所有的接口），并且提炼客户的实际要求，是概念构建中最难的工作 。
   
   - Optimizing the syntax of a Python script to run faster on a specific legacy processor.
   
     优化 Python 脚本的语法以在特定的旧处理器上运行得更快
   
     - **分类**: 附属困难 (Accidental Difficulty)。
     - **理由**: 处理语法和克服底层硬件的速度限制，属于目前伴随着软件生产过程的附属困难 。这与软件设计的抽象本质无关 。 

2. What is software crisis?

   文章中描述了让非技术管理人员感到恐惧的现状：看似简单且无害的软件项目，很容易意外变成导致错失进度、预算超支以及产品存在缺陷的“怪物”。人们迫切希望有一种“银弹”让软件的成本向计算机硬件的成本那样迅速下降（摩尔定律）。

3. Define essential difficulties and accidental difficulties in the context of software engineering. Provide two examples of each type of difficulty.

   定义本质困难和附属困难。并且为每一个困难类型选择两个案例。

   - **本质困难 (Essential Difficulties)**:

     - **定义**: 存在于软件自身性质中的固有困难，其核心在于构建由数据集、算法和函数调用等联锁概念组成的抽象实体 。
     - **示例**:
       - **复杂性 (Complexity)**：软件系统的扩展会导致不同元素数量增加，且元素间的非线性交互使得整体复杂度的增加远超线性 。
       - **不可见性 (Invisibility)**：软件没有内在的空间嵌入性，因此无法用单一的几何图形（如建筑平面图）来直观地表示其全部结构 。

     **附属困难 (Accidental Difficulties)**:

     - **定义**: 目前伴随软件生产过程产生，但并非软件概念本质所固有的困难 。主要是在表达抽象设计以及测试表达保真度时的劳动 。
     - **示例**:
       - **机器语言复杂性**: 在缺乏高级语言时，程序员需要关心位、寄存器、磁盘通道等底层细节 。
       - **批处理的缓慢周转时间**: 在分时系统普及前，缓慢的编译和执行等待会导致程序员遗忘复杂的思维细节 。

4. Software complexity leads to many difficulties, what are they? 软件复杂性导致的困难。

   - 团队成员之间沟通困难 。

     Difficult communication among team members.

   - 沟通困难进一步导致产品缺陷、成本超支和进度延迟 。

     Communication difficulties further lead to product defects, cost overruns, and project delays.

   - 难以列举更难以理解程序的所有可能状态 。

   - 无法掌握所有状态导致了软件的不可靠性 。

   - 功能复杂性导致调用功能困难，从而使程序变得难以使用 。

   - 结构复杂性使得在不产生副作用的情况下扩展程序变得非常困难 。

   - 结构复杂性中存在未被可视化的状态，从而构成了安全隐患（陷门） 。

   - 带来了管理问题，使得系统难以进行全局概览并阻碍概念完整性 。

   - 产生了巨大的学习和理解负担，这使得人员流失成为一场灾难 。

5. In your opinion, why is software perceived as the most conformable element?

   为什么软件被认为是最容易顺应（Conformable）的元素？

   - 在许多情况下，软件必须顺应外界的各种接口，因为它是场景中最晚到达的元素 。

     In many cases, software must adapt to various external interfaces because it is the last element to arrive in the scenario.

   - 在其他情况下，软件必须顺应，因为它本身就被人们认为是最容易被调整和顺应的元素 。

   - 因为软件是纯粹的思想材料（pure thought-stuff），具有无限的可塑性，所以比那些有形成本高昂的建筑或硬件更容易被改变 。

     Because software is purely a material of thought (**pure thought-stuff**) with infinite **malleability**, it is much easier to change than tangible, high-cost constructions like buildings or hardware.

6. Brooks suggests that software development is inherently hard, and advances in programming languages, tools, or development environments can only offer limited improvements in productivity. Evaluate this claim in the context of modern software engineering practices and technologies.

   Brooks 指出，软件开发本质上就是一项艰巨的任务。有关编程语言，工具，开发环境的进步只能为软件开发带来生产效率上的微小提升。

   - 过去的重大技术突破（如高级语言、分时系统和统一编程环境）之所有效，是因为它们攻克了软件开发中的“附属困难” 。例如，高级语言让程序摆脱了底层机器的偶然复杂性 。
   - 但是，一旦这些附属困难被消除，剩余的绝大部分工作都是概念设计的“本质困难” 。
   - 在现代软件工程中，任何仅仅旨在消除设计“表达”障碍的技术（如面向对象编程或高级语言环境），都不能改变设计本身的复杂性 。
   - 既然构思这些概念结构占用了大部分时间，那么仅仅优化“表达概念”的任务，就注定只能带来边际上的生产力增益，而无法实现数量级的跃升 。

7. Is there any possible “silver bullet”? What are they?

   现如今是否真的存在一些“银弹”，请提供案例。

   -  在技术或管理技术方面，并没有任何单一的发展本身可以承诺带来哪怕是一个数量级的改进（即没有绝对的银弹） 。
   - 但是，存在一些针对软件“概念本质”的有效攻击策略（即有希望的道路）：
     - **购买而非构建 (Buy versus build)**: 尽可能利用大众市场购买现成的软件，极大地降低开发成本 。
     - **需求细化与快速原型设计 (Requirements refinement and rapid prototyping)**: 由于客户通常不知道自己想要什么，可以通过原型系统来迭代地提取和验证需求 。
     - **增量开发 (Incremental development)**: 软件不应该被像建筑一样“建造”，而是应该让系统先运行起来，然后像生物一样一步步地自顶向下“生长” 。
     - **培养伟大的设计师 (Great designers)**: 认识到伟大的设计来源于伟大的设计师，组织应该像培养管理人员一样尽最大努力识别和培养顶尖的设计人员 。

8. How do you summarize the essay?

   - 软件项目经常饱受进度延误、预算超支之苦，人们迫切需要一种像银弹一样的解决方案来降低成本 。

   - Brooks 认为这种银弹不存在，因为软件工程中存在不可消除的“本质困难”，即软件固有的复杂性、顺应性、可变性和不可见性 。

   - 过去诸如高级语言等技术突破虽然带来了数倍的生产力提升，但它们解决的仅仅是脱离底层硬件的“附属困难” 。

   - 要实现下一步的飞跃，必须放弃寻找单一的神奇技术，转而直面本质困难。这要求采用购买现成软件、快速原型迭代、增量式“生长”软件等方法，并且最关键的是要用心培养伟大的软件设计师 。

9. Discuss how contemporary practices like Agile and AI-enhanced tools are used to tackle essential difficulties identified by Fredrick Brooks.

   讨论当代的技术手段，例如敏捷开发或者 AI 增强工具是如何被使用去应对 Essential Difficulties 的？

   **敏捷开发 (Agile)**:

   - 敏捷方法的核心完全契合 Brooks 倡导的“快速原型设计”和“增量开发”策略。Brooks 认为，客户甚至在尝试软件的初始版本之前，根本不可能准确指出要求 。敏捷通过短周期迭代和原型交付，直接攻击了“确切决定要构建什么”这个最难的本质问题 。
   - 同时，由于现在的概念结构过于复杂以至于无法一次性完美构建 ，敏捷倡导的持续集成与迭代实际上就是 Brooks 所说的让软件有机地“生长”，这在极大程度上激发了士气并降低了复杂性风险 。

   **AI 增强工具 (AI-enhanced tools)**:

   - Brooks 指出，构建软件的难点在于决定“要表达什么”，而不是“如何表达”，因此他怀疑通用 AI （比如自动编程）能带来颠覆性突破 。
   - 不过，他认可了专家系统（AI 技术的子集）的应用潜力 。他认为 AI 可以充当“顾问”，如提供接口规则建议、测试策略，或是将最优秀程序员的经验提供给缺乏经验的开发者使用 。这在今天演变为了 AI 辅助编程工具（如代码补全、架构建议），它们虽然没有消除核心业务逻辑的复杂性，但在传播最佳实践、减少构建错误方向上起到了巨大的辅助作用 。



 

 

 