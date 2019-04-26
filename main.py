import caller

r = caller.invoke('get', 'https://jsonplaceholder.typicode.com/posts')
print(r.text)