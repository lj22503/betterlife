#!/usr/bin/env python3
"""
极简度评分计算器

基于《极简主义》核心理念，计算用户的极简度得分。
"""

import json
from datetime import datetime


class MinimalismScoreCalculator:
    """极简度评分计算器"""
    
    def __init__(self):
        self.weights = {
            'items': 0.20,        # 物品清理完成度
            'values': 0.15,       # 价值观清晰度
            'relationships': 0.20, # 人际关系质量
            'money': 0.15,        # 金钱健康度
            'digital': 0.10,      # 数字化极简度
            'health': 0.10,       # 健康实践度
            'balance': 0.10       # 五大价值平衡
        }
    
    def calculate_item_score(self, assessment):
        """计算物品清理得分"""
        total_items = 0
        completed_items = 0
        
        for room in assessment.get('rooms', []):
            necessities = room.get('necessities', 0)
            non_necessities = room.get('non_necessities', 0)
            waste = room.get('waste', 0)
            
            total_items += necessities + non_necessities + waste
            completed_items += necessities + non_necessities  # 废品未清理
        
        if total_items == 0:
            return 50  # 默认分
        
        # 废品占比越低，得分越高
        waste_ratio = (total_items - completed_items) / total_items
        score = 100 * (1 - waste_ratio)
        
        # 应用极简守则加分
        rules_applied = assessment.get('rules_applied', 0)
        score += min(20, rules_applied * 3)  # 每应用一个守则加 3 分，最多加 20 分
        
        return min(100, max(0, score))
    
    def calculate_values_score(self, assessment):
        """计算价值观清晰度得分"""
        framework_values = assessment.get('framework_values', [])
        surface_values = assessment.get('surface_values', [])
        false_values = assessment.get('false_values', [])
        
        # 框架价值清晰度（是否列出并定义）
        framework_score = min(100, len(framework_values) * 15)
        
        # 假想价值识别（识别越多，越清晰）
        false_value_score = min(100, len(false_values) * 20)
        
        # 综合得分
        score = (framework_score * 0.7 + false_value_score * 0.3)
        
        return min(100, max(0, score))
    
    def calculate_relationships_score(self, assessment):
        """计算人际关系质量得分"""
        relationships = assessment.get('relationships', [])
        
        if not relationships:
            return 50  # 默认分
        
        total_score = 0
        max_score = 0
        
        for rel in relationships:
            elements = rel.get('elements', {})  # 爱、信任、诚实等 8 要素
            rel_score = sum(elements.values())
            max_possible = len(elements) * 5  # 每项最高 5 分
            
            total_score += rel_score
            max_score += max_possible
        
        if max_score == 0:
            return 50
        
        # 转换为百分制
        score = (total_score / max_score) * 100
        
        return min(100, max(0, score))
    
    def calculate_money_score(self, assessment):
        """计算金钱健康度得分"""
        financial_elements = assessment.get('financial_elements', {})
        
        # 财务自由五要素
        elements = {
            'budget': financial_elements.get('budget', 0),      # 0-3
            'invest': financial_elements.get('invest', 0),      # 0-3
            'debt_free': financial_elements.get('debt_free', 0), # 0-3
            'minimalism': financial_elements.get('minimalism', 0), # 0-3
            'giving': financial_elements.get('giving', 0)       # 0-3
        }
        
        total = sum(elements.values())
        max_total = 15  # 5 要素 × 3 分
        
        score = (total / max_total) * 100
        
        # 冲动消费扣分
        impulse_buying = assessment.get('impulse_buying_count', 0)
        score -= min(20, impulse_buying * 2)
        
        return min(100, max(0, score))
    
    def calculate_digital_score(self, assessment):
        """计算数字化极简度得分"""
        practices = assessment.get('digital_practices', {})
        
        practice_scores = {
            'no_screen_saturday': 25,
            'grayscale_mode': 15,
            'bedtime_no_screen': 25,
            'no_upgrade': 15,
            'app_cleanup': 20
        }
        
        score = 0
        for practice, points in practice_scores.items():
            if practices.get(practice, False):
                score += points
        
        # 屏幕时间扣分
        screen_hours = assessment.get('daily_screen_hours', 4)
        if screen_hours > 6:
            score -= min(20, (screen_hours - 6) * 5)
        
        return min(100, max(0, score))
    
    def calculate_health_score(self, assessment):
        """计算健康实践度得分"""
        health_practices = assessment.get('health_practices', {})
        
        # 四大免费良药
        medicine_scores = {
            'diet': 25,
            'exercise': 25,
            'sleep': 25,
            'sunlight': 25
        }
        
        score = 0
        for medicine, points in medicine_scores.items():
            frequency = health_practices.get(medicine, 0)  # 0-7 (每周次数)
            score += (frequency / 7) * points
        
        # 睡眠质量加分
        sleep_quality = assessment.get('sleep_quality_practices', [])
        score += min(10, len(sleep_quality) * 2)
        
        return min(100, max(0, score))
    
    def calculate_balance_score(self, assessment):
        """计算五大价值平衡得分"""
        five_values = assessment.get('five_values', {})
        
        if not five_values:
            return 50  # 默认分
        
        # 计算五个价值的平均满意度
        satisfactions = [
            five_values.get('health', 5),
            five_values.get('relationships', 5),
            five_values.get('passion', 5),
            five_values.get('growth', 5),
            five_values.get('contribution', 5)
        ]
        
        avg_satisfaction = sum(satisfactions) / len(satisfactions)
        
        # 转换为百分制（满意度 1-10 → 0-100）
        score = (avg_satisfaction / 10) * 100
        
        return min(100, max(0, score))
    
    def calculate_total_score(self, assessment):
        """计算总得分"""
        scores = {
            'items': self.calculate_item_score(assessment),
            'values': self.calculate_values_score(assessment),
            'relationships': self.calculate_relationships_score(assessment),
            'money': self.calculate_money_score(assessment),
            'digital': self.calculate_digital_score(assessment),
            'health': self.calculate_health_score(assessment),
            'balance': self.calculate_balance_score(assessment)
        }
        
        total_score = 0
        for category, score in scores.items():
            total_score += score * self.weights[category]
        
        # 确定等级
        if total_score >= 80:
            level = "极简大师"
        elif total_score >= 60:
            level = "极简实践者"
        elif total_score >= 40:
            level = "极简初学者"
        else:
            level = "需要开始极简之旅"
        
        return {
            'total_score': round(total_score, 1),
            'level': level,
            'category_scores': {k: round(v, 1) for k, v in scores.items()},
            'weights': self.weights,
            'timestamp': datetime.now().isoformat()
        }
    
    def get_recommendations(self, assessment, scores):
        """生成改进建议"""
        recommendations = []
        
        # 找出得分最低的三个维度
        sorted_scores = sorted(scores['category_scores'].items(), key=lambda x: x[1])
        
        for category, score in sorted_scores[:3]:
            if category == 'items' and score < 60:
                recommendations.append({
                    'category': '物品',
                    'suggestion': '从零废品守则开始，选择一个房间进行物品分类',
                    'action': '使用物品预算模板，清理废品'
                })
            elif category == 'values' and score < 60:
                recommendations.append({
                    'category': '价值观',
                    'suggestion': '填写价值观工作表，澄清框架价值和假想价值',
                    'action': '列出你的框架价值和假想价值'
                })
            elif category == 'relationships' and score < 60:
                recommendations.append({
                    'category': '人际关系',
                    'suggestion': '用八大要素评估重要关系，找出需要改善的关系',
                    'action': '与重要的人进行一次深度对话'
                })
            elif category == 'money' and score < 60:
                recommendations.append({
                    'category': '金钱',
                    'suggestion': '建立预算，开始财务自由五要素实践',
                    'action': '记录本月每一笔支出'
                })
            elif category == 'digital' and score < 60:
                recommendations.append({
                    'category': '数字化',
                    'suggestion': '尝试无屏幕周六，减少屏幕时间',
                    'action': '本周六不碰电子设备'
                })
            elif category == 'health' and score < 60:
                recommendations.append({
                    'category': '健康',
                    'suggestion': '实践四大免费良药：饮食、锻炼、睡眠、阳光',
                    'action': '每天保证 8 小时睡眠和 30 分钟运动'
                })
            elif category == 'balance' and score < 60:
                recommendations.append({
                    'category': '价值平衡',
                    'suggestion': '每日自问：如何把五大价值融合在今天的生活中',
                    'action': '每晚记录五大价值实践情况'
                })
        
        return recommendations


