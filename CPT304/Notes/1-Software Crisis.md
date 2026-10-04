# 1 Software Crisis

## 知识图谱

考试重点主要是 handbook 上的 learning outcome 中的 A-E

The challenges and problems faced in software development, particularly in the 1960s and 1970s, when demand for complex software systems outpaced the ability to design, implement, and maintain them effectively.

软件开发所面临的挑战与问题，尤其是在20世纪60至70年代，当时对复杂软件系统的需求超过了有效设计、实现和维护它们的能力。

考试回答建议：Software Crisis is not only about programming difficulty. It refers to a broader management and engineering failure: software projects became too large and complex, but the industry lacked mature methods, processes, tools, and management practices to deliver them reliably.

```plaintext
├── 1. Software Crisis 软件危机
│ ├── 定义
│ │ ├── 软件开发中面临的挑战和问题
│ │ ├── 主要发生在 1960s–1970s
│ │ ├── 复杂软件系统需求增长过快
│ │ └── 人们设计、实现、维护软件的能力跟不上需求增长
│ │
│ ├── 1.1 Historical Context 历史背景
│ │ ├── 40s–50s：The Beginning of Computing
│ │ │ ├── 第一代电子计算机出现
│ │ │ ├── 例子：ENIAC、UNIVAC
│ │ │ ├── 主要用于 scientific applications
│ │ │ ├── 主要用于 military applications
│ │ │ └── 使用 machine language / assembly language
│ │ │ ├── time-consuming
│ │ │ └── error-prone
│ │ │
│ │ ├── 60s：The Beginning of Crisis
│ │ │ ├── commercial computing 兴起
│ │ │ ├── 企业需要更复杂的软件系统
│ │ │ │ ├── payroll system
│ │ │ │ └── inventory management system
│ │ │ ├── 大型项目失败开始出现
│ │ │ │ └── 例子：IBM OS/360
│ │ │ ├── 常见问题
│ │ │ │ ├── project delays
│ │ │ │ ├── budget overruns
│ │ │ │ └── software demand 与 development capability 差距扩大
│ │ │ └── 缺乏 standardized methodologies and processes
│ │ │
│ │ ├── 1968–1969：The Beginning of Software Engineering
│ │ │ ├── 1968 年提出 “Software Crisis”
│ │ │ ├── NATO Conference 承认软件行业存在严重问题
│ │ │ ├── 核心问题
│ │ │ │ ├── 不能按时交付 reliable software
│ │ │ │ ├── 不能在预算内交付 efficient software
│ │ │ │ └── 项目管理和开发方法不足
│ │ │ └── 呼吁建立新学科
│ │ │ ├── disciplined approach
│ │ │ └── software engineering 的基础形成
│ │ │
│ │ ├── 70s：Escalation and Response
│ │ │ ├── 系统越来越复杂
│ │ │ ├── 软件危机进一步加深
│ │ │ ├── 项目继续出现严重 overrun and failure
│ │ │ ├── 应对方式出现
│ │ │ │ ├── structured programming
│ │ │ │ └── Waterfall model
│ │ │ └── software maintenance 成为沉重负担
│ │ │ ├── 消耗大量 resources
│ │ │ └── 消耗大量 budgets
│ │ │
│ │ ├── The Impact of the Crisis 危机影响
│ │ │ ├── Economic Consequences
│ │ │ │ ├── failed projects 造成经济损失
│ │ │ │ └── inefficient software 造成公司财务损失
│ │ │ ├── Human Factors
│ │ │ │ ├── developers 面临 unrealistic deadlines
│ │ │ │ ├── developers 面临 unrealistic requirements
│ │ │ │ └── stress and burnout 变得常见
│ │ │ └── Technological Stagnation
│ │ │ ├── 无法交付 reliable software
│ │ │ └── 阻碍 technological progress and innovation
│ │ │
│ │ ├── The Path Forward 向前的道路
│ │ │ ├── Emergence of Software Engineering
│ │ │ │ └── 软件工程成为独立学科
│ │ │ ├── Focus on Quality and Process
│ │ │ │ ├── quality assurance practices
│ │ │ │ ├── project management techniques
│ │ │ │ └── process improvement models
│ │ │ └── Legacy and Lessons
│ │ │ ├── 理解 software complexity 很重要
│ │ │ ├── effective communication 很重要
│ │ │ └── methodologies 需要 continuous adaptation
│ │ │
│ │ └── Key Issues 主要问题
│ │ ├── Project overruns in time and budget
│ │ ├── Software fails to meet user requirements
│ │ ├── Poor quality and unreliable software
│ │ └── Maintenance challenges and escalating costs
│
├── 2. The Werewolf Appears：No Silver Bullet
│ ├── 2.1 No Silver Bullet 论文背景
│ │ ├── 全名：No Silver Bullet: Essence and Accidents of Software Engineering
│ │ ├── 作者：Frederick P. Brooks
│ │ ├── 发表时间：1986
│ │ └── 重要性：理解软件开发固有困难的经典论文
│ │
│ ├── 2.2 Core Thesis 核心观点
│ │ ├── 不存在单一 breakthrough
│ │ ├── 不存在一个 “silver bullet”
│ │ ├── 没有一种技术或管理方法可以在十年内让软件生产力或可靠性提升一个数量级
│ │ └── Brooks 区分了两类困难
│ │ ├── Essential difficulties
│ │ └── Accidental difficulties
│ │
│ ├── 2.3 Werewolf Metaphor 狼人隐喻
│ │ ├── 软件项目像 “werewolf”
│ │ ├── 表现为
│ │ │ ├── missed schedules
│ │ │ ├── blown budgets
│ │ │ └── flawed products
│ │ └── 人们希望找到 “silver bullet” 让软件成本像硬件成本一样快速下降
│ │
│ └── 2.4 Silver Bullet 的定义
│ ├── 一种单一技术或管理方法
│ ├── 能神奇地解决软件工程怪物问题
│ ├── 必须能单独带来至少一个数量级的提升
│ └── 提升方向包括
│ ├── productivity
│ ├── reliability
│ └── simplicity
│
├── 3. Essence vs Accident
│ ├── 3.1 Essence 本质困难
│ │ ├── 软件固有的、不可完全消除的困难
│ │ ├── 是 inherent and irreducible hard part
│ │ ├── 来自 abstract construct of interlocking concepts
│ │ ├── 包括
│ │ │ ├── data sets
│ │ │ ├── relationships
│ │ │ └── algorithms
│ │ ├── 真正困难的是
│ │ │ ├── specifying conceptual construct
│ │ │ ├── designing conceptual construct
│ │ │ └── testing conceptual construct
│ │ └── 四个本质属性
│ │ ├── complexity
│ │ ├── conformity
│ │ ├── changeability
│ │ └── invisibility
│ │
│ ├── 3.2 Accident 偶然困难
│ │ ├── 不是软件本质固有的问题
│ │ ├── 来自当前开发方法和开发环境
│ │ ├── 是工具、语言、平台带来的副作用
│ │ └── 例子
│ │ ├── syntax errors
│ │ ├── slow compilation times
│ │ └── manual memory management
│ │
│ ├── 3.3 判断方法
│ │ ├── 如果更换工具、语言、框架后问题大幅减少
│ │ │ └── 更可能是 accidental difficulty
│ │ └── 如果工具再完美也必须面对
│ │ └── 更可能是 essential difficulty
│ │
│ └── 3.4 Targeting Essence or Accident
│ ├── Moving from Assembly to Python
│ │ └── 主要减少 accidental difficulty
│ ├── Domain-Driven Design
│ │ └── 帮助处理 essential difficulty，但不能消除业务复杂性
│ ├── Cloud Infrastructure
│ │ └── 主要减少 deployment / infrastructure 的 accidental difficulty
│ └── Test-Driven Development
│ └── 帮助澄清行为和减少错误，但不能自动决定正确需求
│
├── 4. Essential Difficulties 四个本质困难
│ ├── 4.1 Complexity 复杂性
│ │ ├── 定义
│ │ │ └── 系统内部存在大量 states and interactions
│ │ ├── 是 essential property，不是 accidental
│ │ ├── 导致的问题
│ │ │ ├── communication difficulty
│ │ │ ├── 难以理解所有 states
│ │ │ ├── 系统行为可能 unreliable
│ │ │ ├── 扩展功能时容易产生 side effects
│ │ │ └── hidden states 可能形成 security trapdoors
│ │ └── 考试理解
│ │ └── 软件复杂性来自概念、状态、关系、逻辑之间的交织，不只是代码行数多
│ │
│ ├── 4.2 Conformity 一致性 / 适应性
│ │ ├── 软件必须适应 human institutions and systems
│ │ ├── 外部制度和系统本身复杂且不断变化
│ │ ├── 软件必须 conform 的原因
│ │ │ ├── 软件通常是系统中 latest arrival
│ │ │ └── 软件被认为是 most conformable
│ │ └── 考试理解
│ │ └── 现实世界规则不一定逻辑清晰，但软件必须适应它们
│ │
│ ├── 4.3 Changeability 可变性
│ │ ├── 软件会不断被修改
│ │ ├── 原因
│ │ │ ├── requirements evolve
│ │ │ ├── technologies evolve
│ │ │ └── environments evolve
│ │ ├── 成功软件都会被改变
│ │ │ ├── 被用于 original domain 边界之外
│ │ │ └── 存活时间超过最初硬件寿命
│ │ └── 考试理解
│ │ └── 软件越成功，越容易被要求适应新场景
│ │
│ └── 4.4 Invisibility 不可见性
│ ├── 软件没有物理形态
│ ├── unlike physical systems
│ ├── 难以 visualize
│ ├── 难以 conceptualize
│ └── 考试理解
│ └── 软件结构、状态、依赖和运行路径无法像桥梁或机器一样直接观察
│
├── 5. Essential Difficulties Case Study：Knight Capital Group
│ ├── 5.1 Case Background
│ │ ├── Knight Capital Group
│ │ ├── 发生时间：2012
│ │ ├── deployment error
│ │ ├── 45 分钟损失 $440 million
│ │ ├── 使用旧 binary flag 激活 updated module
│ │ ├── 在旧代码中，该 flag 会激活 unwanted module：Power Peg
│ │ ├── 7 台服务器更新了新代码
│ │ └── 第 8 台服务器仍然 unknowingly running old code
│ │
│ ├── 5.2 对应 Complexity
│ │ ├── 系统处于混合状态
│ │ │ ├── 7 updated servers
│ │ │ └── 1 legacy server
│ │ ├── 单个 reused flag 在不同代码环境中行为不同
│ │ └── 开发者没有完全掌握 interlocking complexity
│ │
│ ├── 5.3 对应 Invisibility
│ │ ├── 工程师不能直接“看见”第 8 台服务器运行旧代码
│ │ └── 软件内部状态不像桥梁缺少支撑梁那样可见
│ │
│ ├── 5.4 对应 Conformity
│ │ ├── Knight Capital 必须适应 NYSE 新 RLP rules
│ │ ├── 外部规则变化迫使软件修改
│ │ └── 压力下采取了 repurpose old flag 的 shortcut
│ │
│ └── 5.5 对应 Changeability
│ ├── NYSE 改变交易规则
│ ├── 软件被认为可以快速修改
│ ├── 团队试图快速部署
│ └── rushed manual deployment 跳过第 8 台服务器
│
├── 6. Accidental Difficulties 偶然困难
│ ├── 6.1 定义
│ │ ├── 来自当前 technology, tools, practices
│ │ ├── 不属于软件本质
│ │ └── 是开发方法和环境的副产品
│ │
│ ├── 6.2 例子
│ │ ├── syntax errors
│ │ ├── boilerplate code
│ │ ├── slow compilation
│ │ ├── manual memory management
│ │ ├── C++ segmentation fault
│ │ ├── YAML configuration
│ │ ├── dependency conflict
│ │ └── confusing IDE / toolchain
│ │
│ ├── 6.3 与 Essential 的区别
│ │ ├── Essential
│ │ │ ├── 问题本身固有
│ │ │ ├── 不能通过更换工具彻底消除
│ │ │ └── 例子：复杂业务规则、需求冲突、分布式一致性
│ │ └── Accidental
│ │ ├── 实现方式引入
│ │ ├── 可以通过更好工具或语言减少
│ │ └── 例子：指针错误、编译器错误、环境配置错误
│ │
│ └── 6.4 分类练习
│ ├── Cross-border tax calculation business rules
│ │ └── Essential difficulty
│ ├── Kubernetes YAML high availability configuration
│ │ └── Accidental difficulty
│ ├── C++ Segmentation Fault
│ │ └── Accidental difficulty
│ ├── Conflicting hospital stakeholder requirements
│ │ └── Essential difficulty
│ ├── Python script syntax optimization for legacy processor
│ │ └── Accidental difficulty
│ └── Software complexity causing communication difficulty
│ └── Essential difficulty
│
├── 7. Past Breakthroughs 过去的突破
│ ├── 7.1 High-Level Languages 高级语言
│ │ ├── 是重要的 productivity development
│ │ └── 减少 accidental complexity
│ │
│ ├── 7.2 Time Sharing and Development Interactivity
│ │ ├── 提高交互性
│ │ └── immediacy allows concentration
│ │
│ └── 7.3 Unified Programming Environments
│ ├── 例子：Unix
│ ├── 提供 workbench
│ └── 提供 tools
│
├── 8. Lethal Silver? 曾被期待成为银弹的技术
│ ├── 总体观点
│ │ ├── 这些技术可能有帮助
│ │ ├── 但大多只能缓解 accidental difficulties
│ │ └── 不能根本消除 essential difficulties
│ │
│ ├── Better High-Level Languages
│ │ ├── 减少低层语法和实现细节
│ │ ├── 提高开发效率
│ │ └── 但不能消除需求和设计复杂性
│ │
│ ├── Object-Oriented Programming
│ │ ├── 提高 modularity
│ │ ├── 提高 reusability
│ │ └── 但设计类结构和对象交互仍然困难
│ │
│ ├── Artificial Intelligence
│ │ ├── 可作为生产力工具
│ │ └── 但不能替人类决定真正需求
│ │
│ ├── Expert Systems
│ │ ├── 可以辅助开发者
│ │ └── 但不能简化软件概念结构本身
│ │
│ ├── Automatic Programming
│ │ ├── 通过高层需求生成代码
│ │ └── 但仍需要精确、完整、无矛盾的 specification
│ │
│ ├── Graphical Programming
│ │ ├── 用图形表达程序
│ │ └── 但软件复杂性是多维抽象逻辑，二维图形难以完全表达
│ │
│ ├── Program Verification
│ │ ├── 能证明程序符合 specification
│ │ └── 不能证明 specification 符合用户真实需求
│ │
│ ├── Environment and Tools
│ │ ├── IDE、Git、自动化构建等工具提高效率
│ │ └── 主要解决 accidental difficulty
│ │
│ └── Workstations
│ ├── 提供更强计算资源
│ ├── 减少等待时间
│ └── 不能解决核心概念复杂性
│
├── 9. Promising Attacks 更有希望的应对方向
│ ├── 9.1 Build vs Buy
│ │ ├── Not to build, to buy
│ │ ├── 使用 off-the-shelf software
│ │ ├── 面向 mass market
│ │ ├── 优点
│ │ │ ├── immediate delivery
│ │ │ ├── less errors
│ │ │ └── low cost because cost distributed among users
│ │ └── 例子
│ │ ├── API-driven development
│ │ └── software framework
│ │
│ ├── 9.2 Requirement Refinement & Prototyping
│ │ ├── 最难的是 precisely decide what to build
│ │ ├── 无法一开始就完全、精确、正确地定义需求
│ │ └── 需要 iteratively decide what to build
│ │
│ ├── 9.3 Incremental Development
│ │ ├── 不要一次性构建复杂系统
│ │ ├── bit by bit 地增长软件
│ │ └── 核心思想：grow, don’t build
│ │
│ └── 9.4 Great Designer
│ ├── Great designs come from great designers
│ ├── 优秀设计者能产生更好的结构
│ │ ├── faster
│ │ ├── smaller
│ │ ├── simpler
│ │ ├── cleaner
│ │ └── produced with less effort
│ └── Great products come from one or a few designing minds
│
└── 10. Relevance Today 当代相关性
├── Brooks 的观点至今仍然 relevant
├── 技术进步没有完全消除 essential difficulties
├── Agile 可以帮助迭代需求和增量开发
├── AI-enhanced tools 可以提升编码效率
├── 但 AI 和工具主要缓解部分 accidental difficulties
└── 核心挑战仍然是
├── deciding what to build
├── understanding complex business logic
├── managing change
├── handling invisible system states
└── maintaining communication among stakeholders
```

