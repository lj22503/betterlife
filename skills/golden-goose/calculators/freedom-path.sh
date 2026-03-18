#!/bin/bash
# 财务自由路径计算器
# 用法：./freedom-path.sh <月支出> <当前储蓄> <月储蓄> <年收益率>

if [ $# -lt 4 ]; then
    echo "用法：$0 <月支出> <当前储蓄> <月储蓄> <年收益率 (%)>"
    echo "示例：$0 10000 500000 20000 8"
    exit 1
fi

MONTHLY_EXPENSE=$1
CURRENT_SAVING=$2
MONTHLY_SAVING=$3
RATE=$4

# 财务自由数字 (4% 规则)
FI_NUMBER=$((MONTHLY_EXPENSE * 12 * 25))

echo "================================"
echo "财务自由路径计算"
echo "================================"
echo "月支出：¥$MONTHLY_EXPENSE"
echo "当前储蓄：¥$CURRENT_SAVING"
echo "月储蓄：¥$MONTHLY_SAVING"
echo "年收益率：$RATE%"
echo "--------------------------------"
echo "财务自由数字：¥$FI_NUMBER"
echo "(月支出×12×25，基于 4% 规则)"
echo "--------------------------------"

# 计算需要多少年
CURRENT=$CURRENT_SAVING
YEAR=0
while [ $CURRENT -lt $FI_NUMBER ] && [ $YEAR -lt 50 ]; do
    YEAR=$((YEAR + 1))
    INTEREST=$((CURRENT * RATE / 100))
    SAVING=$((MONTHLY_SAVING * 12))
    CURRENT=$((CURRENT + INTEREST + SAVING))
done

echo "达成财务自由需要：$YEAR 年"
echo "届时年龄：当前年龄 + $YEAR"
echo "最终资产：¥$CURRENT"
echo "================================"
