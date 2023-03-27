import ipdb
from lib import *

# Test your code below...
# Creating Actors
actor1 = Actor("Vanessa Coelho")
actor2 = Actor("Skyler Pup")

# Creating Roles
role1 = Role("Superhero")
role2 = Role("SuperHungry")

# Creating Auditions
audition1 = Audition("New York", role1, actor1)
audition2 = Audition("Los Angeles", role1, actor2)
audition3 = Audition("Chicago", role2, actor1)
audition4 = Audition("San Francisco", role2, actor2)





# the below line allows us to stop & try stuff!
ipdb.set_trace()