---
name: first-income
version: 1.0.0
description: 第一桶金 - 帮助用户找到赚钱机会，获得第一桶金
author: 燃冰 + 小蚂蚁
created: 2026-03-18
skill_type: 通用
---

# 第一桶金 💪

**基于《小狗钱钱》核心理念**

---

## 📋 功能描述

帮助用户（特别是青少年）发现赚钱机会，克服赚钱的心理障碍，获得人生第一桶金。

**适用场景：**
- 青少年财商实践
- 成年人副业探索
- 赚钱机会发现
- 克服"谈钱羞耻"

**边界条件：**
- 不提供违法/灰色建议
- 适合 10 岁以上人群
- 强调合法合规赚钱

---

## 🎯 核心功能

### 1. 赚钱机会发现

基于用户技能、兴趣、时间，推荐赚钱机会。

**输入：**
- 年龄
- 技能/兴趣
- 可用时间（小时/周）
- 地理位置（城市/农村）

**输出：**
```json
{
  "age_group": "青少年（10-18 岁）",
  "opportunities": [
    {
      "name": "遛狗服务",
      "category": "社区服务",
      "estimated_income": "50-100 元/次",
      "time_required": "1 小时/次",
      "skill_required": "喜欢动物，有责任心",
      "difficulty": "低",
      "start_steps": [
        "在小区张贴服务广告",
        "从邻居开始",
        "建立口碑"
      ]
    },
    {
      "name": "二手物品转卖",
      "category": "电商",
      "estimated_income": "100-500 元/月",
      "time_required": "5 小时/周",
      "skill_required": "拍照、描述、沟通",
      "difficulty": "中",
      "start_steps": [
        "整理家中闲置物品",
        "拍摄清晰照片",
        "在闲鱼/转转发布"
      ]
    }
  ]
}
```

### 2. 赚钱心理建设

帮助用户克服"谈钱羞耻"和心理障碍。

**常见障碍：**
- "谈钱很俗"
- "我还小，不适合赚钱"
- "我怕失败"
- "我不知道怎么开始"

**输出：**
```json
{
  "objection": "谈钱很俗",
  "reframe": "钱是中性的，关键是你用它做什么",
  "evidence": [
    "钱可以让你帮助家人",
    "钱可以实现你的梦想",
    "钱可以让你更有选择权"
  ],
  "action": "告诉自己：我值得赚钱，我有价值"
}
```

### 3. 72 小时行动法则

推动用户在 72 小时内开始行动。

**原理：**
- 超过 72 小时，行动概率大幅下降
- 立即行动比完美计划更重要

**输出：**
```json
{
  "idea": "遛狗服务",
  "deadline": "2026-03-21 12:00",
  "action_steps": [
    {
      "step": 1,
      "action": "打印服务广告",
      "deadline": "今天 18:00 前"
    },
    {
      "step": 2,
      "action": "在小区张贴",
      "deadline": "明天 12:00 前"
    },
    {
      "step": 3,
      "action": "等待第一个客户",
      "deadline": "后天 18:00 前"
    }
  ],
  "commitment": "我承诺在 72 小时内完成第一步"
}
```

### 4. 第一桶金规划

规划从 0 到第一桶金的路径。

**第一桶金定义：**
- 青少年：1000-5000 元
- 成年人：5 万 -20 万

**输出：**
```json
{
  "target": "第一桶金 5000 元",
  "current": 0,
  "remaining": 5000,
  "income_sources": [
    {
      "source": "遛狗服务",
      "estimated_monthly": 500,
      "months_to_target": 10
    },
    {
      "source": "二手转卖",
      "estimated_monthly": 300,
      "months_to_target": 17
    }
  ],
  "accelerated_path": {
    "combined_monthly": 800,
    "months_to_target": 6,
    "tip": "多个收入来源并行，加速达成"
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
  "skills": {
    "type": "array",
    "required": false,
    "description": "技能/兴趣列表"
  },
  "available_hours": {
    "type": "number",
    "required": false,
    "description": "每周可用时间（小时）"
  },
  "location": {
    "type": "string",
    "required": false,
    "description": "地理位置（城市/农村）"
  },
  "target_amount": {
    "type": "number",
    "required": false,
    "description": "目标金额"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "opportunities": [],
    "mindset_coaching": {},
    "action_plan": {},
    "first_gold_path": {}
  },
  "error": null
}
```

---

## 🧪 使用示例

### 示例 1：12 岁小学生

```
@ant 我想赚零花钱，有什么建议？

信息：
- 年龄：12 岁
- 技能：喜欢动物、会拍照
- 时间：周末 5 小时
- 地点：城市小区
```

**预期输出：**
- 遛狗服务（50-100 元/次）
- 二手物品转卖（100-500 元/月）
- 72 小时行动计划

### 示例 2：25 岁职场新人

```
@ant 我想发展副业，有什么建议？

信息：
- 年龄：25 岁
- 技能：写作、设计、编程
- 时间：工作日晚上 + 周末 15 小时
- 目标：月入 5000 元
```

**预期输出：**
- 自由职业（写作/设计/编程）
- 知识付费（课程/咨询）
- 内容创作（公众号/视频）
- 6 个月达成路径

---

## ⚠️ 错误处理

| 错误码 | 含义 | 处理建议 |
|--------|------|----------|
| 400 | 参数缺失 | 检查必填字段（年龄） |
| 400 | 年龄过小 | 10 岁以下需要家长陪同 |
| 400 | 目标不合理 | 目标金额应为正数 |
| 500 | 内部错误 | 重试或联系开发者 |

---

## 📚 政策依据

**核心理论：**
- 《小狗钱钱》- 博多·舍费尔
- 72 小时法则
- 多元收入理论

**关键概念：**
- 72 小时法则：决定做的事，72 小时内开始
- 收入多元化：不依赖单一收入来源
- 赚钱不羞耻：钱是中性的

---

## 🔗 相关文件

- `templates/opportunity-list.md` - 赚钱机会清单
- `templates/72h-action-plan.md` - 72 小时行动计划
- `templates/first-gold-tracker.md` - 第一桶金追踪表

## 💡 使用建议

**发现赚钱机会：**
1. 填写 opportunity-list.md
2. 盘点技能/兴趣/资源
3. 选定 1 个机会

**72 小时行动：**
1. 打印 72h-action-plan.md
2. 设定 3 天目标
3. 严格执行，完成后打勾

**追踪进度：**
1. 每月更新 first-gold-tracker.md
2. 庆祝每个里程碑

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*72 小时内行动，获得第一桶金。* 💪
