---
name: asset-allocation
version: 1.0.0
description: 大类资产配置器 - 基于经济周期的大类资产配置建议
author: 燃冰 + 小蚂蚁
created: 2026-03-18
skill_type: 通用
---

# 大类资产配置器 📊

**基于周金涛《涛动周期论》核心理念**

---

## 📋 功能描述

基于经济周期（康波 + 房地产 + 库存）定位，提供大类资产配置建议，优化投资组合。

**适用场景：**
- 个人资产配置
- 投资组合优化
- 经济周期研究
- 长期财富规划

**边界条件：**
- 不提供具体投资建议
- 基于历史规律，非精确预测
- 适合 18 岁以上人群

---

## 🎯 核心功能

### 1. 美林投资时钟改良

基于中国实际情况改良美林投资时钟。

**核心逻辑：**
- 经济周期 → 资产配置
- 增长 + 通胀 → 四象限配置

**四象限：**
- 复苏期（增长↑通胀↓）：股票 > 债券
- 过热期（增长↑通胀↑）：大宗商品 > 股票
- 滞胀期（增长↓通胀↑）：现金 > 大宗商品
- 衰退期（增长↓通胀↓）：债券 > 现金

**输出：**
```json
{
  "economic_phase": "衰退期",
  "growth_trend": "下降",
  "inflation_trend": "下降",
  "asset_ranking": ["债券", "现金", "股票", "大宗商品"],
  "optimal_allocation": {
    "bonds": 0.4,
    "cash": 0.3,
    "stocks": 0.2,
    "commodities": 0.1
  },
  "insight": "衰退期债券最优，保持充足现金"
}
```

### 2. 康波周期资产配置

基于康波周期阶段的资产配置策略。

**各阶段配置：**

| 康波阶段 | 最优资产 | 次优 | 避免 |
|---------|---------|------|------|
| 回升期 | 股票 | 房地产 | 大宗商品 |
| 繁荣期 | 大宗商品 | 股票 | 现金 |
| 衰退期 | 现金 | 黄金 | 股票 |
| 萧条期 | 现金 + 黄金 | 债券 | 大宗商品 |

**输出：**
```json
{
  "kondratieff_phase": "萧条期",
  "phase_period": "2018-2030",
  "optimal_assets": ["现金", "黄金"],
  "sub_optimal": ["债券"],
  "avoid": ["大宗商品", "高杠杆资产"],
  "allocation": {
    "cash": 0.4,
    "gold": 0.3,
    "bonds": 0.2,
    "stocks": 0.1
  },
  "key_insight": "萧条期现金为王，黄金保值"
}
```

### 3. 房地产周期资产配置

基于房地产周期的资产配置策略。

**规律：**
- 房地产上升期：房地产 > 股票 > 债券
- 房地产调整期：债券 > 现金 > 房地产

**输出：**
```json
{
  "real_estate_phase": "调整期",
  "phase_period": "2021-2028",
  "real_estate_strategy": "核心区域保值，非核心减仓",
  "related_assets": {
    "stocks": "低配（房地产产业链）",
    "bonds": "高配（利率下行）",
    "commodities": "低配（需求疲软）"
  },
  "recommendation": "降低房地产相关资产配置"
}
```

### 4. 三周期共振配置

综合康波 + 房地产 + 库存三周期，制定共振配置策略。

**共振逻辑：**
- 三周期同向 → 强信号
- 三周期反向 → 谨慎/均衡

**输出：**
```json
{
  "kondratieff": "萧条期（防守）",
  "real_estate": "调整期（防守）",
  "inventory": "去库存（防守）",
  "resonance": "三周期叠加调整",
  "signal_strength": "强（防守信号）",
  "strategy": "全面防守，现金 + 黄金为主",
  "allocation": {
    "cash": 0.4,
    "gold": 0.3,
    "bonds": 0.25,
    "stocks": 0.05,
    "real_estate": 0.0,
    "commodities": 0.0
  },
  "reversal_watch": [
    "PPI 同比转正",
    "房地产销量企稳",
    "工业企业利润回升"
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
  "total_assets": {
    "type": "number",
    "required": false,
    "description": "总资产（元）"
  },
  "risk_tolerance": {
    "type": "string",
    "required": false,
    "description": "风险承受能力（低/中/高）"
  },
  "investment_horizon": {
    "type": "string",
    "required": false,
    "description": "投资期限（短期/中期/长期）"
  },
  "current_allocation": {
    "type": "object",
    "required": false,
    "description": "当前资产配置"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "economic_phase": {},
    "kondratieff_allocation": {},
    "real_estate_allocation": {},
    "three_cycle_resonance": {},
    "optimal_allocation": {},
    "rebalancing_suggestions": [],
    "action_items": []
  },
  "error": null
}
```

---

## 🧪 使用示例

### 示例 1：当前资产配置

```
@ant 现在是 2026 年，如何配置资产？

信息：
- 年龄：35 岁
- 总资产：500 万
- 风险承受：中
- 投资期限：长期
```

**预期输出：**
- 康波：萧条期 → 现金 + 黄金为主
- 房地产：调整期 → 降低房产配置
- 库存：去库存 → 债券优
- 建议：40% 现金 +30% 黄金 +25% 债券 +5% 股票

### 示例 2：资产再平衡

```
@ant 我当前资产配置：60% 房产 +30% 股票 +10% 现金，需要调整吗？
```

**预期输出：**
- 当前配置：房产过高（60%）
- 风险：房地产调整期，非核心区域可能下跌
- 建议：减持非核心房产，增加现金 + 黄金 + 债券

### 示例 3：反转信号监控

```
@ant 什么时候可以加仓股票？
```

**预期输出：**
- 当前：去库存期，股票熊市
- 反转信号：PPI 同比转正、工业企业利润回升
- 时间：预计 2026 年底 -2027 年初
- 策略：现在定投，反转信号出现后加仓

---

## ⚠️ 错误处理

| 错误码 | 含义 | 处理建议 |
|--------|------|----------|
| 400 | 参数缺失 | 检查必填字段（年龄） |
| 400 | 年龄无效 | 年龄应在 18-100 之间 |
| 400 | 风险承受无效 | 应为低/中/高 |
| 500 | 内部错误 | 重试或联系开发者 |

---

## 📚 政策依据

**核心理论：**
- 《涛动周期论》- 周金涛
- 美林投资时钟（改良版）
- 康波周期理论
- 三周期嵌套理论

**关键概念：**
- 美林投资时钟：复苏/过热/滞胀/衰退
- 康波配置：回升股票/繁荣商品/衰退现金/萧条现金 + 黄金
- 三周期共振：康波 + 房地产 + 库存
- 萧条期最佳配置：现金 + 黄金

---

## 🔗 相关文件

- `calculators/melin-clock.py` - 美林时钟计算器
- `calculators/three-cycle-resonance.py` - 三周期共振计算器
- `templates/asset-allocation.md` - 资产配置模板

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*周期决定配置，配置决定财富。* 📊
