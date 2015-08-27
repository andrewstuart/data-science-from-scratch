from __future__ import division
from collections import Counter, defaultdict

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
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


total_conns = sum(num_friends(u) for u in users)

dens = total_conns / len(users)

nfriends_by_id = [(user["id"], num_friends(user)) for user in users]

nfriends_by_id = sorted(nfriends_by_id,
                        key=lambda f: f[1],
                        reverse=True)

user_fofs = [(u["name"], u["id"], fof(u)) for u in users]

for u in user_fofs:
    my_fofs = [(key[1], u[2][key]) for key in u[2]]
    fof_formatted = "\n\t\t" + "\n\t\t".join("%s: %d friends in common" % (fof[0], fof[1]) for fof in my_fofs)
    print("%s may know:%s" % (u[0], fof_formatted))

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

i_by_u = defaultdict(list)
u_by_i = defaultdict(list)

for u, i in interests:
    i_by_u[u].append(i)
    u_by_i[i].append(u)
