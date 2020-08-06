


import numpy as np
from hmmlearn import hmm

states = ["bottle1", "bottle2", "bottle3"]
n_states = len(states)   # =3

observations = ["red", "yellow", "green"]
n_observations = len(observations)

initial_prob = np.array([0.4, 0.35, 0.25])

transition_prob = np.array([
  [0.3, 0.2, 0.5],
  [0.1, 0.3, 0.6],
  [0.7, 0.25, 0.05]
])

emission_prob = np.array([
  [0.8, 0.1, 0.1],
  [0.2, 0.4, 0.4],
  [0.15, 0.25, 0.6]
])


model = hmm.MultinomialHMM(n_components=n_states)
model.startprob_ = initial_prob
model.transmat_= transition_prob
model.emissionprob_= emission_prob

seen = np.array([[0,0,2,1,2]]).T        # 0: red;     1: yellow     2: green   => red red yellow green yellow
logprob, box = model.decode(seen, algorithm="viterbi")
seen = [0,0,2,1,2]
print("The candy picked:", ", ".join(map(lambda x: observations[x], seen)))
print("The bottle picked from:", ", ".join(map(lambda x: states[x], box)))

seen = np.array([[0,0,2,1,2]]).T
box2 = model.predict(seen)      # same as "viterbi"
seen = [0,0,2,1,2]
print("The candy picked:", ", ".join(map(lambda x: observations[x], seen)))
print("The bottle picked from:", ", ".join(map(lambda x: states[x], box2)))

seen = np.array([[0,0,2,1,2]]).T                  # P(rrygy) =?
print("ln(P(rrygy)) = " , model.score(seen))
print("P(rrygy) = ", np.exp(model.score(seen)))