## Historical Context

### The Beginning of Computing 40 ~ 50s

- Introduction to the first electronic computers, such as ENIAC and UNIVAC, which were primarily used for scientific and military applications.

  第一代电子计算机（如ENIAC和UNIVAC）主要应用于科学与军事领域。

- The use of machine or assembly language, which was time-consuming and error-prone

  使用机器语言或汇编语言耗时且易出错

### The Beginning of Crisis 60s

- The rise of commercial computing and the need for more complex software systems, like payroll and inventory management.

  商业计算的兴起以及对更复杂软件系统（如薪资和库存管理）的需求。

- Project Failures: e.g. the IBM OS/360, delays and budget overruns, the growing gap between software demand and development capabilities.

  项目失败案例：例如IBM OS/360系统，项目延期与预算超支，以及软件需求与开发能力之间日益扩大的差距。

- **lack of standardized methodologies and processes.**

  **缺乏标准化的方法论与流程。**

### The Beginning of Software Engineering 1968-69 软件工程的开端

- Coining the Term “Software Crisis” in 1968

  1968年创造“软件危机”一词

- The NATO conference acknowledged the inability to produce reliable and efficient software on time and within budget as a significant issue.

  北约会议承认，无法在预算内按时开发出可靠高效的软件是一个重大问题。

