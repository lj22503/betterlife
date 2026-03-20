name: family-risk-assessor
description: ［何时使用］当用户需要家庭风险评估器 - 识别家庭最大风险点，确定保障优先级时；当用户提及相关功能时
skill_type: 通用---

# 家庭风险评估器 🏠

**基于《你的保险指南》核心理念**

---

## 📋 功能描述

帮助家庭识别最大风险点，确定保障优先级，避免保障错配（如给孩子买很多保险，经济支柱却裸奔）。

**适用场景：**
- 家庭保障规划
- 保险配置前评估
- 风险识别与分析
- 保障优先级排序

**边界条件：**
- 不提供具体保险建议
- 不替代专业理财规划
- 适合 18 岁以上人群

---

## 🎯 核心功能

### 1. 家庭风险点识别

识别家庭中最大的风险点。

**核心原则：**
- 家庭最大风险 = 主要收入来源者
- 先保大人，后保小孩
- 先保经济支柱，后保其他人

**输出：**
```json
{
  "family_members": [
    {
      "name": "丈夫",
      "age": 35,
      "role": "经济支柱",
      "annual_income": 500000,
      "income_ratio": 0.7,
      "risk_level": "最高",
      "priority": 1
    },
    {
      "name": "妻子",
      "age": 33,
      "role": "次要收入",
      "annual_income": 200000,
      "income_ratio": 0.3,
      "risk_level": "高",
      "priority": 2
    },
    {
      "name": "孩子",
      "age": 5,
      "role": "无收入",
      "annual_income": 0,
      "income_ratio": 0,
      "risk_level": "中",
      "priority": 3
    }
  ],
  "key_insight": "丈夫是家庭最大风险点，应优先配置保障"
}
```

### 2. 8 个自省问题

引导用户思考内心担忧，明确保障需求。

**问题列表：**
1. 有没有什么问题是让你夜不能寐的？
2. 家里的哪位家庭成员一旦生病，现金流就会被切断？
3. 如果赚钱的家庭成员生重病或者去世，你会不会需要卖房子来还房贷？
4. 假设家庭成员有人生病，特别是疑难杂症，希望享受到什么样的医疗服务？
5. 有没有哪一类疾病让你特别担心且恐惧？
6. 你的家庭储蓄目前有多少？能不能一次性无压力地拿出 20 万元？
7. 父母的医疗保障状况如何？你是否会担心他们将来产生的护理和医疗费用？
8. 有没有某一种极端情况发生，会给家庭财务带来毁灭性的打击？

**输出：**
```json
{
  "answers": {
    "q1_night_worry": "担心丈夫生病无法工作",
    "q2_cashflow_risk": "丈夫（主要收入来源）",
    "q3_house_selling": "是（房贷 800 万）",
    "q4_medical_service": "国内特需部",
    "q5_feared_disease": "癌症、心脑血管疾病",
    "q6_savings": "50 万（可拿出 20 万）",
    "q7_parents_coverage": "有社保，无商业保险",
    "q8_extreme_scenario": "经济支柱身故 + 房贷未还"
  },
  "risk_analysis": {
    "primary_risk": "经济支柱身故/重疾导致现金流断裂",
    "secondary_risk": "大额医疗支出耗尽储蓄",
    "tertiary_risk": "父母医疗负担"
  },
  "coverage_priority": [
    "丈夫：定期寿险（覆盖房贷）+ 重疾险",
    "妻子：重疾险 + 医疗险",
    "孩子：医疗险 + 意外险",
    "父母：惠民宝/百万医疗险"
  ]
}
```

### 3. 保障缺口分析

分析现有保障与需求之间的缺口。

**分析维度：**
- 寿险缺口 = 房贷 + 孩子教育 + 父母赡养 + 其他开支
- 重疾险缺口 = 年收入×3-5 倍（收入损失补偿）
- 医疗险缺口 = 社保外用药 coverage
- 意外险缺口 = 身故/伤残保额

**输出：**
```json
{
  "current_coverage": {
    "life_insurance": 2000000,
    "critical_illness": 1000000,
    "medical": "社保",
    "accident": 500000
  },
  "required_coverage": {
    "life_insurance": 10000000,
    "critical_illness": 2500000,
    "medical": "百万医疗",
    "accident": 2000000
  },
  "gap": {
    "life_insurance": 8000000,
    "critical_illness": 1500000,
    "medical": "需补充百万医疗",
    "accident": 1500000
  },
  "priority_action": "优先补充定期寿险 800 万（覆盖房贷）"
}
```

