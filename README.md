# XJTLU-ICS
ICS courses notes
## 课程代码对照表
CPT102 --- Data Structure <br>
CPT104 --- Operating System <br>
INT102 --- Algorithm <br>
INT104 --- Artificial Intelligence
## Git提交方式
### SSH
从右上角的code处复制ssh链接，然后运行如下代码
```git 
  git remote add origin git@github.com:xxxxxxxxx
```

本地的git默认使用的分支名字叫master，但是GitHub的默认主分支名字叫main。可以在本地的git的终端中使用修改master的名字为main
```git 
  git branch -M master main
```

然后将文件放入本地的文件夹中，add，commit之后，使用
```git
  git push origin 远程仓库分支名
```
如果想要再提交的同时创建一个新的远程仓库
```git
  git push -u origin 新创建的远程仓库名
```

每次在提交新内容之前，先从远程仓库拉取一下最新的内容
```git
  git pull origin 拉取的远程仓库分支，不写默认是main
```
如果此时在子分支，请先将子分支的更新内容提交到远程仓库对应的子分支
```git
  git push origin 子分支
```
然后再在本地切换到主分支，先使用pull更新内容，再merge本地的子分支的更新之后的内容，如果没有出现冲突就直接提交
```git
  git checkout main
  git pull origin main
  git merge 本地子分支
  git push origin main
```

