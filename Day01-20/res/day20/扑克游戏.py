# 导入枚举类和随机数模块
from enum import Enum
import random

# 定义扑克牌花色枚举类
class Suite(Enum):
    SPADE, HEART, CLUB, DIAMOND = range(4)  # 分别对应黑桃、红桃、梅花、方块

# 注释掉的测试代码：打印所有花色及其值
# for suite in Suite:
#     print(f'{suite.name} = {suite.value}')

# 定义扑克牌类
class Card:
    
    def __init__(self, suite, face):
        self.suite = suite  # 花色（Suite枚举类型）
        self.face = face    # 牌面大小（1-13，分别对应A-K）

    def __repr__(self):
        suites = '♠♥♣♦'  # 花色符号对应的字符
        faces = ['','A','2','3','4','5','6','7','8','9','10','J','Q','K']  # 牌面大小对应的字符
        return f'{suites[self.suite.value]}{faces[self.face]}'  # 返回扑克牌的字符串表示（如♠A、♥10）
    
    def __lt__(self, other):
        # 定义卡片比较规则：先比较花色值，花色相同则比较牌面大小
        if self.suite == other.suite:
            return self.face < other.face
        return self.suite.value < other.suite.value

# 注释掉的测试代码：创建卡片实例并打印
# card1 = Card(Suite.SPADE, 5)
# card2 = Card(Suite.HEART, 10)
# print(card1)  # 打印卡片1的字符串表示
# print(card2)  # 打印卡片2的字符串表示

# 定义扑克类（一副牌）
class Poker:
    
    def __init__(self):
        # 初始化一副牌：包含4种花色，每种花色13张牌（A-K）
        self.cards = [Card(suite, face)
                      for suite in Suite
                      for face in range(1, 14)]
        self.current = 0  # 当前发牌位置指针

    def shuffle(self):
        self.current = 0  # 重置发牌位置
        random.shuffle(self.cards)  # 随机打乱牌序

    def deal(self):
        # 发牌：返回当前位置的牌，并将指针后移
        card = self.cards[self.current]
        self.current += 1
        return card
    
    @property
    def has_next(self):
        # 检查是否还有剩余牌未发
        return self.current < len(self.cards)

# 注释掉的测试代码：创建扑克实例并测试洗牌和发牌功能
# poker = Poker()
# print(poker.cards)  # 打印初始牌组（未洗牌）
# poker.shuffle()
# print(poker.cards)  # 打印洗牌后的牌组


# 定义玩家类
class Player:
    
    def __init__(self, name):
        self.name = name    # 玩家姓名
        self.cards = []     # 玩家手中的牌

    def get_one(self, card):
        # 玩家获取一张牌
        self.cards.append(card)

    def arrange(self):
        # 玩家整理手中的牌（按大小排序）
        self.cards.sort()


# 游戏主逻辑
# 创建一副扑克牌并洗牌
poker = Poker()
poker.shuffle()

# 创建4个玩家
players = [Player('东邪'), Player('西毒'), Player('南帝'), Player('北丐')]

# 发牌：每个玩家发13张牌（共52张，4人平均分配）
for _ in range(13):
    for player in players:
        player.get_one(poker.deal())

# 每个玩家整理自己的牌并打印
for player in players:
    player.arrange()
    print(f'{player.name}: ', end='')
    print(player.cards)
