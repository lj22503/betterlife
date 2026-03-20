#!/usr/bin/env python3
"""
习惯设计计算器 - 配合 habit-loop 技能使用
"""

import json
from datetime import datetime

def design_habit(habit_type, habit_description, motivation_level, environment_control):
    """设计习惯循环"""
    
    plan = {
        "habit_type": habit_type,
        "habit_description": habit_description,
        "motivation_level": motivation_level,
        "environment_control": environment_control,
        "recommendations": []
    }
    
    if habit_type == "build_good":
        # 培养好习惯
        if motivation_level == "low":
            plan["recommendations"].append("动力低时，从两分钟版本开始")
            plan["recommendations"].append("使用诱惑捆绑增加吸引力")
        
        if environment_control == "low":
            plan["recommendations"].append("先优化环境，减少执行阻力")
            plan["recommendations"].append("将提示放在显眼位置")
        
        plan["recommendations"].append("设计执行意图：我将于［时间］在［地点］做［行为］")
        plan["recommendations"].append("使用习惯叠加：继［当前习惯］之后，我将［新习惯］")
        plan["recommendations"].append("设置即时奖励和追踪机制")
    
    elif habit_type == "break_bad":
        # 戒除坏习惯
        plan["recommendations"].append("识别并移除提示")
        plan["recommendations"].append("增加执行阻力（至少 3 个步骤）")
        plan["recommendations"].append("找问责伙伴")
        plan["recommendations"].append("重构认知：强调坏习惯的负面后果")
    
    return plan

def main():
    print("🔄 习惯设计计算器")
    print("=" * 40)
    
    habit_type = input("习惯类型 (build_good/break_bad): ")
    habit_description = input("习惯描述：")
    motivation_level = input("动力水平 (low/medium/high): ")
    environment_control = input("环境控制 (low/medium/high): ")
    
    plan = design_habit(habit_type, habit_description, motivation_level, environment_control)
    
    print("\n📋 习惯设计计划")
    print("=" * 40)
    print(f"习惯：{plan['habit_description']}")
    print(f"动力水平：{plan['motivation_level']}")
    print(f"环境控制：{plan['environment_control']}")
    print("\n建议：")
    for i, rec in enumerate(plan['recommendations'], 1):
        print(f"  {i}. {rec}")
    
    # 保存到文件
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"habit_plan_{timestamp}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(plan, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 计划已保存到：{filename}")

if __name__ == '__main__':
    main()
