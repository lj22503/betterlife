---
name: real-estate-cycle
version: 1.0.0
description: 房地产周期定位器 - 识别房地产周期位置，把握买房时机
author: 燃冰 + 小蚂蚁
created: 2026-03-18
skill_type: 通用
---

# 房地产周期定位器 🏠

**基于周金涛《涛动周期论》核心理念**

---

## 📋 功能描述

帮助用户识别房地产周期位置（20 年轮回），把握买房时机，优化房产资产配置。

**适用场景：**
- 首次购房规划
- 改善性购房决策
- 房产投资时机
- 房地产周期研究

**边界条件：**
- 不提供具体房产建议
- 基于历史规律，非精确预测
- 适合 20 岁以上人群

---

## 🎯 核心功能

### 1. 房地产周期定位

识别当前房地产周期位置。

**房地产周期：** 20 年轮回一次

**周期阶段：**
- 启动期（3-5 年）：价格底部，适合买入
- 上升期（5-7 年）：价格快速上涨
- 见顶期（2-3 年）：价格高位，谨慎
- 调整期（5-7 年）：价格回调，观望

**输出：**
```json
{
  "current_cycle": 4,
  "cycle_period": "2008-2028",
  "current_phase": "调整期",
  "phase_period": "2021-2028",
  "next_cycle_start": 2028,
  "next_phase": "启动期",
  "insight": "当前处于房地产调整期，2028 年后进入下一轮周期"
}
```

### 2. 人生买房时机规划

规划人生两次买房时机。

**核心观点：**
- 人生买房 2 次：首次置业（27 岁）+ 改善置业（42 岁）
- 消费高峰：46 岁
- 46 岁后消费下降，转向医疗养老

**输出：**
```json
{
  "current_age": 30,
  "buying_opportunities": [
    {
      "type": "首次置业",
      "optimal_age": 27,
      "optimal_year": 2023,
      "status": "已过去",
      "recommendation": "如未买，可在调整期低点买入"
    },
    {
      "type": "改善置业",
      "optimal_age": 42,
      "optimal_year": 2035,
      "status": "未来",
      "recommendation": "等待下一轮周期启动（2028-2030）"
    }
  ],
  "consumption_peak": {
    "age": 46,
    "year": 2039,
    "insight": "46 岁后消费下降，房产不再是核心需求"
  }
}
```

### 3. 买房时机评估

评估当前是否适合买房。

**评估维度：**
- 房地产周期位置
- 个人年龄/需求
- 财务状况
- 城市等级

**输出：**
```json
{
  "market_timing": {
    "cycle_phase": "调整期",
    "price_trend": "回调",
    "recommendation": "观望或选择性买入"
  },
  "personal_readiness": {
    "age": 30,
    "need": "首次置业",
    "financial_status": "稳定",
    "readiness": "高"
  },
  "location_strategy": {
    "tier1_core": "可买入（抗跌）",
    "tier1_non_core": "观望",
    "tier2": "谨慎",
    "tier3_4": "避免"
  },
  "overall_advice": "一线城市核心区域可考虑，非核心区域观望"
}
```

### 4. 房地产周期与康波嵌套

分析房地产周期与康波的关系。

**嵌套关系：**
- 60 年康波 = 3 个房地产周期（20 年×3）
- 康波萧条期的房地产周期相对较弱

**输出：**
```json
{
  "kondratieff_phase": "萧条期",
  "real_estate_cycle_phase": "调整期",
  "cycle_interaction": "双周期调整叠加",
  "implication": "本轮房地产周期相对较弱，不宜高杠杆",
  "strategy": "核心区域保值，非核心区域减仓"
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
  "birth_year": {
    "type": "number",
    "required": false,
    "description": "出生年份"
  },
  "homeownership_status": {
    "type": "string",
    "required": false,
    "description": "房产状况（无房/一套/多套）"
  },
  "city_tier": {
    "type": "string",
    "required": false,
    "description": "城市等级（一线/二线/三线/四线）"
  },
  "financial_status": {
    "type": "string",
    "required": false,
    "description": "财务状况（紧张/稳定/宽裕）"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "real_estate_cycle_position": {},
    "buying_opportunities": [],
    "timing_assessment": {},
    "kondratieff_interaction": {},
    "action_items": []
  },
  "error": null
}
```

---

## 🧪 使用示例

### 示例 1：30 岁首次购房

```
@ant 我 30 岁，现在适合买房吗？

信息：
- 年龄：30 岁
- 房产状况：无房
- 城市：上海
- 财务：稳定
```

**预期输出：**
- 房地产周期：调整期（2021-2028）
- 首次置业时机：27 岁（已过去），现在仍可考虑
- 建议：上海核心区域可买入，非核心观望

### 示例 2：45 岁改善购房

```
@ant 我 45 岁，想改善住房，合适吗？

信息：
- 年龄：45 岁
- 房产状况：一套（老破小）
- 城市：北京
- 财务：宽裕
```

**预期输出：**
- 改善置业时机：42 岁（稍过），但仍在窗口期
- 消费高峰：46 岁（明年）
- 建议：可考虑改善，但避免高杠杆

### 示例 3：投资购房咨询

```
@ant 现在适合投资房产吗？
```

**预期输出：**
- 房地产周期：调整期
- 康波周期：萧条期
- 建议：投资属性减弱，核心区域保值为主

---

## ⚠️ 错误处理

| 错误码 | 含义 | 处理建议 |
|--------|------|----------|
| 400 | 参数缺失 | 检查必填字段（年龄） |
| 400 | 年龄无效 | 年龄应在 20-80 之间 |
| 400 | 城市等级无效 | 应为一二三四线 |
| 500 | 内部错误 | 重试或联系开发者 |

---

## 📚 政策依据

**核心理论：**
- 《涛动周期论》- 周金涛
- 房地产周期理论（20 年轮回）
- 康波周期嵌套理论

**关键概念：**
- 房地产周期：20 年轮回
- 人生买房 2 次：27 岁首次 +42 岁改善
- 消费高峰：46 岁
- 康波萧条期房地产周期相对较弱

---

## 🔗 相关文件

- `calculators/real-estate-cycle.py` - 房地产周期计算器
- `calculators/buying-timing.py` - 买房时机计算器
- `templates/buying-strategy.md` - 买房策略模板

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*人生两次房，把握周期是关键。* 🏠
