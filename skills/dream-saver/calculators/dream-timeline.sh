#!/bin/bash
# 梦想时间线计算器
# 用法：./dream-timeline.sh <梦想名称> <目标金额> <每月储蓄>

if [ $# -lt 3 ]; then
    echo "用法：$0 <梦想名称> <目标金额> <每月储蓄>"
    echo "示例：$0 变速自行车 2000 500"
    exit 1
fi

DREAM_NAME=$1
TARGET=$2
MONTHLY_SAVING=$3

# 计算需要多少个月
MONTHS_NEEDED=$((TARGET / MONTHLY_SAVING))
if [ $((TARGET % MONTHLY_SAVING)) -ne 0 ]; then
    MONTHS_NEEDED=$((MONTHS_NEEDED + 1))
fi

# 计算年数
YEARS=$((MONTHS_NEEDED / 12))
REMAINING_MONTHS=$((MONTHS_NEEDED % 12))

echo "================================"
echo "梦想时间线计算：$DREAM_NAME"
echo "================================"
echo "目标金额：¥$TARGET"
echo "每月储蓄：¥$MONTHLY_SAVING"
echo "--------------------------------"
echo "需要时间：$MONTHS_NEEDED 个月"
if [ $YEARS -gt 0 ]; then
    echo "           ：$YEARS 年 $REMAINING_MONTHS 个月"
fi
echo "================================"

# 计算完成日期
COMPLETION_DATE=$(date -d "+$MONTHS_NEEDED months" +"%Y-%m-%d" 2>/dev/null || date -v+${MONTHS_NEEDED}m +"%Y-%m-%d" 2>/dev/null || echo "请手动计算")
echo "预计完成日期：$COMPLETION_DATE"
echo "================================"
