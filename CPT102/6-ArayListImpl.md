# Implement ArrayList

## Difference between Interface, Abstract Class and Class 接口，抽象类，实现类的区别

- Interface 接口

  - Specifiy types
  - Only defines the method headers

  List<E>

  Specify List contains E type elements

- Abstarct Class 抽象类

  - implements Interface

  - defines some methods
  - leaves other methods “abstract”

  AbstractList <E >

  - implements List <E >

  - defines array of <E >

  - defines addAll, subList, …

  - add, set, get, … are left **abstract**

- Class 类

  - extends Abstract Class
  - defines data structures
  - defines basic methods
  - defines constructors

  ArrayList<E>

  - extends AbstractList
  - implements fields & constructor
  - implements add, get, …

### 创建抽象列表

AbstractList cannot be instantiated. AbstractList 不能被实例化。

```java
// 定义一个抽象列表
public abstract class AbstractList <E> implements List< E>{

	//没有构造器或者类的成员变量

	// 如果是抽象方法，则需要加上abstract，则在抽象类中可以不实现，需要实现类来实现
	public abstarct nt size();

  	public boolean isEmpty(){
    	return (size() == 0);
  	}

	public abstract E get(int index);

  	public void add(int index, E element){
    	throws new UnsupportedOperationException();
  	}

	public boolean add(E element){
		add(size(), element);
	}

 	public boolean contains(Object ob){
		for (int i = 0; i<size(); i++) 
		if (get(i).equals(ob) ) return true;
		return false;
	}
  
	public void clear(){
		while (size() > 0)
		remove(0);
	}

}

```

### 实现抽象列表

```java
public class ArrayList <E> extends AbstractList<E>{
  // fields to hold the data:
  need an array for the items and an int for the count.
    
  // constructor(s) 
  Initialise the array
    
  // definitions of basic methods not defined in AbstractList
  // 也可以重写AbstractList中已经实现的方法
  size() 
  get(index)
  set(index, value) 
  remove(index)
  add(index, value)
  iterator()
    
  // (other methods are inherited from AbstractList )
    
  // definition of the Iterator class
}
```

## 实现ArrayList

- 需要两个成员变量：

  - E[] data; // 用来存放数据

  - int count; // 用来统计一共存放了多少元素

- size()
- get and set
- Add(index, element)

```java
public class ArrayList <E> extends AbstractList <E> {
  // 要使用泛型，才能使列表具有泛用性
	private E[ ] data;
	private int count=0;
	private static int INITIALCAPACITY = 16;
  
  
	public ArrayList(){
    // 定一个一个Objec[]列表，然后cast到E[]
		data = (E[]) new Object[INITIALCAPACITY];
  	}
  
  /** Returns number of elements in collection as integer */
	public int size () {
		return count;
	}
  
  /** Returns true if this set contains no elements. */
  	public boolean isEmpty(){
		return count==0;
	}
  
  /** Returns the value at the specified index.
	* Throws an IndexOutOfBoundsException is index is out of bounds */
	public E get(int index){
    if (index < 0 || index >= count) 
    	throw new IndexOutOfBoundsException();
    return data[index];
  	}
  
  /**Replaces the value at the specified index by the specified value
  * Returns the old value.
  * Throws an IndexOutOfBoundsException if index is out of bounds */
  	public E set(int index, E value){
    	if (index < 0 || index >= count) 
    		throw new IndexOutOfBoundsException();
    	E ans = data[index];
    	data[index] = value;
    	return ans;
	}
  
  /** Removes the element at the specified index, and returns it.
  * Throws an IndexOutOfBoundsException if index is out of 
  bounds */ 
  public E remove (int index){
    if (index < 0 || index >= count) 
    	throw new IndexOutOfBoundsException();
    E ans = data[index]; ←remember
    for (int i=index+1; i< count; i++) // ←move items down
    	data[i-1]=data[i];
    count--; // ←decrement
    data[count] = null; // ←delete previous last element
    return ans; // ←return 
  }
  
  /** Adds the specified element at the specified index.*/
  public void add(int index, E item){
    if (index < 0 || index > count) // ←can add at end?
    	throw new IndexOutOfBoundsException();
    ensureCapacity(); ←make room
    for (int i=count; i > index; i--) // ←move items up
    	data[i]=data[i-1];
    data[index]=item; ←insert  // ←insert
    count++; ←increment  // ←increment
  }
  
  // Extends the capacity
  private void ensureCapacity () {
    if (count < data.length) return; // ← room already
    E [ ] newArray = (E[ ]) (new Object[data.length * 2]);
    for (int i = 0; i < count; i++) // ← copy to new array
    	newArray[i] = data[i]; 
    data = newArray; // ← replace
  }
  
  /** Returns an iterator over the elements in the List */
	public Iterator <E> iterator(){
		return new ArrayListIterator<E>(this);
	}
  
  
}
```

ArrayList's iterator 迭代器

```java
/** Definition of the iterator for an ArrayList 
* Defined inside the ArrayList class, and can therefore access
* the private fields of an ArrayList object. */
private class ArrayListIterator <E> implements Iterator <E>
{
  // fields to store state
  private ArrayList<E> list;// reference to the list it is iterating down
	private int nextIndex = 0; // the index of the next value to return
	private boolean canRemove = false;
  
  // constructor
  private ArrayListIterator (ArrayList <E> list) {
		this.list = list;
	}
  
  // hasNext(), 
  /** Return true if iterator has at least one more element */
	public boolean hasNext () {
		return (nextIndex < list.count);
	}
  
  // next(), 
  /** Return next element in the List */
	public E next () {
		if (nextIndex >= list.count) throw new NoSuchElementException();
    canRemove = true; // for the remove method
    return list.get(nextIndex++); // ← increment and return
	}
  
  // remove() (an optional operation for Iterators) 
  /** Remove from the list the last element returned by the iterator.
	* Can only be called once per call to next. */
	public void remove(){
		if ( ! canRemove ) throw new IllegalStateException();
		canRemove = false; //← can only remove once
		nextIndex--; //← put counter back to last item
		list.remove(nextIndex); //← remove last item
	}
}
```







