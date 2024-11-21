import pickle
import numpy as np
import torch
from transformers import BertTokenizer, BertModel
from sklearn.preprocessing import LabelEncoder
import os

# Load BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Load trained classifiers
with open('clf_L1.pkl', 'rb') as file:
    clf_L1 = pickle.load(file)
with open('clf_L2.pkl', 'rb') as file:
    clf_L2 = pickle.load(file)
with open('clf_L3.pkl', 'rb') as file:
    clf_L3 = pickle.load(file)
with open('clf_L4.pkl', 'rb') as file:
    clf_L4 = pickle.load(file)
with open('clf_L5.pkl', 'rb') as file:
    clf_L5 = pickle.load(file)
with open('clf_L6.pkl', 'rb') as file:
    clf_L6 = pickle.load(file)

# Function to dynamically load or create a label encoder
def load_or_create_label_encoder(classes, filename):
    """
    Load a LabelEncoder from file if it exists, or create it from classifier classes.
    """
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    else:
        # Create label encoder
        le = LabelEncoder()
        le.fit(classes)
        
        # Save the label encoder for future use
        with open(filename, 'wb') as file:
            pickle.dump(le, file)
        
        return le

# Dynamically create or load label encoders
le_L1 = load_or_create_label_encoder(clf_L1.classes_, 'le_L1.pkl')
le_L2 = load_or_create_label_encoder(clf_L2.classes_, 'le_L2.pkl')
le_L3 = load_or_create_label_encoder(clf_L3.classes_, 'le_L3.pkl')
le_L4 = load_or_create_label_encoder(clf_L4.classes_, 'le_L4.pkl')
le_L5 = load_or_create_label_encoder(clf_L5.classes_, 'le_L5.pkl')
le_L6 = load_or_create_label_encoder(clf_L6.classes_, 'le_L6.pkl')

# Function to generate BERT embedding for a sentence
def get_embedding(sentence):
    """
    Generate BERT embeddings for a single sentence.
    """
    try:
        inputs = tokenizer(sentence, return_tensors='pt', padding=True, truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        embedding = outputs.last_hidden_state.mean(dim=1)  # Mean pooling
        return embedding.numpy().flatten()
    except Exception as e:
        print(f"Error generating embedding: {e}")
        return None

# Preprocess a single sentence to generate its embedding
def preprocess_sentence(sentence):
    """
    Preprocess a sentence to generate its BERT embedding.
    """
    embedding = get_embedding(sentence)
    if embedding is None:
        raise ValueError("Failed to generate embedding for the sentence.")
    return embedding.reshape(1, -1)  # Ensure compatible shape for classifiers

# Predict labels for a given sentence
def predict_labels(sentence):
    """
    Predicts labels for the given sentence using trained classifiers.
    """
    # Get embedding
    embedding = preprocess_sentence(sentence)

    # Predict using trained models
    pred_L1 = le_L1.inverse_transform(clf_L1.predict(embedding))
    pred_L2 = le_L2.inverse_transform(clf_L2.predict(embedding))
    pred_L3 = le_L3.inverse_transform(clf_L3.predict(embedding))
    pred_L4 = le_L4.inverse_transform(clf_L4.predict(embedding))
    pred_L5 = le_L5.inverse_transform(clf_L5.predict(embedding))
    pred_L6 = le_L6.inverse_transform(clf_L6.predict(embedding))

    # Return predictions as a dictionary
    return {
        "LABEL1": pred_L1[0],
        "LABEL2": pred_L2[0],
        "LABEL3": pred_L3[0],
        "LABEL4": pred_L4[0],
        "LABEL5": pred_L5[0],
        "LABEL6": pred_L6[0],
    }
