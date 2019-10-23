import os
import sys
import pandas as pd
import plotnine as gg


from base.experiment import BaseExperiment
from finite_arm.agent_finite import FiniteBernoulliBanditTS
from finite_arm.env_finite import FiniteArmedBernoulliBandit

sys.path.append(os.getcwd())

n_arm = 3
probs = [0.7, 0.8, 0.9]
n_steps = 1000
seed = 0

agent = FiniteBernoulliBanditTS(n_arm)
env = FiniteArmedBernoulliBandit(probs)
experiment = BaseExperiment(agent, env, n_steps=1000, seed=seed, unique_id='example')

experiment.run_experiment()

print(experiment.results.head())

p = (gg.ggplot(experiment.results)
     + gg.aes(x='t', y='instant_regret', colour='unique_id')
     + gg.geom_line())
print(p)
