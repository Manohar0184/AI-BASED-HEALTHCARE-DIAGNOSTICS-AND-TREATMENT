import random

# Simulated AI Diagnostic Engine
def ai_diagnose(symptoms):
    known_conditions = {
        "fever": "Flu",
        "cough": "Bronchitis",
        "chest pain": "Heart Disease",
        "headache": "Migraine",
        "fatigue": "Anemia"
    }
    diagnosis = [known_conditions.get(symptom.lower(), "Unknown") for symptom in symptoms]
    return list(set(diagnosis))

# Simple Chatbot Interface
def chatbot():
    print("Welcome to AI-EBPL Healthcare Assistant.")
    print("Please enter your symptoms (comma-separated):")
    user_input = input(">> ")
    symptoms = [s.strip() for s in user_input.split(",")]
    diagnosis = ai_diagnose(symptoms)
    print("\nPreliminary Diagnosis:")
    for d in diagnosis:
        print(f"- {d}")
    print("\nNote: This is an AI-based suggestion. Consult a doctor for confirmation.")

# Simulated IoT Monitoring
def iot_monitoring():
    print("\n--- IoT Real-Time Vitals ---")
    vitals = {
        "Heart Rate": random.randint(60, 100),
        "Temperature": round(random.uniform(36.5, 38.5), 1),
        "Blood Pressure": f"{random.randint(110, 130)}/{random.randint(70, 90)}"
    }
    for k, v in vitals.items():
        print(f"{k}: {v}")

# Run Demo
if _name_ == "_main_":
    chatbot()
    iot_monitoring()