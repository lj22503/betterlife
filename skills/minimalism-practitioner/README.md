# 极简主义实践师 🌿

**基于《极简，是高级的奢侈》核心理念**

---

## 快速开始

```bash
# 运行极简度评分
python3 calculators/minimalism-score.py

# 使用评估模板
cp templates/minimalism-assessment-template.md ~/my-assessment.md
```

---

## 文件结构

```
minimalism-practitioner/
├── SKILL.md                          # Skill 定义
├── README.md                         # 本文件
├── calculators/
│   └── minimalism-score.py          # 极简度评分计算器
└── templates/
    ├── minimalism-assessment-template.md  # 评估模板
    ├── item-budget-template.md           # 物品预算模板
    └── values-worksheet.md                # 价值观工作表
```

---

## 核心功能

### 1. 极简度评分

```python
from calculators.minimalism-score import MinimalismScoreCalculator

calculator = MinimalismScoreCalculator()
assessment = {...}  # 评估数据
scores = calculator.calculate_total_score(assessment)
print(f"极简度：{scores['total_score']}/100 - {scores['level']}")
```

### 2. 物品断舍离

使用 `item-budget-template.md`：
- 零废品守则（必需品/非必需品/废品）
- 20/20 守则
- 30/30 守则
- 一进十出守则
- 90/90 守则

### 3. 价值观澄清

使用 `values-worksheet.md`：
- 框架价值（决定你是谁）
- 表面价值（随兴趣变化）
- 假想价值（阻碍满足感）

### 4. 人际关系评估

八大要素评分：
- 爱、信任、诚实、关怀、支持、专注、可靠、理解

---

## 八大极简守则

| 守则 | 核心规则 | 应用场景 |
|------|---------|---------|
| 零废品 | 必需品/非必需品/废品分类 | 物品清理 |
| 20/20 | 20 分钟内花 20 美元能买回 | 丢弃决策 |
| 30/30 | 超 30 美元等 30 小时 | 冲动购物 |
| 一进十出 | 买 1 件丢 10 件 | 物品控制 |
| 90/90 | 过去/未来 90 天使用 | 季节性清理 |
| 自燃 | 如果自燃会宽慰吗 | 情感释放 |
| 出售期限 | 30 天卖不掉就捐赠 | 闲置处理 |
| 购买前六问 | 6 个问题过滤 | 购物决策 |

---

## 人生五大价值

每日自问：**我是怎样把这五大价值全部融合在我今天的生活中的？**

1. **健康** - 饮食、锻炼、睡眠、阳光
2. **人际关系** - 爱、信任、诚实等八大要素
3. **热情** - 移除四道枷锁（身份、地位、确定性、金钱）
4. **成长** - 无止境的成长 vs 有意识的成长
5. **奉献** - 给予就是活着

---

## 使用场景

- 物品清理和断舍离
- 极简主义生活指导
- 价值观澄清
- 人际关系简化
- 消费习惯优化
- 数字化清理
- 健康极简实践

---

## 输出示例

```
=== 极简度评分报告 ===

总得分：68.5/100
等级：极简实践者

各维度得分：
  items: 72.0
  values: 65.0
  relationships: 75.0
  money: 60.0
  digital: 55.0
  health: 70.0
  balance: 66.0

改进建议：
  【数字化】尝试无屏幕周六，减少屏幕时间
    行动：本周六不碰电子设备
  【金钱】建立预算，开始财务自由五要素实践
    行动：记录本月每一笔支出
  【价值观】填写价值观工作表，澄清框架价值和假想价值
    行动：列出你的框架价值和假想价值
```

---

## 相关 Skill

- `life-experience-investor` - 人生体验投资顾问
- `death-with-zero-planner` - 死前归零规划师
- `frugal-living` - 节俭生活实践器
- `values-finder` - 价值观发现器

---

## 参考资料

- 《极简，是高级的奢侈》- 乔舒亚·菲尔茨·米尔本等
- 斯多葛学派极简传统
- 日本断舍离文化

---

*版本：1.0.0 | 创建：2026-04-11*
