label intro:
    $ narrator.name = renpy.input("What's your name?")
    menu:
        "What are your pronouns?"
        "He/Him":
            $ narrator.pSingular = "he"
            $ narrator.pPossesive = "him"
        "She/Her":
            $ narrator.pSingular = "she"
            $ narrator.pPossesive = "her"
        "They/Them":
            $ narrator.pSingular = "they"
            $ narrator.pPossesive = "them"
        "Someone else":
            $ narrator.pSingular = renpy.input("What is your singular pronoun? EX: he")
            $ narrator.pPossesive = renpy.input("What is your possessive pronoun? EX: him")

    jump afterPronouns
return
