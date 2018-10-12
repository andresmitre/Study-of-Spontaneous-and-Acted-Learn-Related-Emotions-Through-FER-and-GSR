#  Study of Spontaneous and Acted Learn-Related Emotions Through FER and GSR




Authors: [Andres Mitre](https://github.com/andresmitre) [0000−0003−4888−5453] and [Hugo A. Mitre-Hernandez](https://github.com/HugoMitre) [0000−0003−2840−3998]

Human-Centered Computing Lab (HCC) - [Center for Research in Mathematics (CIMAT)](http://www.cimat.mx/en)

Email: andres.mitre@cimat.mx | hmitre@cimat.mx

Twitter:  [@andresmitre_](https://twitter.com/andresmitre_)

Fall 2018

this is a test for version branch

The present work is a paper developed for [11th Workshop on Intelligent Learning Environments, (WILE 2018)](https://nube.iie.org.mx/WILE2018/wile_2018.htm) held in collaboration with [MICAI](http://www.micai.org/) and the support of the Thematic Network on Applied Computational Intelligence, RedICA, of [CONACyT](https://en.wikipedia.org/wiki/Consejo_Nacional_de_Ciencia_y_Tecnolog%C3%ADa_(Mexico)) October 22nd -23rd, 2018, [Guadalajara, México](https://en.wikipedia.org/wiki/Guadalajara).

<!-- The present work is part of an Undergraduate thesis for B.E. in Telecommunications, OS and Electronics in [Autonomous University of Sinaloa (in Spanish: Universidad Autónoma de Sinaloa, UAS)](http://web.uas.edu.mx/web/ingles/index.php) in Sinaloa, México. The work was developed in [Center for Research in Mathematics (CIMAT)](http://www.cimat.mx/en)

**ABOUT COPYING OR USING PARTIAL INFORMATION:**
This script was originally created by [Andres Mitre](https://github.com/andresmitre). READ LICENSE FILE -->

# Repository description

"Deep learning is a group of exciting new technologies for neural networks. Through a combination of advanced training techniques and neural network architectural components, it is now possible to create neural networks of much greater complexity. Deep learning allows a neural network to learn hierarchies of information in a way that is like the function of the human brain" [[1]](https://github.com/jeffheaton/t81_558_deep_learning).

The data collection, starts with a FER (Facial Expression Recognition) using [haarcascades](https://github.com/opencv/opencv), with a professional camera/webcam. Images were taken while 23 participants watched a series of films related with emotions. The images were saved into separate emotions folders. GSR lectures were recorded as well since stress and boredom emotions stimulates the activity of sweet glands. the GSR were captured with the [Grove - GSR sensor](https://www.seeedstudio.com/Grove-GSR-sensor-p-1614.html) and saved into a CSV file.

The classifation for FER was made with a Convolutional Neural Network by [TensorFlow](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0) with a total of 1375 images into 8 different classes, the validation/explotation stage takes 10% of the data set and validates the CNN. On the other hand the identification between emotions was made with use of [Wilcoxon signed-rank test](https://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test) using [IBM SPPS](https://www.ibm.com/products/spss-statistics).

# Abstract

In learning environments emotions can activate or deactivate the learning process. Boredom, stress and happy –learn-related emotions– are included in physiological signals datasets, but not in Facial Expression Recognition (FER) datasets. In addition to this, Galvanic Skin Response (GSR) signal is the most representative data for emotions classification. This paper presents a technique to generate a dataset of facial expressions and physiological signals of spontaneous and acted learn-related emotions –boredom, stress, happy and neutral state– presented during video stimuli and face acting. We conducted an experiment with 22 participants (Mexicans); a dataset of 1,840 facial expressions images and 1,584 GSR registers were generated. Then, a Convolutional Neural Network (CNN) model was trained with the facial expression dataset, then statistical analysis was performed with the GSR dataset. MobileNet’s CNN reached an overall accuracy of 94.36% in a confusion matrix. But, the accuracy decreased to 28% for non-trained external images. The statistical results of GSR presented with significant differences in the confused emotions are discussed.


# Dataset


####  <b>Hispanic Facial Expressions and Galvanic Skin Response (HFEGSR)</b>


<p> A sample of 22 subjects of Hispanic ethnicity participated in the study: 9 female and
13 males with a range from 18 to 62 years.<p/> The dataset consisted of two sessions: spontaneous and acted. Firstly, the procedure of the experiment consisted in provide instructions to the participants (30) about the session and how to position their middle and index phalanges over the GSR electrodes. During the session, participants watched a series of films (stimuli) while raw data was recorded –photos taken at 10 FPS and GSR recording at 10Hz.</p><p>The stimuli for the spontaneous session consisted in the following sequence: Neutral → Stress → Neutral → Boredom → Neutral → Happy; where at the end of every stimuli, neutrality was induced to the participant to generate the correct desired emotion. Raw data was taken in an interval of 30 seconds from the scene where the strongest emotion appeared. The facial expression and GSR reading captured at 10 FPS and Hz respectively for spontaneous emotion

Contact [Author](https://github.com/andresmitre)

# Content

Module|Content
---|---
[Module 1](https://github.com/andresmitre/Emotion_Classification/blob/master/introduction.ipynb) | <ul><li>Introduction</ul>
[Module 2](https://github.com/andresmitre/Emotion_Classification/blob/master/Haar_Feature_based_Cascade_Classifiers.ipynb) | <ul><li>Haar Feature-based Cascade Classifiers</ul>
[Module 3](https://github.com/andresmitre/Emotion_Classification/blob/master/data_acquisition.ipynb) | <ul><li>Data acquisition</ul>
[Module 4](https://github.com/andresmitre/Emotion_Classification/blob/master/CNN.ipynb)| <ul><li>Convolutional Neural Network</ul>



VIVA MEXICO !


[1] Heaton Jeff, "T81 558:Applications of Deep Neural Networks", https://github.com/jeffheaton/t81_558_deep_learning
