# Simple Linear Regression from scratch

# Data (Hours studied vs Marks)
x = [1, 2, 3, 4, 5]   # x = input data (hours studied)
y = [2, 4, 5, 4, 5]   # y = output data (marks obtained)

n = len(x)  # total number of data points (yahan 5)
# Mean (average) calculate kar rahe hain
mean_x = sum(x) / n   # x ka average (center point)
mean_y = sum(y) / n   # y ka average (center point)

# Slope (m) ke liye numerator aur denominator initialize
num = 0   # numerator = relation between x and y
den = 0   # denominator = variation in x

# Loop har data point ke liye chalega
for i in range(n):  
    # (x[i] - mean_x) = x ka deviation (average se kitna door)
    # (y[i] - mean_y) = y ka deviation
    # dono ko multiply karke relation check kar rahe
    num += (x[i] - mean_x) * (y[i] - mean_y)
    
    # (x[i] - mean_x)^2 = x me kitna variation hai
    den += (x[i] - mean_x) ** 2

# Slope (m) calculate kiya
m = num / den   # slope batata hai line kitni steep hai

# Intercept (b) calculate kiya
b = mean_y - m * mean_x   # line ka starting point (y-axis pe)

print("Slope (m):", m)        # slope print kar rahe
print("Intercept (b):", b)    # intercept print kar rahe

# Prediction function banaya
def predict(x_new):  
    return m * x_new + b   # y = mx + b formula use karke prediction

# User se input lena
hours = float(input("Enter study hours: "))   # user se hours input

# Prediction print karna
print("Predicted marks:", predict(hours))   # given hours ke liye marks batayega