- Call for a **New Discipline**: A disciplined approach to software development, laying the groundwork for software engineering.

  呼吁建立新学科：以严谨方法推动软件开发，为软件工程奠定基础。

### Escalation and Response 70s 升级与应对

- As systems grew more complex, the crisis deepened, projects experiencing significant overruns and failures.

  随着系统日趋复杂，危机也愈发深重，各类项目普遍遭遇严重的进度延误与失败困境。

- Introduction of structured programming and the Waterfall model.

  结构化编程与瀑布模型的引入。

- Recognition of the growing burden of **software maintenance**, which consumed a significant portion of resources and budgets.

  认识到软件维护负担日益加重，其消耗了资源与预算的显著部分。

### The Impact of the Crisis 危机的影响

- **Economic Consequences**: The software crisis led to substantial financial losses for companies due to failed projects and inefficient software.

  经济后果：软件危机导致企业因项目失败和软件效率低下而遭受重大财务损失。

- **Human Factors**: Stress and burnout among developers became common, as they struggled to meet unrealistic deadlines and requirements.

  人为因素：由于开发者们只能努力满足不切实际的截止期限和需求，压力与职业倦怠变得普遍。

- **Technological Stagnation**: The inability to deliver reliable software hampered technological progress and innovation in various industries.

  技术停滞：无法交付可靠软件阻碍了各行业的技术进步与创新。

