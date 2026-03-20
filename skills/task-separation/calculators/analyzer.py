#!/usr/bin/env python3
"""
课题分离分析器 - 配合 task-separation 技能使用
"""

import json
from datetime import datetime

def analyze_task_separation(scenario, my_control, others_control):
    """分析课题分离"""
    result = {
        "scenario": scenario,
        "my_tasks": [],
        "others_tasks": [],
        "recommendations": []
    }
    
    # 分析我的课题
    if my_control:
        for item in my_control.split('\n'):
            if item.strip():
                result["my_tasks"].append(item.strip())
    
    # 分析别人的课题
    if others_control:
        for item in others_control.split('\n'):
            if item.strip():
                result["others_tasks"].append(item.strip())
    
    # 生成建议
    result["recommendations"] = [
        "专注做好自己的课题",
        "不干涉别人的课题",
        "不让别人干涉自己的课题",
        "被讨厌是自由的代价"
    ]
    
    return result

def main():
    print("✂️ 课题分离分析器")
    print("=" * 50)
    print("基于《被讨厌的勇气》（阿德勒心理学）\n")
    
    # 收集信息
    scenario = input("当前困扰你的人际关系问题：\n")
    
    print("\n【你能控制的】（你的课题）")
    print("（每行一个，回车结束）")
    my_control = ""
    while True:
        item = input()
        if not item:
            break
        my_control += item + "\n"
    
    print("\n【你不能控制的】（别人的课题）")
    print("（每行一个，回车结束）")
    others_control = ""
    while True:
        item = input()
        if not item:
            break
        others_control += item + "\n"
    
    # 分析
    result = analyze_task_separation(scenario, my_control, others_control)
    
    # 输出
    print("\n" + "=" * 50)
    print("📋 课题分离分析")
    print("=" * 50)
    
    print(f"\n【场景】\n{result['scenario']}")
    
    print(f"\n【你的课题】（你能控制的）")
    for i, task in enumerate(result['my_tasks'], 1):
        print(f"  {i}. {task}")
    
    print(f"\n【别人的课题】（你不能控制的）")
    for i, task in enumerate(result['others_tasks'], 1):
        print(f"  {i}. {task}")
    
    print(f"\n【建议】")
    for rec in result['recommendations']:
        print(f"  ✓ {rec}")
    
    print("\n💡 关键洞察：")
    print("  为了满足别人的期望而活，")
    print("  是对自己撒谎也不断对周围人撒谎的生活方式。")
    
    # 保存
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"task_separation_{timestamp}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 分析已保存：{filename}")

if __name__ == '__main__':
    main()
