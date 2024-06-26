comment = input('Enter your comment: ')

if(comment.find('Make a lot of money')!= -1 or comment.find('buy now')!= -1 or comment.find('subscribe this')!= -1 or comment.find('click this')!= -1 ):
    print('Spam')
else:
    print('Not Spam')