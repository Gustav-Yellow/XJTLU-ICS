# Virtual Machine and Distributed System 虚拟机与分布式系统

## Virtual Machine 虚拟机

**Virtualization** is technology that allows to create multiple simulated environments or dedicated resources from a single, physical hardware system

**虚拟化**是一种允许从单个物理硬件系统创建多个模拟环境或专用资源的技术

Software called a **hypervisor** connects directly to that hardware and allows to split a system into separate, distinct, and secure environments known as **virtual machines (VMs).**

被称为**管理程序**的软件直接与硬件连接，可将系统分割成独立、不同和安全的环境，称为**虚拟机（VM）**。

**Virtual machine manager** (VMM) or **hypervisor** – creates and runs virtual machines by providing interface that is **identical** to the host (except in the case of paravirtualization)

**虚拟机管理器** (VMM)或**管理程序** -通过提供与主机**相同的**接口来创建和运行虚拟机(半虚拟化的情况除外)

Virtual machine implementations involve several components:

虚拟机实施涉及以下几个组件：

- **Host** – the physical hardware equipped with a hypervisor.

  主机 - 配备有管理程序的物理硬件。

- **Guest** – an operating system

  **Guest** -操作系统

- Single physical machine can run multiple operating systems concurrently, each in its own virtual machine

  单个物理机可以同时运行多个操作系统，每个操作系统都在其自己的虚拟机中

The hypervisor provides a **layer between the hardware (the physical host machine) and the Virtual Machines (guest machines).**

管理程序在硬件（物理主机）和虚拟机（客户机）之间提供了一个**层**。

<img src="img/VMachine/img1.png" style="zoom:33%;" />

### Implementation of VMMs VMM 的实现

Types of virtual machine manager VMMs:

- **Type 0 hypervisors** **-** *Hardware-based solutions* that provide support for virtual machine creation and management via firmware.

  **0 型管理程序** **-** *基于硬件的解决方案*，通过固件为虚拟机创建和管理提供支持。

- 

