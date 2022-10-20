
def lexical():
    lexemList = []

    key = ["begin", "end", "var", "integer", "while", "do"]
    S_oper = [">", "<", "=",  "+", ';', '.', ':', '*']
    s_oper = ["<=",">=", "<>", ":="]

    with open ("text", "r") as file:
        for line in file:
            len_line = len(line)
            i = 0
            var = ""
            while i < len_line:
                if line[i] not in S_oper and line[i] != " " and line[i] != "\n":
                    var += line[i]
                elif var != "":
                    if var in key:
                        lexemList.append([0, var])
                    elif not var[0].isdigit():
                        lexemList.append([1, var])
                    elif var.isdigit():
                        lexemList.append([2, var])
                    else:
                        print("Лексический анализ - ошибка")
                        exit()
                    var = ""
                if i < len(line) - 1:
                    if line[i:i+2] in s_oper:
                        lexemList.append([3, line[i:i+2]])
                        i += 1
                    elif line[i] in S_oper:
                        lexemList.append([3, line[i]])
                elif line[i] in S_oper:
                        lexemList.append([3, line[i]])
                i += 1

    with open("lexem.txt", "w") as f:
        for item in lexemList:
            f.write("%s\n" % item)
    return lexemList

lexical()
