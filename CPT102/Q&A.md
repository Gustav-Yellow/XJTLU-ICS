# Week1 Overview

• Both space efficiency & time efficiency are metrics used to evaluate the performance of an algorithm (and a data structure). (T or F?)

空间效率和时间效率都是用于评估算法（和数据）性能的指标结构）。（T 还是 F？)

True

• Dynamic data structures are more space efficient in general. (T or F?)

一般来说,动态数据结构的空间效率更高。

True

• Static data structures are more time efficient in general. (T or F?)

一般来说,静态数据结构的时间效率更高。

True

• Information hiding is the principle that users of a software component need to know only the essential details of how to *initialize* and *access* the component, and do not need to know the details of the implementation (T or F?)

信息隐藏原则是软件组件的用户只需要知道如何初始化和访问组件的基本细节，而不需要知道实现的细节

True

# Week2 Collections

• Name 3 type of collections that can be implemented under Java Programming with Linear collections

命名 3 种可以在 Java Programming with Linear collections 下实现的集合类型

​	List, Set, Map

• Name 3 operations that can be implemented under Java Programming with Linear collections

​	HashSet, HashMap, ArrayList

• Name 2 type of collections that can be implemented under Java Programming with Hierarchical collections

​	TreeMap, TreeSet

• Name 4 operations that can be implemented under Java Programming with Hierarchical collections

​	insert(), remove(), 

• What is a software “library”?

​	"library" is a collection of pre-written code, routines, classes, functions, or procedures that can be reused 	and integrated into software applications

​	“库”是预先编写的代码、例程、类、函数或过程的集合，可以重用并集成到软件应用程序中

• Define Java “Package”. 

​	In Java programming, a package is a mechanism for organizing a group of related classes and interfaces 	into a single namespace

​	在 Java 编程中，包是一种将一组相关类和接口组织到单个命名空间中的机制

• Name Java’s IO library.



• Name Java’s GUI library.

• What is the Java statement to include package or class into your program?

## Week 5

• Java has specified a “Queue” interface. (T or F)  Java 指定了一个 "队列 "接口

True

• Java does not have any class support for “Priority Queue”. (T or F)  

Java 没有任何类支持"优先队列"

False

• peek() operation under the Queue interface will throw an exception if the queue is empty. (T or F)  如果队列为空，则 Queue 接口下的 peek（） 操作将抛出异常。（T 或 F）

False return null value

• poll() operation under the Queue interface will throw an exception if the queue is empty. (T or F)  如果队列为空，则 Queue 接口下的 poll（） 操作将抛出异常。（T 或 F）

False

• There is an element() method under the Queue interface. (T or F)

Queue 接口下有一个 element() 方法(T 或 F)。

 True

• Iterable is an interface specification for a class that is equipped with an Iterator.

Iterable 是配备 Iterator 的类的接口规范。

True

• Iterator is an interface specification for a class that can generate iterative elements.

Iterator 是可以生成迭代元素的类的接口规范。

True

## Lecture 6

• An object defined under a comparable class will have a “natural ordering”. (T or F) 

True

• Objects declared under a comparable class can be compared using which method? 

compareTo(Object 0)

• What is the signature of the *compareTo* method? 

Object o

• Which method can be used to sort list of comparable objects?

哪种方法可用于对可比较对象的列表进行排序?

Collections.sort()

• Comparator is an object that can compare other objects. (T or F) 

True

• What is the signature for the *compare()* method? 

compare(Object 01, Object 02)

• A comparable class can implement multiple comparators. (T or F)

True

## Lecture 7

• A method will do what when something goes wrong? 

Throw a Exception

• An exception provides a local exit when something goes wrong. (T or F) 

False

• Name 3 cases when an exception can be thrown. 

Input/Output Errors, Arithmetic Errors, Null Pointer Dereference

• What do we do with exceptions?

Try Catch to solve the error or just throw the potential Exception and continue to run.

• Exceptions can be caught using what Java statement?

try catch

• Does exception have a type? 

a lot of type

• After the exception handler finishes its work, what will the program do next? 

continue to run the follwing codes

• Can exception handler use information in the exception object?

Yes

• What does “**e.getMessage**()” do where **e** is an exception object?

print the exception's System error message

• Name 3 common Java exceptions. 

IndexOutOfBoundException, FileNotFOundException 

• RuntimeExceptions doesn’t have to be handled. (T or F)

True

• IOException doesn’t have to be handled. (T or F)

False

• Which Java statement can cause an exception? 

Throw

• What happens when we try adding an element to an immutable List?

Exception

• Does a Java Interface provide a ‘constructor’? 

No

• ArrayList implements which Interface? 

List

• **public interface** List <E> extends which Java Interface?

Collection

# Lecture 8

• What are the key features of an abstract class?

can hold method headers and don defined immediately.

• Can an abstract class be instantiated? 

Cannot

• Abstract methods can be defined within a class to save implementation efforts. (T or F)

False

• What are the key issues of implementation when we remove an element from an ArrayList?

 Outofbound; wrong the shift the following elements to new index position.

• What are the key issues of implementation when we add an element from an ArrayList?

Outofbound; Ensure the capacity of the array.

# Lecture 9

• remove() is compulsory in Iterator implementation. (T or F)

False; remove不是必须实现的

• How does ArrayList make use of the ‘type parameter’ in its implementation? 

使用泛型E

• Which element will be removed by ArrayList.remove()?

next指针指向的

• What does ArrayList.next() check before returning the next element in the list? 

Whether the next element is null.

• How does ArrayList.remove() ensure only 1 element can be removed after each call to next()?



• What can happen if 2 or more Iterators running concurrently under the same ArrayList? Name 2 scenarios. 

chaos，miss up data structure

# Lecture 10

• O(log(n)) < O(sqrt(n)) (T or F) 

• O(n^n) < O(n!) (T or F) 

• O(2^n) < O(n^n) (T or F) 

• When analysing the cost of an algorithm, loop usually is the focus. (T or F) 

• Which of the following operations is more expensive?

• Reading a line from a file

• Reading a line from a user

• Worst case cost analysis is usually more difficult than average cost analysis. (T or F) 

False

# Lecture 12

• When do you write test cases for “black box” testing? Before or after implementation?

 

• Explain why array implementations of queue are slow. 



• Linked list allows data removal by? 



• Define references/pointers. 



• What is the purpose of garbage collection in memory management? 

to ensure there have consistent free memory to use.
