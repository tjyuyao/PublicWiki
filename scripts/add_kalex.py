import os.path as osp

html_path = osp.join(osp.dirname(osp.abspath(__file__)), "..", "docs", "index.html")

with open(html_path, "r+", encoding="utf-8") as f:
    content = f.read()
    i = content.find("</head>")
    content = content[:i] + '<script src="static/js/katex.min.js"></script>' + content[i:]
    f.seek(0)
    f.truncate()
    f.write(content)