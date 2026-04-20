# 基金 e 账户 Excel 解析脚本

## 功能说明

解析从基金 e 账户（中证登）导出的 Excel 持仓文件，提取基金持仓信息。

## 前置条件

```bash
pip install pandas openpyxl xlrd
```

## 脚本代码

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
基金 e 账户 Excel 解析脚本
解析从 www.chinaclear.cn 导出的基金持仓 Excel 文件
"""

import pandas as pd
import sys
from pathlib import Path

def parse_fund_excel(file_path: str) -> pd.DataFrame:
    """
    解析基金 e 账户 Excel 文件
    
    Args:
        file_path: Excel 文件路径
    
    Returns:
        DataFrame 包含持仓信息
    """
    # 读取 Excel
    try:
        # 尝试读取第一个 sheet
        df = pd.read_excel(file_path, sheet_name=0)
    except Exception as e:
        print(f"读取 Excel 失败：{e}")
        return None
    
    # 打印列名，帮助调试
    print(f"Excel 列名：{df.columns.tolist()}")
    print(f"数据行数：{len(df)}")
    
    # 标准化列名（根据实际 Excel 格式调整）
    # 基金 e 账户常见列名：
    # 基金代码 | 基金名称 | 持有份额 | 当前净值 | 持有市值 | 持有收益 | 仓位占比
    
    column_mapping = {
        '基金代码': 'fund_code',
        '基金名称': 'fund_name',
        '持有份额': 'shares',
        '当前净值': 'nav',
        '持有市值': 'market_value',
        '持有收益': 'profit',
        '仓位占比': 'ratio',
        # 可能的别名
        '代码': 'fund_code',
        '名称': 'fund_name',
        '份额': 'shares',
        '净值': 'nav',
        '市值': 'market_value',
        '收益': 'profit',
        '占比': 'ratio',
    }
    
    # 重命名列
    df.rename(columns=column_mapping, inplace=True)
    
    # 检查必需列
    required_columns = ['fund_code', 'fund_name']
    for col in required_columns:
        if col not in df.columns:
            print(f"警告：缺少必需列 {col}")
    
    # 数据类型转换
    numeric_columns = ['shares', 'nav', 'market_value', 'profit', 'ratio']
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    return df


def generate_report(df: pd.DataFrame, output_path: str = None):
    """
    生成持仓报告
    
    Args:
        df: 持仓数据 DataFrame
        output_path: 输出文件路径（可选）
    """
    if df is None or len(df) == 0:
        print("没有数据")
        return
    
    # 计算汇总信息
    total_market_value = df['market_value'].sum() if 'market_value' in df.columns else 0
    total_profit = df['profit'].sum() if 'profit' in df.columns else 0
    profit_rate = (total_profit / total_market_value * 100) if total_market_value > 0 else 0
    
    # 打印报告
    print("\n" + "="*50)
    print("基金持仓报告")
    print("="*50)
    print(f"持有基金数：{len(df)}")
    print(f"总市值：{total_market_value:,.2f} 元")
    print(f"总收益：{total_profit:,.2f} 元")
    print(f"收益率：{profit_rate:.2f}%")
    print("="*50)
    
    # 打印持仓明细
    print("\n持仓明细：")
    print(df.to_string(index=False))
    
    # 保存报告
    if output_path:
        df.to_csv(output_path, index=False, encoding='utf-8-sig')
        print(f"\n报告已保存到：{output_path}")


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("用法：python parse_fund_excel.py <Excel 文件路径> [输出文件路径]")
        print("示例：python parse_fund_excel.py 持仓明细.xlsx 持仓报告.csv")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    # 检查文件是否存在
    if not Path(input_file).exists():
        print(f"文件不存在：{input_file}")
        sys.exit(1)
    
    # 解析 Excel
    print(f"正在解析：{input_file}")
    df = parse_fund_excel(input_file)
    
    if df is not None:
        # 生成报告
        generate_report(df, output_file)


if __name__ == '__main__':
    main()
```

## 使用方法

### 命令行使用

```bash
# 解析 Excel 并打印报告
python parse_fund_excel.py 持仓明细.xlsx

# 解析 Excel 并保存 CSV
python parse_fund_excel.py 持仓明细.xlsx 持仓报告.csv
```

### Python 代码调用

```python
from parse_fund_excel import parse_fund_excel, generate_report

# 解析 Excel
df = parse_fund_excel('持仓明细.xlsx')

# 生成报告
generate_report(df, '持仓报告.csv')
```

## 测试数据

创建一个测试 Excel 文件：

```python
# 生成测试数据
import pandas as pd

test_data = {
    '基金代码': ['000001', '000002', '110011'],
    '基金名称': ['华夏成长混合', '嘉实增长混合', '易方达中小盘混合'],
    '持有份额': [10000, 5000, 8000],
    '当前净值': [1.5, 2.0, 3.5],
    '持有市值': [15000, 10000, 28000],
    '持有收益': [1500, -500, 3000],
    '仓位占比': [28.3, 18.9, 52.8]
}

df_test = pd.DataFrame(test_data)
df_test.to_excel('测试持仓.xlsx', index=False)
print("测试数据已生成：测试持仓.xlsx")
```

## 输出示例

```
==================================================
基金持仓报告
==================================================
持有基金数：3
总市值：53,000.00 元
总收益：4,000.00 元
收益率：7.55%
==================================================

持仓明细：
 基金代码        基金名称  持有份额  当前净值  持有市值  持有收益  仓位占比
 000001    华夏成长混合   10000    1.5   15000    1500   28.3
 000002    嘉实增长混合    5000    2.0   10000    -500   18.9
 110011  易方达中小盘混合    8000    3.5   28000    3000   52.8
```

## 注意事项

1. **Excel 格式**：不同时期导出的 Excel 格式可能不同，需要调整 `column_mapping`
2. **编码问题**：保存 CSV 时使用 `utf-8-sig` 编码，避免中文乱码
3. **数据验证**：建议添加数据验证逻辑（如净值>0，份额>0 等）
4. **异常处理**：生产环境需要更完善的异常处理

## 后续优化

- [ ] 支持多种 Excel 格式（不同时期/不同平台）
- [ ] 添加数据验证（异常值检测）
- [ ] 支持批量解析（多个文件）
- [ ] 生成 JSON 格式输出（供前端使用）
- [ ] 添加日志记录
