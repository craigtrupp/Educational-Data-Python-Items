""" We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, 
the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, 
in the files positive_words.txt and negative_words.txt. """


""" Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. 
You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), 
Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, 
and produce a graph of the Net Score vs Number of Retweets.

To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, 
and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.) """


def strip_punctuation(strg):
    wrd_strp = ''
    for char in strg:
        if char in punctuation_chars:
            continue # move on to next character and ignore punctuation
        else:
            wrd_strp += char
    return wrd_strp

def get_neg(strg):
    neg_words = 0
    strg = strg.strip() # remove any leading/trailing whitespace
    for word in strg.split():
        strp_word =  strip_punctuation(word) # strip any punctuation
        if strp_word.lower() in negative_words:
            neg_words += 1
    return neg_words

def get_pos(snt_strg):
    snt_strg = snt_strg.strip() # clean up white space
    count_pst = 0 # counter variable to accumulate positive words in passed sentence
    for word in snt_strg.split():
        word = strip_punctuation(word) # strip punctuation if positive word has character in front of the positive word
        if word.lower() in positive_words:
            count_pst += 1
    return count_pst

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

# Create Output File
outfile = open("resulting_data.csv", "w")
# output the header row
outfile.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
outfile.write('\n')
            
## open project_twitter csv file
with open('project_twitter_data.csv') as twt_d:
    lines = twt_d.readlines()[1:]
    lines_non_newlinechar = [x.replace('\n', '') for x in lines]
    for line in lines_non_newlinechar: # iterate through line of txt file
        line_items = line.split(',')
        retweets, replies = line_items[-2], line_items[-1]
        pos_score, neg_score = get_pos(line_items[0]), get_neg(line_items[0])
        net_score = pos_score - neg_score
        outfile.write('{},{},{},{},{}'.format(retweets, replies, pos_score, neg_score, net_score))
        outfile.write('\n')

outfile.close()
print('\n')


