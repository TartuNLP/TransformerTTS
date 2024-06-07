---
layout: default
title: Enabling Conversational Speech Synthesis using Noisy Spontaneous Data
---

# Enabling Conversational Speech Synthesis using Noisy Spontaneous Data

**Paper:** _Accepted for publication at INTERSPEECH 2024_

**Authors:** Liisa Rätsep, Rasmus Lellep, Mark Fishel

**Abstract:** In recent years, the quality of text-to-speech models has increased significantly, but most text-to-speech
solutions are trained on datasets of read speech and do not cover conversational speaking styles due to the lack of
suitable training data. This paper explores options for creating multi-style speech synthesis using speech recognition
datasets that contain samples of spontaneous speech and dialogues but may also include background noise and an
insufficient number of samples per speaker. We develop an Estonian multi-speaker TTS system that increases prosodic
variability on conversational inputs while still being able to synthesize read speech. We show that our proposed
approach can be used to train models that can be controlled to produce conversational speech with little compromise on
audio quality. We also highlight a potential multilingual use case to achieve cross-lingual speaker and style transfer
to low-resource languages that lack stylistically diverse speech corpora.

## 🎧 Evaluation samples

### Conversational sentences (style transfer)

The top row of each sentence uses a speaker from a neutral dataset, while the bottom row uses a speaker from a fiction
dataset.

<table>
<thead>
  <tr>
    <th>Ground truth</th>
    <th>Ground truth (mel + vocoder)</th>
    <th>Baseline (multi-speaker)</th>
    <th>Multi-speaker + spontaneous data</th>
    <th>Multi-speaker decoder</th>
    <th>Multi-style</th>
    <th>Multi-style, restricted</th>
    <th>Multi-style, 2 stage</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="8">
      Oled sa enda pealt tähele pannud või, või märganud ikkagi midagi konkreetset, mida sa oled teada saanud või millele üle sa oled lapsevanemaks olemise juures jõudnud imestada?<br>
        <i>Have you noticed anything about yourself or, or noticed anything specific, that you've learned or that has surprised you about being a parent?</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/conv-71ID117351938clip552-gt.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117351938clip552-gtvoc.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117351938clip552-multispeaker-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117351938clip552-multispeakerspon-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117351938clip552-multispeakerdecoder-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117351938clip552-multistyle-student-conv.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117351938clip552-restricted-student-conv.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117351938clip552-2stage-student-conv.wav?raw=true"  controls preload></audio></td>    
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td><audio src="files/conv-71ID117351938clip552-multispeaker-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117351938clip552-multispeakerspon-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117351938clip552-multispeakerdecoder-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117351938clip552-multistyle-actor-conv.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117351938clip552-restricted-actor-conv.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117351938clip552-2stage-actor-conv.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="8">
      Ma ei tea seda numbrit peast, aga ka internetist saab selle kindlasti kohe kätte.<br>
        <i>I don't know this number from the top of my head, but you can definitely find it on the internet</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/conv-71ID117360719clip152-gt.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117360719clip152-gtvoc.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117360719clip152-multispeaker-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117360719clip152-multispeakerspon-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117360719clip152-multispeakerdecoder-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117360719clip152-multistyle-student-conv.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117360719clip152-restricted-student-conv.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117360719clip152-2stage-student-conv.wav?raw=true"  controls preload></audio></td>    
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td><audio src="files/conv-71ID117360719clip152-multispeaker-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117360719clip152-multispeakerspon-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117360719clip152-multispeakerdecoder-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117360719clip152-multistyle-actor-conv.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117360719clip152-restricted-actor-conv.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117360719clip152-2stage-actor-conv.wav?raw=true"  controls preload></audio></td>
  </tr>
  <tr>
    <td colspan="8">
      Ma, ma pean siin nüüd täpsustama ühte asja, et tegelikult, kuna ma üksi ei suuda seda rege nagunii vedada, siis nüüd on uus stsenarist Piret Jaaks eks ole, kes kirjutas just selle, selle osa, millest Egon räägib ja ma ei taha mitte kunagi eriti võtetel käia ja näitlejaid traumeerimas me oma kohalolekuga, kes küsivad, mida sa sellega mõtlesid, mida sa sellega mõtlesid?<br>
        <i>I, I have to now clarify one thing here, that actually, as I cannot drive this entire thing alone anyway, then now the new screenwriter is Piret Jaaks, you know, who wrote that, that particular part, that Egon is talking about and I never want to attend the filming much and traumatize the actors with my presence, who ask what's the meaning of this, what's the meaning of this?</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/conv-71ID117347807clip303-gt.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117347807clip303-gtvoc.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117347807clip303-multispeaker-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117347807clip303-multispeakerspon-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117347807clip303-multispeakerdecoder-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117347807clip303-multistyle-student-conv.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117347807clip303-restricted-student-conv.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117347807clip303-2stage-student-conv.wav?raw=true"  controls preload></audio></td>    
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td><audio src="files/conv-71ID117347807clip303-multispeaker-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117347807clip303-multispeakerspon-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117347807clip303-multispeakerdecoder-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117347807clip303-multistyle-actor-conv.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117347807clip303-restricted-actor-conv.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/conv-71ID117347807clip303-2stage-actor-conv.wav?raw=true"  controls preload></audio></td>
  </tr>
