from BeautifulSoup import BeautifulSoup

html_doc = """
<html>
<head>
<title>my web title</title>
</head>
<body>
my web content
</body>
</html>
"""

soup = BeautifulSoup(html_doc)

print(soup.getText(" "))
