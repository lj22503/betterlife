#!/usr/bin/env python3
"""
生命能量计算器 - 配合 life-energy 技能使用

基于《要钱还是要生活》核心理念
"""

import json
from datetime import datetime

def calculate_real_hourly_rate(annual_income, work_expenses, work_hours, work_related_hours):
    """计算实际时薪"""
    net_income = annual_income - work_expenses
    total_hours = work_hours + work_related_hours
    
    if total_hours == 0:
        return 0
    
    return net_income / total_hours

def convert_to_life_energy(amount, real_hourly_rate):
    """将金额转换为生命能量小时"""
    if real_hourly_rate == 0:
        return 0
    return amount / real_hourly_rate

def main():
    print("⏰ 生命能量计算器")
    print("=" * 50)
    print("基于《要钱还是要生活》核心理念\n")
    
    # 收集收入信息
    print("【收入信息】")
    annual_income = float(input("年收入（税后）：") or 0)
    
    # 收集工作相关支出
    print("\n【工作相关支出】（每月）")
    commute_cost = float(input("通勤费用：") or 0)
    work_clothes = float(input("工作服装/装备：") or 0)
    outside_meals = float(input("外食费用：") or 0)
    stress_spending = float(input("减压消费：") or 0)
    childcare = float(input("育儿/家政：") or 0)
    other = float(input("其他：") or 0)
    
    monthly_expenses = commute_cost + work_clothes + outside_meals + stress_spending + childcare + other
    annual_expenses = monthly_expenses * 12
    
    # 收集时间信息
    print("\n【时间信息】（每周）")
    work_hours = float(input("实际工作小时：") or 40)
    commute_time = float(input("通勤时间：") or 0)
    prep_time = float(input("准备时间：") or 0)
    recovery_time = float(input("恢复时间：") or 0)
    overtime = float(input("加班时间：") or 0)
    
    weekly_hours = work_hours + commute_time + prep_time + recovery_time + overtime
    annual_hours = weekly_hours * 52
    
    # 计算
    real_hourly_rate = calculate_real_hourly_rate(annual_income, annual_expenses, annual_hours, 0)
    
    # 输出结果
    print("\n" + "=" * 50)
    print("📊 计算结果")
    print("=" * 50)
    
    print(f"\n【实际时薪】")
    print(f"  名义时薪：¥{annual_income/annual_hours:.2f}/小时")
    print(f"  实际时薪：¥{real_hourly_rate:.2f}/小时")
    print(f"  差异：¥{annual_income/annual_hours - real_hourly_rate:.2f}/小时")
    
    print(f"\n【年度总结】")
    print(f"  年收入：¥{annual_income:,.0f}")
    print(f"  年工作相关支出：¥{annual_expenses:,.0f}")
    print(f"  净收入：¥{annual_income - annual_expenses:,.0f}")
    print(f"  年工作总小时：{annual_hours:,.0f} 小时")
    
    # 生命能量转换
    print(f"\n【生命能量转换】")
    print(f"  实际时薪：¥{real_hourly_rate:.2f}/小时")
    
    # 常见支出转换
    print(f"\n【常见支出的生命能量成本】")
    expenses = {
        "手机费 (¥100/月)": 100,
        "外卖一顿 (¥50)": 50,
        "电影票 (¥80)": 80,
        "衣服 (¥500)": 500,
        "房租 (¥8000/月)": 8000,
    }
    
    for name, amount in expenses.items():
        hours = convert_to_life_energy(amount, real_hourly_rate)
        print(f"  {name}: {hours:.1f} 小时生命能量")
    
    # 保存结果
    result = {
        "calculation_date": datetime.now().isoformat(),
        "annual_income": annual_income,
        "annual_expenses": annual_expenses,
        "annual_hours": annual_hours,
        "real_hourly_rate": real_hourly_rate,
        "nominal_hourly_rate": annual_income/annual_hours,
        "monthly_expenses_breakdown": {
            "commute": commute_cost,
            "clothes": work_clothes,
            "meals": outside_meals,
            "stress": stress_spending,
            "childcare": childcare,
            "other": other
        }
    }
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"life_energy_{timestamp}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 结果已保存到：{filename}")
    print("\n💡 洞察：每一分钱都是你用生命能量换来的。")

if __name__ == '__main__':
    main()
