#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
环境配置检查脚本
验证所有必需的包是否正确安装
"""

import sys
import os

def check_python_version():
    """检查Python版本"""
    print("🐍 Python版本检查")
    print(f"   Python版本: {sys.version}")
    
    if sys.version_info >= (3, 7):
        print("   ✅ Python版本符合要求 (>= 3.7)")
        return True
    else:
        print("   ❌ Python版本过低，需要 >= 3.7")
        return False

def check_packages():
    """检查所有必需的包"""
    print("\n📦 包安装检查")
    
    packages = {
        'pandas': '数据处理',
        'numpy': '数值计算',
        'scikit-learn': '机器学习',
        'xgboost': 'XGBoost算法',
        'lightgbm': 'LightGBM算法',  
        'catboost': 'CatBoost算法',
        'matplotlib': '数据可视化',
        'seaborn': '统计可视化',
        'plotly': '交互式可视化',
        'scipy': '科学计算',
        'statsmodels': '统计建模',
        'jupyter': 'Jupyter环境',
        'tqdm': '进度条'
    }
    
    success_count = 0
    total_count = len(packages)
    
    for package, description in packages.items():
        try:
            if package == 'scikit-learn':
                import sklearn
                version = sklearn.__version__
                print(f"   ✅ {package} ({description}): v{version}")
            else:
                exec(f"import {package}")
                try:
                    version = eval(f"{package}.__version__")
                    print(f"   ✅ {package} ({description}): v{version}")
                except AttributeError:
                    print(f"   ✅ {package} ({description}): 已安装 (版本信息不可用)")
            success_count += 1
        except ImportError:
            print(f"   ❌ {package} ({description}): 未安装")
        except Exception as e:
            print(f"   ⚠️  {package} ({description}): 检查出错 - {e}")
    
    print(f"\n   📊 安装成功率: {success_count}/{total_count} ({success_count/total_count*100:.1f}%)")
    return success_count == total_count

def check_data_files():
    """检查数据文件"""
    print("\n📁 数据文件检查")
    
    data_files = [
        'competition/used_car_price/data/used_car_train_20200313.csv',
        'competition/used_car_price/data/used_car_testA_20200313.csv', 
        'competition/used_car_price/data/used_car_testB_20200421.csv',
        'competition/used_car_price/data/used_car_sample_submit.csv'
    ]
    
    all_exist = True
    for file_path in data_files:
        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path) / (1024*1024)  # MB
            print(f"   ✅ {os.path.basename(file_path)}: {file_size:.1f} MB")
        else:
            print(f"   ❌ {os.path.basename(file_path)}: 文件不存在")
            all_exist = False
    
    return all_exist

def check_project_structure():
    """检查项目结构"""
    print("\n🏗️  项目结构检查")
    
    required_dirs = ['src', 'notebooks', 'models', 'results']
    required_files = ['README.md', 'requirements.txt']
    
    all_good = True
    
    for directory in required_dirs:
        if os.path.exists(directory):
            print(f"   ✅ {directory}/ 目录存在")
        else:
            print(f"   ❌ {directory}/ 目录不存在")
            all_good = False
    
    for file in required_files:
        if os.path.exists(file):
            print(f"   ✅ {file} 文件存在")
        else:
            print(f"   ❌ {file} 文件不存在")
            all_good = False
    
    return all_good

def test_data_loading():
    """测试数据加载"""
    print("\n🔬 数据加载测试")
    
    try:
        import pandas as pd
        
        # 测试加载训练数据
        train_file = 'competition/used_car_price/data/used_car_train_20200313.csv'
        if os.path.exists(train_file):
            df = pd.read_csv(train_file, sep=' ', nrows=5)  # 只读取前5行测试
            print(f"   ✅ 训练数据加载成功: {df.shape[1]} 列")
            print(f"   📊 数据预览: {list(df.columns[:5])}...")
        else:
            print("   ❌ 训练数据文件不存在")
            return False
            
        return True
    except Exception as e:
        print(f"   ❌ 数据加载失败: {e}")
        return False

def main():
    """主函数"""
    print("🚀 二手车价格预测项目 - 环境配置检查")
    print("=" * 60)
    
    # 检查各个组件
    checks = [
        ("Python版本", check_python_version),
        ("依赖包", check_packages),
        ("数据文件", check_data_files),
        ("项目结构", check_project_structure),
        ("数据加载", test_data_loading)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"   ❌ {name}检查出错: {e}")
            results.append((name, False))
    
    # 总结
    print("\n" + "=" * 60)
    print("📋 环境检查总结")
    print("=" * 60)
    
    success_count = 0
    for name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"   {name}: {status}")
        if result:
            success_count += 1
    
    print(f"\n🎯 总体状态: {success_count}/{len(results)} 项检查通过")
    
    if success_count == len(results):
        print("\n🎉 恭喜！您的环境配置完全正确，可以开始项目开发了！")
        print("\n📚 下一步建议:")
        print("   1. 运行 'jupyter lab' 启动开发环境")
        print("   2. 打开 notebooks/data_exploration.ipynb 开始数据探索")
        print("   3. 或者运行 'cd src && python3 data_exploration.py' 快速查看数据")
    else:
        print(f"\n⚠️  还有 {len(results) - success_count} 项需要解决")
        print("   请根据上述检查结果修复相关问题")
    
    return success_count == len(results)

if __name__ == "__main__":
    main() 