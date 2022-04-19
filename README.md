# Node_Computation_with_Ray_Python

### Requirments:

- [Ray](https://docs.ray.io/en/latest/ray-overview/installation.html)

### Run:
```
qsub multi_node.pbs
```

### Change:

- Modules that are needed to be added which will vary as per your own case, i.e, change:

```
module load xyz
conda activate xyz
```

in `multi_node.pbs` and 'startWorkerNode.pbs' to run. 

- change `example_trainer.py` to your script.




#### You are most welcome to change the directives to `SLURM` and commit it.
