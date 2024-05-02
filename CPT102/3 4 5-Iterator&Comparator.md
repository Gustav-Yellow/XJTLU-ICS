# Iterator 迭代器

• Iterator may access inside of collection 迭代器可以访问集合内部

• Iterator provides elements one at a time. 迭代器一次可以选取一个元素

• Each Collection class needs an associated Iterator class 每个 Collection 类都需要一个关联的 Iterator 类

Operation: 迭代器的方法

• **hasNext**() : *returns* true *iff there is another value to get* 返回true如果容器接下来还存有数据

• **next**() : *returns the next value* 获取容器下一个元素

注意：for each（增强for循环只能应用于实现了Iterable接口的类）

Iterable和Iterator接口之间是独立的，实现类先继承Iterable接口然后实现其中的iterator方法，返回一个继承了Iterator接口的迭代器实现类，接下来就可以通过调用iterator方法返回的迭代器实现类来进行迭代了

```java
Iterable <T>
public Iterator<T> iterator();
```

```java
Iterator <T>
public boolean hasNext();
public T next();
```

```java
Iterator<type > itr = construct iterator
while (itr.hasNext() ){
	type var = itr.next();
	… var …
}
```

迭代器并不只属于Collections类，任何类都可以实现Iterator来实现迭代

### Creating Iterator

```java
public class NumberSequence implements Iterable<Integer>{
	private int start;
	private int step;
	public NumberSequence(int start, int step){
		this.start = start;
		this.step = step;
	}
	public Iterator<Integer> iterator(){
		return new NumberSequenceIterator(this);
	}
  
  private class NumberSequenceIterator implements Iterator<Integer>{
		private int nextNum;
		private NumberSequence source;
		public NumberSequenceIterator(NumberSequence ns){
			source = ns;
			nextNum = ns.start;
		}
		public boolean hasNext(){ 
			return true;
		}
		public Integer next(){
			int ans = nextNum;
			nextNum += ns.step;
			return ans;
		}
	} // end of NumberSequenceIterator class
} // end of Number Sequence class
```

# Sorting 比较

## Comparable<T> 接口

• If a class implements the **Comparable<*T* >** interface 

​	• Objects from that class have a “natural ordering” 该类中的对象具有“自然排序” 默认是从小到大

​	• Objects can be compared **using** the **compareTo()** method 要实现 compareTo（Object o） 方法比较对象

​	• **Collections.sort()** can sort Lists of those objects automatically 可以自动调用传入对象的compareTo方法进行比较，传入的对象必须实现Comparable接口

Comparable<T> 是接口，如果一个容器想要能够被Collections.sort()方法来进行排序，需要保证该Collections类实现了Comparable<T>接口的comparaTo()方法。将容器放入Collections.sort()类之后，会自动根据该容器的comparaTo(Object o)方法的排序方式来对容器进行排序

compareTo(Object) : int 返回一个整数，如果整数为负则是正序，整数为正则为倒叙

是西安了Comparable接口的类可以自己跟自己比较

```java
public class User implements Comparable<User> {
    private String name;
    
    @Override
    public int compareTo(User user) {
        // name是String，String类自己也实现了comparaTo的对比，因此可以继续使用String类的comparaTo来进行对比
        if (this.age == user.age) return this.name.compareTo(user.name);
        return this.age - user.age; //将this想像成一排不变的对象(已经按照要求排好序的)，而User就是当前要插入的对象，只有user属性小于this属性才插入从而升序，个人理解，希望有所帮助
    }
}
class Test {
    public static void main(String[] args) {
        List<User> list=new ArrayList<User>();
        .....
        Collections.sort(list); 这样就是直接使用comparaTo(Object o)的方法来进行比较
        System.out.println("Comparable:" + list);
    }
}
```

• ob1.compareTo(ob2) 对比ob1和ob2的值

​	• returns –ve if ob1 ordered before ob2 如果ob1小于ob2，则返回负数（即0b1 - ob2 < 0）

​	• returns 0 if ob1 ordered with ob2 如果返回0则代表两个数相等