</tbody>
</table>

### Fiction sentences (original target speakers and style transfer)

The top row of each sentence uses the original speaker from an audiobook dataset, while the bottom row uses a speaker from a neutral
dataset.

<table>
<thead>
    <tr>
    <th>Ground truth</th>
    <th>Ground truth (mel + vocoder)</th>
    <th>Baseline (multi-speaker)</th>
    <th>Multi-speaker + spontaneous data</th>
    <th>Multi-speaker decoder</th>
    <th>Multi-style</th>
    <th>Multi-style, restricted</th>
    <th>Multi-style, 2 stage</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="8">
      Ma ootasin, et Folora küsib, mispidi siis, aga ta oli vait, nii et ma olin sunnitud ise jätkama, mis tegi mu enesetunde hoopis sandiks – aga ma jätkasin siiski: „Sellega, et ta laseb sul sõita.<br>
        <i>I expected Folora to ask in what way then, but she was silent, so I was forced to continue myself which made me feel particularly bad, but I continued nonetheless: "By letting you drive.</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/fict-PeeterEKIotsekonePeeterotsekonelause01316-gt.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-PeeterEKIotsekonePeeterotsekonelause01316-gtvoc.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-PeeterEKIotsekonePeeterotsekonelause01316-multispeaker-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-PeeterEKIotsekonePeeterotsekonelause01316-multispeakerspon-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-PeeterEKIotsekonePeeterotsekonelause01316-multispeakerdecoder-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-PeeterEKIotsekonePeeterotsekonelause01316-multistyle-actor-fict.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-PeeterEKIotsekonePeeterotsekonelause01316-restricted-actor-fict.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-PeeterEKIotsekonePeeterotsekonelause01316-2stage-actor-fict.wav?raw=true"  controls preload></audio></td>    
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td><audio src="files/fict-PeeterEKIotsekonePeeterotsekonelause01316-multispeaker-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-PeeterEKIotsekonePeeterotsekonelause01316-multispeakerspon-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-PeeterEKIotsekonePeeterotsekonelause01316-multispeakerdecoder-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-PeeterEKIotsekonePeeterotsekonelause01316-multistyle-student-fict.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-PeeterEKIotsekonePeeterotsekonelause01316-restricted-student-fict.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-PeeterEKIotsekonePeeterotsekonelause01316-2stage-student-fict.wav?raw=true"  controls preload></audio></td>    
  </tr>
  <tr>
    <td colspan="8">
      Juba ainuüksi see liialdatuna tunduv karistus pidi jätma inetu jälje lapse südamesse, kes ei mõtelnud ju midagi halba.<br>
        <i>This excessive punishment alone would leave a mark on the child's heart who didn't mean to harm anyone.</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/fict-LiivikaEKIjutustavLiivikajutustavlause03901-gt.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-LiivikaEKIjutustavLiivikajutustavlause03901-gtvoc.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-LiivikaEKIjutustavLiivikajutustavlause03901-multispeaker-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-LiivikaEKIjutustavLiivikajutustavlause03901-multispeakerspon-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-LiivikaEKIjutustavLiivikajutustavlause03901-multispeakerdecoder-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-LiivikaEKIjutustavLiivikajutustavlause03901-multistyle-actor-fict.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-LiivikaEKIjutustavLiivikajutustavlause03901-restricted-actor-fict.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-LiivikaEKIjutustavLiivikajutustavlause03901-2stage-actor-fict.wav?raw=true"  controls preload></audio></td>    
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td><audio src="files/fict-LiivikaEKIjutustavLiivikajutustavlause03901-multispeaker-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-LiivikaEKIjutustavLiivikajutustavlause03901-multispeakerspon-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-LiivikaEKIjutustavLiivikajutustavlause03901-multispeakerdecoder-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-LiivikaEKIjutustavLiivikajutustavlause03901-multistyle-student-fict.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-LiivikaEKIjutustavLiivikajutustavlause03901-restricted-student-fict.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/fict-LiivikaEKIjutustavLiivikajutustavlause03901-2stage-student-fict.wav?raw=true"  controls preload></audio></td>    
  </tr>
