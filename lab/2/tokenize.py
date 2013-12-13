import re, sys

def nested_search_and_replace(filename, container, pattern, repl):
    """Search and replace patterns contained in container with repl.

    filename -- name of the data file.
    container -- a compiled regex s.t. the first group is the contained text.
    pattern -- pattern to replace in the contained text.
    repl - replacement for the pattern in the contained text.

    The function stores the result in the file "tokenized." + filename.
    """
    data = open(filename).read()
    out = open("tokenized." + filename,"w")
    last = 0
    for m in container.finditer(data):
        out.write(data[last:m.start(1)])
        text = m.group(1)
        text = pattern.sub(repl, text)
        out.write(text)
        last = m.end(1)
    out.write(data[last:])

if __name__ == "__main__":
    text = re.compile(r"<TEXT>(.*?)</TEXT>", re.DOTALL | re.MULTILINE)
    punct = re.compile(r"[\x20-\x40\x5b-\x60\x7b-\x7e]+")
    nested_search_and_replace(sys.argv[1], text, punct, ' ')
