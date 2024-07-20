document.getElementById('health-survey-form').addEventListener('submit', async function(event) {
  event.preventDefault();

  // Collect form data directly from elements
  const general_health = document.getElementById('general_health').value;
  const checkup = document.getElementById('checkup').value;
  const exercise = document.getElementById('exercise').value;
  const skin_cancer = document.getElementById('skin_cancer').value;
  const other_cancer = document.getElementById('other_cancer').value;
  const depression = document.getElementById('depression').value;
  const diabetes = document.getElementById('diabetes').value;
  const arthritis = document.getElementById('arthritis').value;
  const age_category = document.getElementById('age_category').value;
  const height = document.getElementById('height').value;
  const weight = document.getElementById('weight').value;
  const bmi = document.getElementById('bmi').value;
  const smoking_history = document.getElementById('smoking_history').value;
  const alcohol_consumption = document.getElementById('alcohol_consumption').value;
  const fruit_consumption = document.getElementById('fruit_consumption').value;
  const green_vegetables_consumption = document.getElementById('green_vegetables_consumption').value;
  const friedpotato_consumption = document.getElementById('friedpotato_consumption').value;
  const sex_female = document.getElementById('sex_female').value;

  try {
      // Send data to Flask server
      const response = await fetch('http://127.0.0.1:5000/predict', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/x-www-form-urlencoded'
          },
          body: new URLSearchParams({
              general_health,
              checkup,
              exercise,
              skin_cancer,
              other_cancer,
              depression,
              diabetes,
              arthritis,
              age_category,
              height,
              weight,
              bmi,
              smoking_history,
              alcohol_consumption,
              fruit_consumption,
              green_vegetables_consumption,
              friedpotato_consumption,
              sex_female
          })  // Send form data as URL encoded
      });

      // Parse and display the response
      const result = await response.json();
      const prediction = result['Cardio-Vascular presence'] ? "Positive" : "Negative";
    //   document.getElementById('prediction-value').innerText = prediction;
        const predictionElement = document.getElementById('prediction-value');

        // Set the prediction text
        predictionElement.innerText = prediction;
        
        // Apply the appropriate class based on the prediction value
        if (prediction === "Positive") {
            predictionElement.className = 'positive';
        } else {
            predictionElement.className = 'negative';
        }

      
  } catch (error) {
      console.error('Error:', error);
      document.getElementById('prediction-value').innerText = 'Error: ' + error;
  }
});
