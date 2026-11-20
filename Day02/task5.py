height_cm = "175"
weight_kg = "68.5"

height_cm = float(height_cm)
weight_kg = float(weight_kg)

height_m = height_cm / 100

# Calculate BMI
bmi = weight_kg / (height_m * height_m)

print("Height in meters:", height_m)
print("Weight in kg:", weight_kg)
print("BMI:", round(bmi, 2))
