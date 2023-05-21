---
layout: default
title: Estonian TTS with non-autoregressive Transformers
---

# Estonian TTS with non-autoregressive Transformers

**Paper:** [PDF](https://doi.org/10.22364/bjmc.2022.10.3.17)

**Web demo:** [Neurokõne](https://neurokone.ee/)

**Authors:** Liisa Rätsep, Rasmus Lellep, Mark Fishel

**Abstract:** While text-to-speech synthesis with non-autoregressive Transformers has achieved state-of-the-art quality
for many languages, the methodology of Estonian text-to-speech synthesis has not been revised for neural methods. This
paper evaluates the quality of Estonian text-to-speech with Transformer-based models using different language-specific
data processing steps. Additionally, we conduct a human evaluation to show how well these models can learn the patterns
of Estonian pronunciation, given different amounts of training data and varying degrees of phonetic information. Our
error analysis shows that using a simple multi-speaker approach can significantly decrease the number of pronunciation
errors, while some information can also be helpful to a smaller extent.

## 🎧 Evaluation samples

<table>
<thead>
  <tr>
    <th>Ground truth</th>
    <th>Ground truth (mel + vocoder)</th>
    <th>Baseline (student-teacher)</th>
    <th>Ext. alignments (single-speaker)</th>
    <th>Ext. alignments (multi-speaker)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="5">
      <br>
      Albert: <i>Teine põhjus meelemürke inimese nägemisväljast eemal hoida seostub meie lastega.</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/mos/27-gt-albert.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/27-gt-voc-albert.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/27-grapheme-albert.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/27-grapheme-kaldi-albert.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/27-grapheme-kaldi-multi-albert.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="5">
      <br>
      Indrek: <i>Ma õppisin teoloogiat, aga mitte selleks, et kantslisse tõusta ja jutlusi pidada.</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/mos/151-gt-indrek.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/151-gt-voc-indrek.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/151-grapheme-indrek.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/151-grapheme-kaldi-indrek.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/151-grapheme-kaldi-multi-indrek.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="5">
      <br>
      Kalev: <i>Ma tahan saada terveks ja loodan peagi tööle naasta", rääkis ta toona.</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/mos/34-gt-kalev.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/34-gt-voc-kalev.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/34-grapheme-kalev.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/34-grapheme-kaldi-kalev.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/34-grapheme-kaldi-multi-kalev.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="5">
      <br>
      Külli: <i>See lihtsalt pidi niiviisi olema, sest kõik muu mu ümber tundus nii tõeline.</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/mos/181-gt-kylli.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/181-gt-voc-kylli.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/181-grapheme-kylli.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/181-grapheme-kaldi-kylli.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/181-grapheme-kaldi-multi-kylli.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="5">
      <br>
      Liivika: <i>Lamasin öösel unetult Šarlote voodis, teki olin kõrvale heitnud, kuna oli liiga soe.</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/mos/159-gt-liivika.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/159-gt-voc-liivika.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/159-grapheme-liivika.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/159-grapheme-kaldi-liivika.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/159-grapheme-kaldi-multi-liivika.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="5">
      <br>
      Mari: <i>"Seda lihtsam on meil võimalik lahendada see kitsaskoht, vähendades nii mõnegi ajateenija olmemuresid ning aidates neil rohkem keskenduda väljaõppele", ütles Rannaveski.</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/mos/180-gt-mari.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/180-gt-voc-mari.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/180-grapheme-mari.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/180-grapheme-kaldi-mari.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/180-grapheme-kaldi-multi-mari.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="5">
      <br>
      Meelis: <i>"Oru Pearul on ometi õigus, kui ta ütleb, et kool kasvatab hobusevargaid."</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/mos/218-gt-meelis.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/218-gt-voc-meelis.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/218-grapheme-meelis.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/218-grapheme-kaldi-meelis.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/218-grapheme-kaldi-multi-meelis.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="5">
      <br>
      Peeter: <i>Kulunud pruuni ülikonda kandev mees toetas küünarnukid lauale, sättis käelaba lõuale toeks ja hakkas teda jõllitama.</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/mos/10-gt-peeter.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/10-gt-voc-peeter.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/10-grapheme-peeter.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/10-grapheme-kaldi-peeter.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/10-grapheme-kaldi-multi-peeter.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="5">
      <br>
      Tambet: <i>Nii sidus eesliajaja looma esijalad kokku, võttis koorma endale selga ja läks tagasi oma üüritud kohta värava juures.</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/mos/6-gt-tambet.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/6-gt-voc-tambet.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/6-grapheme-tambet.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/6-grapheme-kaldi-tambet.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/6-grapheme-kaldi-multi-tambet.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="5">
      <br>
      Vesta: <i>Juba homme läheb Tallinna Lauluväljakul suuremaks võidukihutamiseks!</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/mos/42-gt-vesta.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/42-gt-voc-vesta.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/42-grapheme-vesta.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/42-grapheme-kaldi-vesta.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/mos/42-grapheme-kaldi-multi-vesta.wav?raw=true"  controls preload></audio></td>
  </tr>
</tbody>
</table>

## 🎧 Robustness analysis samples

<table>
<thead>
    <tr>
        <th>Speaker</th>
        <th>Grapheme (single-speaker)</th>
        <th>Grapheme (multi-speaker)</th>
        <th>Vabamorf (single-speaker)</th>
        <th>Vabamorf (multi-speaker)</th>
        <th>Phoneme (single-speaker)</th>
        <th>Phoneme (multi-speaker)</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td colspan="5">
            <br>
            <i>Seega ei suudeta vere kaltsiumisisalduse langedes luudest kaltsiumi mobiliseerida, mistõttu selle sekretsioon piimaga väheneb.</i>
        </td>
    </tr>
    <tr>
        <td>Mari</td>
        <td><audio src="files/robustness/27-grapheme-kaldi-mari.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/27-grapheme-kaldi-multi-mari.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/27-vabamorf-kaldi-mari.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/27-vabamorf-kaldi-multi-mari.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/27-espeak-kaldi-mari.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/27-espeak-kaldi-multi-mari.wav?raw=true"  controls preload></audio></td>
    </tr>
    <tr>
        <td>Vesta</td>
        <td><audio src="files/robustness/27-grapheme-kaldi-vesta.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/27-grapheme-kaldi-multi-vesta.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/27-vabamorf-kaldi-vesta.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/27-vabamorf-kaldi-multi-vesta.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/27-espeak-kaldi-vesta.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/27-espeak-kaldi-multi-vesta.wav?raw=true"  controls preload></audio></td>
    </tr>
    <tr>
        <td>Meelis</td>
        <td><audio src="files/robustness/27-grapheme-kaldi-meelis.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/27-grapheme-kaldi-multi-meelis.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/27-vabamorf-kaldi-meelis.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/27-vabamorf-kaldi-multi-meelis.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/27-espeak-kaldi-meelis.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/27-espeak-kaldi-multi-meelis.wav?raw=true"  controls preload></audio></td>
    </tr>
    <tr>
        <td colspan="5">
            <br>
            <i>Suurem osa nõrgemakasvulistest kloonalustest on saadud liikidevahelise ristamise tulemusena.</i>
        </td>
    </tr>
    <tr>
        <td>Mari</td>
        <td><audio src="files/robustness/11-grapheme-kaldi-mari.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/11-grapheme-kaldi-multi-mari.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/11-vabamorf-kaldi-mari.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/11-vabamorf-kaldi-multi-mari.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/11-espeak-kaldi-mari.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/11-espeak-kaldi-multi-mari.wav?raw=true"  controls preload></audio></td>
    </tr>
    <tr>
        <td>Vesta</td>
        <td><audio src="files/robustness/11-grapheme-kaldi-vesta.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/11-grapheme-kaldi-multi-vesta.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/11-vabamorf-kaldi-vesta.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/11-vabamorf-kaldi-multi-vesta.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/11-espeak-kaldi-vesta.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/11-espeak-kaldi-multi-vesta.wav?raw=true"  controls preload></audio></td>
    </tr>
    <tr>
        <td>Meelis</td>
        <td><audio src="files/robustness/11-grapheme-kaldi-meelis.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/11-grapheme-kaldi-multi-meelis.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/11-vabamorf-kaldi-meelis.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/11-vabamorf-kaldi-multi-meelis.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/11-espeak-kaldi-meelis.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/11-espeak-kaldi-multi-meelis.wav?raw=true"  controls preload></audio></td>
    </tr>
    <tr>
        <td colspan="5">
            <br>
            <i>Islandi tüdrukute puhul oli pöördsõltuvus arvuti kasutamise rohkuse ja testi tulemuse vahel, teistes riikides oli seos pigem positiivne.</i>
        </td>
    </tr>
    <tr>
        <td>Mari</td>
        <td><audio src="files/robustness/35-grapheme-kaldi-mari.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/35-grapheme-kaldi-multi-mari.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/35-vabamorf-kaldi-mari.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/35-vabamorf-kaldi-multi-mari.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/35-espeak-kaldi-mari.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/35-espeak-kaldi-multi-mari.wav?raw=true"  controls preload></audio></td>
    </tr>
    <tr>
        <td>Vesta</td>
        <td><audio src="files/robustness/35-grapheme-kaldi-vesta.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/35-grapheme-kaldi-multi-vesta.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/35-vabamorf-kaldi-vesta.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/35-vabamorf-kaldi-multi-vesta.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/35-espeak-kaldi-vesta.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/35-espeak-kaldi-multi-vesta.wav?raw=true"  controls preload></audio></td>
    </tr>
    <tr>
        <td>Meelis</td>
        <td><audio src="files/robustness/35-grapheme-kaldi-meelis.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/35-grapheme-kaldi-multi-meelis.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/35-vabamorf-kaldi-meelis.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/35-vabamorf-kaldi-multi-meelis.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/35-espeak-kaldi-meelis.wav?raw=true"  controls preload></audio></td>
        <td><audio src="files/robustness/35-espeak-kaldi-multi-meelis.wav?raw=true"  controls preload></audio></td>
    </tr>
</tbody>
</table>
