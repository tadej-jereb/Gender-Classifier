from sklearn import tree

    clf = tree.DecisionTreeClassifier()

X = [[181, 80, 44, 4.8], [177, 70, 43, 4.5], [160, 60, 38, 3.1], [154, 54, 37, 4.8], [166, 65, 40, 4.8],
     [190, 90, 47, 4.8], [175, 64, 39, 4.8],
     [177, 70, 40, 4.8], [159, 55, 37, 4.8], [171, 75, 42, 4.8], [181, 85, 43, 4.8]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

clf = clf.fit(X, Y)
    prediction = clf.predict([[160, 50, 37, 2.2]])
        print(prediction)
