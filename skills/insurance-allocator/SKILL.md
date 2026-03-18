---
name: insurance-allocator
version: 1.0.0
description: 保险配置器 - 根据家庭情况定制保险配置方案
author: 燃冰 + 小蚂蚁
created: 2026-03-18
skill_type: 通用
---

# 保险配置器 📋

**基于《你的保险指南》核心理念**

---

## 📋 功能描述

根据家庭风险状况、预算、健康状况，定制保险配置方案，确保保障全面、预算合理。

**适用场景：**
- 家庭保险规划
- 险种选择与搭配
- 保额计算
- 预算分配

**边界条件：**
- 不提供具体产品推荐
- 不替代专业理财规划
- 适合 18 岁以上人群

---

## 🎯 核心功能

### 1. 五大险种作用解析

解析各险种的作用和适用场景。

**险种说明：**

| 险种 | 作用 | 赔付方式 | 核心用途 |
|------|------|----------|----------|
| 重疾险 | 收入损失补偿 | 一次性给付 | 3-5 年收入补偿 |
| 医疗险 | 住院费用报销 | 报销制 | 覆盖社保外用药 |
| 意外险 | 意外身故/伤残 | 一次性给付 | 意外风险保障 |
| 寿险 | 身故理赔 | 一次性给付 | 覆盖负债 + 家庭责任 |
| 年金险 | 资产增值 + 专款专用 | 分期领取 | 教育/养老规划 |

**输出：**
```json
{
  "insurance_types": {
    "critical_illness": {
      "purpose": "收入损失补偿",
      "payout": "一次性给付",
      "recommended_coverage": "年收入×3-5 倍",
      "priority": "高（经济支柱）"
    },
    "medical": {
      "purpose": "住院费用报销",
      "payout": "报销制",
      "recommended_coverage": "200-400 万",
      "priority": "高（全员）"
    },
    "accident": {
      "purpose": "意外身故/伤残",
      "payout": "一次性给付",
      "recommended_coverage": "年收入×10 倍",
      "priority": "高（全员）"
    },
    "life": {
      "purpose": "身故理赔（覆盖负债）",
      "payout": "一次性给付",
      "recommended_coverage": "房贷 + 孩子教育 + 父母赡养",
      "priority": "高（有负债者）"
    },
    "annuity": {
      "purpose": "资产增值 + 专款专用",
      "payout": "分期领取",
      "recommended_coverage": "根据目标确定",
      "priority": "中（养老金/教育金）"
    }
  }
}
```

### 2. 保额计算

基于不同方法计算推荐保额。

**计算方法：**

**重疾险保额：**
- 收入倍数法：年收入×3-5 倍
- 适用：自由职业者、私企员工

**寿险保额：**
- 公式：房贷 + 车贷 + 孩子教育 + 父母赡养 + 其他必需开支
- 适用：有负债的家庭经济支柱

**意外险保额：**
- 年收入×10 倍
- 适用：全员

**输出：**
```json
{
  "applicant": {
    "age": 35,
    "role": "经济支柱",
    "annual_income": 500000,
    "debts": 8000000,
    "children_education": 1000000,
    "parents_support": 500000
  },
  "recommended_coverage": {
    "critical_illness": {
      "method": "收入倍数法",
      "calculation": "50 万×5 倍",
      "amount": 2500000
    },
    "life_insurance": {
      "method": "负债 + 责任法",
      "calculation": "800 万 +100 万 +50 万",
      "amount": 9500000
    },
    "accident": {
      "method": "年收入倍数法",
      "calculation": "50 万×10 倍",
      "amount": 5000000
    },
    "medical": {
      "method": "固定保额",
      "amount": 3000000
    }
  }
}
```

### 3. 家庭保险方案定制

根据家庭情况定制完整保险方案。

**输出：**
```json
{
  "family_plan": {
    "husband": {
      "age": 35,
      "role": "经济支柱",
      "coverage": {
        "critical_illness": "250 万（消费型）",
        "medical": "300 万（百万医疗）",
        "accident": "500 万（综合意外）",
        "life": "1000 万（定期寿险，保至 60 岁）"
      },
      "annual_premium": 80000,
      "priority": "最高"
    },
    "wife": {
      "age": 33,
      "role": "次要收入",
      "coverage": {
        "critical_illness": "100 万（消费型）",
        "medical": "300 万（百万医疗）",
        "accident": "200 万（综合意外）",
        "life": "500 万（定期寿险）"
      },
      "annual_premium": 40000,
      "priority": "高"
    },
    "child": {
      "age": 5,
      "coverage": {
        "critical_illness": "50 万（少儿重疾）",
        "medical": "300 万（百万医疗）",
        "accident": "50 万（少儿意外）"
      },
      "annual_premium": 5000,
      "priority": "中"
    }
  },
  "total_annual_premium": 125000,
  "premium_to_income_ratio": 0.18,
  "insight": "保费占收入 18%，在合理范围内（10-20%）"
}
```

