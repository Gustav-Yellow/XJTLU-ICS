# Space-for-time Tradeoff 空间换时间，时间换空间

空间换时间的例子：

1. 输入强化（Input-enhancement）
   预处理输入存储一些信息，以待后续使用 (其中就包含非排序算法的Counting sort，和时间更快的字符排序方法Horspool Algorithm)
2. 预构造（Pre-structuring）
   使用一个数据结构处理输入，以便更简单地处理问题

## Coutning Algorithm 计数排序 O(n+k)

### 相比与其他通过比较大小来实现的排序

到目前为止，我们看到的所有排序算法是比较排序：仅通过比较确定元素的相对顺序(例如：Selection sort, Bubble Sort, Insertation Sort, Merge Sort ...)

其中这些通过排序的算法的最快时间复杂度也只能做到O(nlog(n))，通常是在此复杂度和O(n<sup>2</sup>)之间徘徊

而计数排序依靠已排序的桶进行计数排序，不需要进行值比较。其算法时间复杂度**O(n+k)** ，其中k为原始数列中数的范围，也就是桶的数量。

### 具体实现方式

假设现在有一个原始数组列表[1, 3, 5, 2, 3]，使用counting sort来进行排序

1. 根据数列的范围中的元素的数值， 找到每个数值都出现了多少次， 然后根据原始数组中最大的数字作为列表长度，创造一个映射数组。
2. 将每个映射数组的索引假想成代表的是原始数组中的出现的数字，然后根据每个数字在原始数组中出现的次数，映射数组中以该数字作为索引记录出现的次数
3. 从映射数组的第二个元素开始，循环添加，将上一个元素与当前元素的和作为当前元素的新累加值
4. 然后从后向前索引原始数组，将读取到的数字作为索引来映射数组中查找累加值后对应的值，然后将查到的累加值减一之后作为结果列表中的索引，并在该索引位置上放入循环中当前原始数组中的值。

### 代码

```java
public class CountingSort {

    public static void main(String[] args) {

        // 用来记录原本的数组
        int[] base_array = new int[]{1, 2, 5, 3, 2};
        // 用来记录原数组中每个数字出现了多少次
        int[] reflect_array;
        // 结果数组
        int[] result_array = new int[base_array.length];

        // 找到base_array里面最大的数字
        int max = Arrays.stream(base_array).max().getAsInt();

        // 让映射列表的长度等于base_array中最大的数字的长度+1
        reflect_array = new int[max+1];
        // 让映射列表全都为0
        Arrays.fill(reflect_array, 0);

        // 同级初始数组中每个数字出现的次数，并放入映射数组中
        for (int k : base_array) {
            reflect_array[k]++;
        }
        
        // 此时的映射数组[0, 1, 2, 1, 0, 1]

        // 对映射数组进行累加，计算出每个数字前面有多少个空格
        for (int j = 1; j < reflect_array.length; j++) {
            reflect_array[j] = reflect_array[j - 1] + reflect_array[j];
        }

        // 此时的映射数组[0, 1, 3, 4, 4, 5]

        // 结果也是从右向左填入，结果数组[映射数组[原始数组[k]] - 1] = 原始数组[k]
        // 记得将映射数组[原始数组[k]]的值在每次循环之后减1
        for (int k = base_array.length-1; k >= 0; k--) {
            result_array[reflect_array[base_array[k]] - 1] = base_array[k];
            reflect_array[base_array[k]] = reflect_array[base_array[k]] - 1;
        }
        
        // 此时的映射数组[0, 0, 1, 3, 4, 4]
        // 此时的结果[1, 2, 2, 3, 5]
    }
    
}
```

## Horspool’s Algorithm

确认连续字符串子块的位置

### 具体实现方式

算法需要连续子串的shift table来确认按位匹配出错时，子串需要往右移动多少位，基本思想是“需要将子串往右移多少，才能使当前子串末尾对应的字符串元素再次与子串中最靠右的同名元素匹配”。

创建shift table，初始化shift table中元素为字符串中元素范围的所有元素

遍历shift table：

1. 如果遍历的元素不在子串前n-1个中，将shift table中该元素的偏移值记为子串长度
2. 如果遍历的元素在子串前n-1个中，将shift table中该元素的偏移值记为子串前n-1个中最右方的相同元素到子串结尾的距离。

使用shift table找子串位置：

1. 将从后向前对比子串与对应字符串的元素，如果某个位置上的元素不相等就将子串往后挪动。
2. 具体挪多少得看子串最后一位对应的字符串元素，按照该元素在shift table中的偏移值挪动子串。
3. 重复以上操作直到所有子串元素都能对应字符串

例题：给一子串求shift table，BAOBAB, 去掉最后一位→BAOBA_，下面以这个去掉最后一位的残缺串讨论
范围为26个字母，所以table长为26
残缺串的往左数1位到A，A对应1
残缺串的往左数两位到B，B对应2
残缺串的左边没有C，C对应子串长度6*

![在这里插入图片描述](https://img-blog.csdnimg.cn/2021060114580011.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3Nhbm11c2VuX3d1,size_16,color_FFFFFF,t_70)

### 代码

```java
// 查找字符串子串出现的位置
public class Horspool {

    // 根据ASCII码生成一个Shift Table
    public static int[] shiftTable(char[] pattern) {
        int[] table = new int[256]; // For ASCII characters
        // ASCII码一共256长度的数字列表，先默认让所有数字都等于pattern的长度
        for (int i = 0; i < 256; i++) {
            table[i] = pattern.length;
        }
        // 记录pattern中每个字母对应到最右边的字符的移动距离
        for (int i = 0; i < pattern.length - 1; i++) {
            table[pattern[i]] = pattern.length - 1 - i;
        }
        return table;
    }

    // Horspool's algorithm for string matching
    public static int horspoolSearch(char[] text, char[] pattern) {
        // 简单的判断，如果pattern为空，或者text的长度远少于pattern则证明有错误
        if (pattern.length == 0 || text.length < pattern.length) {
            return -1; // Pattern is empty or longer than text
        }

        // 生成Shift Table
        int[] table = shiftTable(pattern);
        // 声明每次移动的偏移值的变量
        int skip;

        // 循环text，每次增加skip的长度的偏移值
        for (int i = 0; i <= text.length - pattern.length; i += skip) {
            skip = 0;
            // 从pattern的最右侧开始判定，然后看从右向左第几个字母匹配不上text，然后对照shift table对应偏移值向右移动
            for (int j = pattern.length - 1; j >= 0; j--) {
                if (pattern[j] != text[i + j]) {
                    skip = Math.max(1, table[text[i + j]]);
                    break;
                }
            }
            // 如果pattern一轮for循环结束，那么证明符合，就可以返回当前i的循环的值
            if (skip == 0) {
                return i; // Match found
            }
        }
        return -1; // No match found
    }

    public static void main(String[] args) {
        String text = "This is a simple example of Horspool's algorithm.";
        String pattern = "example";

        int position = horspoolSearch(text.toCharArray(), pattern.toCharArray());

        if (position != -1) {
            System.out.println("Pattern found at position: " + position);
        } else {
            System.out.println("Pattern not found.");
        }
    }

}
```

