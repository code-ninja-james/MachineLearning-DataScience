#lists
li=[1,2,3,4,5]
li2=['a','b','c']
li3=[1,2,'a',True]


#list slicing
amazon_cart=[
            'notebooks',
            'sunglasses',
            'toys',
            'grapes'
            ]
amazon_cart[0]='laptop'  
new_cart=amazon_cart[:]
new_cart[0]='gum'  
print(new_cart)
print (amazon_cart[1:3])      
print(amazon_cart)