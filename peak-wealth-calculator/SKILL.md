---
name: peak-wealth-calculator
version: 1.0.0
description: 财富峰点计算器 - 帮助用户确定最佳财富峰点年龄
author: 燃冰 + 小蚂蚁
created: 2026-03-18
skill_type: 通用
---

# 财富峰点计算器 📈

**基于《最优解人生》（Die With Zero）核心理念**

---

## 📋 功能描述

帮助用户计算最佳财富峰点年龄，判断是否应该继续积累财富或开始增加支出。

**适用场景：**
- 评估是否应该提前退休
- 判断财富积累是否过度
- 规划"支出>收入"的转折点
- 优化人生充实感

**边界条件：**
- 不提供具体投资建议
- 基于统计模型，非个人定制
- 聚焦峰点判断，非财富规划

---

## 🎯 核心功能

### 1. 峰点年龄计算

基于用户情况计算最佳财富峰点年龄。

**标准范围：** 45-60 岁

**影响因素：**
- 当前年龄
- 健康状况
- 职业满意度
- 家庭负担
- 体验清单紧迫性

**输出：**
```json
{
  "optimal_peak_age_range": "50-55",
  "current_age": 45,
  "years_to_peak": "5-10",
  "status": "积累期",
  "recommendation": "继续积累 5-10 年后开始增加体验支出"
}
```

### 2. 峰点状态评估

评估用户当前是否已过峰点。

**三种状态：**
- 积累期（未达峰点）：继续积累
- 峰点期（合理区间）：维持平衡
- 支出期（已过峰点）：增加支出

**输出：**
```json
{
  "current_age": 58,
  "peak_status": "峰点期",
  "analysis": "你处于财富峰点合理区间（45-60 岁）",
  "action": "开始规划支出>收入的阶段",
  "urgency": "中"
}
```

### 3. 继续工作价值评估

评估继续工作的边际价值。

**核心问题：**
- 多赚的钱是否能显著提升人生充实感？
- 工作的机会成本（时间、健康、体验）是否过高？

**输出：**
```json
{
  "continue_working_value": "低",
  "reasoning": "你已超出生存阈值 200%，继续工作的边际价值递减",
  "opportunity_cost": "每年损失 3-5 个重要体验",
  "recommendation": "考虑减少工作时间或提前退休"
}
```

### 4. 体验支出建议

基于峰点状态，给出体验支出建议。

**策略：**
- 积累期：体验支出占收入 10-20%
- 峰点期：体验支出占收入 20-40%
- 支出期：体验支出占资产 3-5%/年

**输出：**
```json
{
  "current_stage": "峰点期",
  "recommended_experience_spending_ratio": 0.3,
  "annual_experience_budget": 300000,
  "priority_experiences": [
    "体力要求高的旅行（趁身体好）",
    "与家人共同体验（趁孩子还小）",
    "学习新技能（趁认知能力强）"
  ]
}
```

---

## 📊 输入参数

```json
{
  "current_age": {
    "type": "number",
    "required": true,
    "description": "当前年龄"
  },
  "health_score": {
    "type": "number",
    "required": true,
    "description": "健康状况自评（1-10）"
  },
  "current_assets": {
    "type": "number",
    "required": true,
    "description": "当前资产总额（元）"
  },
  "annual_income": {
    "type": "number",
    "required": true,
    "description": "年收入（元）"
  },
  "annual_living_cost": {
    "type": "number",
    "required": true,
    "description": "年生活费（元）"
  },
  "job_satisfaction": {
    "type": "number",
    "required": false,
    "description": "工作满意度（1-10）"
  },
  "family_dependency": {
    "type": "string",
    "required": false,
    "description": "家庭负担（轻/中/重）"
  },
  "urgent_experiences": {
    "type": "array",
    "required": false,
    "description": "紧迫体验清单（年龄/健康限制）"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "peak_age_calculation": {
      "optimal_range": "",
      "years_to_peak": 0,
      "status": ""
    },
    "peak_status_assessment": {},
    "continue_working_value": {},
    "experience_spending_recommendation": {},
    "action_items": []
  },
  "error": null
}
```

---

## 🧪 使用示例

### 示例 1：40 岁高管

```
@ant 帮我评估是否应该继续拼命工作

信息：
- 年龄：40 岁
- 健康：7/10（开始下滑）
- 资产：2000 万
- 年收入：300 万
- 年生活费：100 万
- 工作满意度：5/10（疲惫）
- 紧迫体验：带孩子环游世界（孩子 8 岁）
```

**预期输出：**
- 最佳峰点年龄：50-55 岁
- 当前状态：积累期后期
- 继续工作价值：中低（边际价值递减）
- 建议：减少工作时间，增加家庭体验支出

### 示例 2：62 岁企业家

```
@ant 我 62 岁了，是否应该退休？

信息：
- 年龄：62 岁
- 健康：8/10
- 资产：1 亿
- 年收入：500 万
- 年生活费：200 万
- 工作满意度：9/10（热爱）
- 紧迫体验：无
```

**预期输出：**
- 最佳峰点年龄：已过（45-60 岁）
- 当前状态：支出期
- 继续工作价值：高（因为热爱）
- 建议：可以继续工作，但应大幅增加体验支出（旅行、慈善、赠与）

---

## ⚠️ 错误处理

| 错误码 | 含义 | 处理建议 |
|--------|------|----------|
| 400 | 参数缺失 | 检查必填字段（年龄、健康、资产、收入、生活费） |
| 400 | 年龄无效 | 年龄应在 18-120 之间 |
| 400 | 健康评分无效 | 健康评分应在 1-10 之间 |
| 500 | 内部错误 | 重试或联系开发者 |

---

## 📚 政策依据

**核心理论：**
- 《最优解人生》（Die With Zero）- Bill Perkins
- 生命周期假说（Life-Cycle Hypothesis）
- 边际效用递减理论

**关键数据：**
- 最佳财富峰点年龄：45-60 岁（统计模型）
- 享受能力随年龄下降：从 20 多岁开始微不可察地衰退
- 旅行享受能力：50 岁后显著下降

---

## 🔗 相关文件

- `calculators/peak-wealth-age.py` - 峰点年龄计算器
- `calculators/marginal-value.py` - 边际价值计算器
- `templates/peak-assessment-report.md` - 峰点评估报告模板

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*知道何时停止积累，开始享受。* 📈
