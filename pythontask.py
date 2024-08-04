def wordcount(text):
    text=text.replace("\n"," ").replace("It's","It is").replace('.',' ').replace(',',' ')
    text=text.lower()
    words=text.split()
    count={}
    for word in words:
        if word in count:
            count[word]+=1
        else:
            count[word]=1
    return count

text='''Got this panda plush toy for my daughter's birthday,
who loves it and takes it everywhere. It's soft and
super cute, and its face has a friendly look. It's
a bit small for what I paid though. I think there
might be other options that are bigger for the
same price. It arrived a day earlier than expected,
so I got to play with it myself before I gave it
to her.'''

print(wordcount(text))