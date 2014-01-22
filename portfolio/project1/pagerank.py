from functools import reduce

INIT_SCORE = 0.45/(0.45*5) # 0.2
TRANSITION_PROBABILITY = 0.25

class Node:
  def __init__(self, name, score = 0.45):
    self.name = name
    self.score = score
    self.in_links = []
    self.out_links = []

  def update_score(self):

    # For each in link, compute their score divided by their out links.
    rs = map(lambda node : node.score / len(node.out_links), self.in_links)

    # Compute the cumulative sume of the above.
    r = reduce(lambda x, y: x + y, rs, 0)

    # Compute the final page rank, taking transition probability into account.
    self.score = (1 - TRANSITION_PROBABILITY) + TRANSITION_PROBABILITY * r

  def __repr__(self):
    return "%s(%f)" % (self.name, self.score)

nodes = [Node("Yahoo"), Node("Bing"), Node("Facebook"),
            Node("Google"), Node("Twitter")]

nodes[0].in_links.append(nodes[3])
nodes[1].in_links.append(nodes[0])
nodes[1].in_links.append(nodes[2])
nodes[1].in_links.append(nodes[3])
nodes[2].in_links.append(nodes[4])
nodes[3].in_links.append(nodes[0])
nodes[4].in_links.append(nodes[1])
nodes[4].in_links.append(nodes[3])

nodes[0].out_links.append(nodes[1])
nodes[0].out_links.append(nodes[3])
nodes[1].out_links.append(nodes[4])
nodes[2].out_links.append(nodes[1])
nodes[3].out_links.append(nodes[0])
nodes[3].out_links.append(nodes[1])
nodes[3].out_links.append(nodes[4])
nodes[4].out_links.append(nodes[2])

for i in range(10):
  print("Iteration %d:" % (i+1))

  # Update scores.
  for node in nodes:
    node.update_score()

  # Normalize the scores.
  # Compute the sum of all scores.
  s = reduce(lambda s, node: s + node.score, nodes, 0)
  # Divide all scores by the sum.
  for node in nodes:
    node.score = node.score / s
    print(node)
  print("")

