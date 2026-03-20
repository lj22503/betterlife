#!/usr/bin/env python3
"""
Money Magic计算器
"""

import json
from datetime import datetime

def calculate(income, expenses, assets, liabilities):
    """计算财务指标"""
    net_worth = assets - liabilities
    savings_rate = (income - expenses) / income * 100 if income > 0 else 0
    return {"net_worth": net_worth, "savings_rate": savings_rate, "status": "success"}

def main():
    print("💰 财务计算器")
    print("=" * 40)
    
    income = float(input("月收入：") or 0)
    expenses = float(input("月支出：") or 0)
    assets = float(input("总资产：") or 0)
    liabilities = float(input("总负债：") or 0)
    
    result = calculate(income, expenses, assets, liabilities)
    print(f"\n净资产：¥{result['net_worth']:,.0f}")
    print(f"储蓄率：{result['savings_rate']:.1f}%")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"{skill_name}_{timestamp}.json", 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
    print("\n✅ 已保存")

if __name__ == '__main__':
    main()
