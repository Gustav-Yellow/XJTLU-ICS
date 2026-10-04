# Question 1

## 中文

### a. 什么是中间人攻击 (Man-in-the-Middle Attack) 以及它为什么会发生？ (8 points)

**解释：**

- **中间人攻击 (MITM)** 是指攻击者秘密地将自己插入到通信双方（例如客户端和服务器）之间。攻击者拦截双方发送的原始信息，并在双方不知情的情况下，分别与他们建立独立的联系、交换密钥并转发（甚至篡改）消息。这样一来，通信双方会误以为他们正在通过一个私密的连接直接与对方交谈，而实际上整个对话都在攻击者的控制之下。
- **为什么在这个协议中会发生：** 该协议试图通过为每条消息建立新的共享密钥来实现前向保密 (PFS) 。然而，它发生 MITM 攻击的根本原因是**缺乏身份验证 (Authentication)**。当客户端发送 $g^{x_{1}}$ 时，服务器无法确认这确实来自合法的客户端 ；同样，当服务器回复 $g^{y_{1}}$ 时，客户端也无法验证发送者是不是真正的服务器 。这种仅仅交换公开参数而没有进行身份绑定的 Diffie-Hellman 密钥交换，天然容易受到中间人攻击 。

------

### b. 演示对该协议的中间人攻击过程。 (12 points)

假设攻击者（我们称之为 **M**）位于客户端 (Client) 和服务器 (Server) 之间。M 可以拦截所有通信并生成自己的随机秘密值 $z_{c}$ 和 $z_{s}$。攻击过程如下：

**步骤 1 拦截与替换：**

- **Client $\rightarrow$ M (拦截):** 客户端向服务器发送 $g^{x_{1}}$ 。
- **M $\rightarrow$ Server (伪造):** M 截获该消息，并将其替换为自己生成的 $g^{z_{s}}$ 发给服务器。

**步骤 2 拦截与替换：**

- **Server $\rightarrow$ M (拦截):** 服务器收到 $g^{z_{s}}$（误以为是客户端发来的），生成 $y_{1}$，并回复 $g^{y_{1}}$ 。
- **M $\rightarrow$ Client (伪造):** M 截获 $g^{y_{1}}$，将其替换为自己生成的 $g^{z_{c}}$ 发给客户端。

**密钥计算状态：** 此时，客户端和服务器计算出的会话密钥 $k_{11}$ 是不一样的 ：

- 客户端计算的密钥： $k_{client} = H((g^{z_{c}})^{x_{1}}) = H(g^{x_{1}z_{c}})$
- 服务器计算的密钥： $k_{server} = H((g^{z_{s}})^{y_{1}}) = H(g^{z_{s}y_{1}})$
- 而攻击者 **M 掌握了两个密钥**：M 可以利用自己的秘密值 $z_{c}$ 计算 $H((g^{x_{1}})^{z_{c}})$（等于 $k_{client}$），利用 $z_{s}$ 计算 $H((g^{y_{1}})^{z_{s}})$（等于 $k_{server}$）。

**步骤 3 窃听与篡改：**