### The Path Forward 向前的道路

- **Emergence of Software Engineering**: The crisis catalyzed the development of software engineering as a distinct discipline.

  软件工程学科的兴起：这场危机催生了软件工程作为一个独立学科的发展。

- **Focus on Quality and Process**: Introduction of quality assurance practices, project management techniques, and process improvement models.

  注重质量与流程：引入质量保证实践、项目管理技术及流程改进模型。

- **Legacy and Lessons**: The software crisis highlighted the importance of understanding software complexity, effective communication, and the need for continuous adaptation of methodologies.

  遗产与启示：软件危机凸显了理解软件复杂性、实现有效沟通以及持续调整方法论的重要性。

### Key Issues 一些主要存在的问题

- **Project overruns in time and budget**

  **项目在时间和预算上的超支。**

- **Software that fails to meet user requirements**

  **不符合用户需求的软件**

- **Poor quality and unreliable software**

  **质量低劣且不可靠的软件**

- **Maintenance challenges and escalating costs**

  **维护挑战与成本攀升**

**考试潜在问题 Cause and Effect:** 

- These problems are connected: unclear requirements can lead to software that does not meet user needs; poor design and lack of process can lead to unreliable software; and unreliable software increases maintenance cost. Therefore, software crisis is a chain of **schedule, budget, quality, requirement, and maintenance** problems.

  这些问题环环相扣：不明确的需求会导致软件无法满足用户需求；设计不当及流程缺失会引发软件不可靠；而不可靠的软件则会推高维护成本。因此，软件危机本质上是一个涵盖进度、预算、质量、需求与维护问题的连锁链。

## The werewolf appears 新的危机出现了

Thesis：**No Silver Bullet: Essence and Accidents of Software Engineering** 没有银弹：软件工程的本质与偶然性

- published in 1986 and has since become a seminal work in understanding the inherent challenges of software development.

  该书于1986年出版，自此成为理解软件开发固有挑战的奠基性著作。

- Author Background: Frederick P. Brooks, a renowned computer scientist

  作者背景：弗雷德里克·P·布鲁克斯，著名计算机科学家

### Core Thesis

软件开发的复杂性由其本质决定，而非技术手段可以轻易化解。

- **No Silver Bullet**: Brooks argues that there is no single breakthrough—no “silver bullet”—that will dramatically improve software development productivity or reliability by an order of magnitude within a decade.

  “银弹”的幻象（The Illusion of a Silver Bullet）：Brooks 借用民间传说中杀死狼人的“银弹”来比喻那些被人们寄予厚望、能够瞬间解决软件危机（进度延误、预算超支、产品缺陷）的突破性技术；在十年内，不存在任何单一的技术或管理革新，能像硬件性能（摩尔定律）那样，让软件的生产力或可靠性实现**数量级（10倍以上）**的提升。

- **Essence vs. Accidents**: He distinguishes between the essential difficulties of software engineering and the accidental difficulties.

  本节课最核心的讨论：

  - **本质困难 (Essential Difficulties)：** 软件系统固有的复杂性。包括如何逻辑严密地描述复杂的业务规则、确保成千上万个状态的一致性、以及处理不可见的概念构架。
    - 即使你有一支完美的画笔，构思一副传世名画的“灵魂”依然是极难的。

  - **偶然困难 (Accidental Difficulties)：** 在实现过程中引入的、非必要的困难。比如繁琐的语法、缓慢的编译速度、简陋的调试工具等。
    - 过去我们要自己研磨颜料（偶然困难），现在买现成的画具就能解决。

> become a monster of missed schedules, blown budgets, flawed products …”, in short “a werewolf” the solution to which is a “silver bullet” that “ …makes software costs drop as rapidly as computer hardware costs.
>
> 成为错失期限、预算超支、产品缺陷频出的“怪物”……简而言之，一个“狼人”，而解决之道在于找到使其“软件成本如计算机硬件成本般急速下降”的“银弹”。

### Silver Bullet

- Brooks uses the "silver bullet" as a metaphor for a single technology or management technique that could magically "lay to rest" the monsters of **missed schedules, blown budgets, and flawed products** in software engineering.

  布鲁克斯将“银弹”用作一个隐喻，意指某种单一技术或管理方法能够神奇地“平息”软件工程中进度延误、预算超支和产品缺陷这些怪物。

- He defines a true silver bullet as something that, by itself, promises at least an order-of-magnitude (tenfold) improvement in productivity, reliability, or simplicity.

  他将真正的银弹定义为：其本身就能在生产力、可靠性或简洁性方面带来至少一个数量级（十倍）的改进。

- **这里的 “silver bullet” 是一个比喻，表示一种能够神奇解决软件工程中 missed schedules、blown budgets、flawed products 等问题的单一方案。Brooks 认为，这样的方案并不存在**；Brooks 认为不存在某一种单一技术或管理方法，可以在十年内让软件开发的生产力、可靠性或简洁性提升一个数量级

### Essence

- This is the inherent, irreducible "hard part" of software.
- It is the abstract "construct of interlocking concepts"—the data sets, relationships, and algorithms—and the difficult task of specifying, designing, and testing that conceptual construct.
- Brooks identifies four inherent properties of this essence that make it difficult to master: complexity, conformity, changeability, and invisibility.

这是软件固有的、不可简化的"硬核"部分。它是由相互关联的概念——**数据集**、**关系**与**算法**——构成的抽象"概念体系"，以及对该概念体系进行**规范**、**设计**和**测试**的艰巨任务。布鲁克斯指出了这一本质所固有的四个特性，使其难以驾驭，分别是：**复杂性、一致性、可变性、不可见性**。

