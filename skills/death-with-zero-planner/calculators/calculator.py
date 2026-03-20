#!/usr/bin/env python3
"""
Death With Zero Planner计算器
"""

import json
from datetime import datetime

def calculate_fire_number(annual_expenses):
    """计算 FIRE 数字"""
    return annual_expenses * 25

def main():
    print("🔥 FIRE 计算器")
    print("=" * 40)
    
    expenses = float(input("年支出：") or 0)
    current = float(input("当前资产：") or 0)
    
    fire_number = calculate_fire_number(expenses)
    progress = current / fire_number * 100
    
    print(f"\nFIRE 数字：¥{fire_number:,.0f}")
    print(f"当前进度：{progress:.1f}%")
    
    result = {"fire_number": fire_number, "current": current, "progress": progress}
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"{skill_name}_{timestamp}.json", 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
    print("\n✅ 已保存")

if __name__ == '__main__':
    main()
