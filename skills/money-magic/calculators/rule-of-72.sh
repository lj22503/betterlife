#!/bin/bash
# 72 公式计算器
# 用法：./rule-of-72.sh <收益率/通胀率> <类型：double/halve>

if [ $# -lt 2 ]; then
    echo "用法：$0 <收益率/通胀率 (%> <类型：double|halve>"
    echo "  double: 计算翻倍时间（投资）"
    echo "  halve:  计算贬值一半时间（通胀）"
    echo "示例：$0 8 double"
    echo "      $0 3 halve"
    exit 1
fi

RATE=$1
TYPE=$2

YEARS=$((72 / RATE))

echo "================================"
echo "72 公式计算"
echo "================================"
if [ "$TYPE" = "double" ]; then
    echo "收益率：$RATE%"
    echo "--------------------------------"
    echo "翻倍需要：$YEARS 年"
    echo ""
    echo "示例："
    echo "  第 0 年：¥10,000"
    echo "  第$YEARS 年：¥20,000"
    echo "  第$((YEARS*2)) 年：¥40,000"
    echo "  第$((YEARS*3)) 年：¥80,000"
elif [ "$TYPE" = "halve" ]; then
    echo "通胀率：$RATE%"
    echo "--------------------------------"
    echo "贬值一半需要：$YEARS 年"
    echo ""
    echo "示例："
    echo "  现在：¥100,000 购买力"
    echo "  $YEARS 年后：¥50,000 购买力"
    echo "  $((YEARS*2)) 年后：¥25,000 购买力"
else
    echo "错误：类型必须是 double 或 halve"
    exit 1
fi
echo "================================"
