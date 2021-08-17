import calendar_modify


def train14():
    lyrics = """        歌唱祖国
            --王莘
    五星红旗迎风飘扬
    胜利歌声多么响亮
    歌唱我们亲爱的祖国
    从今走向繁荣富强
    歌唱我们亲爱的祖国
    从今走向繁荣富强
    越过高山 越过平原
    跨过奔腾的黄河长江
    宽广美丽的土地
    是我们亲爱的家乡
    英雄的人民站起来了
    我们团结友爱坚强如钢
    五星红旗迎风飘扬
    胜利歌声多么响亮
    歌唱我们亲爱的祖国
    从今走向繁荣富强
    歌唱我们亲爱的祖国
    从今走向繁荣富强
    我们勤劳 我们勇敢
    独立自由是我们的理想
    我们战胜了多少苦难
    才得到今天的解放
    我们爱和平
    我们爱家乡
    谁敢侵犯我们就叫他灭亡
    五星红旗迎风飘扬
    胜利歌声多么响亮
    歌唱我们亲爱的祖国
    从今走向繁荣富强
    歌唱我们亲爱的祖国
    从今走向繁荣富强
    东方太阳 正在升起
    人民共和国正在成长
    我们领袖毛泽东
    指引着前进的方向
    我们的生活天天向上
    我们的前程万丈光芒
    五星红旗迎风飘扬
    胜利歌声多么响亮
    歌唱我们亲爱的祖国
    从今走向繁荣富强
    歌唱我们亲爱的祖国
    从今走向繁荣富强"""
    print(lyrics)


def slope(p1, p2):
    k = (p2[1] - p1[1]) / (p2[0] - p1[0])
    return k


def intercept(p1, p2):
    k = slope(p1, p2)
    y0 = p1[1] - k * p1[0]
    return y0


def train15():
    p1, p2 = input("input the two point p1, p2(tuple):").split(";")
    p1 = p1.replace(" ", "")
    p2 = p2.replace(" ", "")
    p1 = (float(p1[1]), float(p1[-2]))
    p2 = (float(p2[1]), float(p2[-2]))
    # print(p1, p2)
    k = slope(p1, p2)
    y0 = intercept(p1, p2)
    print("the k is: {}, the y0 is: {}".format(k, y0))


def train16():
    calendar_modify.main()


# train14()
# train15()
train16()
