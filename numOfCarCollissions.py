
numOfSamples = int(input("Enter the number of samples: "))

samples = []
for i in range(numOfSamples):
    samples.append(input("").split(" "))


for i in range(len(samples)):
    x = abs(int(samples[i][0]))
    y = abs(int(samples[i][1]))
    xySpeed = int(samples[i][2])
    xyDistance = pow((pow(x, 2) + pow(y, 2)), 0.5)
    xyTime = xyDistance / xySpeed
    samples[i] = xyTime

numOfCollissions = 0
for i in range(len(samples)):
    for j in range(len(samples)):
        if not(i == j) and i > j:
            if samples[i] == samples[j]:
                numOfCollissions += 1


#print(samples)
print(numOfCollissions)
