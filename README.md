## server-template

Python 项目模板工程。

### 一、运行环境

- Python 3.8

### 二、如何启动

- 命令行方式

  ```bash
  $ python run.py
  ```

  默认运行在 `127.0.0.1` 的 `5000` 端口，如果使用其他 host 或者端口，可临时修改 `run.py` 中 `app.run()` 中的参数即可：

  ```python
  if __name__ == '__main__':
      app.run(host='127.0.0.1', port=5000)
  
  ```

- PyCharm 方式

  配置 `Run/Debug Configurations` 即可，详情可参考 [Run/Debug Configuration: Flask Server](!https://www.jetbrains.com/help/pycharm/run-debug-configuration-flask-server.html)。

### 三、migration 的生成和执行

1. 进入命令行，输入：

    ```bash
    $ flask db migrate
    ```
    此命令依赖于 [Alembic](https://alembic.sqlalchemy.org/en/latest/)，会比较当前 model 和数据库中的表之间的差异，如果存在差异，会生成新版本的 migration 脚本，存放于 `migrations/versions` 目录下；如果不存在差异，则不会生成新 version 的脚本；
    
2. 执行 migration 脚本，使变更同步到数据库，输入以下命令即可：

    ```bash
    $ flask db upgrade
    ```

    **注意：** 如果执行上述命令失败，报如下错误：

    ```bash
    Usage: flask db migrate [OPTIONS]
    
    Error: Failed to find Flask application or factory in module "app". Use "FLASK_APP=app:name to specify one.
    
    ```

    **在项目根目录** 先执行：

    ```bash
    $ export PYTHONPATH=`pwd`
    $ export FLASK_APP=run.py
    ```

    命令，再执行 `flask db upgrade` 即可。

### 四、目录结构

详见[Python工程规范](https://wiki.emhub.top/pages/viewpage.action?pageId=1802364)。

