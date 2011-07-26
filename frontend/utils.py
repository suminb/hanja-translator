# -*- coding:utf-8 -*-

from dict import table as hanja_table
 
class Hangul:
    @staticmethod
    def separate(ch):
        """한글 자모 분리. 주어진 한글 한 글자의 초성, 중성 초성을 반환함."""
        uindex = ord(ch) - 0xac00
        jongseong = uindex % 28
        joongseong = ((uindex - jongseong) / 28) % 21
        choseong = ((uindex - jongseong) / 28) / 21
        
        return (choseong, joongseong, jongseong)
        
    @staticmethod
    def synthesize(choseong, joongseong, jongseong):
        """초성, 중성, 종성을 조합하여 완성형 한 글자를 만듦. 'choseong', 'joongseong', 'jongseong' are offsets. For example, 'ㄱ' is 0, 'ㄲ' is 1, 'ㄴ' is 2, and so on and so fourth."""
        return unichr(((((choseong) * 21) + joongseong) * 28) + jongseong + 0xac00)
        
    @staticmethod
    def dooeum(previous, current):
        p, c = Hangul.separate(previous), Hangul.separate(current)
        offset = 0
        
        # 한자음 '녀, 뇨, 뉴, 니', '랴, 려, 례, 료, 류, 리'가 단어 첫머리에 올 때 '여, 요, 유, 이', '야, 여, 예, 요, 유, 이'로 발음한다.
        if current in (u'녀', u'뇨', u'뉴', u'니'):
            offset = 9
        elif current in (u'랴', u'려', u'례', u'료', u'류', u'리'):
            offset = 6
        # 한자음 '라, 래, 로, 뢰, 루, 르'가 단어 첫머리에 올 때 '나, 내, 노, 뇌, 누, 느'로 발음한다.
        elif current in (u'라', u'래', u'로', u'뢰', u'루', u'르'):
            offset = -3
        # 모음이나 ㄴ 받침 뒤에 이어지는 '렬, 률'은 '열, 율'로 발음한다.
        elif current in (u'렬', u'률') and p[2] in (0, 2):
            offset = 6
    
        return Hangul.synthesize(c[0]+offset, c[1], c[2])
        
    @staticmethod
    def is_hangul(ch):
        return ord(ch) >= 0xac00 and ord(ch) <= 0xd7a3

class Hanja:
    """두음법칙에 관련된 내용은 http://ko.wikipedia.org/wiki/%EB%91%90%EC%9D%8C_%EB%B2%95%EC%B9%99 를 참고했음."""
    
    @staticmethod
    def translate_syllable(previous, current):
        if current in hanja_table:
            if previous in hanja_table: 
                return hanja_table[current]
            else:
                return Hangul.dooeum(previous, hanja_table[current])

        return current
        
    @staticmethod
    def translate(text):
        return ''.join(map(Hanja.translate_syllable, u' '+text[:-1], text))
       