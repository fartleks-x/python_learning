## 一、选择语句
### if 语句
```python
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
```
示例：  
```python
h = float(input("身高："))
w = float(input("体重："))
bmi = w/(h/100)**2
print(bmi)
if bmi < 18.5:
    print("你的体重过轻")
elif bmi < 24:
    print("你的体重正常")
elif bmi < 27:
    print("你的体重过重")
else:
    print("你的体重严重肥胖")
```
### match-case语句
```python
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2>:
        <action_2>
    case <pattern_3>:
        <action_3>
    case _:
        <action_wildcard>
```
示例：  
```python
status = 400
match status:
    case 400:
        print("Bad request")
    case 404:
        print("Not found")
    case 418:
        print("I'm a teapot")
    case _:
        print("Something's wrong with the internet")
```


## 二、循环语句

### while循环
```python
while 判断条件(condition)：
    执行语句(statements)
```  
示例：  
```python
a = 1
while a<10:
    print(a)
    a +=2
```

### while-else语句
```python
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
```

示例：  
```python
a = 1
while a<10:
    print(a)
    a +=2
else:
    print(a)
```

### for语句
```python
for <variable> in <sequence>:
    <statements>
else:
    <statements>
```

示例：  
```python
for i in range(10):
    print('*'*i)
```

### for-else语句
```python
for item in iterable:
    # 循环主体
else:
    # 循环结束后执行的代码
```

### range()函数
示例：
```python
for i in range(10):
    print('*'*i)
```

### break、continue、pass

