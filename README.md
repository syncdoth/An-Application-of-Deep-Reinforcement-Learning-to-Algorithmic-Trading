# An Application of Deep Reinforcement Learning to Algorithmic Trading
Experimental code supporting the results presented in the scientific research paper:
> Thibaut Théate and Damien Ernst. "An Application of Deep Reinforcement Learning to Algorithmic Trading." (2020).
> [[arxiv]](https://arxiv.org/abs/2004.06627)

# Personal Implication of Reinforcement Learning in different aspects, such as Deep Q Learning, usage of CNN in Reinforcement Learning.
# HKUST AIDL Society November - December Algorithmic Trading Project


# Dependencies

The dependencies are listed in the text file "requirements.txt":
* Python >= 3.6.8
* Pytorch >= 1.7.1
* Tensorboard
* Gym
* Numpy
* Pandas
* Matplotlib
* Scipy
* Seaborn
* Statsmodels
* Requests
* Pandas-datareader
* TQDM
* Tabulate




# Usage

Simulating (training and testing) a chosen supported algorithmic trading strategy on a chosen supported stock is performed by running the following command:

```bash
python main.py -strategy STRATEGY -stock STOCK
# Currently working with Apple, Samsung Electronics
```

with:
* STRATEGY being the name of the trading strategy (by default TDQN),
* STOCK being the name of the stock (by default Apple).

The performance of this algorithmic trading policy will be automatically displayed in the terminal, and some graphs will be generated and stored in the folder named "Figures".



# Citation

If you make use of this experimental code, please cite the associated research paper:

```
@inproceedings{Theate2020,
  title={An Aplication of Deep Reinforcement Learning to Algorithmic Trading},
  author={Theate, Thibaut and Ernst, Damien},
  year={2020}
}
```
