#!/usr/bin/env python3
"""
Health Declaring计算器
"""

import json
from datetime import datetime

def calculate(income, age, dependents):
    """保险需求计算"""
    critical = income * 3
    accident = income * 10
    life = income * 10 + dependents * 500000
    return {"critical": critical, "accident": accident, "life": life, "status": "success"}

def main():
    print("保险需求计算器")
    print("=" * 40)
    
    income = float(input("年收入（万）: ") or 0)
    age = int(input("年龄：") or 30)
    dependents = int(input("抚养人数：") or 0)
    
    result = calculate(income * 10000, age, dependents)
    print("\n建议保额")
    for k, v in result.items():
        if k != "status":
            print(f"  {k}: {v:,.0f}")
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"insurance_{timestamp}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
    print(f"\n已保存：{filename}")

if __name__ == '__main__':
    main()