- **Client $\rightarrow$ M (拦截):** 客户端开始发送加密数据，发送 $g^{x_{2}}, E(M_{1},k_{client})$ 。
- 攻击者 M 拦截该消息，使用 $k_{client}$ 解密得到明文 $M_{1}$。M 可以直接读取甚至将其篡改为 $M_{1}'$。
- **M $\rightarrow$ Server (转发):** M 将篡改后的消息用服务器的密钥 $k_{server}$ 重新加密，发送 $g^{z_{s2}}, E(M_{1}',k_{server})$。
- 服务器成功解密，完全不知道通信已经被中间人窃听和篡改。

------

### c. 提出并详细说明修复该问题的方法。 (10 points)

题目提示可以基于预共享的长期密钥或正确的公钥分发等假设 。为了修复缺乏身份验证的问题，我们可以引入**数字签名**（基于公钥基础设施 PKI）或**消息认证码 (MAC)**（基于预共享密钥）。

这里提供基于 **公钥分配假设 (Public Key Distribution)** 的修复方案：

**假设：**

客户端和服务器已经正确获取了对方的长期公钥。客户端拥有自己的私钥 $SK_{c}$，服务器拥有自己的私钥 $SK_{s}$。

**修复后的协议 (引入数字签名)：**

我们在 Diffie-Hellman 参数交换的步骤中加入数字签名，以确保参数不被篡改且来源真实。

1. **client $\rightarrow$ server:**

   $$g^{x_{1}}, Sign_{SK_{c}}(g^{x_{1}})$$

   *(客户端发送其公开参数，并用自己的私钥对其进行签名以证明身份)*

2. **server $\rightarrow$ client:**

   $$g^{y_{1}}, Sign_{SK_{s}}(g^{y_{1}}, g^{x_{1}})$$

   *(服务器发送其公开参数，并用私钥对自己的参数 $g^{y_{1}}$ 和客户端发来的参数 $g^{x_{1}}$ 一起签名。包含 $g^{x_{1}}$ 可以防止重放攻击)*

3. **client $\rightarrow$ server:**

   $$g^{x_{2}}, E(M_{1},k_{11}), Sign_{SK_{c}}(g^{x_{2}}, g^{y_{1}})$$

   *(后续的每一步交互都在交换新的参数时附加签名)*

**为什么能修复问题：**

通过这种方式，如果中间人试图在步骤 1 或步骤 2 中把 $g^{x_{1}}$ 或 $g^{y_{1}}$ 替换为自己的值，由于中间人没有客户端或服务器的长期私钥，他无法伪造出合法的数字签名 $Sign_{SK}(\dots)$。接收方在验证签名失败后，会立刻终止连接，从而成功防御了 MITM 攻击。

## English

### a. Explain in your own words what is a man-in-the-middle attack and why it can happen. (8 points) 

**Explanation:**

- A **Man-in-the-Middle (MITM) attack** occurs when an attacker secretly intercepts and relays communications between two parties who believe they are communicating directly with each other. The attacker can eavesdrop on the conversation or even alter the messages before passing them along.
- **Why it happens in this protocol:** The provided protocol aims to achieve perfect forward secrecy (PFS) by establishing fresh share keys for each message. However, it is vulnerable to MITM attacks because it completely lacks **authentication**. In steps 1 and 2, when the client and server exchange their public parameters ($g^{x_{1}}$ and $g^{y_{1}}$), there is no mechanism to verify the true identity of the sender. This anonymous Diffie-Hellman key exchange allows an attacker to easily step in and impersonate both the client and the server.

------

### b. Illustrate a man-in-the-middle attack to the protocol. (12 points) 

Let's assume an attacker (let's call them **M**) is positioned between the client and the server, capable of intercepting and modifying messages. M generates their own secret values, $z_{c}$ and $z_{s}$. The attack proceeds as follows:

**Step 1: Interception & Replacement**

- **Client $\rightarrow$ M (Intercepted):** The client attempts to send $g^{x_{1}}$ to the server.
- **M $\rightarrow$ Server (Forged):** M intercepts this message and sends their own generated parameter $g^{z_{s}}$ to the server instead.

**Step 2: Interception & Replacement**

