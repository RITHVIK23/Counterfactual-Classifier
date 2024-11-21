1. Introduction:
The project aims to support individuals in improving their health behaviors by employing Natural Language Processing (NLP) to classify counterfactual thoughts related to managing chronic conditions like diabetes. It uses machine learning models to automate the analysis of counterfactual thinking, such as whether individuals wish they had made different choices regarding their blood glucose regulation.

2. Data Collection and Organization:
The data was gathered through surveys from participants reflecting on their blood glucose levels and behaviors. These surveys prompted participants to recall negative events related to their blood glucose levels, generate counterfactual thoughts, and reflect on potential behavioral changes. The collected data includes various labels, such as whether the thought was counterfactual, its direction (upward or downward), its structure (additive, subtractive, or substitutive), and more.

3. Methods:
This section describes the identification and classification of counterfactuals based on several criteria, such as direction, structure, focus, controllability, and specificity. The methods also involved tokenizing text using BERT and Byte Pair Encoding (BPE), followed by training classifiers to predict various labels associated with counterfactuals.

4. Evaluation and Results:
The report compares the performance of different classifiers:

Logistic Regression: Served as a baseline model and showed reasonable results but struggled with capturing complex patterns, especially with imbalanced classes.
XGBoost: Performed better by handling both binary and multi-class classification tasks more efficiently, though it also struggled with minority subclasses.
MLP (Multi-Layer Perceptron): Showed promising results, particularly in terms of consistent performance across various labels, though variations existed for certain subclasses.
5. Evaluation Metrics:
You discussed several key metrics:

Precision: Measures the accuracy of positive predictions.
Recall: Measures how well the model identifies all positive instances.
F1 Score: A balance between precision and recall, particularly useful for imbalanced datasets.
6. Figures and Visuals:
Word Cloud Analysis: Helped to visualize common themes in the text data.
Confusion Matrices: Showed the performance of the XGBoost classifier across different labels.
