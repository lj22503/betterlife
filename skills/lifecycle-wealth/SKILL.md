---
name: lifecycle-wealth
version: 1.0.0
description: 人生财富轨迹规划器 - 基于康波理论规划一生财富
author: 燃冰 + 小蚂蚁
created: 2026-03-18
skill_type: 通用
---

# 人生财富轨迹规划器 💰

**基于周金涛《涛动周期论》核心理念**

---

## 📋 功能描述

基于康德拉季耶夫周期理论，规划个人一生财富轨迹，识别 3 次财富机会，实现财富阶层跃迁。

**适用场景：**
- 人生财富规划
- 财富机会识别
- 资产配置策略
- 长期投资决策

**边界条件：**
- 不提供具体投资建议
- 基于历史规律，非精确预测
- 适合 18 岁以上人群

---

## 🎯 核心功能

### 1. 人生财富机会识别

识别个人一生的 3 次财富机会。

**核心观点：**
- 人生财富机会只有 3 次
- 每次机会间隔约 10 年
- 抓住 1 次即可成为中产阶级
- 3 次都抓住可成为富人

**输出：**
```json
{
  "birth_year": 1990,
  "current_age": 36,
  "wealth_opportunities": [
    {
      "opportunity": 1,
      "year": 2019,
      "age": 29,
      "kondratieff_phase": "萧条期起点",
      "optimal_assets": ["现金", "黄金"],
      "status": "已过去",
      "caught": false,
      "description": "2019 年萧条期低点，现金为王"
    },
    {
      "opportunity": 2,
      "year": 2029,
      "age": 39,
      "kondratieff_phase": "回升期起点",
      "optimal_assets": ["股票", "大宗商品"],
      "status": "未来（5 年后）",
      "caught": null,
      "description": "2029 年康波回升期，布局风险资产",
      "preparation": "现在积累现金，等待机会"
    },
    {
      "opportunity": 3,
      "year": 2039,
      "age": 49,
      "kondratieff_phase": "繁荣期",
      "optimal_assets": ["大宗商品", "股票"],
      "status": "未来（15 年后）",
      "caught": null,
      "description": "2039 年康波繁荣期，风险资产大牛市"
    }
  ],
  "caught_count": 0,
  "wealth_trajectory": "如抓住 2/3 次机会，可达高净值",
  "recommendation": "准备迎接 2029 年第二次机会"
}
```

### 2. 人生财富轨迹模拟

模拟不同情景下的财富轨迹。

**情景：**
- 悲观：3 次机会都没抓住
- 中性：抓住 1 次机会
- 乐观：抓住 2-3 次机会

**输出：**
```json
{
  "scenarios": {
    "pessimistic": {
      "caught": 0,
      "wealth_level": "温饱",
      "net_worth_at_60": "100 万",
      "description": "3 次机会都没抓住，靠工资生活"
    },
    "neutral": {
      "caught": 1,
      "wealth_level": "中产",
      "net_worth_at_60": "1000 万",
      "description": "抓住 1 次机会，成为中产阶级"
    },
    "optimistic": {
      "caught": 2,
      "wealth_level": "高净值",
      "net_worth_at_60": "5000 万+",
      "description": "抓住 2 次机会，实现财富自由"
    }
  },
  "key_insight": "人生财富不是靠工资，而是靠对资产价格的投资"
}
```

### 3. 财富机会准备策略

为下一次财富机会做准备。

**准备策略：**
- 现金积累（保持流动性）
- 能力提升（识别机会的能力）
- 人脉积累（获取信息的渠道）
- 心理准备（敢于下注的勇气）

**输出：**
```json
{
  "next_opportunity": {
    "year": 2029,
    "age": 39,
    "years_to_prepare": 3,
    "asset_class": "股票/大宗商品"
  },
  "preparation_plan": {
    "financial": {
      "goal": "积累 100 万现金",
      "current": 300000,
      "monthly_saving": 20000,
      "on_track": true
    },
    "skill": {
      "goal": "学习投资知识",
      "actions": [
        "学习康波周期理论",
        "研究历史资产价格",
        "实践小规模投资"
      ]
    },
    "network": {
      "goal": "建立投资圈人脉",
      "actions": [
        "参加投资社群",
        "关注优质投资者",
        "交流投资心得"
      ]
    },
    "mindset": {
      "goal": "培养赌博勇气",
      "insight": "任何机会都是赌博，没有完全确定的机会"
    }
  }
}
```

