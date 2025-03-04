## :page_facing_up: On the Unknowable Limits to Prediction :page_facing_up:

![coverage](https://img.shields.io/badge/ResponseLetter-yellow)
[![Generic badge](https://img.shields.io/badge/GNU3.0-purple.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Maintained-brightgreen.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/BuildPassing-orange.svg)](https://shields.io/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14674893.svg)](https://doi.org/10.5281/zenodo.14674893)

---

#### Introduction

This is a place to hold some simple matplotlib code which creates hypothetical learning curves. These learning curves live within a new framework which [Jiani Yan](https://github.com/vallerrr) and I have created which is in response to the recent rise in the application of machine and deep learning methods. Our preprint is entitled `On the Unknowable Limits to Prediction', and can be found on arXiV here:

<div align="center">
  <a href="https://arxiv.org/abs/2411.19223">arxiv.org/abs/2411.19223</a>
</div>

A very quick standfirst for this work is:

> We critique the classic dichotomization of prediction error into reducible and irreducible components, noting that certain types of error can be eliminated at differential speeds. We propose an improved analytical framework that better distinguishes epistemic from aleatoric uncertainty, emphasizing that predictability depends on information sets. We also caution against premature claims of unpredictability.


#### Running the code

See `./src` for code which makes the figure, and `./output` for the figure itself. Within `./src`, we have both interactive jupyter notebooks (the `.iypnb`s) which make the two figures in the Correspondence (Figure 1 and Supplementary Information Figure 1), and a Python file (the `figure_helpers.py`) which contains helper functions. A `requirements.txt` accompanies this repository, and can be used to install the necessary packages. It contains nothing more than a standard Anaconda build.

#### Citing this work

If you would be interested in citing this work, please use the following BibTeX entry:

```bibtex
@misc{yan2024unknowablelimitsprediction,
      title={On the Unknowable Limits to Prediction}, 
      author={Jiani Yan and Charles Rahal},
      year={2025},
      journal={Nat Comput Sci},
      url={https://doi.org/10.1038/s43588-025-00776-y), 
}
```


or copy and paste this Chicago style citation:

>Yan, Jiani, and Charles Rahal. "On the Unknowable Limits to Prediction.", Nat Comput Sci (2025). https://doi.org/10.1038/s43588-025-00776-y.


#### Data Availability Statement

There is no data.

#### License

This work is made available under a GNU General Public License v3.0.

