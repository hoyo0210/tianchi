# 环境配置指南

## 快速开始

### 1. 一键安装（推荐）

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate  # macOS/Linux
# 或者
venv\Scripts\activate     # Windows

# 安装依赖
pip install --upgrade pip
pip install -r requirements.txt

# 验证安装
python3 check_environment.py
```

### 2. 启动开发环境

```bash
# 使用启动脚本（推荐）
./start_project.sh

# 或者手动启动
source venv/bin/activate
jupyter lab
```

## 环境要求

- **Python**: 3.7 或更高版本
- **内存**: 建议 8GB 或以上
- **磁盘空间**: 至少 2GB 可用空间

## 已安装的包

### 数据处理
- pandas (2.3.1) - 数据处理和分析
- numpy (2.0.2) - 数值计算

### 机器学习
- scikit-learn (1.6.1) - 机器学习算法
- xgboost (2.1.4) - XGBoost 梯度提升
- lightgbm (4.6.0) - LightGBM 梯度提升
- catboost (1.2.8) - CatBoost 梯度提升

### 数据可视化
- matplotlib (3.9.4) - 基础绘图
- seaborn (0.13.2) - 统计可视化
- plotly (6.2.0) - 交互式图表

### 开发环境
- jupyter - Jupyter 笔记本环境
- ipykernel - Python 内核
- tqdm - 进度条显示

### 科学计算
- scipy (1.13.1) - 科学计算
- statsmodels (0.14.5) - 统计建模

## 故障排除

### 1. Python 版本问题
```bash
# 检查 Python 版本
python3 --version

# 如果版本过低，需要升级 Python
```

### 2. 包安装失败
```bash
# 升级 pip
pip install --upgrade pip

# 清理缓存重新安装
pip cache purge
pip install -r requirements.txt
```

### 3. 虚拟环境问题
```bash
# 删除旧的虚拟环境
rm -rf venv

# 重新创建
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. 数据文件问题
确保以下文件存在于 `competition/used_car_price/data/` 目录：
- `used_car_train_20200313.csv`
- `used_car_testA_20200313.csv`
- `used_car_testB_20200421.csv`
- `used_car_sample_submit.csv`

## 验证安装

运行环境检查脚本：
```bash
python3 check_environment.py
```

如果所有检查都通过，您就可以开始项目开发了！

## 下一步

1. **数据探索**: 运行 `notebooks/data_exploration.ipynb`
2. **快速分析**: 运行 `cd src && python3 data_exploration.py`
3. **开始建模**: 参考 README.md 中的项目流程

## 联系支持

如果遇到问题，请：
1. 检查错误信息
2. 查看本文档的故障排除部分
3. 确保满足环境要求 