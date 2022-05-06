import matplotlib.pyplot as plt

x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
y = [10, 30, 20, 50, 70, 80, 80, 90, 100, 120]

mean_x = 0
mean_y = 0
n = len(x)
# finding mean of x and y
sum = 0
sum_1 = 0
for i in range(0,n):
    sum+=i
    sum_1+=i
mean_y = sum_1/n
mean_x = sum/n
    
xy = []
xx = []
for i in range(0,n):
    xy.append(x[i]*y[i])
    xx.append(x[i]*x[i])
sum_xy = 0
sum_xx = 0
for i in range(0,n):
    sum_xy+=xy[i]
    sum_xx+=xx[i]

SS_xy = sum_xy - n*mean_x*mean_y
SS_xx = sum_xx - n*mean_x*mean_y

# Calculate coefficients
b_1 = SS_xy / SS_xx
b_0 = mean_y - b_1*mean_x

# Predicting values of Y
plt.scatter(x, y, color = "m",
			marker = "o", s = 30)

	# predicted response vector
y_pred = []
for i in range(0,n):
    y_pred.append(b_1 + b_1*x[i]) 
print(y, y_pred)
plt.plot(x, y_pred, color = "g")
plt.xlabel('x')
plt.ylabel('y')
plt.show()
