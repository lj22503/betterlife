#!/usr/bin/env python3
"""问题树报告生成器"""

import json
import sys
from datetime import datetime

def generate_report(data):
    """根据对话数据生成问题树报告"""
    
    template = f"""# 🔍 问题树报告

**生成时间：** {datetime.now().strftime('%Y-%m-%d %H:%M')}
**用户：** {data.get('user_name', '用户')}
**核心问题：** {data.get('core_problem', '未定义')}

---

## 一、问题定义

### 5W2H 结构化分析

| 维度 | 内容 |
|------|------|
| **What**（是什么） | {data.get('what', '待补充')} |
| **Why**（为什么） | {data.get('why', '待补充')} |
| **Who**（涉及谁） | {data.get('who', '待补充')} |
| **When**（何时） | {data.get('when', '待补充')} |
| **Where**（何地） | {data.get('where', '待补充')} |
| **How**（如何应对） | {data.get('how', '待补充')} |
| **How much**（严重程度） | {data.get('severity', '待评估')}/10 |

---

## 二、成功标准

{data.get('success_criteria', '待补充')}

---

## 三、挑战评估

### 内部障碍
{data.get('internal_barriers', '待补充')}

### 外部障碍
{data.get('external_barriers', '待补充')}

### 风险评估
**最大风险：** {data.get('max_risk', '待评估')}

**应对策略：** {data.get('risk_strategy', '待制定')}

---

## 四、方案对比

{data.get('options_comparison', '待补充')}

**推荐方案：** {data.get('recommended_option', '待选择')}

**理由：** {data.get('recommendation_reason', '待说明')}

---

## 五、行动计划

### 近期行动（下周）
{data.get('immediate_actions', '待规划')}

### 复盘机制
- **频率：** {data.get('review_frequency', '每周')}
- **内容：** 进展检查 / 障碍识别 / 策略调整

---

## 六、洞察与建议

### 看得远（回路分析）
- **一阶后果：** {data.get('first_order', '待分析')}
- **二阶后果：** {data.get('second_order', '待分析')}
- **三阶后果：** {data.get('third_order', '待分析')}

### 看得透（层级分析）
- **事件层：** {data.get('event_level', '待分析')}
- **模式层：** {data.get('pattern_level', '待分析')}
- **结构层：** {data.get('structure_level', '待分析')}

---

*本报告由 problem-mapper 技能生成*
*基于"全景式问题解决树"框架*
"""
    
    return template

def main():
    if len(sys.argv) < 2:
        print("用法：python3 generate-report.py <json_data_file>")
        print("示例：python3 generate-report.py problem-data.json")
        sys.exit(1)
    
    data_file = sys.argv[1]
    
    try:
        with open(data_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"❌ 文件不存在：{data_file}")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"❌ JSON 格式错误：{data_file}")
        sys.exit(1)
    
    report = generate_report(data)
    
    # 输出报告
    print(report)
    
    # 保存到文件
    output_file = f"problem-tree-report-{datetime.now().strftime('%Y%m%d-%H%M%S')}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"\n✅ 报告已保存到：{output_file}")

if __name__ == '__main__':
    main()
