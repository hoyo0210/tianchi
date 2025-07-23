#!/bin/bash

# 二手车价格预测项目启动脚本

echo "🚀 启动二手车价格预测项目开发环境"
echo "=================================="

# 检查虚拟环境是否存在
if [ ! -d "venv" ]; then
    echo "❌ 虚拟环境不存在，请先运行环境配置"
    echo "   运行命令: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# 激活虚拟环境
echo "📦 激活虚拟环境..."
source venv/bin/activate

# 检查环境配置
echo "🔍 检查环境配置..."
python3 check_environment.py

# 询问用户想要启动什么
echo ""
echo "请选择要启动的开发环境:"
echo "1. Jupyter Lab (推荐用于数据探索和可视化)"
echo "2. Jupyter Notebook (传统笔记本环境)"
echo "3. 运行数据探索脚本"
echo "4. 退出"

read -p "请输入选择 (1-4): " choice

case $choice in
    1)
        echo "🚀 启动 Jupyter Lab..."
        jupyter lab
        ;;
    2)
        echo "🚀 启动 Jupyter Notebook..."
        jupyter notebook
        ;;
    3)
        echo "🔬 运行数据探索脚本..."
        cd src && python3 data_exploration.py
        ;;
    4)
        echo "👋 再见！"
        exit 0
        ;;
    *)
        echo "❌ 无效选择，请输入 1-4"
        exit 1
        ;;
esac 