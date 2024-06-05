import requests
import json

# Azure Cognitive Services endpoint for text analytics
endpoint = "YOUR_ENDPOINT"
subscription_key = "YOUR_SUBSCRIPTION_KEY"

# Function to analyze text for disease detection
def analyze_text(text):
    headers = {
        "Ocp-Apim-Subscription-Key": subscription_key,
        "Content-Type": "application/json"
    }
    data = {
        "documents": [
            {
                "id": "1",
                "text": text
            }
        ]
    }
    analyze_url = endpoint + "/text/analytics/v3.0/entities/recognition/general"
    response = requests.post(analyze_url, headers=headers, json=data)
    entities = response.json()["documents"][0]["entities"]
    diseases = []
    for entity in entities:
        if entity["category"] == "HealthCondition":
            diseases.append(entity["text"])
    return diseases

# Sample text for disease detection
text = """
I have been experiencing a persistent cough and fever for the past week. 
I'm worried it might be something serious like pneumonia or tuberculosis.
"""

# Call the function to analyze the text
detected_diseases = analyze_text(text)

# Print the detected diseases
if detected_diseases:
    print("Detected diseases:")
    for disease in detected_diseases:
        print("-", disease)
else:
    print("No diseases detected.")
