# python-web

---------------------

基于fastapi，学习验证向

[mysql8安装教程](./mysql8install.md)

 

1. 创建虚拟环境

```shell
 python -m venv venv  
```

第二个参数是创建虚拟环境的位置。通常，您可以在您的项目中创建它并将其命名为 venv

2. 激活虚拟环境

```shell
 # activate virtual environment
 source venv/bin/activate 
````

```shell
  # windows
 .\venv\Scripts\activate.bat 
```

如果你想切换项目或以其他方式离开你的虚拟环境，只需运行：

```shell
 deactivate # 或者 exit()
```

3. 安装fastapi

```shell
 pip install "fastapi[all]"
```

以上安装还包括了 uvicorn，你可以将其用作运行代码的服务器。
doc:https://fastapi.tiangolo.com/zh/tutorial/#fastapi

4. 启动服务器

```shell
 uvicorn main:app --reload
```

uvicorn main:app 命令含义如下:

* main：main.py 文件（一个 Python「模块」）。
* app：在 main.py 文件中通过 app = FastAPI() 创建的对象。
* --reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。
# mysql

```sql
-- 创建库
CREATE DATABASE lichonglou_db;

-- 删除库
DROP DATABASE lichonglou_db;

-- 查看库
SHOW DATABASES;

--- 使用库
use lichonglou_db;

--- 退出库
exit;
```

我是不会用命令行建库建表的，所以我用的是navicat
