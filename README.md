# Natural Language Generation for Counterfactual Intervention

### Overview
This project utilizes Natural Language Processing (NLP) and machine learning techniques to analyze counterfactual thinking in health-related behavior change. Specifically, it focuses on reflecting upon blood glucose management and behavioral adjustments for individuals with diabetes. The system categorizes and classifies participants' counterfactual statements to better understand their health behavior intentions and enhance personalized interventions.

### Data
The data was collected from surveys where participants reflected on instances of elevated blood glucose levels. The survey consisted of:

### Negative Event Recall: Participants described situations where their blood glucose exceeded 140 mg/dL.
Counterfactual Thinking: Participants generated "If only I...then..." statements to reflect on alternative behaviors they could have performed to improve glucose levels.
Follow-Up: Participants rated the likelihood of applying the counterfactual strategies in the upcoming week.

#### Methods
The project involves the manual labeling of counterfactual statements based on criteria such as:

Direction of Counterfactuals: Upward or downward counterfactuals.
Behavioral Intentions: Identifying key elements in participants' reflections to assess their potential for behavior change.

### Requirements
Python 3.x
Necessary libraries: pandas, numpy, sklearn, nltk, tensorflow, etc.

### Usage
Clone the repository or download the files.
Install the required libraries:
pip install -r requirements.txt
Run the analysis script to begin processing the counterfactual data.
### License
This project is licensed under the MIT License - see the LICENSE file for details.
