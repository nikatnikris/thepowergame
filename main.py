gameState = {
    "name":"",
    "money": 100,
    "race": "",
    "class": ""
}

questions = [
    {
        "questionType": "first",
        "question": "What is your name?",
        "outcome": "name"
    },
    {
        "questionType": "second",
        "question": "What is your class?",
        "outcome": "class"
    },
]


print(gameState)

firstQuestion = [q for q in questions if q["questionType"]=="first"][0]
print(firstQuestion["question"])
answer = input()
gameState[firstQuestion["outcome"]] = answer

print(gameState)

secondQuestion = [q for q in questions if q["questionType"]=="second"][0]
print(secondQuestion["question"])
answer = input()
gameState[secondQuestion["outcome"]] = answer


print(gameState)