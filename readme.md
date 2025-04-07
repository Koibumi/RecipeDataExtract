# tModLoader配方处理脚本

## 概述
- 本项目从tModLoader中动态（运行时）提取配方数据，本地处理配方数据，并生成为xlsx表格（灰机wiki的MongoDB所使用的数据库所支持的类型）
- 本项目**没有**包括从数据库中提取数据并生成html样式所需的模块和模板，也无意写这部分内容（俗称摸了）
- 本项目**没有**包括批量修改合成表模板的相关脚本，但如果你对此感兴趣，可以看看[这个C#项目](https://github.com/riiiiiiin/MWEditor)，其中包含笔者的一些早期工作（不保证work）

## 文件结构
- `RecipeReader.tmod` 用于动态提取配方数据
  - 这个mod支持从配置选项指定的目标mod读取数据，默认为`CalamityMod`
- `Source/` 处理数据，生成表格
- `Data/` 待处理的新旧数据
- `Output` 生成的xlsx数据

## 输出结构概述：下游编写者必读
- 输出结构的主要思想是压平+倒排索引
- `recipes.xlsx` 为压平的配方数据，包含4个列：
  - `workstations` 为工作站列表，使用英文分号`;`分割
  - `conditions` 为条件列表，使用英文分号`;`分割
  - `result` 为生成物，结构为物品名`:`数量（英文冒号）
  - `ingredients` 为成分（中文苦手）列表，每个项结构为物品名`:`数量（英文冒号），项之间使用英文分号`;`分割
- `recipes_ws_index.xlsx` 为工作站倒排索引，包含两个列
  - `workstation` 为工作站名称
  - `row_indices` 为需求该工作站的所有配方的索引的列表，使用英文分号`;`分割
    - Hint:在灰机的MongoDB数据库中，每一行都可以通过`filename.xlsx#i`的方式提取出来
- `recipes_ingredient_index.xlsx` 为成分倒排索引，包含两个列
  - `ingredient` 为工作站名称
  - `row_indices` 为需求该成分的所有配方的索引的列表，使用英文分号`;`分割

## 使用方法
1. 从灰机下载旧版本的数据，重命名为`old_recipes.xlsx`，放置在`Data/`文件夹下
   - 如果文件夹还不存在，请自己创建
   - 如果还没有数据，这一步可以省略
2. 将`RecipeReader.tmod`放在`tModLoader/Mod`文件夹下并加载，将`tModLoader`下的`RecipeReaderOutput.json`重命名为`new_recipes.json`，放置在`Data/`文件夹下
   - 读取数据的时机为加载，请在加载完成后查找输出文件
   - 如果修改了配置或者需要重新生成，请重新加载
3. 打开终端，在项目目录下运行以下命令：
    ```sh
    cd Source
    python Main.py
    ```
    - 当然，我假定你在使用Windows，如果你在使用Linux或MaxOS，你最好自己会
4. 程序执行完毕后，会在`Output/`下生成三个 CSV 文件，终端也会提示“数据处理完成，文件已保存。”

## 依赖
- Python 3.x
- `openpyxl`
    ```sh
    pip install openpyxl
    ```
