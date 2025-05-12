import random
import time

# 1. AI Diagnosis Simulation
def diagnose():
    diagnosis = random.choice(["Healthy", "Need Checkup", "Critical"])
    print("Diagnosis:", diagnosis)

# 2. Chatbot Simulation
def chatbot():
    question = input("Ask your health question: ")
    if "pain" in question:
        print("It might be serious. Please visit a doctor.")
    elif "appointment" in question:
        print("Appointment booked successfully.")
    else:
        print("Please ask a health-related question.")

# 3. IoT Device Data
def iot_data():
    heart_rate = random.randint(60, 100)
    bp = f"{random.randint(110, 130)}/{random.randint(70, 90)}"
    print("Heart Rate:", heart_rate)
    print("Blood Pressure:", bp)

# 4. Security Access
def access_control():
    user = input("Enter role (doctor/nurse/patient): ")
    if user == "doctor":
        print("Access: Full medical data")
    elif user == "nurse":
        print("Access: Basic info only")
    else:
        print("Access: Denied")

# 5. Performance Testing
def performance_test():
    start = time.time()
    for _ in range(100):
        diagnose()
    end = time.time()
    print("Checked 100 patients in", round(end - start, 2), "seconds")

# Run all functions simply
print("Healthcare System Demo")
diagnose()
iot_data()
chatbot()
access_control()
performance_test()