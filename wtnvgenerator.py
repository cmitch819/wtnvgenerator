import random as r
import pytumblr

client = pytumblr.TumblrRestClient(
    'GoifuYwhFIv2UC5descfS9G6lhkhDQlEnUSZRqjPDSJXPwZoiv',
    'eUQllKGJx6wKR87q01tKK9UZ7iIiqkbv40Vv1Y6PwMbfUvr9d2',
    'Rc3VbCCh8Askjx4Ec0EUKYG6omUtTr3WtFD5LREZCZOn6TFVXb',
    'DbJ2AjdD2ZlINhbIFXuwdlN14dwM6w4gZNaLkMuH5y8Gpqy1yQ'
)  # Authenticate via OAuth

client.info()  # Make the request


def stripThe(word):
    newWord = word.split(" ")
    if newWord[0] == 'the' or newWord[0] == 'a':
        newWord.remove(newWord[0])
    word = ""
    for k in newWord:
        word += k + " "
    return word


file1 = open("wtnvformats.txt", "r")  # open files and read lines
formats = file1.readlines()
file2 = open("wtnvnouns.txt", "r")
nouns = file2.readlines()
file3 = open("wtnvaddons.txt", "r")
addons = file3.readlines()
file4 = open("wtnvprefixes.txt", "r")
prefixes = file4.readlines()
file5 = open("wtnvverbs.txt", "r")
verbs = file5.readlines()
adjectives = ["pleased", "confused", "afraid", "concerned"]  # adjectives list

def generate():
    tagList = ["wtnv", "welcome to night vale"]
    post = r.choice(formats)
    if "but go off" in post:
        tagList.append("go off meme")
    counter = 0
    for i in range(len(post)):  # iterate through post and count how many replaces there are
        if post[i] == '#':
            if post[i + 1] == 'r' or post[i + 1] == 'k' or post[i + 1] == 'a' or post[i + 1] == 'v':
                counter += 1
    if counter > 1 and 'look around you' not in post and 'who let you in here' not in post and "is usually fine" not in \
            post and "is an awesome" not in post and "don't kill people" not in post and 'i love you' not in post and \
            'the password' not in post and 'you cannot escape it' not in post and 'byproducts' not in post and \
            'you are always' not in post:
        split = post.split('#')
        splitString = ""
        for i in range(len(split)):
            if split[i] == 'keepthe':
                insert = r.choice(nouns)
                if '#s' in post and insert[len(insert)-2] == 's' and 'los' not in insert and 'Hiram' not in insert:
                    insert = insert.replace(insert[len(insert) - 2], "")
                splitString += insert.strip()
            elif split[i] == 'replace':
                insert = r.choice(nouns)
                if '#s' in post and insert[len(insert)-2] == 's' and 'los' not in insert and 'Hiram' not in insert:
                    insert = insert.replace(insert[len(insert)-2], "")
                insert = stripThe(insert)
                splitString += insert.strip()
            elif split[i] == 'adjective':
                insert = r.choice(adjectives)
                splitString += insert.strip()
            elif split[i] == 'verb':
                insert = r.choice(verbs)
                if 'keepthe' in insert:
                    noun = r.choice(nouns)
                    insert = insert.replace('#keepthe#', noun.strip())
                splitString += insert.strip()
            elif split[i] == 'verb-ing':
                insert = r.choice(verbs)
                if 'keepthe' in insert:
                    noun = r.choice(nouns)
                    insert = insert.replace('#keepthe#', noun.strip())
                if " " in insert:
                    insertTemp = insert.split(" ")
                    insert = ""
                    for j in range(len(insertTemp)):
                        if j == 1:
                            insert += 'ing'
                        insert += ' ' + insertTemp[j]
                else:
                    insert = insert.strip()
                    insert += "ing"
                splitString += insert.strip()
            else:
                splitString += split[i]
    else:
        insert = r.choice(nouns)
        if 'keepthe' in post:
            if '#s' in post and insert[len(insert)-2] == 's' and 'los' not in insert and 'Hiram' not in insert:
                insert = insert.replace(insert[len(insert)-2], "")
            post = post.replace('#keepthe#', insert.strip())
        elif 'replace' in post:
            if '#s' in post and insert[len(insert)-2] == 's' and 'los' not in insert and 'Hiram' not in insert:
                insert = insert.replace(insert[len(insert)-2], "")
            insert = stripThe(insert)
            post = post.replace('#replace#', insert.strip())
        else:
            insert = r.choice(verbs)
            if 'keepthe' in insert:
                noun = r.choice(nouns)
                insert = insert.replace('#keepthe#', noun)
            if 'verb-ing' in post:
                if " " in insert:
                    insertTemp = insert.split(" ")
                    insert = ""
                    for i in range(len(insertTemp)):
                        if i == 1:
                            insert += 'ing'
                        insert += ' ' + insertTemp[i]
                else:
                    insert = insert.strip()
                    insert += "ing"
                post = post.replace('#verb-ing#', insert.strip())
            else:
                post = post.replace('#verb#', insert.strip())
        splitString = post

    number = r.randint(1, 15)
    if number < 3:  # if the number is less than 3
        addon = r.choice(addons)  # choose a random add on for the end of the post
        if '#replace#' in addon:  # if the prefix has a replace spot
            fuckPEP8 = r.choice(nouns)  # choose random noun, called fuckPEP8 because PEP 8 hates my code for no reason
            addon = (addon.replace('#replace#', fuckPEP8.strip())).strip()  # replace prefix replace with random noun
        splitString = splitString + addon.strip()
    elif number > 13:  # if number greater than 12
        prefix = r.choice(prefixes)  # choose random prefix
        if '#replace#' in prefix:  # if the prefix has a replace spot
            fuckPEP8 = r.choice(nouns)  # choose random noun, called fuckPEP8 because PEP 8 hates my code for no reason
            prefix = prefix.replace('#replace#', fuckPEP8.strip())  # replace prefix replace with random noun
        splitString = prefix.strip() + " " + splitString
    elif number == 10:
        addon = r.choice(addons)  # choose a random add on for the end of the post
        if '#replace#' in addon:  # if the prefix has a replace spot
            fuckPEP8 = r.choice(nouns)  # choose random noun, called fuckPEP8 because PEP 8 hates my code for no reason
            addon = (addon.replace('#replace#', fuckPEP8.strip())).strip()  # replace prefix replace with random noun
        splitString = splitString + addon.strip()
        prefix = r.choice(prefixes)  # choose random prefix
        if '#replace#' in prefix:  # if the prefix has a replace spot
            fuckPEP8 = r.choice(nouns)  # choose random noun, called fuckPEP8 because PEP 8 hates my code for no reason
            prefix = prefix.replace('#replace#', fuckPEP8.strip())  # replace prefix replace with random noun
        splitString = prefix.strip() + " " + splitString
    splitString = splitString.replace("\n", "")
    if "spider" in splitString or "tarantula" in splitString:
        tagList.append("spider mention")
    print(splitString)
    client.create_text("wtnvgenerator", state="queue", body=splitString, tags=tagList)


for l in range(20):
    generate()

file1.close()  # close files
file2.close()
file3.close()
file4.close()
file5.close()
