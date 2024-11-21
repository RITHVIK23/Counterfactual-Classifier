function classifySentence() {
    // Get the sentence from the input field
    const input = document.getElementById("sentence");
    const sentence = input.value.trim();

    // Check if the input is empty
    if (!sentence) {
        alert("Please enter a sentence.");
        return;
    }

    // Make a POST request to the Flask backend with the sentence
    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ sentence: sentence })
    })
    .then(response => response.json()) // Parse JSON response from the backend
    .then(data => {
        // Check if there was an error in the backend
        if (data.error) {
            alert(data.error);
        } else {
            // Update the predictions in the HTML
            const predictionsElement = document.getElementById("predictions");
            predictionsElement.innerHTML = `
                <ul>
                    <li><strong>LABEL1:</strong> ${data.LABEL1}</li>
                    <li><strong>LABEL2:</strong> ${data.LABEL2}</li>
                    <li><strong>LABEL3:</strong> ${data.LABEL3}</li>
                    <li><strong>LABEL4:</strong> ${data.LABEL4}</li>
                    <li><strong>LABEL5:</strong> ${data.LABEL5}</li>
                    <li><strong>LABEL6:</strong> ${data.LABEL6}</li>
                </ul>
            `;

            // Update the input sentence display
            const sentenceElement = document.getElementById("inputSentence");
            sentenceElement.textContent = data.Sentence;
        }
    })
    .catch(error => {
        // Handle errors in the fetch request
        alert("Error occurred while classifying the sentence.");
        console.error(error);
    });
}
