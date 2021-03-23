"""
Write a function that returns the number of users in a chatroom based on the
following rules:

  1. If there is no one, return `"no one online"`.
  2. If there is 1 person, return `"user1 online"`.
  3. If there are 2 people, return `user1 and user2 online"`.
  4. If there are `n>2` people, return the first two names and add `"and n-2 more online"`.

For example, if there are 5 users, return:

    "user1, user2 and 3 more online"

### Examples

    chatroom_status([]) ➞ "no one online"
    
    chatroom_status(["paRIE_to"]) ➞ "paRIE_to online"
    
    chatroom_status(["s234f", "mailbox2"]) ➞ "s234f and mailbox2 online"
    
    chatroom_status(["pap_ier44", "townieBOY", "panda321", "motor_bike5", "sandwichmaker833", "violinist91"])
    ➞ "pap_ier44, townieBOY and 4 more online"

### Notes

N/A

"""

def chatroom_status(users):
  return "no one online" if not users else "{} online".format(users[0]) if len(users) == 1 else "{} and {} online".format(users[0], users[1]) if len(users) == 2 else "{}, {} and {} more online".format(users[0], users[1], len(users) - 2)

