from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave), 
    Or(And(AKnight, AKnave), AKnave), 
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave), 
    Or(BKnight, BKnave),
    # A says "We are both knaves."
    Or(And(AKnave, BKnave), AKnave),
    And(Not(And(AKnave, BKnave)), AKnave),
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave), 
    Or(BKnight, BKnave),
    # A says "We are the same kind."
    Or(And(AKnight, BKnight), AKnave),
    Or(And(AKnave, AKnave), AKnave),
    # B says "We are of different kinds."
    Or(Not(And(AKnight, BKnight)), BKnight),
    Or(Not(And(AKnave, BKnave)), BKnight),

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),

    # A says either "I am a knight." or "I am a knave.", but you don't know which.

    # B says "A said 'I am a knave'."
    # no-one can say they are a knave
    BKnave,

    # B says "C is a knave."
    Or(CKnave, BKnave),
    And(CKnight, BKnave),


    # C says "A is a knight."
    Or(AKnight, CKnave),
    And(CKnight, AKnight),

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
