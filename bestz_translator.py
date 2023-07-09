from tokenize import tokenize, untokenize


def translate(file: str):
    key_words: dict = {
        'tosey': 'if',
        'makeen': 'else',
        'aslong': 'for',
        'area': 'range',
        'show_dem': 'print',
        'write_sumtin': 'input',
        'na_true': 'True',
        'na_lie': 'False'
    }

    with open(file, 'rb') as source_code:
        tokens: list = []

        for token in tokenize(source_code.readline):
            if token.string in key_words:
                t = (token.type, key_words[token.string])
            else:
                t = (token.type, token.string)

            tokens.append(t)

    code = untokenize(tokens).decode('utf-8')
    exec(code)



