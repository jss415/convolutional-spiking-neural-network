# Convolutional Spiking Neural Network for Handwritten Character Recognition

## Problem

Offline handwritten character recognition is becoming increasingly crucial as more aspects of life transition from analog to digital. IoT devices utilizing this technology require fast, accurate, and efficient algorithms. Spiking Neural Networks (SNNs) offer computational efficiency but typically underperform in classification tasks compared to conventional models like Convolutional Neural Networks (CNNs). To address this problem, we developed a convolutional SNN trained using the spatiotemporal backpropagation (STBP) algorithm, suitable for spiking neurons. Tested on a subset of the EMNIST Balanced dataset (letters a, b, d, g, and q), our network's results are promising compared to earlier models

## Network Structure

![image](https://github.com/user-attachments/assets/bc25d229-97b3-4673-835b-8d827f8f3746)


## Hyperparameters for Training SNN

![image](https://github.com/user-attachments/assets/86a58a09-0638-4d34-9cd0-801cc0492957)


## Result

![image](https://github.com/user-attachments/assets/575d8a35-f97d-4e75-ab3a-a7bbc7b6c33e)


## Discussion

We trained a convolutional Spiking Neural Network (SNN) on 4000 samples, with 800 samples for each of the letters a, b, d, g, and q, and tested the network on 400 samples per character. The network's test accuracy plateaued around the 30th epoch, achieving a maximum accuracy of 88.61% between the 30th and 40th epochs. The network struggled with characters g and q, with accuracies fluctuating between 60% and 80%. Accuracy for g increased when q decreased, suggesting competitive interactions between output neurons. The confusion matrix confirmed that most misclassifications of g and q were due to the network confusing them with each other. Despite challenges, the network's performance for g and q, peaking at around 70%, was competitive with the 65.6% accuracy reported by an OPIUM-based classifier on the EMNIST dataset.
