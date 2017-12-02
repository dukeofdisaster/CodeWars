# Define a function that takes in a message and deletes a specified
# hashtag from that message. If the hashtag occurs multiple times,
# only delete the first occurence of the specified hashtag. Otherwise
# if there is NO occurence of the hashtag, simply return the message

# below we have the novice solution
def omit_hashtag(message, hashtag):
    if hashtag in message:
        return message.replace(hashtag, "", 1)
    return message


# The expert solution is a one iner
def omitHashtag(message, hashtag):
    return message.replace(hashtag, '' , 1) if hashtag in message else message

# good practice for looking for more concise ways to do the problems
# is think of them in plain english
# we're goign to return the message with the hashtag replaced once if the
# hashtag is in the message otherwise we'll just return the message
