## Questions：

1. ```java
   double n = 0;
   double m = 0;
   double result = n / m;
   ```

   - **静态检查（编译时检查）**：

     - 在编译阶段，Java 编译器会检查代码的语法和类型是否正确。
     - 在这段代码中，变量 `n` 和 `m` 都被正确地声明为 `double` 类型，并且除法操作 `n / m` 在语法上是合法的。
     - **编译器不会报错**，因为静态检查无法在编译时确定 `m` 的值是否为零。

   - **动态检查（运行时检查）**：

     - 在运行时，当代码执行到 `n / m` 时，`m` 的值是 `0`。

     - 在 Java 中，

       **浮点数除以零不会抛出异常**，而是会返回一个特殊的值：

       - 如果被除数是 `0.0`，结果是 `NaN`（Not a Number）。
       - 如果被除数不是 `0.0`，结果是 `Infinity` 或 `-Infinity`（取决于被除数的符号）。

     - 因此，这段代码在运行时不会抛出异常，但结果是一个无效的数学值（`NaN`）。

   **结论**

   - **没有静态错误**：代码可以通过编译。
   - **没有动态异常**：运行时不会抛出异常，但结果是无效的数学值。
   - **问题类型**：这是一个**动态检查**，会报 Error ： “/ by zero”

2. ```java
   double n = 7;
   double m = 0;
   double result = n / m;
   ```

   - **静态检查（编译时检查）**：
     - 同样地，编译器不会报错，因为 `n` 和 `m` 的声明和除法操作在语法上是合法的。
     - 静态检查无法在编译时确定 `m` 的值是否为零。
   - **动态检查（运行时检查）**：
     - 在运行时，`m` 的值是 `0`，因此执行 `n / m` 会导致浮点数除以零。
     - 如前所述，浮点数除以零不会抛出异常，而是返回 `Infinity` 或 `-Infinity`（取决于被除数的符号）。
     - 因此，这段代码在运行时也不会抛出异常，但结果是一个无效的数学值（`Infinity`）。

   **结论**

   - **没有静态错误**：代码可以通过编译。
   - **没有动态异常**：运行时不会抛出异常，但结果是无效的数学值。
   - **问题类型**：这是一个**逻辑错误**，因为除以零在数学上是未定义的，但 Java 的浮点数运算允许这种情况发生。

3. ```java
   double prob = 1/5;
   ```

   **问题类型**：这是一个**逻辑错误**，因为浮点数计算中包含了整数，Integer Division

4. “Object pointed by final variable cannot be mutated” 这句话是错误，实际上你是可以修改的，但是他会报错

5. When you try to assign a final variable, Java compiler will produce a compiler error. Therefore, final provides "Static check" for "immutable" references.

   ```java
   List<Integer> list1 = new ArrayList<>();
   list1.add(1);
   list1.add(2);
   
   final List<Integer> list2 = list1;
   list1.add(3);
   // 这么做就会报错，因为静态检查
   ```

6. 