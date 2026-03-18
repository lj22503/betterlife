---
name: life-segmentation-designer
version: 1.0.0
description: 人生分段设计师 - 帮助用户将人生分为不同季节，分配体验
author: 燃冰 + 小蚂蚁
created: 2026-03-18
skill_type: 通用
---

# 人生分段设计师 📅

**基于《最优解人生》（Die With Zero）核心理念**

---

## 📋 功能描述

帮助用户将人生视为不同季节，将体验清单分配到合适的人生阶段，避免"错过当季"的遗憾。

**适用场景：**
- 规划未来 30 年人生体验
- 识别"现在不做就晚了"的体验
- 协调家庭共同体验时机
- 避免体验冲突和资源浪费

**边界条件：**
- 不提供医疗/法律建议
- 基于用户输入，非预测未来
- 聚焦体验分配，非财务规划

---

## 🎯 核心功能

### 1. 人生季节划分

将人生划分为不同季节，每季有独特主题。

**标准分段：**
- 探索季（20-35 岁）：尝试、学习、冒险
- 积累季（35-50 岁）：事业、家庭、资产
- 收获季（50-65 岁）：成就、传承、深度体验
- 享受季（65-80 岁）：休闲、健康、回忆
- 沉淀季（80 岁+）：智慧、传承、平静

**输出：**
```json
{
  "current_season": "积累季",
  "current_age": 42,
  "season_theme": "事业、家庭、资产",
  "years_remaining_in_season": 8,
  "next_season": "收获季",
  "next_season_prep": "开始规划深度体验清单"
}
```

### 2. 体验分配到季节

将体验清单分配到最合适的人生季节。

**分配原则：**
- 体力要求高的 → 早期（探索季、积累季）
- 认知要求高的 → 中期（积累季、收获季）
- 休闲放松的 → 后期（享受季、沉淀季）
- 家庭共同的 → 考虑家人生命周期

**输出：**
```json
{
  "experience": "攀登珠峰",
  "optimal_season": "探索季（20-35 岁）",
  "reason": "体力要求极高，年龄增长后风险显著增加",
  "urgency": "高",
  "alternative": "如错过，可考虑低海拔登山"
}
```

### 3. 家庭体验同步

协调家庭成员的生命周期，找到共同体验的最佳时机。

**考虑因素：**
- 孩子年龄（太小/太大都不合适）
- 父母健康（趁还能同行）
- 配偶时间（假期协调）

**输出：**
```json
{
  "experience": "全家环游世界",
  "optimal_timing": "现在（孩子 6-12 岁）",
  "window": "3-5 年",
  "reason": "孩子青春期后可能不愿同行，父母还能长途旅行",
  "action": "建议 3 年内启动"
}
```

### 4. 冲突检测与优化

识别体验之间的冲突，提供优化建议。

**冲突类型：**
- 时间冲突（同一时期过多体验）
- 资源冲突（预算不足）
- 身体冲突（体力/健康不允许）

**输出：**
```json
{
  "conflicts": [
    {
      "type": "时间冲突",
      "experiences": ["MBA 学习", "创业"],
      "resolution": "建议先创业，工作后再读 MBA"
    }
  ],
  "optimization_suggestions": [
    "将高体力体验集中在 45 岁前",
    "将家庭体验安排在孩子 6-15 岁期间"
  ]
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
  "life_expectancy": {
    "type": "number",
    "required": false,
    "description": "预期寿命（默认 85）"
  },
  "experience_list": {
    "type": "array",
    "required": true,
    "description": "体验清单"
  },
  "family_members": {
    "type": "array",
    "required": false,
    "description": "家庭成员信息（年龄、健康状况）"
  },
  "health_constraints": {
    "type": "array",
    "required": false,
    "description": "健康限制（影响体验选择）"
  },
  "budget_constraints": {
    "type": "object",
    "required": false,
    "description": "预算限制"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "life_seasons": {},
    "experience_allocation": {},
    "family_synchronization": {},
    "conflict_detection": {},
    "optimization_suggestions": [],
    "action_items": []
  },
  "error": null
}
```

---

## 🧪 使用示例

### 示例 1：35 岁新手父母

```
@ant 帮我规划未来 30 年人生体验

信息：
- 年龄：35 岁
- 家庭成员：配偶（33 岁）、孩子（2 岁）
- 体验清单：
  - 带孩子环游世界
  - 创业
  - 读 MBA
  - 攀登乞力马扎罗
  - 写一本书
  - 学习潜水
```

**预期输出：**
- 探索季（35-40 岁）：潜水、创业
- 积累季（40-50 岁）：MBA、写书
- 收获季（50-65 岁）：乞力马扎罗（体力要求高，趁身体好）
- 家庭同步：孩子 6-12 岁期间环游世界（2030-2036）

### 示例 2：55 岁空巢家庭

```
@ant 我们 55 岁了，如何规划余生？

信息：
- 年龄：55 岁（配偶 53 岁）
- 家庭成员：孩子已独立
- 体验清单：
  - 欧洲深度游
  - 学习钢琴
  - 做慈善
  - 写回忆录
  - 带孙子旅行
```

**预期输出：**
- 收获季（55-65 岁）：欧洲深度游、学习钢琴、写回忆录
- 享受季（65-80 岁）：带孙子旅行、做慈善
- 建议：趁身体好，优先安排长途旅行

---

## ⚠️ 错误处理

| 错误码 | 含义 | 处理建议 |
|--------|------|----------|
| 400 | 参数缺失 | 检查必填字段（年龄、体验清单） |
| 400 | 年龄无效 | 年龄应在 18-120 之间 |
| 400 | 体验清单为空 | 至少提供一个体验 |
| 500 | 内部错误 | 重试或联系开发者 |

---

## 📚 政策依据

**核心理论：**
- 《最优解人生》（Die With Zero）- Bill Perkins
- 人生发展阶段理论（Erikson）
- 家庭生命周期理论

**关键概念：**
- 人生季节（Life Seasons）
- 体验当季（Optimal Timing）
- 家庭同步（Family Synchronization）
- 错过成本（Missed Opportunity Cost）

---

## 🔗 相关文件

- `templates/life-season-map.md` - 人生季节地图模板
- `templates/experience-timeline.md` - 体验时间线模板
- `calculators/timing-optimizer.py` - 时机优化器

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*将人生视为季节，每季都有当季体验。* 📅
