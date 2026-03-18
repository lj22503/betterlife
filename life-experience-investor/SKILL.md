---
name: life-experience-investor
version: 1.0.0
description: 人生体验投资顾问 - 帮助用户规划体验投资，最大化人生充实感
author: 燃冰 + 小蚂蚁
created: 2026-03-18
skill_type: 通用
---

# 人生体验投资顾问 💡

**基于《最优解人生》（Die With Zero）核心理念**

---

## 📋 功能描述

帮助用户从"积累财富"转向"投资体验"，最大化人生充实感。

**适用场景：**
- 规划年度体验清单
- 评估体验投资的 ROI（回忆红利）
- 识别"现在不做就晚了"的体验
- 平衡生存与尽兴活着

**边界条件：**
- 不提供财务投资建议
- 不替代专业理财规划
- 聚焦体验规划，非财富积累

---

## 🎯 核心功能

### 1. 体验清单生成

基于用户年龄、健康状况、兴趣，生成个性化体验清单。

**输入：**
- 年龄
- 健康状况（自评 1-10）
- 兴趣领域（旅行/学习/运动/社交/创造）
- 年度体验预算

**输出：**
```json
{
  "experiences": [
    {
      "name": "西藏徒步",
      "category": "旅行",
      "urgency": "高",
      "reason": "体力要求高，建议 45 岁前完成",
      "estimated_cost": 20000,
      "memory_dividend": "高"
    }
  ],
  "total_cost": 50000,
  "priority_order": ["西藏徒步", "潜水考证", "写作工作坊"]
}
```

### 2. 回忆红利计算

评估体验的长期价值（回忆红利）。

**公式：**
```
回忆红利 = 体验愉悦度 × 剩余寿命年数 × 分享次数
```

**示例：**
- 20 岁时的毕业旅行 → 愉悦度 8 × 60 年 × 100 次分享 = 48000 红利点
- 70 岁时的豪华旅行 → 愉悦度 6 × 15 年 × 10 次分享 = 900 红利点

### 3. 时机评估

判断体验的最佳执行时机。

**评估维度：**
- 身体要求（现在 vs 未来的能力）
- 财务要求（现在 vs 未来的负担）
- 时间要求（现在 vs 未来的空闲）
- 同伴要求（家人朋友的可参与性）

**输出：**
```json
{
  "experience": "带孩子环游世界",
  "best_timing": "现在（孩子 6-12 岁）",
  "window": "3 年",
  "reason": "孩子青春期后可能不愿同行",
  "action": "建议今年暑假启动"
}
```

### 4. 体验投资组合

优化年度体验投资组合。

**策略：**
- 70% 低成本高频体验（周末短途、学习新技能）
- 20% 中成本中频体验（年度旅行、工作坊）
- 10% 高成本低频体验（梦想清单、一生一次）

---

## 📊 输入参数

```json
{
  "age": {
    "type": "number",
    "required": true,
    "description": "当前年龄"
  },
  "health_score": {
    "type": "number",
    "required": true,
    "description": "健康状况自评（1-10）"
  },
  "annual_experience_budget": {
    "type": "number",
    "required": true,
    "description": "年度体验预算（元）"
  },
  "interests": {
    "type": "array",
    "required": false,
    "description": "兴趣领域列表"
  },
  "life_stage": {
    "type": "string",
    "required": false,
    "description": "人生阶段（单身/已婚/有孩/空巢/退休）"
  },
  "bucket_list": {
    "type": "array",
    "required": false,
    "description": "现有梦想清单"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "experience_plan": {
      "immediate": [],
      "short_term": [],
      "long_term": []
    },
    "memory_dividend_analysis": {},
    "timing_recommendations": [],
    "portfolio_allocation": {
      "low_cost": 0.7,
      "mid_cost": 0.2,
      "high_cost": 0.1
    }
  },
  "error": null
}
```

---

## 🧪 使用示例

### 示例 1：35 岁职场人士

```
@ant 帮我规划年度体验投资

信息：
- 年龄：35 岁
- 健康：8/10
- 年度体验预算：5 万元
- 兴趣：旅行、摄影、滑雪
- 人生阶段：已婚，孩子 5 岁
```

**预期输出：**
- 立即行动：带孩子暑假旅行（孩子还小，愿意同行）
- 短期（1-2 年）：滑雪进阶课程（体力要求高）
- 长期（3-5 年）：摄影展参观/工作坊

### 示例 2：55 岁临近退休

```
@ant 我 55 岁了，如何规划余生体验？

信息：
- 年龄：55 岁
- 健康：7/10
- 年度体验预算：10 万元
- 兴趣：历史、美食、慢旅行
- 人生阶段：空巢
```

**预期输出：**
- 识别"现在不做就晚了"的体验（体力要求高的）
- 规划"黄金 10 年"（55-65 岁）重点体验
- 建议健康投资（延长享受能力）

---

## ⚠️ 错误处理

| 错误码 | 含义 | 处理建议 |
|--------|------|----------|
| 400 | 参数缺失 | 检查必填字段（年龄、健康、预算） |
| 400 | 年龄无效 | 年龄应在 18-100 之间 |
| 400 | 预算不合理 | 预算应为正数，建议为年收入 10-30% |
| 500 | 内部错误 | 重试或联系开发者 |

---

## 📚 政策依据

**核心理论：**
- 《最优解人生》（Die With Zero）- Bill Perkins
- 生命周期假说（Life-Cycle Hypothesis）
- 回忆红利理论（Memory Dividend）

**关键概念：**
- 死前归零（Die With Zero）
- 生存阈值（Survival Threshold）
- 财富峰点（Peak Wealth Age）
- 人生分段（Life Segmentation）

---

## 🔗 相关文件

- `prompts/experience-interview.md` - 体验需求访谈提纲
- `templates/experience-plan.md` - 体验计划模板
- `calculators/memory-dividend.py` - 回忆红利计算器

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*投资体验，收获回忆红利。* 💡
