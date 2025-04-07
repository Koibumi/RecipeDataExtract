# tModLoader配方处理脚本

## 概述
本项目的上游为RecipeReader mod，下游为
本项目用于更新和处理配方数据。程序会加载旧的配方数据（`old_recipes.xlsx`）和新的配方数据（`new_recipes.json`），合并后生成压平的行数据及倒排索引，并将结果写入 CSV 文件。

## 文件说明
- **Main.py**  
  主入口程序，负责数据加载、合并和输出。参见 [Main.py](d:/CalWiki/Recipe/Main.py)。
- **ParseFromExcel.py**  
  提供 [`load_recipes_from_xlsx`](d:/CalWiki/Recipe/ParseFromExcel.py) 函数，用于从 Excel 文件中加载旧数据。
- **ParseFromJson.py**  
  提供 [`load_recipes_from_json`](d:/CalWiki/Recipe/ParseFromJson.py) 函数，用于从 JSON 文件中加载新数据。
- **WriteOutput.py**  
  提供 [`write_xlsx_files`](d:/CalWiki/Recipe/WriteOutput.py) 函数，用于将处理结果写出为 CSV 文件。
- **DataStructures.py**  
  定义项目中所使用的数据结构和模型。

## 使用方法
1. 将数据文件 `old_recipes.xlsx` 和 `new_recipes.json` 放置于工程根目录下。如果 `old_recipes.xlsx` 不存在，程序会使用空集合作为旧数据进行处理。
2. 打开终端，在项目目录下运行以下命令：
    ```sh
    python Main.py
    ```
3. 程序执行完毕后，会生成三个 CSV 文件，并在终端打印“数据处理完成，文件已保存。”

## 依赖
- Python 3.x
- 可能需要安装第三方库（例如处理 Excel 的库），请参考 `ParseFromExcel.py` 中的依赖说明。

## 错误处理
- 加载 `old_recipes.xlsx` 时，如文件不存在或读取失败，程序会输出错误提示并默认使用空集合。
- 其他异常情况均已在代码中捕获，确保程序不会异常终止。

## 注意事项
- 请确保数据文件格式与解析函数的预期一致，以免数据解析错误。
- 函数的详细实现请参见各自文件：[ParseFromExcel.py](d:/CalWiki/Recipe/ParseFromExcel.py)、[ParseFromJson.py](d:/CalWiki/Recipe/ParseFromJson.py) 和 [WriteOutput.py](d:/CalWiki/Recipe/WriteOutput.py)。

## 联系方式
如有疑问或建议，请联系项目维护者。