- **Server $\rightarrow$ M (Intercepted):** The server receives $g^{z_{s}}$ (believing it's from the client), generates $y_{1}$, and replies with $g^{y_{1}}$.
- **M $\rightarrow$ Client (Forged):** M intercepts $g^{y_{1}}$ and replaces it with $g^{z_{c}}$, sending it to the client.

**Key Calculation State:**

At this point, the client and server compute different session keys, while M has the keys to communicate with both:

- Client computes: $k_{client} = H((g^{z_{c}})^{x_{1}}) = H(g^{x_{1}z_{c}})$
- Server computes: $k_{server} = H((g^{z_{s}})^{y_{1}}) = H(g^{z_{s}y_{1}})$
- **Attacker M knows both:** M calculates $H((g^{x_{1}})^{z_{c}})$ to communicate with the client, and $H((g^{y_{1}})^{z_{s}})$ to communicate with the server.

**Step 3: Eavesdropping & Tampering**

- **Client $\rightarrow$ M (Intercepted):** The client sends the encrypted message $g^{x_{2}}, E(M_{1},k_{client})$.
- M intercepts the message, decrypts it using $k_{client}$ to read $M_{1}$, and can modify it to a forged message $M_{1}'$.
- **M $\rightarrow$ Server (Forwarded):** M re-encrypts the tampered message using the server's key and sends $g^{z_{s2}}, E(M_{1}',k_{server})$. The server successfully decrypts it, completely unaware that the connection is compromised.

------

### c. Propose and detail your method to fix the problem. (10 points) 

To fix the vulnerability caused by the lack of authentication, we can rely on the assumption of **correct public keys distribution among the client and server**. We can integrate digital signatures into the parameter exchange.

**Assumption:**

The client possesses a private key $SK_{c}$ and the server has securely obtained the client's public key. Similarly, the server possesses a private key $SK_{s}$ and the client has the server's public key.

**Proposed Fix (Authenticated Diffie-Hellman):**

We append digital signatures to the messages to prove the sender's identity and bind the exchanged parameters to that identity.

1. **client $\rightarrow$ server:**

   $$g^{x_{1}}, Sign_{SK_{c}}(g^{x_{1}})$$

   *(The client sends their parameter and signs it with their private key).*

