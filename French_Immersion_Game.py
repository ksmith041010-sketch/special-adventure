score = 0

print("Bienvenue au quiz de français ! 🥐\n")

# Question 1
print("1. Quelle est la capitale de la France ?")
print("A. Lyon")
print("B. Marseille")
print("C. Paris")
print("D. Nice")

answer = input("Votre réponse (A, B, C, D): ").upper()

if answer == "C":
    print("Correct !\n")
    score+= 1
else:
    print("Incorrect. La Bonne réponse est C.\n")
    
# Question 2
print("2. Que signifie 'Il fait froid' ?")
print("A. Il a faim")
print("B. La temperature est basse")
print("C. Il est fatigué")
print("D. Il pleut")

answer = input("Votre réponse (A, B, C, D): ").upper()

if answer == "B":
    print("Correct !\n")
    score += 1
else:
    print("Incorrect. La bonne réponse est B.\n")
    
# Final Score
print(f"Votre score final est: {score}/2")

