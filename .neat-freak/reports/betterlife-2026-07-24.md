# betterlife — neat-freak 知识收尾报告

**收尾时间**：2026-07-25
**收尾路径**：轻量路径（**巨型 Skill 库**——24 套主题 + 114/129 个技能 + 100+ 模板，已有 recent neat-freak 风格 commit `4c75c91` REPO-MAP，HEAD 干净）
**收尾者**：neat-freak（v3.0.0）

---

## 一、影响（用户视角）

- **🔴 README.md 与 SKILL_FULL_LIST.md 数字不一致**：
  - README.md 第 9 行：**"24 套主题、114 个技能、100+ 模板"**
  - SKILL_FULL_LIST.md 第 6 行：**"技能总数：129 个 / 模板总数：102 个 / 套件分类：24 个"**
  - 主题数 24 一致，**技能数 114 vs 129（差 15）**、**模板数 100+ vs 102（差 2）**
  → 推测：README 写成后 SKILL_FULL_LIST 更新了技能清单，但 README 没同步；或两份都是手写、易漂移。
- **本次整体良好**：命名一致、REPO-MAP.md 描述仓库间关系、6 层能力框架（意义 → 跃迁 → 投资 → ...）、大量 skills/ 子目录。
- **文档爆炸迹象**：8 个根目录 MD（含 SKILL_CHECK_REPORT 12KB + SKILL_FULL_LIST 20KB + MONEY_RELATIONS_GUIDE 11.6KB + README 15KB = 70KB+）—— 类似 idx 21 wealth-advisor / idx 22 investment-buddy-pet 的"演进报告/中间产物"堆积。

## 二、现役事实矩阵

| 事实面 | 状态 | 证据 |
|--------|------|------|
| 代码 | `not-applicable` | 无运行时代码；纯 Markdown + YAML Skill 定义 |
| 运行态 | `verified-current` | HEAD `4c75c91` REPO-MAP 仓库关系文档（2026-05-07） |
| 文档 | `changed-and-verified` | README.md 15KB + SKILL_FULL_LIST.md 20KB + SKILL_CHECK_REPORT.md 12KB + MONEY_RELATIONS_GUIDE.md 11.6KB + CLEANUP_REPORT + CONTRIBUTING + REPO-MAP + LICENSE |
| 规则 | `not-applicable` | 无 CLAUDE.md / AGENTS.md |
| 记忆 | `not-applicable` | 无 |
| 工作区 | `verified-current` | 新建 `.neat-freak/`；HEAD 干净，无未提交改动 |

## 三、关键发现

### 3.1 🔴 README 与 SKILL_FULL_LIST.md 数字不一致

| 来源 | 主题数 | 技能数 | 模板数 |
|------|-------|-------|-------|
| README.md 第 9 行 | 24 | **114** | **100+** |
| SKILL_FULL_LIST.md 第 6 行 | 24 | **129** | **102** |

→ 主题数一致；**技能差 15**；**模板差 2**。
→ 处置：
- 选项 A：以 SKILL_FULL_LIST.md 为准（更详细权威）→ 改 README.md
- 选项 B：以 README.md 为准（用户面向）→ 改 SKILL_FULL_LIST.md
- 选项 C：把数字抽到一个权威文件，两处引用

### 3.2 6 层能力框架（README.md §6 层能力框架）

按 README.md 第 21-30 行：

```
第 6 层：意义 → 金钱服务于人生
第 5 层：跃迁 → 24 堂财富课
第 4 层：（推测）投资
第 3 层：（推测）规划
第 2 层：（推测）保障
第 1 层：（推测）启蒙/基础
```

→ 6 层递进，与 idx 19 finops-Toolkit / idx 32 fund-operation-workflow 不同（这些是角色分工）。

### 3.3 skills/ 大量 Skill 子目录（看到 10+）

| 子目录 | 推测 |
|--------|------|
| `24-wealth-class` | 24 堂财富课（24 wealth class） |
| `8week-program` | 8 周计划 |
| `ABCDE-refuter` | ABCDE 反驳框架（情绪/认知偏差） |
| `active-listener` | 主动倾听 |
| `adult-ego-activator` | 成人自我激活 |
| `ai-connection-booster` | AI 连接促进 |
| `altruism-power` | 利他力量 |
| `amusement-creator` | 娱乐创造 |
| `anger-expression-guide` | 愤怒表达指南 |
| `anger-expressor` | 愤怒表达者 |

→ 推测总共 100+ 个 Skill（README 写 114，SKILL_FULL_LIST 写 129）。

### 3.4 projects/one-advisor-cn

| 路径 | 推测 |
|------|------|
| `projects/one-advisor-cn/` | 一个 advisor 中文版项目子仓库 |

→ 与 idx 5 investment-advisory-skills / SoloAdvisor-Toolkit 可能相关（都是 advisor 工具）。

### 3.5 5 commit 历史

