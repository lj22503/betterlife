---
name: insurance-comparator
version: 1.0.0
description: 保险产品对比工具 - 多维度对比保险产品，选择最优方案
author: 燃冰 + 小蚂蚁
created: 2026-03-18
skill_type: 通用
---

# 保险产品对比工具 🔍

**基于《你的保险指南》核心理念**

---

## 📋 功能描述

帮助用户多维度对比保险产品，识别关键差异，选择最适合的保障方案。

**适用场景：**
- 保险产品对比
- 保障责任分析
- 性价比评估
- 投保决策辅助

**边界条件：**
- 不提供具体产品推荐
- 不替代专业建议
- 适合 18 岁以上人群

---

## 🎯 核心功能

### 1. 重疾险对比维度

从多个维度对比重疾险产品。

**对比维度：**
- 保障责任：赔付次数、分组/不分组、赔付额度
- 保险公司服务：绿色通道等增值服务
- 轻症种类：高发轻症覆盖数量
- 缴费方式和价格

**输出：**
```json
{
  "comparison_dimensions": {
    "coverage_responsibility": {
      "payout_times": "1 次/多次",
      "grouping": "分组/不分组",
      "coverage_amount": "100%/120%/150%"
    },
    "insurance_company_service": {
      "green_channel": "有/无",
      "second_opinion": "有/无",
      "claim_service": "线上/线下"
    },
    "light_illness_coverage": {
      "total_types": 50,
      "high_incidence_count": 8,
      "coverage_ratio": "30%保额"
    },
    "payment_and_price": {
      "payment_period": "20 年/30 年",
      "annual_premium": 20000,
      "cost_effectiveness": "高/中/低"
    }
  }
}
```

### 2. 高发轻症核对

核对产品是否覆盖高发轻症。

**8 种高发轻症：**
1. 极早期恶性肿瘤或者恶性病变
2. 轻微脑中风
3. 不典型急性心肌梗死
4. 冠状动脉介入手术
5. 视力严重受损
6. 较小面积Ⅲ度烧伤
7. 主动脉手术
8. 脑垂体瘤、脑囊肿、脑动脉瘤及脑血管瘤

**输出：**
```json
{
  "high_incidence_light_illness": {
    "total_count": 8,
    "covered_count": 7,
    "missing": ["视力严重受损"],
    "coverage_rate": 0.875,
    "insight": "该产品缺少 1 种高发轻症（视力严重受损），需注意"
  }
}
```

### 3. 产品优缺点分析

分析产品的优缺点。

**输出：**
```json
{
  "product_analysis": {
    "product_name": "XX 重疾险",
    "pros": [
      "不分组多次赔付",
      "覆盖全部 8 种高发轻症",
      "含投保人豁免",
      "保费合理"
    ],
    "cons": [
      "不含中症责任",
      "等待期 180 天（较长）",
      "保险公司网点较少"
    ],
    "suitable_for": [
      "追求全面保障的人群",
      "关注多次赔付的人群",
      "预算中等的人群"
    ],
    "not_suitable_for": [
      "追求极致性价比的人群",
      "已有中症保障的人群"
    ]
  }
}
```

### 4. 投保渠道对比

对比不同投保渠道的优劣。

**渠道类型：**
- 经纪人：产品线广，但单家公司服务深度有限
- 代理人：单家公司，服务更到位
- 互联网自助：价格透明，但需自行研究

**输出：**
```json
{
  "channel_comparison": {
    "broker": {
      "product_range": "广（对接多家保险公司）",
      "service_depth": "中（单家公司深度有限）",
      "price": "有折扣",
      "suitable_for": "想对比多家产品的人群"
    },
    "agent": {
      "product_range": "窄（单家公司）",
      "service_depth": "深（售后服务到位）",
      "price": "标准价",
      "suitable_for": "看重服务的人群"
    },
    "online": {
      "product_range": "中（网红产品）",
      "service_depth": "浅（自助为主）",
      "price": "最优惠",
      "suitable_for": "懂保险、追求性价比的人群"
    }
  },
  "recommendation": "根据需求选择：对比选经纪人，服务选代理人，性价比选互联网"
}
```

---

## 📊 输入参数

```json
{
  "insurance_type": {
    "type": "string",
    "required": true,
    "description": "保险类型（重疾/医疗/意外/寿险）"
  },
  "products": {
    "type": "array",
    "required": true,
    "description": "待对比产品列表"
  },
  "budget": {
    "type": "number",
    "required": false,
    "description": "预算范围"
  },
  "priority": {
    "type": "string",
    "required": false,
    "description": "优先考虑（保障/价格/服务）"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "comparison_dimensions": {},
    "light_illness_check": {},
    "product_analysis": {},
    "channel_comparison": {},
    "recommendation": "",
    "action_items": []
  },
  "error": null
}
```

---

## 📚 政策依据

**核心理论：**
- 《你的保险指南》- 健康管理角度规划保险
- 保险产品对比方法
- 投保渠道选择

**关键概念：**
- 重疾险对比 4 维度
- 8 种高发轻症核对
- 经纪人 vs 代理人 vs 互联网

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*多维度对比，选择最适合的产品。* 🔍
