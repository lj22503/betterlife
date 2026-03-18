---
name: financial-diagnosis
version: 1.0.0
description: 财务状况诊断器 - 七大问题法分析财务状况
author: 燃冰 + 小蚂蚁
created: 2026-03-18
skill_type: 通用
---

# 财务状况诊断器 📊

**基于《理财就是理生活》核心理念**

---

## 📋 功能描述

通过七大问题法帮助用户全面分析财务状况，识别问题，制定改进方向。

**适用场景：**
- 个人/家庭财务诊断
- 理财起点评估
- 财务状况盘点
- 理财规划起点

**边界条件：**
- 不提供投资建议
- 不替代专业理财规划
- 适合 18 岁以上人群

---

## 🎯 核心功能

### 1. 七大问题诊断

通过七个核心问题全面诊断财务状况。

**七大问题：**
1. 月收入多少？
2. 月支出多少？
3. 有多少资产？
4. 有多少负债？
5. 其他还有什么？（公积金、养老金、保险等）
6. 想要什么？（人生目标）
7. 有哪些可以立刻变现的技能？

**输出：**
```json
{
  "seven_questions": {
    "q1_monthly_income": {
      "answer": 30000,
      "analysis": "家庭月收入 3 万，处于中等水平",
      "suggestion": "考虑增加被动收入"
    },
    "q2_monthly_expense": {
      "answer": 5000,
      "analysis": "月支出 5000，储蓄率 83%，非常优秀",
      "suggestion": "保持低支出习惯"
    },
    "q3_assets": {
      "answer": 1500000,
      "analysis": "资产 150 万（不含自住房车）",
      "suggestion": "盘点沉睡资产"
    },
    "q4_liabilities": {
      "answer": 200000,
      "analysis": "负债 20 万，负债收入比 35%",
      "suggestion": "负债可控，继续优化"
    },
    "q5_others": {
      "answer": "公积金、养老金、商业保险",
      "analysis": "保障体系完善",
      "suggestion": "定期检视保障充足性"
    },
    "q6_goals": {
      "answer": "为自己工作，开启事业",
      "analysis": "有明确的财务自由目标",
      "suggestion": "制定 5 年计划"
    },
    "q7_skills": {
      "answer": "数据分析、写作、摄影",
      "analysis": "有多元化变现技能",
      "suggestion": "发展副业，创建摇钱树"
    }
  },
  "overall_assessment": "财务状况健康，储蓄率高，有明确目标",
  "priority_actions": ["发展副业", "持续购入资产", "分散风险"]
}
```

### 2. 三张财务报表

生成家庭资产负债表、年度收支表、现金流量表。

**输出：**
```json
{
  "financial_statements": {
    "balance_sheet": {
      "assets": {
        "liquid": 300000,
        "financial": 1000000,
        "fixed": 200000,
        "total": 1500000
      },
      "liabilities": {
        "credit_card": 0,
        "mortgage": 200000,
        "other": 0,
        "total": 200000
      },
      "net_worth": 1300000
    },
    "income_expense_sheet": {
      "monthly_income": 30000,
      "monthly_expense": 5000,
      "monthly_saving": 25000,
      "saving_rate": 0.83
    },
    "cash_flow": {
      "active_income": 30000,
      "passive_income": 5000,
      "total_income": 35000,
      "expense": 5000,
      "net_cash_flow": 30000
    }
  }
}
```

### 3. 四个财务指标评估

计算并评估关键财务指标。

**指标：**
- 财务自由度 = 被动收入/日常开支
- 资产流动性比率 = 流动资产/月支出
- 负债收入比 = 月负债支出/月收入
- 投资合理比 = 投资资产/净资产

**输出：**
```json
{
  "financial_indicators": {
    "financial_freedom": {
      "value": 1.0,
      "formula": "被动收入/日常开支",
      "reference": "第一步>1，第二步>工资收入",
      "status": "初步达标",
      "suggestion": "继续增加被动收入"
    },
    "liquidity_ratio": {
      "value": 60,
      "formula": "流动资产/月支出",
      "reference": 3,
      "status": "过高",
      "suggestion": "部分资金可用于投资"
    },
    "debt_income_ratio": {
      "value": 0.35,
      "formula": "月负债支出/月收入",
      "reference": 0.4,
      "status": "合理可控",
      "suggestion": "继续优化"
    },
    "investment_ratio": {
      "value": 0.67,
      "formula": "投资资产/净资产",
      "reference": 0.5,
      "status": "较高",
      "suggestion": "注意风险分散"
    }
  },
  "overall_health": "良好",
  "key_improvements": ["降低流动资产比例", "增加被动收入"]
}
```

### 4. 草帽曲线定位

识别人生所处的草帽曲线阶段。

**阶段：**
- 22-32 岁：消费控制 + 发展技能
- 32-42 岁：债务管理 + 购入资产
- 42-52 岁：风险分散 + 部署退休

**输出：**
```json
{
  "life_stage": {
    "age": 35,
    "stage": "32-42 岁（第二个 10 年）",
    "focus": [
      "债务管理",
      "挖掘沉睡资产",
      "发展副业/创业",
      "持续购入资产"
    ],
    "wealth_pool": {
      "current": 1500000,
      "target_5y": 3700000,
      "gap": 2200000
    },
    "strategy": "利用优势，找到适合自己的蓝海"
  }
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
  "monthly_expense": {
    "type": "number",
    "required": true,
    "description": "月支出"
  },
  "total_assets": {
    "type": "number",
    "required": true,
    "description": "总资产"
  },
  "total_liabilities": {
    "type": "number",
    "required": false,
    "description": "总负债"
  },
  "passive_income": {
    "type": "number",
    "required": false,
    "description": "被动收入"
  },
  "skills": {
    "type": "array",
    "required": false,
    "description": "可变现技能列表"
  },
  "goals": {
    "type": "string",
    "required": false,
    "description": "财务目标"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "seven_questions_analysis": {},
    "financial_statements": {},
    "financial_indicators": {},
    "life_stage_positioning": {},
    "action_items": []
  },
  "error": null
}
```

---

## 📚 政策依据

**核心理论：**
- 《理财就是理生活》- 艾玛·沈
- 状况剖析七大问题法
- 草帽曲线理论
- 财务四指标评估

**关键概念：**
- 草帽曲线：收入线 - 支出线 = 财富蓄水池
- 七大问题：全面诊断财务状况
- 四指标：财务自由度、流动性、负债收入比、投资合理比

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*理财就是理生活，先诊断后行动。* 📊
