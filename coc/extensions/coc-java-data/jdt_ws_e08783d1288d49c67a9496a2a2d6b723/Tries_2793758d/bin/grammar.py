from gingerit.gingerit import GingerIt

text = 'Advantages of computer. : online chat. hand eye coordination. Access internet. ability to learn. fast. benefits society. access information.'

parser = GingerIt()
text=parser.parse(text)
print(text)
print(len(text['corrections']))
