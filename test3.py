def processor(writings):
    paragraphs = writings.split("\n\n")
    for i in range(len(paragraphs)):
        tmp = paragraphs[i].split("~~")
        for x in range(len(tmp) - 1):
            if x % 2 == 0:
                tmp[x] += "<del>"
            else:
                tmp[x] += "</del>"
        paragraphs[i] = "".join(tmp)
        lines = paragraphs[i].split("\n")
        isBlock = False
        for j in range(len(lines)):
            if lines[j].startswith(">"):
                lines[j] = lines[j][1::]
                if not isBlock:
                    lines[j] = "<blockquote>" + lines[j]
                    isBlock = True
            else:
                if isBlock:
                    lines[j-1] += "</blockquote>"
                    isBlock = False

        if isBlock:
            lines[-1] += "</blockquote>"

        paragraphs[i] = "<p>" + "</br>\n".join(lines) + "</p>\n"
    return "".join(paragraphs)












input = "This is a paragraph with a soft\n" + \
        "line break.\n\n" + \
        "This is another paragraph that has\n" + \
        "> Some text that\n" + \
        "> is in a\n" + \
        "> block quote.\n\n" + \
        "This is another paragraph with a ~~strikethrough~~ word."

print(processor(writings=input))

# expected = <p>This is a paragraph with a soft</br>
# line break.</p>
# <p>This is another paragraph that has</br>
# <blockquote> Some text that</br>
#  is in a</br>
#  block quote.</blockquote></p>
# <p>This is another paragraph with a <del>strikethrough</del> word.</p>