​	• returns +ve if ob1 ordered after ob2  如果ob1大于ob2，则返回正数 (即0b1 - ob2 > 0)

## Comparator 函数接口

对一组数据进行排序有两种方法，除了上面的直接使用Collections.sort对一个继承了Comarable接口并且实现了comparaTo方法的容器进行自然排序以外，还可以通过改写Comparator接口的compare(T t1, T t2)方法

类自身实现Comparator接口重写compare方法的比较器并传入Collections.sort()方法中进行按照指定的compare方法进行比较

Requires

• **public** int compare(T o1, T o2);

​	→ –ve if o1 ordered before o2

​	→ 0 if o1 equals o2 [ must be compatible with equals()! ]

​	→ +ve if o1 ordered after o2 

```java
public class User implements Comparable<User> {
    private String name;
    
    // 类中实现的compara方法
    @Override
    public int compare(User o1, User o2) {
        return o1.age-o2.age;
    }
}
class Test {
    public static void main(String[] args) {
        List<User> list=new ArrayList<User>();
        .....
        // 使用类中实现的compara方法来进行排序
        Collections.sort(list, new User()); // 类实现了的Comparator能满足需求
        System.out.println("类自身实现Comparator:"+list);
        
        //现在我想要按照名字升序，显然类中实现的不能满足要求，于是可以在类外自己实现想要的比较器
        Collections.sort(list, new Comparator<User>() {
            @Override
            public int compare(User o1, User o2) {
                return o1.getName().compareTo(o2.getName()); //按照名字升序,使用String类实现的c
            }
        });
        System.out.println("匿名内部类方式："+list);
        //由于Comparator接口是一个函数式接口，因此根据jdk1.8新特性，我们可以采用Lambda表达式简化代码
        Collections.sort(list,(u1,u2)->{return u1.getName().compareTo(u2.getName());});
        System.out.println("Lambda表达式方式："+list);
    }
}
```

# Exception 异常

当一个方法在运行或者编译时遇到异常的时候，需要抛出一个一场来终止程序

An Exception is a “non-local exit”  异常时非本地出口

当遇到异常的时候，两种处理方法

- try catch
- throw new Exception

如果使用throw来抛出异常，可以详细定义报错的信息让错误更清晰地展示

```Java
try {
	… code that might throw an exception
}
catch (〈ExceptionType1〉 e1) { …actions to do in this case….}
catch (〈ExceptionType2〉 e2) { …actions to do in this case….}
catch (〈ExceptionType3〉 e3) { …actions to do in this case….}

```

try catch 操作方法:

1. 捕获异常，如果try代码块中的代码出现异常，则停止并跳转到catch代码块
2. 如果存在多个异常捕获，则匹配try中抛出的异常和catch中的哪一个相同或被包涵
3. 匹配到正确的catch后，跳转到最硬的代码块中执行异常处理代码
4. catch运行结束后，继续执行接下来的代码

## Types of Exception 异常的类型

 

**RuntimeExceptions don’t have to be handled**:

• An uncaught RuntimeException will result in an error message 运行时异常

​	• You can catch them if you want. 可以捕获也可以不捕获，最终会展示报错信息

• **Other Exceptions must be handled**: 编译异常 必须被捕获

​	• eg IOException (which is why we always used a **try…catch** when opening files).

​	通常使用try catch来捕获处理

# Generic and Type variable “泛型”和类型变量

• Declaring a variable/field holding a List: 声明一个包含 List 的变量/字段:

​	• Must specify the type of the elements in the List 生命容器必须告知其变量

​		private List <**Shape**> drawing;

• Constructing a List object: 构建一个List对象

​	• Must specify the type of the elements in the List

​		crowd = **new** ArrayList <**Face**> ();

• Defining the List interface, or the ArrayList class:

​	• We are defining *every* kind of List 

​	• We use a *type variable* to stand for whatever element type is specified in declaration or constructor. 可以使用泛型，代表之后list存放的类型可以留作后续被引用的时候指定

​			**public interface** List <E> **extends** Collection <E> 

​	• E will be bound to a real type when a List is declared or constructed
