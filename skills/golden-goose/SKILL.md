---
name: golden-goose
version: 1.0.0
description: 金鹅账户 - 帮助用户建立投资本金，实现被动收入
author: 燃冰 + 小蚂蚁
created: 2026-03-18
skill_type: 通用
---

# 金鹅账户 🪿

**基于《小狗钱钱》核心理念**

---

## 📋 功能描述

帮助用户理解"养鹅生蛋"原理，建立投资本金账户，实现被动收入，最终达到财务自由。

**适用场景：**
- 儿童/青少年财商启蒙
- 成年人投资规划
- 被动收入建立
- 财务自由路径规划

**边界条件：**
- 不提供具体投资建议
- 不推荐具体产品
- 聚焦理念和规划

---

## 🎯 核心功能

### 1. 金鹅账户设立

帮助用户理解并设立金鹅账户。

**核心理念：**
- 鹅 = 本金（不能花）
- 蛋 = 利息/收益（可以花或再投资）
- 杀鹅取卵 = 花掉本金（错误）

**输出：**
```json
{
  "account_type": "金鹅账户",
  "purpose": "投资本金（养鹅生蛋）",
  "rule": "本金永远不花，只花利息/收益",
  "initial_deposit": 10000,
  "monthly_contribution": 1000,
  "target_goose_size": 100000,
  "estimated_egg_income": "年化 5% = 5000 元/年"
}
```

### 2. 收入分配建议

将收入合理分配到不同账户。

**50/30/20 法则：**
- 50% 梦想储蓄（短期目标）
- 30% 日常开销（生活费）
- 20% 金鹅账户（投资本金）

**输出：**
```json
{
  "monthly_income": 10000,
  "allocation": {
    "dream_saving": {
      "amount": 5000,
      "percentage": 0.5,
      "purpose": "梦想目标（买车、旅行等）"
    },
    "daily_spending": {
      "amount": 3000,
      "percentage": 0.3,
      "purpose": "日常开销（房租、吃饭等）"
    },
    "golden_goose": {
      "amount": 2000,
      "percentage": 0.2,
      "purpose": "投资本金（永远不花）"
    }
  },
  "goose_growth_projection": {
    "year_1": 24000,
    "year_5": 120000,
    "year_10": 240000
  }
}
```

### 3. 被动收入计算

计算金鹅产生的被动收入（金蛋）。

**公式：**
```
年金蛋 = 本金 × 年化收益率
月被动收入 = 年金蛋 ÷ 12
```

**输出：**
```json
{
  "current_goose": 50000,
  "annual_return_rate": 0.05,
  "annual_egg_income": 2500,
  "monthly_passive_income": 208,
  "financial_freedom_target": 1000000,
  "years_to_freedom": 15,
  "insight": "你的金鹅每年下 2500 元蛋，继续养大它！"
}
```

### 4. 财务自由路径

规划从当前到财务自由的路径。

**财务自由定义：**
```
财务自由 = 被动收入 ≥ 生活开销
```

**输出：**
```json
{
  "current_status": {
    "goose_size": 50000,
    "passive_income": 2500,
    "annual_expenses": 60000,
    "freedom_ratio": 0.04
  },
  "target_status": {
    "required_goose": 1200000,
    "required_passive_income": 60000,
    "freedom_ratio": 1.0
  },
  "path": [
    {"year": 1, "goose": 74000, "passive": 3700},
    {"year": 5, "goose": 170000, "passive": 8500},
    {"year": 10, "goose": 340000, "passive": 17000},
    {"year": 15, "goose": 600000, "passive": 30000}
  ],
  "acceleration_tips": [
    "增加收入（提升技能、副业）",
    "降低开销（极简生活）",
    "提高投资回报率（学习投资）"
  ]
}
```

---

## 📊 输入参数

```json
{
  "age": {
    "type": "number",
    "required": true,
    "description": "年龄"
  },
  "monthly_income": {
    "type": "number",
    "required": true,
    "description": "月收入"
  },
  "monthly_expenses": {
    "type": "number",
    "required": true,
    "description": "月开销"
  },
  "current_savings": {
    "type": "number",
    "required": false,
    "description": "当前储蓄"
  },
  "expected_return_rate": {
    "type": "number",
    "required": false,
    "description": "预期年化收益率（默认 5%）"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "goose_account": {},
    "income_allocation": {},
    "passive_income_calculation": {},
    "financial_freedom_path": {},
    "action_items": []
  },
  "error": null
}
```

---

## 🧪 使用示例

### 示例 1：12 岁小学生

```
@ant 我想开始养金鹅

信息：
- 年龄：12 岁
- 月收入：500 元（零花钱）
- 月开销：300 元
- 当前储蓄：2000 元
```

**预期输出：**
- 每月可存 100 元到金鹅账户（20%）
- 年化 5% 收益，10 年后金鹅大小
- 建议：不要花掉金鹅，让它长大

### 示例 2：30 岁职场人士

```
@ant 我想规划财务自由

信息：
- 年龄：30 岁
- 月收入：20000 元
- 月开销：12000 元
- 当前储蓄：100000 元
```

**预期输出：**
- 每月可存 4000 元到金鹅账户
- 当前被动收入：5000 元/年
- 财务自由目标：240 万（年开销 14.4 万÷5%）
- 预计达成时间：15-20 年

---

## ⚠️ 错误处理

| 错误码 | 含义 | 处理建议 |
|--------|------|----------|
| 400 | 参数缺失 | 检查必填字段（年龄、收入、开销） |
| 400 | 开销大于收入 | 需要降低开销或增加收入 |
| 400 | 收益率不合理 | 收益率应在 1%-15% 之间 |
| 500 | 内部错误 | 重试或联系开发者 |

---

## 📚 政策依据

**核心理论：**
- 《小狗钱钱》- 博多·舍费尔
- 复利效应（Compound Interest）
- 财务自由理论（FIRE Movement）

**关键概念：**
- 金鹅 = 本金（永远不花）
- 金蛋 = 利息/收益（可以花）
- 杀鹅取卵 = 花掉本金（错误）
- 财务自由 = 被动收入 ≥ 生活开销

---

## 🔗 相关文件

- `calculators/compound-interest.sh` - 复利计算器
- `calculators/freedom-path.sh` - 财务自由路径
- `templates/goose-account.md` - 金鹅账户模板

## 💡 使用建议

**开设金鹅账户：**
1. 打印 goose-account.md
2. 开设独立投资账户
3. 设置每月自动定投

**计算复利：**
```bash
./calculators/compound-interest.sh 10000 8 30
```

**计算财务自由路径：**
```bash
./calculators/freedom-path.sh 10000 500000 20000 8
```

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*养大你的金鹅，让它为你下蛋。* 🪿
