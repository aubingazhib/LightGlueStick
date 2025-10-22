    

<p align="center">
  <h1 align="center"><ins><i>LightGlueStick</i></ins><br><i>Fast and Robust Joint Point-Line Matching</i></h1>
  <h3 align="center"><i>Accepted at ICCVW 2025</i></h3>
  <p align="center">
    <a href="https://arxiv.org/abs/2510.16438" target="_blank">
      <img src="https://img.shields.io/badge/arXiv-2510.16438-b31b1b.svg?logo=arxiv&logoColor=white" alt="arXiv link">
    </a>
  </p>
</p>


<div align="center">
  <img src="assets/viz_4th_layer_exit_lines.png" alt="4th Layer Exit Lines" width="700">
  <br>
  <img src="assets/viz_7th_layer_exit_lines.png" alt="7th Layer Exit Lines" width="700">
</div>

<div align="center" style="max-width:800px; margin:auto;">
  <i>LightGlueStick adaptively adjusts its depth based on image difficulty, exiting after the 4th layer for the top image pair (easy) and the 7th layer for the bottom pair (hard). These pairs are processed in just 27ms and 42ms, respectively.</i>
</div>

## Installation
To install the software follow these instructions (tested on Ubuntu)
```bash
git clone https://github.com/aubingazhib/LightGlueStick.git
cd LightGlueStick
python -m venv venv
source venv/bin/activate
pip install .
```

## LightGlueStick Inference
You can match features with:

```bash
python -m lightgluestick.run -img1 assets/img1.jpg -img2 assets/img2.jpg
```
## Training 🏋️
The training code is available in a separate repository, [GlueFactory](https://github.com/cvg/glue-factory). Within GlueFactory, you can not only train LightGlueStick, but also other deep matchers such as [LightGlue](https://github.com/cvg/LightGlue) and [GlueStick](https://github.com/cvg/GlueStick), use multiple feature extractors, line extractors, robust estimators, as well as run evaluations on multiple benchmarks.

## Licence 📜
Our code is licenced under [Apache-2.0 license](https://github.com/aubingazhib/LightGlueStick/blob/main/LICENSE).
However, bear in mind that it uses a SuperPoint backbone that has a 
[non-commercial licence](https://github.com/magicleap/SuperPointPretrainedNetwork/blob/master/LICENSE). Therefore, the overall system is non-commercial 😞.

## BibTeX Citation
Please consider citing the following papers if you found this code useful:

```bibtex
@InProceedings{Ubingazhibov_2025_ICCV,
    author    = {Ubingazhibov, Aidyn and Pautrat, R{\'e}mi and Su{\'a}rez, Iago and Liu, Shaohui and Pollefeys, Marc and Larsson, Viktor},
    title     = {LightGlueStick: a Fast and Robust Glue for Joint Point-Line Matching},
    booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV) Workshops},
    month     = {October},
    year      = {2025},
    pages     = {7244-7254}
}
```
