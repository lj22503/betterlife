#!/bin/bash
# 复利计算器
# 用法：./compound-interest.sh <本金> <年收益率> <年数>

if [ $# -lt 3 ]; then
    echo "用法：$0 <本金> <年收益率 (%)> <年数>"
    echo "示例：$0 10000 8 30"
    exit 1
fi

PRINCIPAL=$1
RATE=$2
YEARS=$3

echo "================================"
echo "复利计算"
echo "================================"
echo "本金：¥$PRINCIPAL"
echo "年收益率：$RATE%"
echo "投资年限：$YEARS 年"
echo "--------------------------------"
echo "年份    本金        利息        总额"
echo "================================"

TOTAL=$PRINCIPAL
for ((i=1; i<=YEARS; i++)); do
    INTEREST=$((TOTAL * RATE / 100))
    TOTAL=$((TOTAL + INTEREST))
    printf "%-4d    ¥%-10d  ¥%-10d  ¥%-10d\n" $i $PRINCIPAL $INTEREST $TOTAL
done

echo "================================"
echo "$YEARS 年后总额：¥$TOTAL"
echo "总收益：¥$((TOTAL - PRINCIPAL))"
echo "================================"
