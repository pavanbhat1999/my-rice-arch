import language_check
tool = language_check.LanguageTool('en-US')
text = "This are flowers"
matches = tool.check(text)

print(len(matches))

print(matches)

print(language_check.correct(text,matches))
