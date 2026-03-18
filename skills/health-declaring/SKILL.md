---
name: health-declaring
version: 1.0.0
description: 健康告知助手 - 汇总体检异常，辅助健康告知
author: 燃冰 + 小蚂蚁
created: 2026-03-18
skill_type: 通用
---

# 健康告知助手 🏥

**基于《你的保险指南》核心理念**

---

## 📋 功能描述

帮助用户汇总体检异常指标，理解健康告知规则，避免因告知不当导致拒赔。

**适用场景：**
- 投保前健康告知
- 体检异常汇总
- 核保结果预测
- 多家投保对比

**边界条件：**
- 不提供医疗建议
- 不替代专业核保
- 适合 18 岁以上人群

---

## 🎯 核心功能

### 1. 体检异常汇总

汇总体检报告中的异常指标。

**常见异常指标：**
- 血糖异常（空腹血糖、糖耐量测试）
- 甲状腺问题（结节、甲减、甲亢）
- 胃炎、肝血管瘤、肝囊肿
- 乳腺问题（结节、增生）
- 新生儿卵圆孔未闭合、黄疸
- 高血压、肺结节、血尿酸/痛风

**输出：**
```json
{
  "abnormal_indicators": [
    {
      "name": "甲状腺结节",
      "severity": "轻度",
      "impact": "可能加费承保",
      "suggestion": "提供近期 B 超报告"
    },
    {
      "name": "空腹血糖偏高",
      "severity": "中度",
      "impact": "可能加费或除外",
      "suggestion": "提供糖耐量测试报告"
    },
    {
      "name": "肺结节",
      "severity": "需观察",
      "impact": "可能延期或拒保",
      "suggestion": "改善作息，复查后投保"
    }
  ],
  "overall_impact": "部分产品可能加费或除外",
  "recommendation": "优先选择核保宽松的产品"
}
```

### 2. 健康告知规则解析

解析健康告知的有限告知原则。

**核心原则：**
- 有限告知：问什么答什么，不问不答
- 无需专门体检：不要为了投保而去体检
- 如实告知：已知的异常情况必须告知

**输出：**
```json
{
  "declaration_principle": "有限告知",
  "explanation": "问什么答什么，不问不答",
  "common_questions": [
    "过去 2 年内是否住院？",
    "过去 5 年内是否被医生建议住院或手术？",
    "是否患有高血压、糖尿病、心脏病？",
    "是否有体检异常（如结节、肿块）？"
  ],
  "key_insight": "不要为了投保而去体检，已有异常如实告知"
}
```

### 3. 核保结果预测

预测可能的核保结果。

**核保结果：**
- 标准体：正常承保
- 加费：保费上浮
- 除外：特定疾病不保
- 延期：观察后再决定
- 拒保：无法承保

**输出：**
```json
{
  "predicted_result": "加费承保",
  "confidence": "中",
  "reasoning": "甲状腺结节 TI-RADS 3 级，多家保险公司可能加费",
  "alternative_products": [
    "产品 A：标准体承保",
    "产品 B：加费 10%",
    "产品 C：除外甲状腺疾病"
  ],
  "recommendation": "优先选择产品 A（标准体）"
}
```

### 4. 特殊情况指导

针对特殊人群提供投保指导。

**特殊情况：**
- 孕期（甲减/甲亢）
- 新生儿（卵圆孔未闭、黄疸）
- 慢性病（高血压、糖尿病）
- 既往症（癌症康复、手术史）

**输出：**
```json
{
  "special_case": "孕期甲状腺异常",
  "guidance": {
    "condition": "孕期 TSH 浓度异常（甲减/甲亢）",
    "impact": "受孕激素影响，属于正常状况",
    "suggestion": "持续观察，无须过度担心",
    "timing": "孕期结束后甲状腺功能恢复正常，不影响正常投保"
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
  "health_conditions": {
    "type": "array",
    "required": false,
    "description": "健康状况/体检异常列表"
  },
  "recent_hospitalization": {
    "type": "boolean",
    "required": false,
    "description": "过去 2 年是否住院"
  },
  "chronic_diseases": {
    "type": "array",
    "required": false,
    "description": "慢性疾病列表"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "abnormal_indicators_summary": {},
    "declaration_rules": {},
    "underwriting_prediction": {},
    "special_case_guidance": {},
    "action_items": []
  },
  "error": null
}
```

---

## 📚 政策依据

**核心理论：**
- 《你的保险指南》- 健康管理角度规划保险
- 保险健康告知规则
- 有限告知原则

**关键概念：**
- 有限告知：问什么答什么
- 不要为了投保而去体检
- 已有异常如实告知

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*先看体检报告，再看保险产品。* 🏥