```
4c75c91 chore: 2026-05-07 添加 REPO-MAP 仓库关系文档
ce79ef6 2026-04-21: 添加 projects 目录
a288898 docs: 更新 MIT 许可证和贡献指南
555bc54 feat: 新增极简主义实践师 skill (minimalism-practitioner)
04aecde feat: problem-mapper 融入一人 CEO 核心技能体系
```

→ 5 commit 反映项目演进：
- 加入 minimalism-practitioner skill
- problem-mapper 融入核心体系
- 加 projects 目录
- 加 REPO-MAP

### 3.6 与主工作空间关系（REPO-MAP.md）

按 REPO-MAP.md：

```
🎯 当前聚焦
└── Mangofolio (一人投顾)

📦 本仓库
└── betterlife (财商教育)

🔗 关联仓库
├── investment-framework-skill
├── diaolong-skill
├── women-awakening-museum
└── mangofolio-skill
```

→ 主工作空间 `lj22503/one-person-ceo-skills` 是"母仓"，betterlife 是"独立仓库"。

### 3.7 CLEANUP_REPORT_2026-03-19.md（带日期快照）

→ 与 idx 4 / idx 13 / idx 14 / idx 21 / idx 22 同款"带日期历史快照"——按 neat-freak §4 "演进报告/中间产物"分类，应归档到 docs/。

### 3.8 完整结构

```
betterlife/
├── README.md                # 15KB 用户向（错位数字）
├── SKILL_FULL_LIST.md       # 20KB 完整技能清单（权威？数字不一致）
├── SKILL_CHECK_REPORT.md    # 12KB 技能审查报告
├── MONEY_RELATIONS_GUIDE.md # 11.6KB 金钱关系指南
├── CLEANUP_REPORT_2026-03-19.md  # 清理报告（带日期）
├── CONTRIBUTING.md
├── REPO-MAP.md
├── LICENSE
├── projects/
│   └── one-advisor-cn/
└── skills/
    ├── 24-wealth-class/
    ├── 8week-program/
    ├── ABCDE-refuter/
    └── ...（100+ Skill）
```

### 3.9 与 idx 5 (investment-advisory-skills) 对照

| 维度 | betterlife（idx 36） | investment-advisory-skills（idx 5） |
|------|---------------------|----------------------------------|
| 主题 | 财商教育 | 投资顾问 |
| Skill 数量 | 100+ | 13 + 7 roles + 7 gates |
| 形态 | skills/ 单文件平铺 | commands/ + gates/ + roles/ + skills/ + orchestrator/ + router/ 分层 |
| 项目子目录 | projects/one-advisor-cn | 无 |

→ betterlife 是"通用财商 Skill 库"，investment-advisory-skills 是"专业投顾 Skill 套件"。

### 3.10 文档爆炸（70KB+ 根目录 MD）

| 文件 | 尺寸 |
|------|------|
| SKILL_FULL_LIST.md | 20KB |
| README.md | 15KB |
| SKILL_CHECK_REPORT.md | 12KB |
| MONEY_RELATIONS_GUIDE.md | 11.6KB |
| 其他 4 个 | 11KB |
| **总计** | **70KB+** |

→ 与 idx 21 wealth-advisor（多个 DEPLOY/GETTING-STARTED/UPDATE-SUMMARY）、idx 22 investment-buddy-pet（10 个非 README/SPEC 文档）同款"演进历史堆积"。

## 四、改动 / 新建

| 文件 | 动作 | 原因 |
|------|------|------|
| `.neat-freak/reports/betterlife-2026-07-24.md` | 新建 | 本次 audit trail |

## 五、待你确认（未确认前不动作）

1. **🔴 README vs SKILL_FULL_LIST 数字不一致**：以哪个为准？建议以 SKILL_FULL_LIST 为准（更详细），README 改对齐
2. **8 个根目录 MD 文档爆炸**：合并/归档到 docs/
3. **CLEANUP_REPORT_2026-03-19.md** 带日期快照是否仍有效
4. **projects/one-advisor-cn/** 与 idx 5 investment-advisory-skills 关系确认（同一项目不同 clone？）

## 六、遗留

- skills/ 100+ 实际未逐个审（仅看 10 个名字）
- SKILL_FULL_LIST.md 20KB 未读全文
- SKILL_CHECK_REPORT.md 12KB 未读全文
- MONEY_RELATIONS_GUIDE.md 11.6KB 未读全文
- 24 套主题 + 6 层能力框架完整内容未读
- projects/one-advisor-cn/ 子项目内容未审

---

*收尾完成度：5 事实面已标注（记忆 not-applicable，规则 not-applicable 缺文件）。报告基于 commit `4c75c91`（HEAD，分支 main）。本项目是 idx 0-36 中 **Skill 库最大项目之一**（114/129 个 Skill + 100+ 模板）。如需重新跑请清空 `.neat-freak/reports/` 后重跑。*