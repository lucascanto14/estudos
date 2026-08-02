##>>> print("Languages:\nPython\nC\nJavascript")
##Languages:
##Python
##C
##Javascript
##>>> print("Languages:\n\tPython\n\tC\n\tJavascript")
##Languages:
##        Python
##        C
##        Javascript
##>>> favorite_language = 'python '
##>>> favorite_language
##'python '
##>>> favoritelanguage.rstrip()
## (most recent call last):
##  File "<stdin>", line 1, in <module>
##    favoritelanguage.rstrip()
##^^^^^^^^^^^^^^^^
##NameError: name 'favoritelanguage' is not defined. Did you mean: 'favorite_language'?
## favorite_language.rstrip()
##'python'
##>>> favorite_language.strip() 
##python'
##>>> favorite_language = ' python '
## favorite_language.strip()     
##'python'
##>>> x = 'https://nostarch.com'
##>>> x.removeprefix('https://')
##'nostarch.com'