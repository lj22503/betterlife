name: fasting-safety
description: ［何时使用］当用户需要断食安全评估 - 禁忌症与风险提示时；当用户提及相关功能时
skill_type: 通用---

# 断食安全评估 ⚠️

**基于《疗愈的饮食与断食》第 48、52 章**

---

## 📋 功能描述

评估用户是否适合断食，识别禁忌症和风险因素。

**适用场景：**
- 开始断食前评估
- 长时间断食计划
- 有基础疾病者
- 特殊人群（女士、老人）

**边界条件：**
- 不替代医疗建议
- 高风险人群需医师指导
- 出现不适立即停止

---

## 🎯 核心功能

### 1. 断食禁忌症筛查

**❌ 绝对禁忌（不应断食）：**
```
• 怀孕
• 哺乳期
• 体重不足（BMI<18.5）
• 营养不良
• 进食障碍史（厌食症、暴食症）
• 1 型糖尿病
• 晚期癌症
• 严重肝肾功能不全
```

**⚠️ 相对禁忌（需医师指导）：**
```
• 2 型糖尿病（用胰岛素或磺脲类药物）
• 低血压
• 痛风
• 胆结石
• 胃溃疡
• 肾上腺疲劳
• 甲状腺疾病
• 自体免疫疾病
• 正在服用特定药物
```

### 2. 女士断食特殊考量

**生理周期影响：**
```
月经后 2 周：
✓ 雌激素较高
✓ 胰岛素敏感性较好
✓ 断食黄金期

月经前 1 周：
× 黄体素下降
× 胰岛素分泌增加
× 血糖易波动
× 渴望甜食
× 避开断食
```

**女士风险信号：**
```
• 月经紊乱/停经
• 过度疲劳
• 头发脱落
• 怕冷
• 情绪波动加剧
```

### 3. 药物相互作用

**需调整剂量的药物：**
```
• 降血糖药（胰岛素、磺脲类）→ 低血糖风险
• 降压药 → 低血压风险
• 利尿剂 → 脱水/电解质失衡
• 抗凝血药 → 需监测
• 甲状腺药物 → 可能需调整
```

**建议：**
- 断食前咨询医师
- 监测血糖/血压
- 准备调整药物剂量

### 4. 断食副作用管理

**常见副作用（通常短暂）：**
```
• 头痛 → 多喝水、补充电解质
• 疲倦 → 休息、适应期
• 头晕 → 慢慢起身、补充盐分
• 便秘 → 多喝水、好脂肪
• 抽筋 → 补充镁、钾
• 失眠 → 避免晚上断食、放松
• 口臭 → 正常现象、多喝水
```

**酮流感（3-7 天）：**
```
• 头痛、疲倦、恶心
• 反应变慢、易怒
• 渴望甜食
• 应对：多喝水、补充电解质、好脂肪
```

### 5. 何时停止断食

**立即停止的信号：**
```
• 严重头晕/晕厥
• 心悸、胸痛
• 严重虚弱
• 持续呕吐
• 意识模糊
• 血糖过低（<70 mg/dL）
• 极度不适
```

**建议停止的情况：**
```
• 副作用持续超过 1 周
• 体重下降过快（>1kg/天）
• 月经紊乱
• 情绪严重受影响
• 生活质量明显下降
```

---

## 📊 输入参数

```json
{
  "age": {"type": "number", "required": true},
  "gender": {"type": "string", "enum": ["male", "female"], "required": true},
  "bmi": {"type": "number", "required": true},
  "health_conditions": {"type": "array", "items": {"type": "string"}, "required": false},
  "medications": {"type": "array", "items": {"type": "string"}, "required": false},
  "pregnant_or_breastfeeding": {"type": "boolean", "required": true},
  "eating_disorder_history": {"type": "boolean", "required": true},
  "fasting_goal": {"type": "string", "required": true},
  "planned_duration": {"type": "string", "enum": ["16h", "24h", "48h", "72h+", "unknown"], "required": true}
}
```

---

## 📤 输出格式

```json
{
  "status": "success|warning|danger",
  "data": {
    "fasting_safety": "safe|caution|contraindicated",
    "absolute_contraindications": [],
    "relative_contraindications": [],
    "medication_interactions": [],
    "special_considerations": [],
    "side_effects_preview": [],
    "stop_signals": [],
    "recommendations": []
  },
  "error": null
}
```

---

## 🧪 使用示例

```
@ant 帮我评估是否适合断食

信息：
- 年龄：45 岁
- 性别：女
- BMI: 26
- 健康状况：2 型糖尿病前期
- 用药：无
- 怀孕/哺乳：否
- 进食障碍史：无
- 断食目标：改善代谢
- 计划时长：16-8 间歇性断食
```

**预期输出：**
- 安全等级：安全（可开始）
- 注意事项：监测血糖
- 副作用预警
- 建议从 14-10 开始渐进

---

## 📚 核心理念

**关键洞察：**
1. 断食不适合所有人
2. 女士需配合生理周期
3. 药物可能需调整
4. 副作用通常短暂
5. 知道何时停止很重要

**安全原则：**
- 从短时间开始（12-14 小时）
- 渐进延长
- 倾听身体信号
- 有疑虑咨询医师

---

## 🔗 相关文件

- `templates/fasting-safety-checklist.md` - 安全筛查清单
- `templates/medication-log.md` - 药物记录表
- `templates/female-cycle-tracker.md` - 生理周期追踪

---

*生病的人若要进行长时间的激烈断食，一定要有合格医事专业人员从旁协助指导。* ⚠️
---

## 🔧 故障排查

| 问题 | 检查项 |
|------|--------|
| 不触发 | description 是否包含触发词？ |
| 运行失败 | 脚本有执行权限吗？(`chmod +x`) |
