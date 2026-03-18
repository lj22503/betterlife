#!/bin/bash
# 边际成本计算器
# 用法：./marginal-cost-calculator.sh <固定成本> <单位变动成本> <产量>

if [ $# -lt 3 ]; then
    echo "用法：$0 <固定成本> <单位变动成本> <产量>"
    echo "示例：$0 100000 10 1000"
    exit 1
fi

FIXED_COST=$1
VARIABLE_COST=$2
QUANTITY=$3

# 计算总成本
TOTAL_COST=$((FIXED_COST + VARIABLE_COST * QUANTITY))

# 计算平均成本
if [ $QUANTITY -gt 0 ]; then
    AVERAGE_COST=$((TOTAL_COST / QUANTITY))
else
    AVERAGE_COST=0
fi

echo "================================"
echo "边际成本计算"
echo "================================"
echo "固定成本：¥$FIXED_COST"
echo "单位变动成本：¥$VARIABLE_COST"
echo "产量：$QUANTITY"
echo "--------------------------------"
echo "总成本：¥$TOTAL_COST"
echo "平均成本：¥$AVERAGE_COST/单位"
echo "================================"

# 计算不同产量下的平均成本
echo ""
echo "规模效应分析："
echo "产量    总成本      平均成本"
echo "================================"

for q in 100 500 1000 5000 10000; do
    total=$((FIXED_COST + VARIABLE_COST * q))
    avg=$((total / q))
    printf "%-8d ¥%-10d ¥%-10d\n" $q $total $avg
done

echo "================================"
echo "产量越大，平均成本越低，规模效应越明显。"