**Essential difficulty 是软件本身固有的、不可完全消除的困难。它来自软件要表达的 <u>conceptual construct</u>，也就是数据、关系、算法、业务规则和状态之间相互关联的抽象结构。Brooks 认为，软件真正困难的部分是 <u>specification、design 和 testing</u> 这个 conceptual construct，而不是把它写成代码本身。**

### Accident

-  Difficulties that are not intrinsic to the nature of software but are instead **byproducts** of the methods and environments in which software is developed.
- Examples include syntax errors, slow compilation times, and manual memory management

并非软件本质固有的困难，而是**软件开发方法**及**环境**所产生的**衍生问题**。例如**语法错误**、**编译时间过长**以及**手动内存管理**等。

**Accidental difficulty 不是软件本身固有的困难，而是由当前开发工具、语言、平台、环境和实现方式带来的副作用。课件给出的例子包括 syntax errors、slow compilation times 和 manual memory management。**

### Targeting Essence or Accident ?

- Moving from Assembly to Python

  从汇编到Python

- Domain-Driven Design

  领域驱动设计

- Cloud Infrastructure

  云服务

- Test-Driven Development

  测试驱动开发

| Practice                       | Mainly targets                  | Why                                                          |
| ------------------------------ | ------------------------------- | ------------------------------------------------------------ |
| Moving from Assembly to Python | Accidental difficulty           | Reduces low-level syntax and memory-management burden        |
| Cloud Infrastructure           | Mostly accidental difficulty    | Reduces deployment and infrastructure management effort      |
| Domain-Driven Design           | Partly essential difficulty     | Helps model complex business domains, but does not remove the domain complexity |
| Test-Driven Development        | Partly essential and accidental | Helps clarify expected behavior and detect errors early, but cannot decide true requirements automatically |

> I believe the hard part of building software to be the specification, design, and testing of this conceptual construct, not the labor of representing it and testing the fidelity of the representation. [Brooks]
>
> 我认为构建软件的难点在于这个**概念结构本身的规格制定、设计与测试**，而非将其表达出来并验证表达准确性的过程。[Brooks]

## Essence Difficulties  本质困难

### Essential Difficulties 1 - Complexity 复杂性

- Vast number of states and interactions within the system.

- An essential property, not accidental

- Difficulties:

  - Communication

  - Understanding all states, unreliable

  - Extending functions without side-effect

  - Hidden states that constitute security trapdoors

- 软件系统有大量状态、变量和交互关系。复杂性会导致沟通困难、难以理解所有系统状态、扩展功能时容易产生副作用，也可能隐藏 security trapdoors。

  考试中可以这样写：Software complexity is essential because it comes from the large number of interrelated states and interactions. It makes communication harder, makes the system difficult to understand completely, and increases the risk of side effects when extending the software.

### Essential Difficulties 2 - Conformity 一致性

- Software must conform to human institutions and systems, which are themselves complex and ever-changing.

- Software must conform because: -

  - It is the most recent arrival on the scene


  - Perceived as the most conformable


- 软件必须适应现实世界中的制度、组织流程、法律规则、旧系统和业务习惯。这些外部规则本身复杂且不断变化。课件指出，软件之所以必须 conform，是因为软件通常是后来加入现实系统的元素，而且人们认为软件最容易修改。

### Essential Difficulties 3 - Changeability 可变性

- Software is subject to continuous change due to evolving requirements, technologies, and environments.

- All successful software get changed: -

  - It is being used at the edge of or beyond the original domain

  - Survives beyond the normal life of the machine it was written for

- 软件会持续变化，因为需求、技术和运行环境都会变化。课件特别提到，所有成功的软件都会被修改：一方面是因为它会被用于原本设计范围之外的场景，另一方面是因为软件通常会活得比最初运行它的硬件更久。

### Essential Difficulties 4 - Invisibility 不可见性

- Unlike physical systems, software lacks a physical form, making it difficult to visualize and conceptualize.
- 软件不像桥梁、建筑或机器那样有物理形态，所以很难被完整可视化。系统内部状态、逻辑路径和模块关系往往是抽象的，这会增加理解、沟通和调试的难度。

### Essential Difficulties – Case Studies

课件中的 Knight Capital Group 例子非常重要。2012 年 Knight Capital 因部署错误在 45 分钟内损失 4.4 亿美元。它将一个旧 binary flag 重新用于激活新模块，但旧代码中该 flag 会激活 Power Peg 模块。部署时 7 台服务器更新了新代码，但第 8 台服务器仍然运行旧代码，最终导致大量错误交易。

这个案例可以对应四个 essential difficulties：

- Complexity：系统处于 7 台新服务器 + 1 台旧服务器的混合状态，开发者没有完全理解这个状态组合会带来的复杂交互
- Invisibility：工程师看不到第 8 台服务器仍然运行旧代码，就像不能直接“看见”软件内部结构。
- Conformity：系统必须适应 NYSE 的新 RLP rules，外部规则变化迫使软件快速修改。
- Changeability：因为软件被认为容易修改，所以团队尝试快速部署，但这种快速变化导致了人为部署错误。

- Complexity
  - The "state" of the system was unintended: a mix of 7 updated servers and 1 legacy server. The developers failed to account for the **interlocking complexity** of how a single repurposed flag would behave if the environment wasn't perfectly uniform.
- Invisibility
  - Unlike a bridge where you can see a missing support beam, Knight Capital’s engineers couldn't "see" that the 8th server was running old code.
- Conformity

  - Knight Capital had to change its software to conform to the NYSE's new RLP rules. This external pressure to conform often leads to "accidental" shortcuts—like repurposing an old flag rather than designing a clean, new interface.
- Changeability

  - The NYSE changed its rules for trading. If Knight Capital’s system had been a hardware circuit, they might have said, "We can't change this fast enough."

  - Because it was software, there was an assumption that it *could* and *should* be changed instantly to meet the deadline. This pressure to exploit software's changeability is exactly what led to the rushed, manual deployment that skipped the 8th server.

## Accident Difficulties 偶然困难

- Accidental difficulties are the challenges that arise from the current state of **technology**, **tools**, and **practices** used in software development.

  偶然性困难源自软件开发中当前**技术**、**工具**及**实践**现状所引发的挑战。

- These difficulties are not intrinsic to the nature of software but are instead **byproducts** of the methods and environments in which software is developed.

  这些困难并非软件本质所固有，而是软件开发方法与环境**衍生的副产品**。

