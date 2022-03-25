
def GRADING(per_clf,tanh,ReLu,LeakyRelu,derivative,X_train):

    import numpy as np

    grades={"Peceptron":False, 
            "tanh":False, 
            "ReLu":False,
            "LeakyRelu":False,
            "derivative": False,
            "X_train_prepro":False}
    
    try:
        if(per_clf.predict([X[5,:]])[0]==1): grades["Peceptron"]=True
    except: grades["Peceptron"]=False

    try:
        if(round(tanh(5),4)==round(0.999909204262595,4)): grades["tanh"]=True
    except: grades["tanh"]=False

    try:
        if(ReLu(-2)==0 and ReLu(10)==10): grades["ReLu"]=True
    except: grades["ReLu"]=False

    try:
        if(LeakyRelu(3)==3 and LeakyRelu(-3,1)==-3): grades["LeakyRelu"]=True
    except: grades["LeakyRelu"]=False

    try:
        if(round(derivative(np.tanh,0.5),4)==0.7864): grades["derivative"]=True
    except: grades["derivative"]=False

    try:
        if(round(np.mean(X_train),3)==0.131): grades["X_train_prepro"]=True
    except: grades["X_train_prepro"]=False

    for x in grades:
        print (x,':',grades[x])
    print("LOOK AT PLOT & TIME <300s| 5min")
        
    