from __future__ import division
from collections import Counter

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]


for user in users:
    user["friends"] = []

for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])

def num_friends(user):
    """How many friends does a user have?

    :user: @todo
    :returns: @todo

    """
    return len(user["friends"])

total_conns = sum(num_friends(u) for u in users)

dens = total_conns / len(users)

nfriends_by_id = [(user["id"], num_friends(user)) for user in users]

nfriends_by_id = sorted(nfriends_by_id,
       key=lambda f: f[1],
       reverse=True)

def not_the_same(u1, u2):
    """Returns whether the users share the same id

    :u1: User to compare
    :u2: User to compare
    :returns: Bool

    """
    return u1["id"] != u2["id"]

def not_already_friends(u1, u2):
    """two users are not already friends."""

    return all(not_the_same(f, u2) for f in u1["friends"])

def fof(user):
    return Counter((foaf["id"], foaf["name"])
                   for friend in user["friends"]
                   for foaf in friend["friends"]
                   if not_the_same(user, foaf)
                   and not_already_friends(user, foaf))

uar = [(u["name"], u["id"], fof(u)) for u in users]
t = '\n'.join(str(f) for f in uar)
print(t)