### Exercise

**Accidental Difficulties** 是指那些由于我们选择的**开发环境、编程语言或特定实现方式**所产生的困难。它们不是问题本身固有的，而是“自找的”。

- **语言特性驱动：** 段错误通常源于 C++ 的特性（如指针操作、手动 `new`/`delete`）。如果你换一种具有垃圾回收机制（GC）的语言（如 Java、Python 或 Go），或者使用现代 C++ 的智能指针（`std::unique_ptr`），这个问题在很大程度上会消失。
- **非业务逻辑相关：** 解决段错误并不会让你离解决业务目标（例如“计算财务报表”或“渲染 3D 图形”）更近一步，它只是在修补你所使用的工具带来的副作用。

**Essential Difficulties** 是指软件系统**本质上**固有的复杂性。无论你用什么语言、什么工具，这些困难都无法消除。

- **逻辑复杂性：** 如果你的算法逻辑本身极其复杂，或者业务规则之间存在冲突，无论你用 C++ 还是 Python，这种逻辑上的“烧脑”都是避不开的。

- **一致性与不可见性：** 确保一个分布式系统在断电时数据不丢失，这就是本质困难，因为它涉及到物理现实和逻辑完备性的挑战。

- Categorize each as either an Essential Difficulty or an Accidental Difficulty, and provide a brief justification

  - Determining the interlocking business rules for a cross-border tax calculation engine.

    **essential difficulties**

  - Configuring the YAML files for a Kubernetes cluster to ensure high availability.

    **accidental difficulties**

  - Resolving a "Segmentation Fault" caused by manual memory management in C++.

    **accidental difficulties**

  - Mapping out the conflicting requirements between three different stakeholders for a new hospital management system.

    **essential difficulties**

  - Optimizing the syntax of a Python script to run faster on a specific legacy processor.

    **accidental Difficulty**

  - Software complexity leads to many difficulties, what are they?

    **essential difficulties**

    lead difficulties in communication. will further cause misunderstanding. 

  - In your opinion, why is software perceived as the most conformable element?

    **essential Difficulty**

  - Define essential difficulties and accidental difficulties in the context of software engineering. Provide two examples of each type of difficulty.

    - **Essential Difficulties (本质困难)**

      **定义：** 软件系统固有的、无法简化的核心复杂性。这涉及到如何将现实世界极其复杂的逻辑映射成严谨的抽象概念（数据结构、算法、交互关系）。

      - **示例 1：需求规格说明 (Specification)。** 试图搞清楚银行系统如何处理几千种复杂的利息计算规则，并确保没有逻辑冲突。
      - **示例 2：分布式系统的一致性 (Consistency)。** 在高并发环境下，确保全球数千台服务器上的数据状态实时、准确、无误。

    - **Accidental Difficulties (偶然困难)**

      **定义：** 并非软件本质固有，而是由于我们使用的工具、编程语言、或特定的开发环境所产生的副作用或人为障碍。

      - **示例 1：语法与样板代码 (Syntax & Boilerplate)。** 比如在 C 语言中为了实现一个简单的列表，需要写大量冗长的指针操作代码。
      - **示例 2：环境配置与依赖管理 (Environment & Dependencies)。** 比如因为 Python 版本冲突或编译器设置错误导致程序无法运行。

## 判断 Essence Difficult 还是 Activation Difficult 的方法

如果换一个更好的工具、语言或环境后问题基本消失，那么它更可能是 accidental difficulty；如果无论用什么工具都必须面对，它更可能是 essential difficulty。

## Past Breakthroughs 过往突破

### A successful past (in 1986)

- **High level languages 高级语言**
  
  - **Most important productivity development**
  
    最重要的生产力发展
  
  - Reduces accidental complexity
  
    减少意外复杂性
  
- **Time sharing and development interactivity**
  
  分时共享与开发互动性
  
  - **Immediacy** allows concentration
  
    即时性有助于集中注意力。
  
- **Unified programming environments**
  
  统一编程环境
  
  - e.g. Unix, provides a workbench and tool

### Lethal Silver ? 下面的那些技术可以用于根本上解决 Essential Difficulties

Brook在分析完“本质”与“偶然”困难后，逐一审视了当时（1987年前后）被人们寄予厚望、认为可能成为“银弹”的各种技术。

但是他最后得到的核心结论是：**这些技术大多只能解决“偶然困难”（Accidental Difficulties），而无法触及软件开发的“本质困难”（Essential Difficulties），因此它们都不是银弹。**

- Better High-Level Languages?
  - 像 Ada、C++ 或后来的 Python、Java 等。
  - **Brooks 的观点：** 高级语言通过消除低级的语法细节（如寄存器分配、繁琐的调用约定）解决了大量的**偶然困难**。
  - **结论：** 随着语言越来越高级，解决偶然困难的边际收益递减。剩下的核心逻辑复杂性（本质困难）依然存在。

- Object Oriented programming?
  - 使用类、继承和封装来组织代码。
  - **Brooks 的观点：** OOP 提高了代码的移用性（Reusability）和模块化，减少了重复造轮子的偶然困难。
  - **结论：** 尽管它是一个巨大的进步，但设计一个复杂系统的“类层级结构”和“对象交互逻辑”本身依然极其困难（本质复杂性）。
- Artificial intelligence
  - 当时人们期望 AI 能自动理解需求并写出代码。

  - **Brooks 的观点：** 区分了“强 AI”和“实用 AI”。他认为 AI 主要是提高生产力的工具。
  - **结论：** 软件最难的部分是**定义需求**，而 AI 无法替人类决定到底想要什么（本质困难）。

- Expert systems
  - 基于规则的推理系统，模拟人类专家的决策。(such as copilot)
  - **Brooks 的观点：** 专家系统可以辅助初级程序员，或者作为调试工具。
  - **结论：** 它只是改进了过程，并没有简化软件逻辑结构的构建过程。

- “Automatic” programming
  - 通过高层级的需求描述自动生成可执行代码。
  - **Brooks 的观点：** 他认为这本质上只是“更高级的语言”。
  - **结论：** 即使代码是自动生成的，你依然需要一套极其严密、逻辑一致的“规格说明”来告诉机器生成什么，这本身就是**本质困难**。