</tbody>
</table>

### Neutral sentences (original target speakers and style transfer)

The top row of each sentence uses the original speaker from a neutral dataset, while the bottom row uses a speaker from a fiction
dataset.

<table>
<thead>
    <tr>
    <th>Ground truth</th>
    <th>Ground truth (mel + vocoder)</th>
    <th>Baseline (multi-speaker)</th>
    <th>Multi-speaker + spontaneous data</th>
    <th>Multi-speaker decoder</th>
    <th>Multi-style</th>
    <th>Multi-style, restricted</th>
    <th>Multi-style, 2 stage</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="8">
      Selleks et selliseid põhimõttelisi muutusi teha, on vaja kogu Eesti poliitilist süsteemi värskendada.<br>
        <i>The entire Estonian political system has to be updated to make such fundamental changes.</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/neutral-Mariwavs0001art627lause11-gt.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Mariwavs0001art627lause11-gtvoc.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Mariwavs0001art627lause11-multispeaker-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Mariwavs0001art627lause11-multispeakerspon-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Mariwavs0001art627lause11-multispeakerdecoder-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Mariwavs0001art627lause11-multistyle-student-neutral.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Mariwavs0001art627lause11-restricted-student-neutral.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Mariwavs0001art627lause11-2stage-student-neutral.wav?raw=true"  controls preload></audio></td>    
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td><audio src="files/neutral-Mariwavs0001art627lause11-multispeaker-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Mariwavs0001art627lause11-multispeakerspon-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Mariwavs0001art627lause11-multispeakerdecoder-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Mariwavs0001art627lause11-multistyle-actor-neutral.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Mariwavs0001art627lause11-restricted-actor-neutral.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Mariwavs0001art627lause11-2stage-actor-neutral.wav?raw=true"  controls preload></audio></td>    
  </tr>
  <tr>
    <td colspan="8">
      Sellise sõnumi esitas paavst kahepäevasel konverentsil Vatikanis naftakompaniide juhtidele.<br>
        <i>This was the message was presented by the Pope to oil company executives at a two-day conference in the Vatican.</i>
    </td>
  </tr>
  <tr>
    <td><audio src="files/neutral-Vestawavs0001art99lause4-gt.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Vestawavs0001art99lause4-gtvoc.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Vestawavs0001art99lause4-multispeaker-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Vestawavs0001art99lause4-multispeakerspon-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Vestawavs0001art99lause4-multispeakerdecoder-student.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Vestawavs0001art99lause4-multistyle-student-neutral.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Vestawavs0001art99lause4-restricted-student-neutral.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Vestawavs0001art99lause4-2stage-student-neutral.wav?raw=true"  controls preload></audio></td>    
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td><audio src="files/neutral-Vestawavs0001art99lause4-multispeaker-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Vestawavs0001art99lause4-multispeakerspon-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Vestawavs0001art99lause4-multispeakerdecoder-actor.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Vestawavs0001art99lause4-multistyle-actor-neutral.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Vestawavs0001art99lause4-restricted-actor-neutral.wav?raw=true"  controls preload></audio></td>
    <td><audio src="files/neutral-Vestawavs0001art99lause4-2stage-actor-neutral.wav?raw=true"  controls preload></audio></td>    
  </tr>
</tbody>
</table>