### 4. 不同家庭类型方案

针对不同类型家庭提供定制方案。

**家庭类型：**
- 单身贵族/丁克
- 新手爸妈
- 全职主妇
- 企业主

**输出：**
```json
{
  "family_type": "新手爸妈",
  "characteristics": "有房贷、有孩子、双收入",
  "plan": {
    "priority_order": ["丈夫", "妻子", "孩子"],
    "husband": "重疾险 + 医疗险 + 意外险 + 定期寿险",
    "wife": "重疾险 + 医疗险 + 意外险 + 定期寿险",
    "child": "重疾险 + 医疗险 + 意外险",
    "parents": "惠民宝/百万医疗险（如有）"
  },
  "budget_allocation": {
    "husband": 0.5,
    "wife": 0.35,
    "child": 0.15
  },
  "key_insight": "先保大人后保小孩，经济支柱优先"
}
```

---

## 📊 输入参数

```json
{
  "family_type": {
    "type": "string",
    "required": true,
    "description": "家庭类型（单身/新手爸妈/全职主妇/企业主）"
  },
  "family_members": {
    "type": "array",
    "required": true,
    "description": "家庭成员信息"
  },
  "annual_income": {
    "type": "number",
    "required": true,
    "description": "家庭年收入"
  },
  "annual_budget": {
    "type": "number",
    "required": false,
    "description": "保险年度预算"
  },
  "debts": {
    "type": "number",
    "required": false,
    "description": "家庭负债"
  },
  "special_needs": {
    "type": "array",
    "required": false,
    "description": "特殊需求（如养老社区、子女教育等）"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "insurance_types_explanation": {},
    "coverage_calculation": {},
    "family_plan": {},
    "family_type_specific_plan": {},
    "budget_allocation": {},
    "action_items": []
  },
  "error": null
}
```

---

## 🧪 使用示例

### 示例 1：新手爸妈

```
@ant 我们是新手爸妈，如何配置保险？

信息：
- 丈夫：35 岁，年收入 50 万
- 妻子：33 岁，年收入 20 万
- 孩子：5 岁
- 房贷：800 万
- 保险预算：15 万/年
```

**预期输出：**
- 优先级：丈夫>妻子>孩子
- 丈夫：重疾 250 万 + 医疗 300 万 + 意外 500 万 + 寿险 1000 万
- 妻子：重疾 100 万 + 医疗 300 万 + 意外 200 万 + 寿险 500 万
- 孩子：重疾 50 万 + 医疗 300 万 + 意外 50 万
- 总保费：约 12-15 万/年

### 示例 2：单身贵族

```
@ant 我单身，需要哪些保险？
```

**预期输出：**
- 优先：重疾险 + 医疗险 + 意外险
- 如有房贷：加定期寿险
- 充足养老金（自己照顾自己）

### 示例 3：企业主

```
@ant 我是企业主，如何配置保险？
```

**预期输出：**
- 原则：家企分离
- 打底资产 + 子女教育现金流
- 终身寿险（资产传承、债务隔离）

---

## ⚠️ 错误处理

| 错误码 | 含义 | 处理建议 |
|--------|------|----------|
| 400 | 参数缺失 | 检查必填字段（家庭类型、成员、收入） |
| 400 | 预算不合理 | 保费建议为年收入 10-20% |
| 400 | 家庭类型无效 | 应为单身/新手爸妈/全职主妇/企业主 |
| 500 | 内部错误 | 重试或联系开发者 |

---

## 📚 政策依据

**核心理论：**
- 《你的保险指南》- 健康管理角度规划保险
- 保险配置五步走
- 家庭风险管理理论

**关键概念：**
- 重疾险：年收入×3-5 倍（收入损失补偿）
- 寿险：房贷 + 孩子教育 + 父母赡养
- 医疗险：覆盖社保外用药
- 意外险：年收入×10 倍

---

## 🔗 相关文件

- `calculators/coverage-amount.py` - 保额计算器
- `templates/family-plan.md` - 家庭方案模板
- `templates/budget-allocation.md` - 预算分配模板

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*先保大风险，后保小风险。先保大人，后保小孩。* 📋