- Graphical programming
  - 使用流程图或视觉组件代替文本编写程序。
  - **Brooks 的观点：** 软件的本质是多维的、抽象的逻辑，流程图只能展示极简单的、二维的控制流。
  - **结论：** 软件的复杂性来自于隐藏的逻辑关系，而不是代码是“写”的还是“画”的。

- Program verification
  - 使用数学方法证明代码的正确性。
  - **Brooks 的观点：** 这只能证明代码符合“规格说明”，但无法证明“规格说明”本身符合“用户的真实需求”。
  - **结论：** 它能减少 Bug，但不能降低设计系统的复杂度，且成本极高。

- Environment and tools
  - 更好的 IDE、版本控制系统（Git）、自动化构建工具。
  - **Brooks 的观点：** 这些确实能让开发更顺畅，但属于对“偶然困难”的修补。
  - **结论：** 工具能提速，但不能替你思考逻辑。

- Workstations
  - 为每个程序员提供更强大的个人计算资源（当时从主机终端向个人电脑转型）。
  - **Brooks 的观点：** 减少了等待编译和运行的时间。
  - **结论：** 这纯粹是硬件层面的进步，解决了**偶然困难**，对思考软件逻辑没有直接帮助。


### Lethal Silver - Discussion

- Brooks dismissed(驳回) Artificial Intelligence and Expert Systems as "Lethal Silver" in 1986.
- Today, Large Language Models (LLMs) like GitHub Copilot are often framed as a revolution
- **Does AI solve Essential or Accidental difficulties?**

AI 极大地消灭了“偶然困难”（Accidental Difficulties），但在挑战“本质困难”（Essential Difficulties）上仍处于辅助地位。

**“AI 并不是杀死狼人的‘银弹’，而是一把极其锋利的‘手术刀’。”**

虽然 LLM 让我们在处理“偶然困难”时实现了数量级的飞跃，使得编写代码本身变得前所未有的简单，但它并没有减轻“思考逻辑”的痛苦。

随着 AI 消灭了大部分编码工作（偶然困难），软件开发的重心将进一步向**本质困难**偏移。未来的程序员将更像“架构师”和“审查者”：我们需要花费更多精力去确保 AI 生成的逻辑符合复杂的现实业务，并处理那些 AI 无法理解的人类需求冲突。

## The Promising Attacks 有希望的"攻击"

**"Promising Attacks"（有希望的攻势）** 是指那些虽然称不上“银弹”（不能瞬间带来 10 倍提升），但能够切实有效降低软件开发成本、管理复杂性的现实策略。

### 1. Build vs. Buy

传统的软件开发倾向于“量身定制”（Build），但这会引入大量的本质困难（需求理清、逻辑设计）和偶然困难（编码、测试、Bug 修复）。Brooks 建议尽可能选择“购买”（Buy）。

- **不开发，直接买（Not to build, to buy）：** 如果市面上已经有成熟的解决方案，直接集成比从零开发要高效得多。
- **大众市场的现成品（Off-the-shelf for mass market）：** 针对大众市场设计的软件（如数据库系统、云服务、办公软件）经过了数百万用户的验证。
  - **即时交付（Immediate delivery）：** 省去了漫长的开发周期。
  - **更少的错误（Less errors）：** 成熟产品在发布前已经过严格测试，且有大量用户反馈。
  - **低成本（Low cost）：** 开发成本由成千上万个用户分担（Cost distributed），这比单独为一个公司定制要便宜得多。

- Example:
  - API-driven development
    - 现在的开发者不需要自己写短信发送逻辑、支付接口或地图渲染引擎。
      - **本质：** 通过集成 Stripe (支付)、Twilio (通信) 或 Google Maps API，你将这些复杂的**本质困难**外包给了专门处理这些问题的专家。
      - **结果：** 你只需要处理自己业务最核心的逻辑，极大地缩短了开发路径。
  - Software framework
    - 如 React, Spring Boot, 或 Django。
      - **本质：** 框架定义了软件的“骨架”。它处理了如何处理 HTTP 请求、如何连接数据库、如何管理状态等通用逻辑。
      - **结果：** 框架消除了大量的**偶然困难**（如底层的网络协议处理）和部分**本质困难**（如通用的系统构架设计），让开发者专注于业务创新。

### 2. Requirement Refinement & Prototyping 需求细化与原型设计

- Hardest part of building a software system is deciding precisely what to build. 

  构建软件系统最困难的部分在于精确决定要构建什么。

- Impossible to specify completely, precisely, and correctly the exact requirements.

  无法完全、精确且正确地指定确切的需求。

- **Iteratively** deciding "precisely what to build"

  迭代式确定“具体构建内容”

### 3. Incremental Development 迭代开发

- "Growing" software bit by bit rather than trying to build a complex system all at once.

  逐步“培育”软件，而非试图一次性构建复杂系统。

- **grow, don't build**

  增长而不是创建

### Great Designer 优秀的设计者

- Great designs come from great designers. 

  杰出设计源于卓越设计师。

- Best designers produce structures that are **faster, smaller, simpler, cleaner, and produced with less effort**. 

  优秀设计师打造的架构更快捷、更精简、更简洁、更清晰，且投入更少。

- Great products come from one or a few designing minds, great designers. 

  卓越的产品源于少数设计天才的匠心独运。

### Relevance Today

- **Enduring Insights**: Despite technological advancements since the article’s publication, the core challenges identified by Brooks remain relevant.

  **持久洞见**：尽管自文章发表以来技术已取得长足进步，Brooks 所指出的核心挑战至今仍具现实意义。

- **Exercise**: Discuss how contemporary practices like Agile and AI-enhanced tools are used to tackle essential difficulties identified by Fredrick Brooks.

  **练习**：讨论敏捷开发与人工智能增强工具等当代实践如何应对 Brooks 所指出的本质性困难。

### The Laymen Terms

- **Essential difficulties** are the hurdles that are part of the nature of software. They are "essential" because even if you had a perfect computer, these problems would still exist.

  本质困难是软件固有属性中的障碍。它们之所以"本质"，是因为即便拥有完美的计算机，这些问题依然存在。

- This is the **Logic.** It is the task of deciding exactly how the tax laws should be calculated, or how 100 different microservices should talk to each other without crashing.

  这就是逻辑层。它的任务是精确决定税法应如何计算，或是确保上百个微服务在相互通信时不会崩溃。

### The Laymen Terms

