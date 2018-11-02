message = 'Mobile phone is one of the recent invention of modern science .It has added  a new dimension of our life and to our communication system.  It is a telephone system that works without any wire. It can be moved easily and quickly from place to place. We can send message at any of time. We can also communicate with others at any place. It is easily portable. Though mobile phone we can send messages to distant place, play games and sports, know about time ,solve the work of calculation. Be aware of different kinds of news and views. At present the popularity of mobile phone is increasing.  The price of phone is also decreasing in comparison with the past. It has some drawbacks. Scientist have recently discovered that phone can cause cancer to the users. If a user continues his or her conversation more than two minutes, the blood brain barrier  gets damage. Besides ,it has become a fashion with the young people to keep the mobile phone. The terrorists are also using it to spread out the terrorism all around the world. The government should have an official restriction on using mobile phone by children and pregnant women.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)