#Lab 1

def symbolic_decision(score,complete):
    if complete and score >= 70:
        return "Review"
    return "Hold"

def threshold_decision(probability):
    if probability >= 0.70:
        return "Review"
    return "Hold"

test = [
    ("complete_high",82,True,0.81),
    ("complete_low",68,True,0.74),
    ("incomplete_high",91,False,0.88),
    ("boundary",70,True,0.70)    
]

print("case/symbolic/threshold/disagreement")

for name , score, complete, probability in test:
    symbolic = symbolic_decision(score,complete)
    threshold = threshold_decision(probability)

    difference = symbolic != threshold  

    print(name,symbolic,threshold,difference,sep= "/")