- **Accidental difficulties** are the hurdles we encounter because of the way we build software today. They are not part of the problem itself; they are just part of our current technology

  偶然性困难源于当前软件开发方式所带来的障碍。这些问题并非任务本身固有，而是现有技术局限性的体现。

- This includes things like managing memory manually (in C), dealing with slow compilers, inefficient server configuration, or struggling with a confusing IDE.

  这包括手动管理内存（如使用C语言）、处理缓慢的编译器、低效的服务器配置，或是在混乱的集成开发环境中挣扎。

### Essential Reading Material

No Silver Bullet: Essence and Accidents of Software Engineering, by Frederick P. Brooks

# 潜在考试题与参考答案

## Question 1

**Define Software Crisis and explain two key problems caused by it.**

**Answer:**
 Software Crisis refers to the challenges and failures in software development, especially in the 1960s and 1970s, when the demand for complex software systems exceeded the ability to design, implement, and maintain them effectively. Two key problems are project overruns and poor software quality. Project overruns mean software projects often exceed planned time and budget because requirements are unclear and development methods are immature. Poor software quality means the delivered software may be unreliable, contain defects, or fail to meet user requirements. These problems increased maintenance costs and showed the need for software engineering as a disciplined approach.

------

## Question 2

**What does Brooks mean by “No Silver Bullet”?**

**Answer:**
 Brooks means that there is no single technology or management technique that can dramatically improve software development **productivity, reliability, or simplicity** by ten times within a decade. A “silver bullet” is a metaphor for a magical solution that can solve software problems such as **missed schedules, blown budgets, and flawed products**. Brooks argues that such a solution does not exist because many software difficulties are essential. They come from the nature of software itself, such as complexity, conformity, changeability, and invisibility. Tools and languages can reduce accidental difficulties, but they cannot remove the core conceptual difficulty of software design.

------

## Question 3

**Differentiate essential difficulties and accidental difficulties with examples.**

**Answer:**
 Essential difficulties are inherent difficulties of software. They remain even if we have perfect tools and programming languages. They include understanding complex business rules, designing correct system behavior, handling many interacting states, and dealing with changing requirements. For example, determining cross-border tax rules is essential because the business logic itself is complex.

Accidental difficulties are caused by current tools, languages, environments, or implementation choices. They are not part of the core problem. For example, a segmentation fault caused by manual memory management in C++ is accidental because using Java, Python, or smart pointers can reduce this problem. YAML configuration errors in Kubernetes are also accidental because they come from tooling and deployment complexity.

------

## Question 4

**Explain the four essential properties of software according to Brooks.**

**Answer:**
 The four essential properties are complexity, conformity, changeability, and invisibility. Complexity means software has many states, interactions, and dependencies, making it hard to understand and modify safely. Conformity means software must adapt to human organizations, laws, business processes, and legacy systems, even if those systems are inconsistent. Changeability means successful software is constantly changed because requirements, technologies, and environments evolve. Invisibility means software has no physical form, so its structure and behavior are difficult to visualize. These four properties make software development inherently difficult.

------

## Question 5

**Why is software perceived as the most conformable element?**

**Answer:**
 Software is perceived as the most conformable element because it is usually the newest part added to an existing human or technical system. Organizations, laws, workflows, and hardware constraints may already exist and are difficult to change. Therefore, people expect software to adapt to them. Also, software appears easier to modify than physical systems because changing code seems cheaper than changing buildings, machines, or business institutions. However, this expectation creates pressure on developers and increases software complexity because the software must fit messy real-world rules.

------

## Question 6

**Classify the following as essential or accidental difficulties: configuring Kubernetes YAML files, resolving C++ segmentation fault, mapping conflicting hospital requirements.**

**Answer:**
 Configuring Kubernetes YAML files is mainly an accidental difficulty because it is caused by the chosen deployment tool and configuration environment. A better tool or abstraction could reduce this burden. Resolving a C++ segmentation fault is also accidental because it comes from manual memory management and pointer handling in C++. Using a language with garbage collection or safer memory features could reduce it. Mapping conflicting hospital requirements is an essential difficulty because the conflict comes from real stakeholders, medical workflows, and business rules. Even with perfect programming tools, the conflict must still be understood and resolved.

------

## Question 7

**Use the Knight Capital case to explain software complexity and invisibility.**

**Answer:**
 In the Knight Capital case, the company lost $440 million in 45 minutes because of a deployment error. Seven servers were updated with new code, but one server still used old code. This created an unintended system state: a mix of new and old behavior. This shows complexity because the system had many interacting parts, and developers failed to understand how the reused flag would behave in a non-uniform environment. It also shows invisibility because engineers could not directly see that the eighth server was running old code. Unlike a physical bridge, software errors can be hidden inside abstract states and configurations.

------

## Question 8

**Why are high-level languages not a silver bullet?**

**Answer:**
 High-level languages are very useful because they reduce accidental difficulties such as low-level syntax, register management, and manual machine-level operations. Moving from assembly language to Python or Java can greatly improve productivity. However, high-level languages do not remove essential difficulties. Developers still need to understand requirements, design correct abstractions, manage complex business rules, and test the conceptual structure of the system. Therefore, high-level languages are important improvements, but they are not a silver bullet because they mainly reduce accidental complexity rather than eliminating essential complexity.

------

## Question 9

**Explain why program verification cannot fully solve the software crisis.**

**Answer:**
 Program verification can mathematically prove that a program satisfies a formal specification. This can reduce defects and improve reliability. However, it cannot prove that the specification itself correctly represents the user’s real needs. If the requirements are incomplete, ambiguous, or wrong, a verified program may still be useless or incorrect from the user’s perspective. Therefore, program verification can help with correctness relative to a specification, but it cannot solve the essential difficulty of deciding exactly what to build.

------

## Question 10

**What are Brooks’ promising attacks against software difficulties?**

**Answer:**
 Brooks suggests several promising approaches, but none of them is a silver bullet. Build vs Buy means using off-the-shelf software, APIs, or frameworks when possible instead of building everything from scratch. Requirement refinement and prototyping help developers iteratively discover what users actually need. Incremental development means growing the system step by step instead of attempting to build a huge system all at once. Great designers are also important because strong designers can create simpler, cleaner, and more efficient structures. These approaches help manage software difficulty, but they do not completely eliminate essential complexity.
