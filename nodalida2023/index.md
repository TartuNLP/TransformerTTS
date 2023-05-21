---
layout: nodalida
title: Neural Text-to-Speech Synthesis for Võro
---

# Neural Text-to-Speech Synthesis for Võro

**Paper:** [ACL Anthology](https://aclanthology.org/2023.nodalida-1.73/)

**Web demo:** [Neurokõne](https://neurokone.ee/)

**Authors:** Liisa Rätsep, Mark Fishel

**Abstract:** This paper presents the first high-quality neural text-to-speech (TTS) system for Võro, a minority
language spoken in Southern Estonia. By leveraging existing Estonian TTS models and datasets, we analyze whether common
low-resource NLP techniques, such as cross-lingual transfer learning from related languages or multitask learning, can
benefit our low-resource use case. Our results show that we can achieve high-quality Võro TTS without transfer learning
and that using more diverse training data can even decrease synthesis quality. While these techniques may still be
useful in some cases, our work highlights the need for caution when applied in specific low-resource scenarios, and it
can provide valuable insights for future low-resource research and efforts in preserving minority languages.

## 🎧 Evaluation samples

<table>
<thead>
  <tr>
    <th>Speaker</th>
    <th>Ground truth</th>
    <th>Ground truth (mel + vocoder)</th>
    <th>Single-speaker</th>
    <th>Single-speaker (transfer)</th>
    <th>Multi-speaker</th>
    <th>Multi-speaker (transfer)</th>
    <th>Multilingual</th>
    <th>Multilingual (transfer)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="8">
      <br>
      <i>Lell om esä veli.</i>
    </td>
  </tr>
  <tr>
    <td>Sulev</td>
    <td><audio src="files/gt/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00012.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00012.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00012.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00012.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00012.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00012.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00012.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00012.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td>Lee</td>
    <td><audio src="files/gt/EKI-voru-Hella_Voru_Hella_eki_et_hll_00012.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Hella_Voru_Hella_eki_et_hll_00012.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Hella_Voru_Hella_eki_et_hll_00012.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00012.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Hella_Voru_Hella_eki_et_hll_00012.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00012.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Hella_Voru_Hella_eki_et_hll_00012.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00012.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="8">
      <br>
      <i>Jah, a nii hää om, ku kiäki minno tuld hoitõn uut.</i>
    </td>
  </tr>
  <tr>
    <td>Sulev</td>
    <td><audio src="files/gt/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00025.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00025.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00025.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00025.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00025.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00025.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00025.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00025.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td>Lee</td>
    <td><audio src="files/gt/EKI-voru-Hella_Voru_Hella_eki_et_hll_00025.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Hella_Voru_Hella_eki_et_hll_00025.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Hella_Voru_Hella_eki_et_hll_00025.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00025.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Hella_Voru_Hella_eki_et_hll_00025.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00025.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Hella_Voru_Hella_eki_et_hll_00025.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00025.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="8">
      <br>
      <i>Kõik’, miä om muq külen kinniq, om muq uma ja midä inämb, tuud parõmb.</i>
    </td>
  </tr>
  <tr>
    <td>Sulev</td>
    <td><audio src="files/gt/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00031.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00031.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00031.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00031.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00031.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00031.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00031.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00031.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td>Lee</td>
    <td><audio src="files/gt/EKI-voru-Hella_Voru_Hella_eki_et_hll_00031.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Hella_Voru_Hella_eki_et_hll_00031.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Hella_Voru_Hella_eki_et_hll_00031.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00031.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Hella_Voru_Hella_eki_et_hll_00031.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00031.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Hella_Voru_Hella_eki_et_hll_00031.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00031.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="8">
      <br>
      <i>Tõnõkõrd käü inemine tuud puud kaeman.</i>
    </td>
  </tr>
  <tr>
    <td>Sulev</td>
    <td><audio src="files/gt/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00040.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00040.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00040.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00040.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00040.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00040.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00040.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00040.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td>Lee</td>
    <td><audio src="files/gt/EKI-voru-Hella_Voru_Hella_eki_et_hll_00040.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Hella_Voru_Hella_eki_et_hll_00040.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Hella_Voru_Hella_eki_et_hll_00040.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00040.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Hella_Voru_Hella_eki_et_hll_00040.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00040.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Hella_Voru_Hella_eki_et_hll_00040.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00040.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="8">
      <br>
      <i>Nä säädväq telgi üles, tegeväq tuld ja meisterdäseq vibu.</i>
    </td>
  </tr>
  <tr>
    <td>Sulev</td>
    <td><audio src="files/gt/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00059.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00059.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00059.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00059.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00059.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00059.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00059.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00059.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td>Lee</td>
    <td><audio src="files/gt/EKI-voru-Hella_Voru_Hella_eki_et_hll_00059.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Hella_Voru_Hella_eki_et_hll_00059.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Hella_Voru_Hella_eki_et_hll_00059.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00059.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Hella_Voru_Hella_eki_et_hll_00059.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00059.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Hella_Voru_Hella_eki_et_hll_00059.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00059.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="8">
      <br>
      <i>Üts’ sõbõr tuu ärqkuivadu tsiakõrva, tõnõ -hanna ja kolmas jürämiskundi.</i>
    </td>
  </tr>
  <tr>
    <td>Sulev</td>
    <td><audio src="files/gt/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00085.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00085.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00085.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00085.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00085.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00085.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00085.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00085.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td>Lee</td>
    <td><audio src="files/gt/EKI-voru-Hella_Voru_Hella_eki_et_hll_00085.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Hella_Voru_Hella_eki_et_hll_00085.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Hella_Voru_Hella_eki_et_hll_00085.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00085.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Hella_Voru_Hella_eki_et_hll_00085.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00085.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Hella_Voru_Hella_eki_et_hll_00085.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00085.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="8">
      <br>
      <i>Ku jummal’ taht, et võro kiil’ ärq häös, egaq sis tavalinõ inemine hinnäst sinnäq protsessi sekäq ei toheq!</i>
    </td>
  </tr>
  <tr>
    <td>Sulev</td>
    <td><audio src="files/gt/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00135.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00135.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00135.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00135.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00135.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00135.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00135.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00135.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td>Lee</td>
    <td><audio src="files/gt/EKI-voru-Hella_Voru_Hella_eki_et_hll_00135.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Hella_Voru_Hella_eki_et_hll_00135.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Hella_Voru_Hella_eki_et_hll_00135.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00135.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Hella_Voru_Hella_eki_et_hll_00135.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00135.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Hella_Voru_Hella_eki_et_hll_00135.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00135.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="8">
      <br>
      <i>Kreeka tekk’ Euruupalõ tagaotsagaq äräq!</i>
    </td>
  </tr>
  <tr>
    <td>Sulev</td>
    <td><audio src="files/gt/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00149.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00149.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00149.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00149.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00149.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00149.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00149.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Sulev_Voru_Sulev_eki_et_adp_00149.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td>Lee</td>
    <td><audio src="files/gt/EKI-voru-Hella_Voru_Hella_eki_et_hll_00149.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/gt-voc/EKI-voru-Hella_Voru_Hella_eki_et_hll_00149.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single/EKI-voru-Hella_Voru_Hella_eki_et_hll_00149.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/single-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00149.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro/EKI-voru-Hella_Voru_Hella_eki_et_hll_00149.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/vro-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00149.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix/EKI-voru-Hella_Voru_Hella_eki_et_hll_00149.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mix-ft/EKI-voru-Hella_Voru_Hella_eki_et_hll_00149.wav?raw=true"  controls preload></audio></td>
  </tr>
</tbody>
</table>