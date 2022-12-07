guest_list = ['DanikaXIX', 'Nicki Minaj', 'Amy Lee']

print(f"Hi {guest_list[0]}, love your work, I'm a huge Dune and X-Men fan and would be honored to have you attend my annual intellectual gala as a distingushed guest.Thank you in advance.")

print(f"\nQueen {guest_list[1]} you have been selected to represent humanity in all Space for being so talented and perfect, peasants on Earth don't deserve the light that bring into the world.")

print(f"\nDear {guest_list[2]} you have been cordially invited to the  annual Music Genius awards for your amazing contribution to the music world with your incomparable talent and grace.")

change_guest = guest_list.pop(1)
print(f"\nDear honored guests, {change_guest} unfortunately won't be able to make it to our event, thank you for understandng.")

#print(change_guest)

guest_list.insert(1, 'Rihanna')
print(f"\n New guest list: {guest_list}") 

print(f"\n Dear {guest_list[0]}, you are cordially invited to the annual intellectual awards for your immeasurable contribution to the world of art.")

print(f"\n Dear {guest_list[1]}, you are cordially invited to the annual music world awards to honor your impeccable contribution to the music world.")

print(f"\n Dear {guest_list[2]}, you are cordially invited to the annual music genius awards for your ongoin countless, amazing contribution to the world of music and art.")

print("\n Dear distinguihed guests, it is with great pleasure that I announce our new list of guests, starting from the beginning, they are:")

guest_list.insert(0, "Dan Levy")

guest_list.insert(1, "Andre Lamoglia")

guest_list.append('Annie Murphy')
print(guest_list[:])

print(f"\n Dear {guest_list[0]} you are cordially invited to attend the annual tv and film genius awards for your incredible contributions to the writing and acting world")

print(f"\n Dear {guest_list[1]}, you are cordially invited to the annual tv and film genius awards for your exquisite contribution to the acting world.")

print(f"\n Dear {guest_list[5]}, you are cordially invited to the annual tv and film genius awards for your exquisite contribution to the acting world.")

print("\nDear Honored guests, \n\nit was with utmost dismay that I regrettably inform you that the music world, \nmusic genius and annual tv and film genius awards have all been cancelled, \nas such we I can only invite two guests. \nI send my sincere apologies to anyone negatively affected by this.")


print(guest_list)
shrinked_list = guest_list.pop(0)
print(f"\n{shrinked_list}, you're unfortunately uninvited to the award ceremony.")
shrinked_list = guest_list.pop()
print(f"\n{shrinked_list}, you're unfortunately uninvited to the award ceremony.")
shrinked_list = guest_list.pop(0)
print(f"\n{shrinked_list}, you've unfortunately been uninvited to the award ceremony, \nyou're still an icon though.")
shrinked_list = guest_list.pop(1)
print(f"\n{shrinked_list}, you've unfortunately been uninvited to the award ceremony, \nyou're still critically reviewed though.")
print(f"\n{guest_list}")
print(f"\nLady {guest_list[0]}, \nyou're still invited to the annual intellectual awards, \nto receive the award for outstanding, cosplay, excellent book club, \nperfect movie reviews and most importantly for you legendary X-Men and Game of Thrones series")
print(f"\n{guest_list[1]}, \nyou're still invited to the music genius awards for your astounding and remarkable contributions to the music world.")

del guest_list[1]
del guest_list[0]

print(f"\n{guest_list}")
