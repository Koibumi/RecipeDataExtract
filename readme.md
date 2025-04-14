# tModLoader配方处理脚本

## HINT
- `配方测试`和`配方测试/配方组`下有能跑通的雏形，当前进度：成功从数据库读取文件
- Mongo DB的查询不stable，因此不能考虑本地排序，需要查询后排序
  - 因为列表类型不支持group by或排序，考虑手工将工作站列表压平后排序

## TODO
- 重构代码
  - 配方组返回Data行
  - 配方在查询时，如果为byIngredient，首先byItem查询配方组，扩展为物品名，配方组名的列表，利用实现好的or机制查询，其他类型照常查询，返回Data行
- 什么，还有更上层的调用，摸了

## 概述
- 本项目从tModLoader中动态（运行时）提取配方和配方组数据，本地处理数据，并生成为xlsx表格（灰机wiki的MongoDB所使用的数据库所支持的类型）
- 本项目**没有**包括从数据库中提取数据并生成html样式所需的模块和模板
  - 这部分内容会直接写在wiki上
  - 当前进展：数据提取跑通，需要重构代码；需要整合
- 本项目**没有**包括批量修改合成表模板的相关脚本，但如果你对此感兴趣，可以看看[这个C#项目](https://github.com/riiiiiiin/MWEditor)，其中包含笔者的一些早期工作（不保证work）

## 文件结构
- `RecipeReader.tmod` 用于动态提取配方和配方组数据
  - 这个mod支持从配置选项指定的目标mod读取数据，默认为`CalamityMod`
- `Source/` 处理数据，生成表格的源码所在处
- `Data/` 待处理的新旧数据
- `Output/` 生成的xlsx数据

## 输出结构概述：下游编写者必读
- 输出结构将会被压平，列表会被灰机的数据库处理好
- `recipes.xlsx` 为压平的配方数据，包含4个列：
  - `workstations` 为工作站列表
  - `conditions` 为条件列表
  - `result` 为生成物，结构为物品名`:`数量（英文冒号）
  - `ingredients` 为材料列表，项结构为物品名`:`数量
- `groups.xlsx` 为压平的配方组数据，包含2个列：
  - `name` 为配方组名称
  - `items` 为配方组包含的物品列表
- 注：所谓列表指的是使用英文分号`;`分割的一串数据，会被灰机在入库时整理为列表
- 输出的文件可以直接放进数据库中

## 使用方法
1. 从灰机下载旧版本的数据，重命名为`old_recipes.xlsx`，放置在`Data/`文件夹下
   - 如果文件夹还不存在，请自己创建
   - 如果还没有数据，这一步可以省略
2. 将`RecipeReader.tmod`放在`tModLoader/Mod`文件夹下并加载，将`tModLoader`下的`Recipes.json`重命名为`new_recipes.json`，`Groups.json`重命名为`groups.json`，放置在`Data/`文件夹下
   - 读取数据的时机为加载，请在加载完成后查找输出文件
   - 如果修改了配置或者需要重新生成，请重新加载
3. 打开终端，在项目目录下运行以下命令：
    ```sh
    cd Source
    python Main.py
    ```
    - 当然，我假定你在使用Windows，如果你在使用Linux或MaxOS，你最好自己会
4. 程序执行完毕后，会在`Output/`下生成 xlsx 文件，终端也会提示“数据处理完成，文件已保存。”

## 依赖
- Python 3.x
- `openpyxl`
    ```sh
    pip install openpyxl
    ```