2. **server $\rightarrow$ client:**

   $$g^{y_{1}}, Sign_{SK_{s}}(g^{y_{1}}, g^{x_{1}})$$

   *(The server sends their parameter and signs both their parameter $g^{y_{1}}$ and the client's parameter $g^{x_{1}}$. Including $g^{x_{1}}$ prevents replay attacks).*

3. **client $\rightarrow$ server:**

   $$g^{x_{2}}, E(M_{1},k_{11}), Sign_{SK_{c}}(g^{x_{2}}, g^{y_{1}})$$

   *(Subsequent parameter exchanges are also signed).*

**Why this fixes the problem:**

If an attacker M tries to intercept and replace $g^{x_{1}}$ or $g^{y_{1}}$, they will not be able to generate a valid signature $Sign(\dots)$ because they do not have access to the legitimate private keys ($SK_{c}$ or $SK_{s}$). The receiving party will verify the signature using the pre-shared public key, find that it is invalid, and instantly drop the connection, effectively stopping the MITM attack.



# Question 2

## 中文

### a. 解释 A 和 B 如何通过该协议获取共享会话密钥。 (6 points)

**解答：**

A 和 B 获取共享会话密钥 $K_{AB}$ 的过程如下：

1. **A 的解密：** 在协议的第 2 步中，服务器 S 将包含会话密钥的加密消息发送给 A 。A 收到后，使用自己与服务器共享的长期密钥 $K_{AS}$ 解密第一部分 $\{K_{AB}\}_{K_{AS}}$。通过解密，A 成功获取了会话密钥 $K_{AB}$ 。
2. **B 的解密：** A 在第 3 步中将消息的第二部分 $\{K_{AB}\}_{K_{BS}}$ 转发给 B 。B 收到该消息后，使用自己与服务器共享的长期密钥 $K_{BS}$ 对其进行解密，从而也获取了相同的会话密钥 $K_{AB}$ 。 至此，A 和 B 都获得了服务器 S 分发的共享密钥 $K_{AB}$。

## b. 解释攻击者 C 如何对该协议发起攻击，使得 C 分别与 A 和 B 建立会话密钥，而 A 和 B 却以为他们互相建立了共享密钥。 (10 points)

**解答：** 该协议的一个严重安全漏洞在于：**服务器返回的加密密钥包中，没有包含通信对端的身份信息（Identity Binding）**。这导致接收方无法验证该密钥究竟是分配给谁的。攻击者 C 可以利用这一点发起以下攻击 ：

1. **拦截 A 的请求：** 攻击者 C 拦截 A 发给 S 的初始请求（第 1 步）。

2. **C 伪造向 S 请求与 A 通信：** C 冒充自己想与 A 通信，向服务器 S 发送请求：$C \rightarrow S: C, A, \{C, A\}_{K_{CS}}$。服务器 S 正常响应，返回给 C：$\{K_{CA}\}_{K_{CS}}, \{K_{CA}\}_{K_{AS}}$。此时 C 掌握了 $K_{CA}$。

3. **C 伪造向 S 请求与 B 通信：** C 又向服务器 S 发送请求，希望与 B 通信：$C \rightarrow S: C, B, \{C, B\}_{K_{CS}}$。服务器 S 正常响应，返回给 C：$\{K_{CB}\}_{K_{CS}}, \{K_{CB}\}_{K_{BS}}$。此时 C 掌握了 $K_{CB}$。

4. **C 欺骗 A 和 B：** C 将刚才从服务器获取的两个加密包组合起来，伪装成服务器对 A 初始请求的响应，发送给 A：$C \rightarrow A: \{K_{CA}\}_{K_{AS}}, \{K_{CB}\}_{K_{BS}}$。

5. **A 和 B 被误导：** * A 使用 $K_{AS}$ 解密第一部分，得到 $K_{CA}$。由于密文中没有身份信息，A 误以为这就是 S 分配给 A 和 B 的会话密钥 $K_{AB}$。

   - A 按照协议将第二部分 $\{K_{CB}\}_{K_{BS}}$ 转发给 B（A 以为发的是 $\{K_{AB}\}_{K_{BS}}$）。

   - B 收到后用 $K_{BS}$ 解密，得到 $K_{CB}$。同样，B 误以为这就是与 A 的会话密钥 $K_{AB}$

     **结果：** A 使用 $K_{CA}$ 加密消息，B 使用 $K_{CB}$ 加密消息。攻击者 C 掌握这两个密钥，可以完美地进行中间人窃听和篡改 。

### c. 提出并详细说明修复该问题的方法。 (14 points)

**解答：**

为了修复这个漏洞，必须在加密的票据（Ticket）中**绑定通信对端的身份信息（Identity Binding）**。这样，当 A 或 B 解密密钥包时，可以明确知道这个密钥是用来和谁通信的。

**修复后的协议如下：**

1. $A \rightarrow S: A, B, \{A, B\}_{K_{AS}}$  (保持不变，或加入 Nonce 防止重放攻击)

2. $S \rightarrow A: \{K_{AB}, \mathbf{B}\}_{K_{AS}}, \{K_{AB}, \mathbf{A}\}_{K_{BS}}$

   *(服务器在给 A 的密文中加入 B 的身份，在给 B 的密文中加入 A 的身份)*

3. $A \rightarrow B: \{K_{AB}, \mathbf{A}\}_{K_{BS}}$

**修复原理：**

如果攻击者 C 尝试重复上述攻击，向 A 发送 $\{K_{CA}, \mathbf{C}\}_{K_{AS}}$ 和 $\{K_{CB}, \mathbf{C}\}_{K_{BS}}$。

- 当 A 解密自己那部分时，看到里面的对端身份是 **C** 而不是预期的 **B**，A 会立刻发现异常并终止连接。

- 当 B 解密自己那部分时，看到对端身份是 **C** 而不是宣称发送消息的 **A**，B 也会发现异常并拒绝该密钥。

  这种将身份信息包含在密文内的做法，有效防止了密钥被移花接木。

## English Version

### a. Explain how A and B can acquire the shared session key through the protocol. (6 points)

**Answer:**

A and B acquire the shared session key $K_{AB}$ through the following decryption processes:

1. **A's Decryption:** In step 2 of the protocol, the server S sends the encrypted messages containing the session key to A. A uses its long-term secret key $K_{AS}$, shared with the server, to decrypt the first part: $\{K_{AB}\}_{K_{AS}}$. Through this decryption, A successfully obtains the session key $K_{AB}$.

2. **B's Decryption:** In step 3, A forwards the second part of the message, $\{K_{AB}\}_{K_{BS}}$, to B. Upon receiving it, B uses its own long-term secret key $K_{BS}$, shared with the server, to decrypt the message and obtain the same session key $K_{AB}$. Now, both A and B have acquired the shared key $K_{AB}$ distributed by the server.

### b. Explain an attack on the protocol where the attacker C establishes shared session keys with A and B while both A and B think they established a shared session key with each other. (10 points)

**Answer:** A critical security vulnerability in this protocol is the **lack of identity binding** within the encrypted tickets. The ciphertexts returned by the server do not include the identity of the intended communication peer. Attacker C can exploit this to launch the following attack:

1. **Intercept A's request:** Attacker C intercepts A's initial request to S (Step 1).

2. **C requests a key with A:** C initiates a legitimate request to S claiming they want to communicate with A: $C \rightarrow S: C, A, \{C, A\}_{K_{CS}}$. S responds to C with: $\{K_{CA}\}_{K_{CS}}, \{K_{CA}\}_{K_{AS}}$. C now possesses $K_{CA}$.

3. **C requests a key with B:** C initiates another request to S claiming they want to communicate with B: $C \rightarrow S: C, B, \{C, B\}_{K_{CS}}$. S responds to C with: $\{K_{CB}\}_{K_{CS}}, \{K_{CB}\}_{K_{BS}}$. C now possesses $K_{CB}$.

4. **C deceives A and B:** C combines the tickets obtained from the server and sends them to A, pretending to be the server responding to A's initial request: $C \rightarrow A: \{K_{CA}\}_{K_{AS}}, \{K_{CB}\}_{K_{BS}}$.

5. **A and B are misled:** * A decrypts the first part using $K_{AS}$ and gets $K_{CA}$. Since there is no identity inside, A mistakenly believes this is $K_{AB}$.

   - A forwards the second part $\{K_{CB}\}_{K_{BS}}$ to B.

   - B decrypts it using $K_{BS}$ and gets $K_{CB}$. B mistakenly believes this is the session key with A. **Result:** A encrypts messages using $K_{CA}$, and B encrypts using $K_{CB}$. Since attacker C knows both keys, C can seamlessly intercept, decrypt, read, and re-encrypt traffic between A and B, successfully executing a Man-In-The-Middle attack.


### c. Propose and detail your method to fix the problem. (14 points)

**Answer:**

To fix this vulnerability, it is essential to implement **Identity Binding** within the encrypted tickets. The server must include the identity of the communicating peer *inside* the encryption so that when A or B decrypts the package, they can explicitly verify who the key is intended for.

**Proposed Fixed Protocol:**

1. $A \rightarrow S: A, B, \{A, B\}_{K_{AS}}$  *(Remains unchanged, though adding a Nonce here is good practice against replay attacks)*

2. $S \rightarrow A: \{K_{AB}, \mathbf{B}\}_{K_{AS}}, \{K_{AB}, \mathbf{A}\}_{K_{BS}}$

   *(The server includes B's identity in A's ticket, and A's identity in B's ticket)*

3. $A \rightarrow B: \{K_{AB}, \mathbf{A}\}_{K_{BS}}$

**Why this fixes the problem:**

If attacker C attempts the same attack and sends $\{K_{CA}, \mathbf{C}\}_{K_{AS}}$ and $\{K_{CB}, \mathbf{C}\}_{K_{BS}}$ to A.

- When A decrypts their portion, they will see that the intended peer is **C**, not the requested **B**. A will immediately detect the anomaly and drop the connection.

- Similarly, when B decrypts their portion, they will see the peer is **C**, not the expected **A**. B will reject the key.

  By binding the identities cryptographically to the session key, the attacker can no longer successfully substitute tickets.



# Question 3

## 中文

### a. 补全协议的第 5 步。给出一个与第 3 步类似的公式，展示 B 是如何计算共享密钥的。(8 points)

**解答：** 在 Diffie-Hellman 密钥交换中，双方必须计算出相同的秘密值。根据表格定义，公钥和私钥的关系是 $pk = g^{sk}$ 。 A 在第 3 步计算的共享密钥是： $pk_{B2}^{sk_{A1}} || pk_{B1}^{sk_{A3}} || pk_{B2}^{sk_{A3}} || pk_{B3}^{sk_{A3}}$ 

这实际上等于：

$g^{sk_{B2}sk_{A1}} || g^{sk_{B1}sk_{A3}} || g^{sk_{B2}sk_{A3}} || g^{sk_{B3}sk_{A3}}$

B 收到了 A 的公钥 $pk_{A1}$ 和 $pk_{A3}$ ，并且 B 拥有自己的私钥 $sk_{B1}, sk_{B2}, sk_{B3}$ 。为了计算出完全相同的字符串，B 需要使用自己的私钥和 A 的公钥进行指数运算。第 5 步的公式如下：

**B calculates the shared secret as:**

$$pk_{A1}^{sk_{B2}} || pk_{A3}^{sk_{B1}} || pk_{A3}^{sk_{B2}} || pk_{A3}^{sk_{B3}}$$

### b. 比较简化的 X3DH 与基础 (EC)DH 密钥协商协议的开销。评估通信开销（消息数量）和计算开销（指数运算的次数，不包括生成密钥对的开销）。(8 points)

**解答：**

- **基础 (EC)DH 协议：**

  - **通信开销：** 2 条消息（A 发送公钥给 B，B 发送公钥给 A，即 1 次往返）。
  - **计算开销：** 2 次指数运算（排除生成密钥的开销，A 和 B 各需进行 1 次指数运算来计算最终的共享密钥）。

- **简化的 X3DH 协议：**

  - **通信开销：** 3 条消息（A 向 S 请求 B 的公钥 ；S 返回公钥给 A ；A 发送包含身份和公钥的消息给 B ）。

  - **计算开销：** 8 次指数运算（A 在第 3 步进行了 4 次指数运算来拼接共享密钥 ，B 在第 5 步也需要进行 4 次相应的指数运算来得出相同的密钥）。

### c. 简化的 X3DH 协议是否容易受到中间人 (MITM) 攻击？如果不是，解释原因；如果是，请演示攻击过程。(14 points)

**解答：**

**是的，它容易受到特定形式的中间人攻击（具体为身份冒充/身份错绑攻击）。**

**原因与攻击过程：** 虽然客户端与服务器 (S) 之间的通信是经过认证的 ，这意味着 A 拿到的确实是 B 真实的公钥，因此 A 发送给 B 的加密数据，中间人是**无法解密**的（因为攻击者没有 B 的私钥）。 但是，正如提示所言，**初始阶段 A 发送给 B 的消息（第 4 步）是没有经过网络认证的** 。攻击者可以利用这一点劫持与 B 的会话：

1. **拦截：** 攻击者 M 拦截 A 发给 B 的初始消息 $A, pk_{A1}, pk_{A3}$。

2. **替换与伪造：** M 无法解密 A 的后续密文，但 M 的目标是欺骗 B。M 生成自己的密钥对 $(pk_{M1}, sk_{M1})$ 和 $(pk_{M3}, sk_{M3})$。M 将被拦截消息中的公钥替换为自己的，并向 B 发送：$A, pk_{M1}, pk_{M3}$。

3. **B 被误导：** B 收到消息后，因为没有机制去服务器 S 验证发来的 $pk_{A1}$ 是否真的属于 A，B 会盲目相信这就是 A 的公钥。

4. **建立虚假信任：** B 使用 $pk_{M1}$ 和 $pk_{M3}$ 计算共享密钥。由于 M 拥有对应的私钥，M 也能计算出相同的密钥。

   **结果：** B 以为自己正在和 A 建立安全会话，但实际上 B 的共享密钥是和攻击者 M 建立的。M 可以随后伪造 A 的身份向 B 发送恶意消息。

## English Version

### a. Complete Step 5 in the protocol. You need to give a formula as in Step 3 to show how the shared secret is calculated by B. (8 points)

**Answer:** In Diffie-Hellman, both parties must arrive at the same shared secret. The relationship between public and private keys is $pk = g^{sk}$. A computes the shared secret as: $pk_{B2}^{sk_{A1}} || pk_{B1}^{sk_{A3}} || pk_{B2}^{sk_{A3}} || pk_{B3}^{sk_{A3}}$ 

Mathematically, this expands to:

$g^{sk_{B2}sk_{A1}} || g^{sk_{B1}sk_{A3}} || g^{sk_{B2}sk_{A3}} || g^{sk_{B3}sk_{A3}}$

B receives A's public keys $pk_{A1}$ and $pk_{A3}$ , and possesses its own private keys $sk_{B1}, sk_{B2}, sk_{B3}$. To compute the exact same string, B uses A's public keys as the base and its own private keys as the exponents.

**B calculates the shared secret as:**

$$pk_{A1}^{sk_{B2}} || pk_{A3}^{sk_{B1}} || pk_{A3}^{sk_{B2}} || pk_{A3}^{sk_{B3}}$$

### b. Compare the costs of the simplified X3DH the with basic (EC)DH key agreement protocol. You need to evaluate the communicating cost via the number of messages and the computing cost via the number of exponentiations involved in these protocols, excluding the cost for generating key pairs. (8 points)

**Answer:**

- **Basic (EC)DH Protocol:**

  - **Communication Cost:** 2 messages (A sends public key to B, B sends public key to A; equivalent to 1 round trip).
  - **Computing Cost:** 2 exponentiations (Excluding key generation, A and B each perform 1 exponentiation to derive the final shared secret).

- **Simplified X3DH Protocol:**

  - **Communication Cost:** 3 messages (A requests keys from S; S returns keys to A; A sends identity and keys to B ).

  - **Computing Cost:** 8 exponentiations (A performs 4 exponentiations in Step 3 to build the concatenated secret, and B must correspondingly perform 4 exponentiations in Step 5).

### c. Is the simplified X3DH protocol vulnerable to Man-In-The-Middle (MITM) attacks? If your answer is no, explain your reason; otherwise, illustrate an MITM attack to the protocol. (14 points)

**Answer:**

**Yes, it is vulnerable to a specific form of MITM attack known as an Impersonation or Identity Misbinding attack.**

**Reason & Illustration:** Because the communication between clients and the server is authenticated, A receives B's genuine public keys. Therefore, an attacker *cannot* decrypt the actual payload A intends for B (preventing classic eavesdropping). However, as the hint suggests, **the initial session communication from client to client (Step 4) is unauthenticated**. An attacker (M) can exploit this to hijack the session towards B:

1. **Interception:** Attacker M intercepts A's message to B: $A, pk_{A1}, pk_{A3}$.

2. **Replacement & Forgery:** M generates their own key pairs $(pk_{M1}, sk_{M1})$ and $(pk_{M3}, sk_{M3})$. M replaces A's public keys with their own and forwards the forged message to B: $A, pk_{M1}, pk_{M3}$.

3. **B is Misled:** B receives the message. Because B does not contact the server S in this simplified protocol to verify if $pk_{A1}$ actually belongs to A, B blindly accepts $pk_{M1}$ as A's long-term public key.

4. **False Trust Established:** B calculates the shared secret using the attacker's public keys ($pk_{M1}, pk_{M3}$). Since M holds the corresponding private keys, M calculates the exact same shared secret.

   **Result:** B believes it has established a secure session key with A, but in reality, B shares the key with attacker M. M can now send encrypted messages to B, successfully impersonating A.
