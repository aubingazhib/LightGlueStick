    

<p align="center">
  <h1 align="center"><ins><i>LightGlueStick</i></ins><br><i>Fast and Robust Joint Point-Line Matching</i></h1>
  <h2 align="center">
    <p><i>Accepted at ICCVW 2025</i></p>
    <a href="#" align="center"><i>Paper (coming soon)</i></a>
  </h2>
  <p align="center"><em><i>Codebase under active development.</i></em></p>
</p>


<div align="center">
  <img src="assets/viz_4th_layer_exit_lines.png" alt="4th Layer Exit Lines" width="700">
  <br>
  <img src="assets/viz_7th_layer_exit_lines.png" alt="7th Layer Exit Lines" width="700">
</div>

<div align="center" style="max-width:800px; margin:auto;">
  <i>LightGlueStick adaptively adjusts its depth based on image difficulty, exiting after the 4th layer for the top image pair (easy) and the 7th layer for the bottom pair (hard). These pairs are processed in just 27ms and 42ms, respectively.</i>
</div>

## Training 🏋️
The training code is available in a separate repository, [GlueFactory](https://github.com/cvg/glue-factory). Within GlueFactory, you can not only train LightGlueStick, but also other deep matchers such as [LightGlue](https://github.com/cvg/LightGlue) and [GlueStick](https://github.com/cvg/GlueStick), use multiple feature extractors, line extractors, robust estimators, as well as run evaluations on multiple benchmarks.

## Licence 📜
Our code is licenced under [Apache-2.0 license](https://github.com/aubingazhib/LightGlueStick/blob/main/LICENSE).
However, bear in mind that it uses a SuperPoint backbone that has a 
[non-commercial licence](https://github.com/magicleap/SuperPointPretrainedNetwork/blob/master/LICENSE). Therefore, the overall system is non-commercial 😞.