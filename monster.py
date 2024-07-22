class Monster:
    def __init__(self, h, a, b, c, d, s, personality, characteristic):
        self.h = h #HP
        self.a = a #攻撃
        self.b = b #防御
        self.c = c #特攻
        self.d = d #特防
        self.s = s #素早さ
        self.personality = personality #性格 personality
        self.characteristic = characteristic #特性 characteristic 


class Atyamo(Monster):
    def __init__(self, name, h, a, b, c, d, s, personality, characteristic):
        super().__init__(h, a, b, c, d, s, personality, characteristic)
        self.name = name

    def AtyamoPrint(self):
        print('名前:', self.name)
        print('HP:', self.h)
        print('攻撃:', self.a)
        print('防御', self.b)
        print('特攻', self.c)
        print('特防', self.d)
        print('素早さ:', self.s)
        print('性格', self.personality)
        print('特性', self.characteristic)

callAtyamo = Atyamo('アチャモ', 9, 6, 3, 4, 6, 5, "ゆうかん", 'かそく')

callAtyamo.AtyamoPrint()

#名前,HP,攻撃,防御,特攻,特防,素早さ,の順で出力してね
