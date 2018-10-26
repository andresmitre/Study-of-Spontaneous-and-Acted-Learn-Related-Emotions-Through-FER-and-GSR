
## Documentation


[Center for Research in Mathematics (CIMAT)](http://www.cimat.mx/en)

Author: [Andres Mitre](https://github.com/andresmitre)

Email: andres.mitre@cimat.mx | andres18m@gmail.com

Twitter:  [@andresmitre_](https://twitter.com/andresmitre_)

Fall 2018

The present work got the **"Best Paper Award"** and is part of [11th Workshop on Intelligent Learning Environments, (WILE 2018)](https://nube.iie.org.mx/WILE2018/wile_2018.htm) held in collaboration with [MICAI](http://www.micai.org/) and the support of the Thematic Network on Applied Computational Intelligence, RedICA, of [CONACyT](https://en.wikipedia.org/wiki/Consejo_Nacional_de_Ciencia_y_Tecnolog%C3%ADa_(Mexico) October 22nd -23rd, 2018, [Guadalajara, México](https://en.wikipedia.org/wiki/Guadalajara).


# Repository description

"Deep learning is a group of exciting new technologies for neural networks. Through a combination of advanced training techniques and neural network architectural components, it is now possible to create neural networks of much greater complexity. Deep learning allows a neural network to learn hierarchies of information in a way that is like the function of the human brain" [[1]](https://github.com/jeffheaton/t81_558_deep_learning).

The data collection, starts with a FER (Facial Expression Recognition) using [haarcascades](https://github.com/opencv/opencv), with a professional camera/webcam. Images were taken while 23 participants watched a series of films related with emotions. The images were saved into separate emotions folders. GSR lectures were recorded as well since stress and boredom emotions stimulates the activity of sweet glands. the GSR were captured with the [Grove - GSR sensor](https://www.seeedstudio.com/Grove-GSR-sensor-p-1614.html) and saved into a CSV file.

The classifation for FER was made with a Convolutional Neural Network by [TensorFlow](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0) with a total of 1375 images into 8 different classes, the validation/explotation stage takes 10% of the data set and validates the CNN. On the other hand the identification between emotions was made with use of [Wilcoxon signed-rank test](https://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test) using [IBM SPPS](https://www.ibm.com/products/spss-statistics).

# Abstract

In learning environments emotions can activate or deactivate the learning process. Boredom, stress and happy –learn-related emotions– are included in physiological signals datasets, but not in Facial Expression Recognition (FER) datasets. In addition to this, Galvanic Skin Response (GSR) signal is the most representative data for emotions classification. This paper presents a technique to generate a dataset of facial expressions and physiological signals of spontaneous and acted learn-related emotions –boredom, stress, happy and neutral state– presented during video stimuli and face acting. We conducted an experiment with 22 participants (Mexicans); a **dataset of 1,840 facial expressions images and 1,584 GSR registers were generated**. Then, a Convolutional Neural Network (CNN) model was trained with the facial expression dataset, then statistical analysis was performed with the GSR dataset. MobileNet’s CNN reached an overall accuracy of 94.36% in a confusion matrix. But, the accuracy decreased to 28% for non-trained external images. The statistical results of GSR presented with significant differences in the confused emotions are discussed.


# Datasets

Contact [Author](https://github.com/andresmitre)

# Content

Module|Content
---|---
[Module 1](https://github.com/andresmitre/Study-of-Spontaneous-and-Acted-Learn-Related-Emotions-Through-FER-and-GSR/blob/master/introduction.ipynb) | <ul><li>Introduction</ul>
[Module 2](https://github.com/andresmitre/Study-of-Spontaneous-and-Acted-Learn-Related-Emotions-Through-FER-and-GSR/blob/master/Haar_Feature_based_Cascade_Classifiers.ipynb) | <ul><li>Haar Feature-based Cascade Classifiers</ul>
[Module 3](https://github.com/andresmitre/Study-of-Spontaneous-and-Acted-Learn-Related-Emotions-Through-FER-and-GSR/blob/master/data_acquisition.ipynb) | <ul><li>Data acquisition</ul>
[Module 4](https://github.com/andresmitre/Study-of-Spontaneous-and-Acted-Learn-Related-Emotions-Through-FER-and-GSR/blob/master/CNN.ipynb)| <ul><li>Convolutional Neural Network</ul>



VIVA MEXICO !


[1] Heaton Jeff, "T81 558:Applications of Deep Neural Networks", https://github.com/jeffheaton/t81_558_deep_learning
