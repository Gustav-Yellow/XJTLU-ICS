# Woo-Lam 共享密钥认证协议 — ProVerif 模型总结

## 概述

本项目包含两个使用 ProVerif（自动化密码协议验证器）建模的 **Woo-Lam 共享密钥认证协议**（1992）文件。两者对同一协议的不同版本进行形式化建模和安全性验证。

---

## 1. `woo-lam.pv` — 原始（有缺陷）版本

### 协议消息流

```
A -> B : A
B -> A : N (fresh nonce)
A -> B : { m3, N }_kAS
B -> S : { m4, A, { m3, N }_kAS }_kBS
S -> B : { m5, N }_kBS
B : 验证来自 S 的消息
```

### 实现内容

- **四个进程**：Initiator（A）、Responder（B）、Server（S）、Key Registration（K）
- **响应者 B** 将 A 发来的密文 `{ m3, N }_kAS` 嵌套在自己的加密消息 `{ m4, A, ... }_kBS` 中转发给服务器
- 服务器解密外层（用 kBS）、再解密内层（用 kAS），验证后返回 `{ m5, N }_kBS`

### 验证结果

> **存在攻击，协议终止。** 文件注释中标注 "Terminates with attack."

原始版本的问题在于：B 向 S 转发消息时用自己的密钥 kBS 加密整个包，但 S 返回给 B 的响应中 **没有绑定 A 的身份**（只有 `{ m5, N }_kBS`），攻击者可以进行重放/中间人攻击。

---

## 2. `woo-lam-corrected.pv` — 修正版本（Gordon & Jeffrey, CSFW 2001）

### 协议消息流

```
A -> B : A
B -> A : N (fresh nonce)
A -> B : { m3, B, N }_kAS          ← 关键修正：密文中绑定了 B 的身份
B -> S : A, B, { m3, B, N }_kAS    ← 明文转发，不再嵌套加密
S -> B : { m5, A, N }_kBS          ← 关键修正：响应中绑定了 A 的身份
B : 验证来自 S 的消息
```

### 关键修正

| 位置 | 原始版本 | 修正版本 |
|------|---------|---------|
| A→B (第3条) | `{ m3, N }_kAS` | `{ m3, B, N }_kAS` — 密文绑定 B 的身份 |
| B→S (第4条) | `{ m4, A, {m3,N}_kAS }_kBS` 嵌套加密 | `A, B, { m3, B, N }_kAS` 明文转发 |
| S→B (第5条) | `{ m5, N }_kBS` | `{ m5, A, N }_kBS` — 响应绑定 A 的身份 |

### 验证结果

> **协议正确。** 文件注释中标注 "Correct."

修正版本通过以下两点消除了攻击：
1. A 的密文中绑定 B 的身份，防止攻击者重定向消息
2. S 的响应中绑定 A 的身份，使 B 能确认通信对端

### 关于 Full Agreement 的说明

文件注释指出：严格意义上的 **Full Agreement**（完全一致）不成立，因为攻击者可以让 B 看到与 `{ m3, B, N }_kAS` 不同的消息。但这 **不是真正的攻击**，因为服务器和 A 都能正确看到该消息，协议的安全性目标（认证）仍然满足。

---

## 共同结构

两个文件共享相同的建模框架：

- **类型系统**：`tag`、`host`、`nonce`、`key`
- **共享密钥加密**：`encrypt`/`decrypt` 函数及归约规则
- **密钥保密假设**：`not attacker(new Kas)` 和 `not attacker(new Kbs)`
- **两个诚实主机**：A 和 B
- **密钥注册表**：`table keys(host, key)`
- **查询**：使用 `inj-event` 注入式对应关系验证认证属性
- **无限会话模型**：所有进程通过 `!` 运算符启动无界并发实例

---

## 结论

`woo-lam.pv` 展示了 Woo-Lam 协议原始设计中存在的安全漏洞，而 `woo-lam-corrected.pv` 通过 Gordon & Jeffrey（CSFW 2001）提出的修正，在密文中绑定通信双方身份，成功消除了攻击路径。这是一个经典的形式化方法案例，展示了 ProVerif 在自动发现和验证密码协议安全性方面的价值。
