fin=open('config.txt')
for line in fin:
  word= line.strip()
  word=line.split()
  if word[0] == 'interface':
    x=word[1]
    #return (x)
  if word[0] == 'nameif': 
    y=word[1]
    #return (y)
    print([(x,y)])  

