# vim:set et sts=4:
# -*- coding: utf-8 -*-

punct_map = (
    (u'',  (u'·', u'，', u'。', u'「', u'」', u'、', u'：', u'；', u'？', u'！',)),
    (u'!', (u'！', u'﹗', u'‼', u'⁉',)),
    (u'"', (u'“', u'”', u'＂',)),
    (u'#', (u'＃', u'﹟', u'♯',)),
    (u'$', (u'＄', u'€', u'﹩', u'￠', u'￡', u'￥',)),
    (u'%', (u'％', u'﹪', u'‰', u'‱', u'㏙', u'㏗',)),
    (u'&', (u'＆', u'﹠',)),
    (u'\'', (u'、', u'‘', u'’',)),
    (u'(', (u'（', u'︵', u'﹙',)),
    (u')', (u'）', u'︶', u'﹚',)),
    (u'*', (u'＊', u'×', u'※', u'╳', u'﹡', u'⁎', u'⁑', u'⁂', u'⌘',)),
    (u'+', (u'＋', u'±', u'﹢',)),
    (u',', (u'，', u'、', u'﹐', u'﹑',)),
    (u'-', (u'…', u'—', u'－', u'¯', u'﹉', u'￣', u'﹊', u'ˍ', u'–', u'‥',)),
    (u'.', (u'。', u'·', u'‧', u'﹒', u'．',)),
    (u'/', (u'／', u'÷', u'↗', u'↙', u'∕',)),
    (u'0', (u'０', u'0')),
    (u'1', (u'１', u'1')),
    (u'2', (u'２', u'2')),
    (u'3', (u'３', u'3')),
    (u'4', (u'４', u'4')),
    (u'5', (u'５', u'5')),
    (u'6', (u'６', u'6')),
    (u'7', (u'７', u'7')),
    (u'8', (u'８', u'8')),
    (u'9', (u'９', u'9')),
    (u':', (u'：', u'︰', u'﹕',)),
    (u';', (u'；', u'﹔',)),
    (u'<', (u'＜', u'〈', u'《', u'︽', u'︿', u'﹤',)),
    (u'=', (u'＝', u'≒', u'≠', u'≡', u'≦', u'≧', u'﹦',)),
    (u'>', (u'＞', u'〉', u'》', u'︾', u'﹀', u'﹥',)),
    (u'?', (u'？', u'﹖', u'⁇', u'⁈',)),
    (u'@', (u'＠', u'⊕', u'⊙', u'㊣', u'﹫', u'◉', u'◎',)),
    (u'A', (u'Ａ', u'A')),
    (u'B', (u'Ｂ', u'B')),
    (u'C', (u'Ｃ', u'C')),
    (u'D', (u'Ｄ', u'D')),
    (u'E', (u'Ｅ', u'E')),
    (u'F', (u'Ｆ', u'F')),
    (u'G', (u'Ｇ', u'G')),
    (u'H', (u'Ｈ', u'H')),
    (u'I', (u'Ｉ', u'I')),
    (u'J', (u'Ｊ', u'J')),
    (u'K', (u'Ｋ', u'K')),
    (u'L', (u'Ｌ', u'L')),
    (u'M', (u'Ｍ', u'M')),
    (u'N', (u'Ｎ', u'N')),
    (u'O', (u'Ｏ', u'O')),
    (u'P', (u'Ｐ', u'P')),
    (u'Q', (u'Ｑ', u'Q')),
    (u'R', (u'Ｒ', u'R')),
    (u'S', (u'Ｓ', u'S')),
    (u'T', (u'Ｔ', u'T')),
    (u'U', (u'Ｕ', u'U')),
    (u'V', (u'Ｖ', u'V')),
    (u'W', (u'Ｗ', u'W')),
    (u'X', (u'Ｘ', u'X')),
    (u'Y', (u'Ｙ', u'Y')),
    (u'Z', (u'Ｚ', u'Z')),
    (u'[', (u'「', u'［', u'『', u'【', u'｢', u'︻', u'﹁', u'﹃',)),
    (u'\\', (u'＼', u'↖', u'↘', u'﹨',)),
    (u']', (u'」', u'］', u'』', u'】', u'｣', u'︼', u'﹂', u'﹄',)),
    (u'^', (u'︿', u'〈', u'《', u'︽', u'﹤', u'＜',)),
    (u'_', (u'＿', u'╴', u'←', u'→',)),
    (u'`', (u'‵', u'′',)),
    (u'a', (u'ａ', u'a')),
    (u'b', (u'ｂ', u'b')),
    (u'c', (u'ｃ', u'c')),
    (u'd', (u'ｄ', u'd')),
    (u'e', (u'ｅ', u'e')),
    (u'f', (u'ｆ', u'f')),
    (u'g', (u'ｇ', u'g')),
    (u'h', (u'ｈ', u'h')),
    (u'i', (u'ｉ', u'i')),
    (u'j', (u'ｊ', u'j')),
    (u'k', (u'ｋ', u'k')),
    (u'l', (u'ｌ', u'l')),
    (u'm', (u'ｍ', u'm')),
    (u'n', (u'ｎ', u'n')),
    (u'o', (u'ｏ', u'o')),
    (u'p', (u'ｐ', u'p')),
    (u'q', (u'ｑ', u'q')),
    (u'r', (u'ｒ', u'r')),
    (u's', (u'ｓ', u's')),
    (u't', (u'ｔ', u't')),
    (u'u', (u'ｕ', u'u')),
    (u'v', (u'ｖ', u'v')),
    (u'w', (u'ｗ', u'w')),
    (u'x', (u'ｘ', u'x')),
    (u'y', (u'ｙ', u'y')),
    (u'z', (u'ｚ', u'z')),
    (u'{', (u'｛', u'︷', u'﹛', u'〔', u'﹝', u'︹',)),
    (u'|', (u'｜', u'↑', u'↓', u'∣', u'∥', u'︱', u'︳', u'︴', u'￤',)),
    (u'}', (u'｝', u'︸', u'﹜', u'〕', u'﹞', u'︺',)),
    (u'~', (u'～', u'﹋', u'﹌',)),
)
