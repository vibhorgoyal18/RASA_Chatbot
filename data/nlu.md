## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- thank you

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir
- hi
- hello
- hola

## intent:deny
- nope
- no
- No, thanks
- Never mind
- Don't bother

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I'm looking for a place in the [north](location) of town
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- I’m hungry. Looking out for some good [mexican](cuisine) restaurants in [chandigarh](location)
- I’m hungry looking out for some good [mexican](cuisine) restaurants in [chandigarh](location)
- I’m hungry. Looking out for some good [mexican](cuisine) restaurants in [varanasi](location)
- I’m hungry looking out for some good [mexican](cuisine) restaurants in [varanasi](location)
- I’m hungry. Looking out for some good [italian](cuisine) restaurants in [agra](location)
- I’m hungry looking out for some good [italian](cuisine) restaurants in [agra](location)
- I’m hungry. Looking out for some good [north indian](cuisine) restaurants in [agra](location)
- I’m hungry looking out for some good [north indian](cuisine) restaurants in [agra](location)
- I’m hungry. Looking out for some good [south indian](cuisine) restaurants in [hyderabad](location)
- I’m hungry looking out for some good [south indian](cuisine) restaurants in [hyderabad](location)
- I’m hungry. Looking out for some good [italian](cuisine) restaurants
- I’m hungry. Looking out for some good [mexiacn](cuisine) restaurants
- I’m hungry. Looking out for some good [north indian](cuisine) restaurants
- I’m hungry. Looking out for some good [chinese](cuisine) restaurants
- I’m hungry. Looking out in [delhi](location) under [556](budgetmax)
- I’m hungry. Looking out in [delhi](location) over [565](budgetmin)
- I’m hungry. Looking out in [Delhi](location) within [678](budgetmax)
- I’m looking out in [Delhi](location) between [565](budgetmin) and [678](budgetmax)
- show me [chinese](cuisine) restaurants over [565](budgetmin)
- show me [chines](cuisine) restaurants over [600](budgetmin)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Mexican](cuisine)
- [American](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate](price:mid) price range with [british](cuisine) food for [four](people:4) people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- [Chinese](cuisine:chinese)
- show me restaurants
- [mumbai](location)
- [Italian](cuisine)
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- please show me a few [chinese](cuisine) restaurants in [north](location)
- less than [113](budgetmax)
- more than [113](budgetmin)

## synonym:4
- four

## synonym:Delhi
- New Delhi

## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:Mexican
- mexica
- taco
- mex
- spanish

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## synonym:low
- lower
- cheap
- cheaper
- <300
- < 300
- inexpensive
- less than 300
- Lesser than Rs. 300
- Lesser than Rs.300
- lesser than Rs. 300
- lesser than Rs.300
- Lesserthan Rs. 300
- lesserthan Rs. 300
- lesserthan Rs.300
- cost under 300
- Lesserthan Rs.300
- Less than Rs. 300
- Less than Rs.300
- less than Rs. 300
- less than Rs.300
- Lessthan Rs. 300
- lessthan Rs. 300
- lessthan Rs.300
- Lessthan Rs.300
- Lesser than 300
- lesser than 300
- Lesserthan 300
- lesserthan 300
- Less than 300
- less than 300
- lessthan 300
- Lessthan 300

## synonym:medium
- moderately
- moderate
- mid
- in range of 300 to 700
- 300 to 700
- 300-700
- Rs. 300 to 700
- Rs.300 to 700
- in range of 300 to 700  
- 300 to 700  
- 300-700 
- Rs. 300 to 700 
- Rs.300 to 700 

## synonym:high
- expensive
- costly
- More than 700
- >700
- > 700 
- greater than 700
- 700 or more
- luxury
- luxurious
- More than 700
- More than Rs.700
- More than Rs. 700
- more than 700
- more than Rs.700
- more than Rs. 700
- Morethan 700
- Morethan Rs.700
- Morethan Rs. 700
- morethan 700
- morethan Rs.700
- morethan Rs. 700
      
## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## regex:low
- ^<[0-9]{2,3}$

## regex:medium
- ^[0-9]{3}-[0-9]{3}$

## regex:high
- ^>[0-9]{3}$

## regex:greet_hey
- hey[^\\s]*

## regex:email
- ^[_A-Za-z0-9-\\+]+(\\.[_A-Za-z0-9-]+)*@[A-Za-z0-9-]+(\\.[A-Za-z0-9]+)*(\\.[A-Za-z]{2,})$

## regex:greet_hi
- hi[^\\s]*

## regex:greet_hello
- hello[^\\s]*
