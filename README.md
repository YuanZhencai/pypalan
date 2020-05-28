# pypalan

1. 安装

    ```
    pip install --no-cache git+https://github.com/YuanZhencai/pypalan.git
    ```

2. 使用

    ```python
    import pypalan
    pypalan.read_sql('select * from cp.`employee.json`')
    pypalan.read_table('cp.`employee.json`')
    ```
