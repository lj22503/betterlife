---
name: policy-organizer
version: 1.0.0
description: 保单整理工具 - 整理家庭保单，避免保单沉睡
author: 燃冰 + 小蚂蚁
created: 2026-03-18
skill_type: 通用
---

# 保单整理工具 📁

**基于《你的保险指南》核心理念**

---

## 📋 功能描述

帮助家庭整理所有保单，建立保单档案，确保家人知晓保障内容，避免保单沉睡。

**适用场景：**
- 家庭保单整理
- 保单档案管理
- 受益人告知
- 保单查询与理赔

**边界条件：**
- 不提供投资建议
- 不替代专业服务
- 适合 18 岁以上人群

---

## 🎯 核心功能

### 1. 家庭保单分类整理

按家庭成员和险种分类整理保单。

**分类维度：**
- 按成员：丈夫/妻子/孩子/父母
- 按险种：重疾/医疗/意外/寿险/年金
- 按状态：有效/失效/待缴费

**输出：**
```json
{
  "family_policies": {
    "husband": [
      {
        "policy_id": "P001",
        "company": "XX 保险",
        "type": "重疾险",
        "coverage": 1000000,
        "premium": 20000,
        "payment_period": "20 年",
        "coverage_period": "终身",
        "status": "有效",
        "next_payment_date": "2026-06-01"
      }
    ],
    "wife": [...],
    "child": [...]
  },
  "summary": {
    "total_policies": 10,
    "total_coverage": 20000000,
    "total_annual_premium": 150000
  }
}
```

### 2. 保单查询指导

指导如何查询家人保单。

**查询方式：**
- 金事通 APP（官方平台）
- 检查纸质保单
- 联系保险业务员
- 查询银行流水
- 联系保险公司客服

**输出：**
```json
{
  "query_methods": [
    {
      "method": "金事通 APP",
      "description": "中国银保信官方平台",
      "steps": ["下载 APP", "实名认证", "登录查询"],
      "coverage": "国内保单"
    },
    {
      "method": "检查银行流水",
      "description": "查找保险缴费记录",
      "steps": ["导出银行流水", "筛选保险扣款", "联系保险公司"],
      "coverage": "所有银行卡扣款保单"
    }
  ],
  "key_insight": "优先使用金事通 APP 查询，再结合其他方式"
}
```

### 3. 受益人告知

确保受益人知晓保单信息。

**告知内容：**
- 保单在哪里
- 保险公司联系方式
- 理赔流程
- 所需材料

**输出：**
```json
{
  "beneficiary_notification": {
    "policy_location": "家庭保险档案盒（书房抽屉）",
    "digital_backup": "云盘/保险 APP",
    "agent_contact": "张三 138****1234",
    "claims_process": [
      "拨打保险公司客服电话",
      "准备理赔材料（诊断证明、病历等）",
      "提交理赔申请",
      "等待审核赔付"
    ],
    "key_documents": [
      "保单原件",
      "身份证",
      "银行卡",
      "医疗单据"
    ]
  }
}
```

### 4. 保单检视提醒

定期检视保单，确保保障有效。

**检视内容：**
- 保费是否按时缴纳
- 保障是否充足
- 受益人是否需要更新
- 联系方式是否变更

**输出：**
```json
{
  "review_reminders": [
    {
      "type": "缴费提醒",
      "policy": "丈夫重疾险",
      "next_date": "2026-06-01",
      "amount": 20000
    },
    {
      "type": "年度检视",
      "date": "每年 1 月",
      "content": "检查保障是否充足、受益人是否需要更新"
    }
  ],
  "recommendation": "设置自动缴费，避免保单失效"
}
```

---

## 📊 输入参数

```json
{
  "family_members": {
    "type": "array",
    "required": true,
    "description": "家庭成员列表"
  },
  "existing_policies": {
    "type": "array",
    "required": false,
    "description": "现有保单列表"
  },
  "storage_method": {
    "type": "string",
    "required": false,
    "description": "保单存储方式（纸质/电子/混合）"
  }
}
```

---

## 📤 输出格式

```json
{
  "status": "success",
  "data": {
    "policy_classification": {},
    "query_guidance": {},
    "beneficiary_notification": {},
    "review_reminders": {},
    "action_items": []
  },
  "error": null
}
```

---

## 📚 政策依据

**核心理论：**
- 《你的保险指南》- 健康管理角度规划保险
- 保单整理五步走
- 家庭档案管理

**关键概念：**
- 整理家庭保单，避免保单沉睡
- 受益人知晓保单信息
- 定期检视保障是否充足

---

## 📝 变更日志

- v1.0.0 (2026-03-18): 初始版本

---

*整理保单，让保障真正生效。* 📁