def main():
    """主函数"""
    calculator = MinimalismScoreCalculator()
    
    # 示例评估数据
    sample_assessment = {
        'rooms': [
            {'necessities': 20, 'non_necessities': 30, 'waste': 10},
            {'necessities': 15, 'non_necessities': 25, 'waste': 15}
        ],
        'rules_applied': 3,
        'framework_values': ['自主性', '足够', '质量'],
        'surface_values': ['阅读', '写作'],
        'false_values': ['忙碌', '社交媒体'],
        'relationships': [
            {'elements': {'爱': 4, '信任': 5, '诚实': 4, '关怀': 4, '支持': 3, '专注': 3, '可靠': 4, '理解': 4}}
        ],
        'financial_elements': {
            'budget': 2,
            'invest': 1,
            'debt_free': 1,
            'minimalism': 2,
            'giving': 1
        },
        'impulse_buying_count': 3,
        'digital_practices': {
            'no_screen_saturday': True,
            'grayscale_mode': False,
            'bedtime_no_screen': True,
            'no_upgrade': True,
            'app_cleanup': False
        },
        'daily_screen_hours': 5,
        'health_practices': {
            'diet': 5,
            'exercise': 3,
            'sleep': 6,
            'sunlight': 4
        },
        'sleep_quality_practices': ['固定时间', '遮光帘', '无电子产品'],
        'five_values': {
            'health': 7,
            'relationships': 8,
            'passion': 6,
            'growth': 7,
            'contribution': 5
        }
    }
    
    scores = calculator.calculate_total_score(sample_assessment)
    recommendations = calculator.get_recommendations(sample_assessment, scores)
    
    print("=== 极简度评分报告 ===\n")
    print(f"总得分：{scores['total_score']}/100")
    print(f"等级：{scores['level']}\n")
    
    print("各维度得分：")
    for category, score in scores['category_scores'].items():
        print(f"  {category}: {score}")
    
    print("\n改进建议：")
    for rec in recommendations:
        print(f"  【{rec['category']}】{rec['suggestion']}")
        print(f"    行动：{rec['action']}\n")


if __name__ == '__main__':
    main()
