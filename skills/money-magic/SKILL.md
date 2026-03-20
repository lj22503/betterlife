name: money-magic
description: ［何时使用］当用户需要金钱魔法 - 72 公式计算器，快速估算复利和通胀时；当用户提及相关功能时
skill_type: 通用---

# 金钱魔法 72 公式 🎯

**基于《小狗钱钱》核心理念**

---

## 📋 功能描述

用 72 公式快速估算投资翻倍时间、通胀贬值速度，帮助用户理解复利的魔力。

**适用场景：**
- 投资回报估算
- 通胀影响分析
- 财商教育
- 快速决策参考

**边界条件：**
- 快速估算工具，非精确计算
- 不提供投资建议
- 适合 12 岁以上人群

---

## 🎯 核心功能

### 1. 投资翻倍时间计算

用 72 公式计算投资翻倍所需年数。

**公式：**
```
翻倍年数 = 72 ÷ 年化收益率%
```

**示例：**
- 年化 5% → 72÷5 = 14.4 年翻倍
- 年化 8% → 72÷8 = 9 年翻倍
- 年化 12% → 72÷12 = 6 年翻倍

**输出：**
```json
{
  "investment_amount": 10000,
  "annual_return_rate": 0.08,
  "years_to_double": 9,
  "doubled_amount": 20000,
  "insight": "年化 8% 的情况下，你的投资 9 年后翻倍"
}
```

### 2. 通胀贬值时间计算

用 72 公式计算货币贬值一半所需年数。

**公式：**
```
贬值年数 = 72 ÷ 通胀率%
```

**示例：**
- 通胀 3% → 72÷3 = 24 年贬值一半
- 通胀 5% → 72÷5 = 14.4 年贬值一半
- 通胀 10% → 72÷10 = 7.2 年贬值一半

**输出：**
```json
{
  "current_value": 10000,
  "inflation_rate": 0.03,
  "years_to_halve": 24,
  "halved_value": 5000,
  "insight": "通胀 3% 的情况下，你的钱 24 年后只值现在的一半"
}
```

### 3. 复利魔力演示

展示复利随时间的增长曲线。

**输出：**
```json
{
  "principal": 10000,
  "annual_return": 0.08,
  "projection": [
    {"year": 0, "value": 10000, "event": "初始本金"},
    {"year": 9, "value": 20000, "event": "第 1 次翻倍"},
    {"year": 18, "value": 40000, "event": "第 2 次翻倍"},
    {"year": 27, "value": 80000, "event": "第 3 次翻倍"},
    {"year": 36, "value": 160000, "event": "第 4 次翻倍"}
  ],
  "insight": "36 年后，你的 1 万变成 16 万！这就是复利的魔力"
}
```

### 4. 投资决策辅助

比较不同投资选择的长期效果。

**输出：**
```json
{
  "options": [
    {
      "name": "银行定期",
      "return_rate": 0.03,
      "years_to_double": 24,
      "value_after_30y": 24000
    },
    {
      "name": "债券基金",
      "return_rate": 0.05,
      "years_to_double": 14.4,
      "value_after_30y": 43000
    },
    {
      "name": "指数基金",
      "return_rate": 0.08,
      "years_to_double": 9,
      "value_after_30y": 100000
    }
  ],
  "recommendation": "长期投资选择指数基金，30 年后收益是银行定期的 4 倍",
  "risk_warning": "高收益伴随高风险，根据自身风险承受能力选择"
}
```

---

## 📊 输入参数

```json
{
  "action": {
    "type": "string",
    "required": true,
    "description": "操作类型（double/halte/compound/compare）"
  },
  "principal": {
    "type": "number",
    "required": false,
    "description": "本金金额"
  },
  "return_rate": {
    "type": "number",
    "required": false,
    "description": "年化收益率（小数，如 0.08 表示 8%）"
  },
  "inflation_rate": {
    "type": "number",
    "required": false,
    "description": "通胀率（小数，如 0.03 表示 3%）"
  },
  "years": {
    "type": "number",
    "required": false,
    "description": "投资年限"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "action": "",
    "calculation": {},
    "insight": ""
  },
  "error": null
}
```

---

## 🧪 使用示例

### 示例 1：计算投资翻倍时间

```
@ant 年化 8% 的收益，多久翻倍？
```

**预期输出：**
- 72÷8 = 9 年翻倍
- 10 万投资，9 年后变 20 万

### 示例 2：计算通胀贬值

```
@ant 通胀 3%，我的钱多久贬值一半？
```

**预期输出：**
- 72÷3 = 24 年贬值一半
- 现在的 100 万，24 年后只值 50 万

### 示例 3：复利魔力演示

```
@ant 10 万本金，年化 8%，30 年后多少？
```

**预期输出：**
- 9 年：20 万（第 1 次翻倍）
- 18 年：40 万（第 2 次翻倍）
- 27 年：80 万（第 3 次翻倍）
- 30 年：约 100 万

### 示例 4：投资选择对比

```
@ant 银行定期 3% vs 指数基金 8%，30 年后差多少？
```

**预期输出：**
- 银行定期：24 万
- 指数基金：100 万
- 差距：4 倍

---

## ⚠️ 错误处理

| 错误码 | 含义 | 处理建议 |
|--------|------|----------|
| 400 | 参数缺失 | 检查必填字段（action） |
| 400 | 收益率无效 | 收益率应在 1%-20% 之间 |
| 400 | 通胀率无效 | 通胀率应在 0%-15% 之间 |
| 500 | 内部错误 | 重试或联系开发者 |

---

## 📚 政策依据

**核心理论：**
- 《小狗钱钱》- 博多·舍费尔
- 72 公式（Rule of 72）
- 复利效应（Compound Interest）

**关键概念：**
- 72 公式：翻倍年数 = 72÷收益率%
- 复利魔力：时间越长，效果越惊人
- 通胀侵蚀：钱不投资就会贬值

---

## 🔗 相关文件

- `calculators/rule-of-72.sh` - 72 公式计算器
- `calculators/compound-interest.sh` - 复利计算器（与 golden-goose 共用）
- `templates/inflation-warning.md` - 通胀警示模板

## 💡 使用建议

**计算翻倍时间：**
```bash
./calculators/rule-of-72.sh 8 double
# 年化 8%，9 年翻倍
```

**计算贬值时间：**
```bash
./calculators/rule-of-72.sh 3 halve
# 通胀 3%，24 年贬值一半
```

**填写通胀警示：**
1. 打印 inflation-warning.md
2. 填入当前金额和通胀率
3. 贴在显眼位置提醒自己

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*72 公式，一眼看穿复利魔力。* 🎯
---

## 🔧 故障排查

| 问题 | 检查项 |
|------|--------|
| 不触发 | description 是否包含触发词？ |
| 运行失败 | 脚本有执行权限吗？(`chmod +x`) |