### 4. 家庭风险矩阵

生成家庭风险矩阵，可视化风险分布。

**输出：**
```json
{
  "risk_matrix": {
    "economic_pillar": {
      "health_risk": "高",
      "life_risk": "高",
      "disability_risk": "高",
      "longevity_risk": "中"
    },
    "spouse": {
      "health_risk": "中",
      "life_risk": "中",
      "disability_risk": "中",
      "longevity_risk": "中"
    },
    "children": {
      "health_risk": "低",
      "life_risk": "低",
      "disability_risk": "低",
      "longevity_risk": "低"
    },
    "parents": {
      "health_risk": "高",
      "life_risk": "中",
      "disability_risk": "中",
      "longevity_risk": "高"
    }
  },
  "visualization": "风险热力图",
  "key_insight": "经济支柱风险最高，应优先保障"
}
```

---

## 📊 输入参数

```json
{
  "family_members": {
    "type": "array",
    "required": true,
    "description": "家庭成员列表"
  },
  "annual_income": {
    "type": "number",
    "required": true,
    "description": "家庭年收入"
  },
  "savings": {
    "type": "number",
    "required": false,
    "description": "家庭储蓄"
  },
  "debts": {
    "type": "number",
    "required": false,
    "description": "家庭负债（房贷等）"
  },
  "existing_coverage": {
    "type": "object",
    "required": false,
    "description": "现有保障"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "risk_identification": {},
    "self_reflection_answers": {},
    "coverage_gap_analysis": {},
    "risk_matrix": {},
    "priority_actions": [],
    "action_items": []
  },
  "error": null
}
```

---

## 🧪 使用示例

### 示例 1：新手爸妈

```
@ant 我们是新手爸妈，如何评估家庭风险？

信息：
- 丈夫：35 岁，年收入 50 万
- 妻子：33 岁，年收入 20 万
- 孩子：5 岁
- 房贷：800 万
- 储蓄：50 万
```

**预期输出：**
- 最大风险点：丈夫（贡献 70% 收入）
- 保障优先级：丈夫>妻子>孩子
- 寿险缺口：800 万（房贷）+ 孩子教育
- 建议：优先给丈夫配置定期寿险

### 示例 2：单身贵族

```
@ant 我单身，需要买保险吗？
```

**预期输出：**
- 风险点：自己（唯一收入来源）
- 优先配置：重疾险 + 医疗险 + 意外险
- 如有房贷：加定期寿险
- 建议：充足养老金（自己照顾自己）

### 示例 3：企业主

```
@ant 我是企业主，如何规划保障？
```

**预期输出：**
- 风险：企业经营风险 + 债务风险
- 原则：家企分离
- 建议：打底资产 + 子女教育现金流
- 工具：终身寿险（资产传承）

---

## ⚠️ 错误处理

| 错误码 | 含义 | 处理建议 |
|--------|------|----------|
| 400 | 参数缺失 | 检查必填字段（家庭成员、收入） |
| 400 | 收入为负 | 收入应为正数 |
| 400 | 成员过多 | 家庭成员不超过 10 人 |
| 500 | 内部错误 | 重试或联系开发者 |

---

## 📚 政策依据

**核心理论：**
- 《你的保险指南》- 健康管理角度规划保险
- 家庭风险管理理论
- 保险配置 3 大原则

**关键概念：**
- 原则 1：先考虑大风险，再看小风险
- 原则 2：先看体检报告，再看保险产品
- 原则 3：先自省内心担忧，再看产品类型
- 家庭最大风险 = 主要收入来源者

---

## 🔗 相关文件

- `templates/risk-assessment.md` - 风险评估模板
- `templates/self-reflection-questions.md` - 8 个自省问题
- `calculators/coverage-gap.py` - 保障缺口计算器

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*先保大人，后保小孩。经济支柱优先。* 🏠
---

## 🔧 故障排查

| 问题 | 检查项 |
|------|--------|
| 不触发 | description 是否包含触发词？ |
| 运行失败 | 脚本有执行权限吗？(`chmod +x`) |
