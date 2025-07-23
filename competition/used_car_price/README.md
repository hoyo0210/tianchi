# 二手车价格预测项目

## 项目简介

本项目基于天池大赛【AI入门系列】车市先知：二手车价格预测学习赛，旨在通过机器学习技术预测二手车的市场价格。这是一个面向AI初学者的完整机器学习项目实践。

## 比赛背景

- **比赛平台**: [天池大赛](https://tianchi.aliyun.com/competition/entrance/231784/information)
- **比赛类型**: AI入门系列学习赛
- **目标**: 利用车辆特征预测二手车价格
- **适用人群**: AI初学者、机器学习爱好者

## 数据集说明

### 数据文件
- `used_car_train_20200313.csv` (52MB) - 训练数据集
- `used_car_testA_20200313.csv` (17MB) - 测试数据集A
- `used_car_testB_20200421.csv` (17MB) - 测试数据集B
- `used_car_sample_submit.csv` (439KB) - 提交格式示例

### 数据特征
数据集包含二手车的各种特征信息，具体字段如下：

| 字段名 | 描述 |
|--------|------|
| SaleID | 交易ID，唯一编码 |
| name | 汽车交易名称，已脱敏 |
| regDate | 汽车注册日期，例如20160101，2016年01月01日 |
| model | 车型编码，已脱敏 |
| brand | 汽车品牌，已脱敏 |
| bodyType | 车身类型：豪华轿车：0，微型车：1，厢型车：2，大巴车：3，敞篷车：4，双门汽车：5，商务车：6，搅拌车：7 |
| fuelType | 燃油类型：汽油：0，柴油：1，液化石油气：2，天然气：3，混合动力：4，其他：5，电动：6 |
| gearbox | 变速箱：手动：0，自动：1 |
| power | 发动机功率：范围 [ 0, 600 ] |
| kilometer | 汽车已行驶公里，单位万km |
| notRepairedDamage | 汽车有尚未修复的损坏：是：0，否：1 |
| regionCode | 地区编码，已脱敏 |
| seller | 销售方：个体：0，非个体：1 |
| offerType | 报价类型：提供：0，请求：1 |
| creatDate | 汽车上线时间，即开始售卖时间 |
| price | 二手车交易价格（预测目标） |
| v系列特征 | 匿名特征，包含v0-14在内15个匿名特征 |

**注意**：
- 部分字段已进行脱敏处理（name、model、brand、regionCode）
- 分类特征已编码为数值
- price 字段为预测目标变量
- v0-v14 为匿名特征，需要进一步分析其含义和重要性

## 项目结构

```
used_car_price/
├── README.md                           # 项目说明文档
├── SETUP.md                            # 项目设置说明
├── start_project.sh                    # 项目启动脚本
├── check_environment.py                # 环境检查脚本
├── requirements.txt                    # 项目依赖
├── LICENSE                             # 许可证文件
├── data/                               # 数据集目录
│   ├── used_car_train_20200313.csv
│   ├── used_car_testA_20200313.csv
│   ├── used_car_testB_20200421.csv
│   └── used_car_sample_submit.csv
├── src/                                # 源代码目录
│   ├── data_preprocessing.py           # 数据预处理
│   ├── feature_engineering.py          # 特征工程
│   ├── model_training.py               # 模型训练
│   └── prediction.py                   # 预测和提交
├── notebooks/                          # Jupyter笔记本
│   ├── data_exploration.ipynb          # 数据探索分析
│   └── model_development.ipynb         # 模型开发
├── models/                             # 训练好的模型
├── results/                            # 预测结果
└── venv/                               # 虚拟环境
```

## 技术栈

- **编程语言**: Python 3.7+
- **数据处理**: Pandas, NumPy
- **机器学习**: Scikit-learn, XGBoost, LightGBM
- **数据可视化**: Matplotlib, Seaborn
- **开发环境**: Jupyter Notebook

## 项目流程

### 1. 数据探索 (Data Exploration)
- 了解数据结构和特征
- 分析数据分布和相关性
- 识别缺失值和异常值

### 2. 数据预处理 (Data Preprocessing)
- 处理缺失值
- 处理异常值
- 数据类型转换
- 数据清洗

### 3. 特征工程 (Feature Engineering)
- 特征选择
- 特征变换
- 特征组合
- 编码分类变量

### 4. 模型开发 (Model Development)
- 数据分割（训练集/验证集）
- 模型选择和训练
- 超参数调优
- 模型评估

### 5. 预测和提交 (Prediction & Submission)
- 对测试数据进行预测
- 生成提交文件
- 结果验证

**重要提醒**：
- 提交前请确保预测结果的格式与 `used_car_sample_submit.csv` 中的格式一致
- 提交文件后缀名必须为 `.csv`
- 请仔细检查提交文件的列名和数据类型

## 安装和使用

### 环境要求
- Python 3.7+
- 8GB+ 内存（推荐）
- 足够的磁盘空间存储数据集

### 安装步骤

1. 克隆项目
```bash
git clone <repository-url>
cd tianchi/competition/used_car_price
```

2. 创建虚拟环境（推荐）
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 运行数据探索
```bash
jupyter notebook notebooks/data_exploration.ipynb
```

## 评估指标

比赛使用 **MAE (Mean Absolute Error，平均绝对误差)** 作为评估指标来衡量模型性能。

### MAE 计算公式
```
MAE = (1/n) * Σ|y_true - y_pred|
```

其中：
- `y_true` 为真实价格
- `y_pred` 为预测价格
- `n` 为样本数量

### MAE 特点
- **优点**：直观易懂，单位与目标变量相同（元）
- **特点**：对异常值相对不敏感
- **目标**：MAE 越小，模型性能越好

### 使用建议
- 在模型训练过程中，建议同时监控 MAE 和 RMSE 等指标
- 可以通过交叉验证来评估模型的稳定性
- 注意避免过拟合，确保模型在测试集上的泛化能力

## 注意事项

- 请确保数据集文件完整且未损坏
- 建议在开始建模前先进行充分的数据探索
- 注意保存中间结果和模型文件
- 定期备份重要的代码和结果

## 贡献指南

欢迎提交Issue和Pull Request来改进项目。

## 许可证

本项目遵循MIT许可证，详见LICENSE文件。

## 联系方式

如有问题，请通过以下方式联系：
- 提交GitHub Issue
- 发送邮件至：[your-email@example.com]

---

**注意**: 本项目仅用于学习和研究目的，请遵守相关数据使用协议和比赛规则。 