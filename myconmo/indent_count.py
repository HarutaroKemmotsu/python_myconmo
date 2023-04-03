#行頭のインデント数をカウントするためのモジュール
def count_indent(text):

    indent_counts = {}

    for line in text:

        # \nか!\n以外の行のインデントをカウント
        if not "\n" == line and not "!\n" == line:
            indent = len(line) - len(line.lstrip())

            # indent_counts辞書に{インデント数:行数}で入れていく
            if indent in indent_counts:
                indent_counts[indent] += 1
            else:
                indent_counts[indent] = 1

    # 最も多かったインデント数を返り値とする
    return max(indent_counts, key=indent_counts.get)