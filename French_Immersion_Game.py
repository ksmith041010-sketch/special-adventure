# Quiz Data
questions = [
    {
        "question": "Quelle est la capitale de la France ?",
        "choices": ["A. Lyon", "B. Marseille", "C. Paris", "D. Nice"],
        "answer": "C"
        },
        {
            "question": "Que signifie 'Il fait froid' ?",
            "choices": ["A. Il a faim", "B. La température est basse", "C. Il est fatigué", "D. Il pleut"],
            "answer": "B"
        },
        {
            "question": "Quel est le contrraire de 'chaud' ?",
            "choices": ["A. Froid", "B. Lent", "C. Grand", "D. Heureaux"],
            "answer": "A"
        }
]

score = 0

print("Bienvenue au quiz de français ! 🥐\n")

for q in questions:
    print(q["question"])
    
    for choice in q["choices"]:
        print(choice)
    
    user_answer = input("Votre réponse: ").upper()
    
    if user_answer == q["answer"]:
        print("Correct !\n")
        score += 1
    else:
        print(f"Incorrect. La bonne réponse est {q['answer']}.\n")
        
print(f"Score final: {score}/{len(questions)}")
