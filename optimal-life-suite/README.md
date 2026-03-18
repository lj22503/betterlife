# 最优解人生 Skill 套件

**基于《最优解人生》（Die With Zero）核心理念**

---

## 📦 套件概览

这套 skill 帮助人们从"积累财富"转向"投资体验"，最大化人生充实感。

| Skill | 用途 | 级别 | 状态 |
|------|------|------|------|
| `life-experience-investor` | 人生体验投资顾问 | 通用🟡 | ✅ v1.0.0 |
| `death-with-zero-planner` | 死前归零规划师 | 通用🟡 | ✅ v1.0.0 |
| `peak-wealth-calculator` | 财富峰点计算器 | 通用🟡 | ✅ v1.0.0 |
| `life-segmentation-designer` | 人生分段设计师 | 通用🟡 | ✅ v1.0.0 |
| `experience-memory-tracker` | 体验记忆追踪器 | 内部🟢 | ✅ v1.0.0 |

---

## 🎯 核心理念

### 准则 1：正面人生体验最大化
- 相比于花钱买物品，将钱花在体验上能让我们更加快乐
- 体验会随着时间增值（回忆红利）

### 准则 2：提早开始投资体验
- 现在就开始，不要等
- 体验需要时间和金钱，但当下就能获得愉悦

### 准则 3：以死前归零为目标
- 要在你的人生历程中钱尽其用
- 身逝之日，财富用尽

### 准则 4：利用所有可用的工具
- 精算师寿命计算器
- 年金保险
- 凶猛花在喜欢的体验上

### 准则 5：在钱能发挥最大作用时交给子女
- 子女 26-35 岁是最佳接收年龄
- 生前赠与优于遗产继承

### 准则 6：平衡人生
- 50-30-20 法则的变体
- 最佳平衡因人而异，随年龄变化

### 准则 7：将人生视作不同季节
- 探索季、积累季、收获季、享受季、沉淀季
- 每季都有当季体验

### 准则 8：知道什么时候停止财富增长
- 最佳净资产峰点：45-60 岁
- 过了峰点后，应增加体验支出

### 准则 9：在没什么可失去时，冒最大的险
- 年轻时冒险，回报丰厚，损失有限
- 无所行动的风险被低估

---

## 🚀 使用方式

### 场景 1：年度体验规划

```
@ant 帮我规划 2026 年的体验投资

信息：
- 年龄：35 岁
- 健康：8/10
- 年度体验预算：5 万元
- 兴趣：旅行、摄影、滑雪
- 人生阶段：已婚，孩子 5 岁
```

**调用技能：**
1. `life-experience-investor` - 生成体验清单
2. `life-segmentation-designer` - 分配到人生季节
3. `experience-memory-tracker` - 记录执行进度

### 场景 2：财富峰点评估

```
@ant 我 50 岁了，是否需要继续积累财富？

信息：
- 年龄：50 岁
- 年生活费：50 万
- 当前资产：3000 万
- 年收入：200 万
```

**调用技能：**
1. `death-with-zero-planner` - 计算生存阈值
2. `peak-wealth-calculator` - 评估峰点状态
3. `life-experience-investor` - 生成支出建议

### 场景 3：家庭体验同步

```
@ant 我想带孩子环游世界，什么时候最合适？

信息：
- 孩子年龄：8 岁
- 家庭预算：50 万
- 时间：2 周
```

**调用技能：**
1. `life-segmentation-designer` - 家庭体验同步
2. `life-experience-investor` - 体验规划
3. `experience-memory-tracker` - 记录和追踪

---

## 📊 技能协作流程

```
┌─────────────────────────────────────────────────────────┐
│                    用户需求                              │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
        ┌────────────────────────┐
        │  life-experience-      │
        │  investor              │
        │  （体验规划）          │
        └───────────┬────────────┘
                    │
        ┌───────────▼────────────┐
        │  death-with-zero-      │
        │  planner               │
        │  （财务可行性）        │
        └───────────┬────────────┘
                    │
        ┌───────────▼────────────┐
        │  peak-wealth-          │
        │  calculator            │
        │  （时机评估）          │
        └───────────┬────────────┘
                    │
        ┌───────────▼────────────┐
        │  life-segmentation-    │
        │  designer              │
        │  （人生季节分配）      │
        └───────────┬────────────┘
                    │
        ┌───────────▼────────────┐
        │  experience-memory-    │
        │  tracker               │
        │  （记录和追踪）        │
        └────────────────────────┘
```

---

## 📁 文件结构

```
skills/
├── life-experience-investor/
│   ├── SKILL.md
│   ├── prompts/
│   │   └── experience-interview.md
│   ├── templates/
│   │   └── experience-plan.md
│   └── calculators/
│       └── memory-dividend.py
├── death-with-zero-planner/
│   ├── SKILL.md
│   ├── calculators/
│   │   ├── survival-threshold.py
│   │   └── peak-wealth-age.py
│   └── templates/
│       └── spending-curve.md
├── peak-wealth-calculator/
│   ├── SKILL.md
│   ├── calculators/
│   │   └── marginal-value.py
│   └── templates/
│       └── peak-assessment-report.md
├── life-segmentation-designer/
│   ├── SKILL.md
│   ├── templates/
│   │   ├── life-season-map.md
│   │   └── experience-timeline.md
│   └── calculators/
│       └── timing-optimizer.py
└── experience-memory-tracker/
    ├── SKILL.md
    ├── storage/
    │   └── experiences/
    ├── templates/
    │   ├── experience-record.md
    │   └── annual-report.md
    └── calculators/
        └── memory-dividend.py
```

---

## 🧪 测试计划

### 测试场景 1：35 岁职场人士

**输入：**
- 年龄：35 岁
- 健康：8/10
- 资产：500 万
- 年收入：100 万
- 年生活费：40 万
- 孩子：5 岁

**预期输出：**
- 生存阈值：约 700 万（未达标，继续积累）
- 财富峰点：50-55 岁（积累期）
- 体验建议：年度体验预算 10-20 万
- 家庭同步：孩子 6-12 岁期间安排共同体验

### 测试场景 2：55 岁高净值人士

**输入：**
- 年龄：55 岁
- 健康：7/10
- 资产：5000 万
- 年收入：300 万
- 年生活费：100 万
- 孩子：已独立

**预期输出：**
- 生存阈值：约 2100 万（已超标）
- 财富峰点：已过（开始支出期）
- 体验建议：年度体验预算 100-150 万
- 重点：体力要求高的体验（趁身体好）

---

## 📚 参考资料

- 《最优解人生》（Die With Zero）- Bill Perkins
- 生命周期假说（Life-Cycle Hypothesis）
- 精算师寿命计算器：https://www.longevityillustrator.org/
- 活到 100 计算器：https://www.livingto100.com

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本，5 个核心 skill 完成

---

*投资体验，收获回忆红利。死前归零，人生尽兴。* 💡
