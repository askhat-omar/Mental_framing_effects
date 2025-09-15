# oTree Experiment Code

## 📖 About

This repository contains the **oTree experiment code** used in the paper:

**“Mental framing effects in dynamic portfolio choice”**  
_Authors_: Enrico De Giorgi, Askhat Omar, Thierry Post  
Published in *Journal of Behavioral and Experimental Finance*, 2025.  
DOI: [https://doi.org/10.1016/j.jbef.2025.101109](https://doi.org/10.1016/j.jbef.2025.101109) 

This repository provides a fully replicable version of the experiment as it was used in the published paper.

---

## 🔧 Installation & Usage

Create a new conda environment:

```bash
conda create -n experiment_replication python=3.10.8
conda activate experiment_replication
```

Clone the repository and install dependencies:

```bash
git clone https://github.com/askhat-omar/Mental_framing_effects.git
cd Mental_framing_effects
pip install -r requirements.txt
```

Run the experiment on your local machine:
```bash
otree devserver
```

