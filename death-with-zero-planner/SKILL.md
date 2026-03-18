---
name: death-with-zero-planner
version: 1.0.0
description: 死前归零规划师 - 帮助用户规划财富支出，实现死前归零
author: 燃冰 + 小蚂蚁
created: 2026-03-18
skill_type: 通用
---

# 死前归零规划师 💰

**基于《最优解人生》（Die With Zero）核心理念**

---

## 📋 功能描述

帮助用户计算"生存阈值"，规划财富支出曲线，避免"赚了一辈子钱，死前花不完"。

**适用场景：**
- 评估是否需要继续积累财富
- 规划退休支出策略
- 确定财富峰点年龄
- 制定遗产/赠与计划

**边界条件：**
- 不提供具体投资建议
- 不替代专业理财规划
- 聚焦支出规划，非财富增值

---

## 🎯 核心功能

### 1. 生存阈值计算

计算维持基本生活所需的财富总额。

**公式：**
```
生存阈值 = 0.7 × 年生活费 × 剩余寿命
```

**输入：**
- 当前年龄
- 预期寿命（默认 85 岁，可调整）
- 年生活费（元）
- 已有资产（元）

**输出：**
```json
{
  "survival_threshold": 2100000,
  "current_assets": 5000000,
  "excess": 2900000,
  "excess_ratio": 1.38,
  "recommendation": "你已超出生存阈值 138%，可以增加体验支出"
}
```

### 2. 财富峰点评估

评估用户的财富峰点年龄是否合理。

**标准峰点范围：** 45-60 岁

**评估逻辑：**
- <45 岁：可能过早停止积累
- 45-60 岁：合理区间
- >60 岁：可能过度积累，建议增加支出

**输出：**
```json
{
  "current_age": 55,
  "peak_wealth_age": 55,
  "status": "合理",
  "analysis": "你的财富峰点在合理区间（45-60 岁）",
  "action": "开始规划支出大于收入的阶段"
}
```

### 3. 支出曲线规划

规划从当前到生命结束的支出曲线。

**策略：**
- 活力之年（65-75 岁）：高支出，多体验
- 慢活之年（75-85 岁）：中支出，适度体验
- 失活之年（85 岁+）：低支出，医疗为主

**输出：**
```json
{
  "go_go_years": {
    "age_range": "65-75",
    "annual_spending": 300000,
    "focus": "旅行、爱好、体验"
  },
  "slow_go_years": {
    "age_range": "75-85",
    "annual_spending": 200000,
    "focus": "医疗、照护、家庭"
  },
  "no_go_years": {
    "age_range": "85+",
    "annual_spending": 150000,
    "focus": "医疗、护理"
  }
}
```

### 4. 遗产/赠与优化

评估何时将财富交给子女/慈善效益最大。

**核心原则：**
- 子女 26-35 岁是最佳接收年龄
- 生前赠与优于遗产继承
- 考虑子女实际需求时间点

**输出：**
```json
{
  "children": [
    {
      "name": "孩子 A",
      "current_age": 8,
      "optimal_gift_age": "26-35 岁",
      "optimal_gift_year": "2044-2053",
      "suggested_amount": 500000,
      "reason": "创业/购房/教育关键期"
    }
  ],
  "recommendation": "建议在子女 26-35 岁期间分批赠与，而非一次性遗产"
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
  "annual_living_cost": {
    "type": "number",
    "required": true,
    "description": "年生活费（元）"
  },
  "current_assets": {
    "type": "number",
    "required": true,
    "description": "当前资产总额（元）"
  },
  "annual_income": {
    "type": "number",
    "required": false,
    "description": "年收入（元）"
  },
  "expected_retirement_age": {
    "type": "number",
    "required": false,
    "description": "预期退休年龄"
  },
  "life_expectancy": {
    "type": "number",
    "required": false,
    "description": "预期寿命（默认 85）"
  },
  "children": {
    "type": "array",
    "required": false,
    "description": "子女信息列表"
  },
  "pension_income": {
    "type": "number",
    "required": false,
    "description": "退休后年收入（养老金等）"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "survival_threshold": {
      "amount": 0,
      "calculation": "",
      "excess": 0
    },
    "peak_wealth_assessment": {
      "status": "",
      "analysis": ""
    },
    "spending_curve": {},
    "inheritance_optimization": {},
    "action_items": []
  },
  "error": null
}
```

---

## 🧪 使用示例

### 示例 1：50 岁高净值人士

```
@ant 帮我评估是否需要继续积累财富

信息：
- 年龄：50 岁
- 年生活费：50 万
- 当前资产：3000 万
- 年收入：200 万
- 预期退休：55 岁
- 子女：1 个（10 岁）
```

**预期输出：**
- 生存阈值：约 1200 万（0.7×50 万×35 年）
- 当前超出阈值 1800 万
- 建议：55 岁后可开始支出大于收入
- 子女赠与规划：2044-2053 年分批赠与

### 示例 2：65 岁退休人员

```
@ant 我退休了，如何规划余生支出？

信息：
- 年龄：65 岁
- 年生活费：20 万
- 当前资产：800 万
- 养老金：15 万/年
- 预期寿命：90 岁
```

**预期输出：**
- 生存阈值：约 350 万（0.7×20 万×25 年）
- 当前超出阈值 450 万
- 建议：活力之年（65-75）年支出可提升至 40-50 万
- 重点：旅行、爱好、健康投资

---

## ⚠️ 错误处理

| 错误码 | 含义 | 处理建议 |
|--------|------|----------|
| 400 | 参数缺失 | 检查必填字段（年龄、生活费、资产） |
| 400 | 年龄无效 | 年龄应在 18-120 之间 |
| 400 | 资产为负 | 资产应为正数 |
| 500 | 内部错误 | 重试或联系开发者 |

---

## 📚 政策依据

**核心理论：**
- 《最优解人生》（Die With Zero）- Bill Perkins
- 生命周期假说（Life-Cycle Hypothesis）
- 精算师寿命计算器（Longevity Illustrator）

**关键公式：**
- 生存阈值 = 0.7 × 年生活费 × 剩余寿命
- 最佳净资产峰点年龄：45-60 岁
- 子女最佳接收年龄：26-35 岁

---

## 🔗 相关文件

- `calculators/survival-threshold.py` - 生存阈值计算器
- `calculators/peak-wealth-age.py` - 财富峰点计算器
- `templates/spending-curve.md` - 支出曲线模板

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*钱尽其用，死前归零。* 💰
