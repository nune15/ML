train_data = [
     [25, 200, 50, 1],
    [30, 180, 90, 0],
    [22,150,30,1],
    [40,300,120,0],
    [35,220,70,1],
    [28,250,60,1],
    [50,400,200,0],
    [45,350,150,0],
    [27,160,40,1],
    [33,210,80,1],
    [31,190,95,0],
    [29,230,55,1],
    [42,280,130,0],
    [36,240,75,1],
    [38,260,100,0],
    [26,170,45,1]
]

test_data = [
    [32, 200,85],
    [24,180,35],
    [44,120,140],
    [27,210,50]
]

K = 3
def euclidean_distance(p1, p2):
    d1 = (p1[0] - p2[0]) ** 2
    d2 = (p1[1] - p2[1]) ** 2
    d3 = (p1[2] - p2[2]) ** 2
    return (d1 + d2 + d3) ** 0.5

def predict(test_point):
    distances = []

    for train_point in train_data:
        dist = euclidean_distance(test_point, train_point[:3])  
        label = train_point[3]  
        distances.append([dist, label])  

    neighbors = []
    for _ in range(K):
        min_index = 0
        for i in range(1, len(distances)):
            if distances[i][0] < distances[min_index][0]:
                min_index = i
        neighbors.append(distances[min_index][1])
        distances.pop(min_index)

    count_1 = 0
    count_0 = 0
    for label in neighbors:
        if label == 1:
            count_1 += 1
        else:
            count_0 += 1

    if count_1 > count_0:
        return 1
    else:
        return 0

for i in range(len(test_data)):
    result = predict(test_data[i])
    print(f"Թեստային հաճախորդ {i+1} – Կփակի պարտքը՞ → {result}")