### 4. 人生财富复盘

复盘已过去的财富机会，总结经验。

**复盘维度：**
- 当时是否识别到机会
- 为什么没有抓住（或抓住了）
- 从中学到什么

**输出：**
```json
{
  "review_opportunity": {
    "opportunity": 1,
    "year": 2019,
    "age": 29,
    "market_condition": "康波萧条期低点",
    "optimal_action": "买入核心资产",
    "actual_action": "持有现金/买入房产",
    "result": "部分正确/错误",
    "lesson": "当时不理解康波理论，错失良机"
  },
  "improvement": {
    "knowledge_gap": "缺乏周期理论知识",
    "mindset_gap": "不敢在低点下注",
    "action_gap": "没有及时行动",
    "next_time": "2029 年机会来临时，敢于下注"
  }
}
```

---

## 📊 输入参数

```json
{
  "birth_year": {
    "type": "number",
    "required": true,
    "description": "出生年份"
  },
  "current_age": {
    "type": "number",
    "required": false,
    "description": "当前年龄"
  },
  "current_net_worth": {
    "type": "number",
    "required": false,
    "description": "当前净资产（元）"
  },
  "annual_income": {
    "type": "number",
    "required": false,
    "description": "年收入（元）"
  },
  "investment_experience": {
    "type": "string",
    "required": false,
    "description": "投资经验（新手/有经验/资深）"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "wealth_opportunities": [],
    "wealth_trajectory_simulation": {},
    "preparation_strategy": {},
    "past_opportunity_review": {},
    "action_items": []
  },
  "error": null
}
```

---

## 🧪 使用示例

### 示例 1：1990 年出生

```
@ant 我 1990 年出生，人生财富机会在哪？
```

**预期输出：**
- 第一次机会：2019 年（29 岁）- 已过去
- 第二次机会：2029 年（39 岁）- 准备中
- 第三次机会：2039 年（49 岁）- 未来
- 建议：积累现金 + 学习，等待 2029 年机会

### 示例 2：1980 年出生

```
@ant 我 1980 年出生，45 岁了，还有机会吗？
```

**预期输出：**
- 第一次机会：2009 年（29 岁）- 已过去
- 第二次机会：2019 年（39 岁）- 已过去
- 第三次机会：2029 年（49 岁）- 未来（3 年后）
- 建议：准备迎接最后一次机会

### 示例 3：财富复盘

```
@ant 我 2019 年没买房，是不是错过了机会？
```

**预期输出：**
- 2019 年机会：现金为王（非房产）
- 真正机会：2015 年之前买房
- 2019 年正确策略：持有现金，等待 2029 年
- 建议：不要后悔，准备下一次机会

---

## ⚠️ 错误处理

| 错误码 | 含义 | 处理建议 |
|--------|------|----------|
| 400 | 参数缺失 | 检查必填字段（出生年份） |
| 400 | 年龄无效 | 年龄应在 18-100 之间 |
| 400 | 投资经验无效 | 应为新手/有经验/资深 |
| 500 | 内部错误 | 重试或联系开发者 |

---

## 📚 政策依据

**核心理论：**
- 《涛动周期论》- 周金涛
- 康德拉季耶夫周期（Kondratieff Wave）
- 人生财富机会理论（3 次/生）

**关键概念：**
- 人生财富机会：3 次/生
- 机会间隔：约 10 年
- 抓住 1 次：中产阶级
- 抓住 2-3 次：富人
- 人生财富不是靠工资，而是靠资产价格投资

---

## 🔗 相关文件

- `calculators/wealth-opportunity.py` - 财富机会计算器
- `calculators/wealth-trajectory.py` - 财富轨迹模拟器
- `templates/opportunity-review.md` - 机会复盘模板

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*人生就是一场康波，3 次机会决定财富命运。* 💰
