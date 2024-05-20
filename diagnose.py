import marimo

__generated_with = "0.6.0"
app = marimo.App()


@app.cell
def __(mo):
    mo.md(
        r"""
        #### Cognitive
        * Is my brain spirialing on something?
        * Am I blocked and can't figure out how to get around it?
        #### Emotional 
        * How am I feeling about things right now?
        * If I was poked just right, would I cry?
        * Am I picking up on / feeling / reacting to other people's strong emotions?
          * Does the feeling even belong to me?
        #### Gastrointestinal 
        * How's my stomach? Does it need something? Is it upset?
        * Did I take my omeprazole?
        * Do I need probiotics? Yogurt? Something fermented (veggies, sourdough, etc)?
        #### Endocrine
        * How close to my HRT dose is it?
        * Could this be cycle related?
        * Is anyone else in my house having their cycle?
        #### Sartorical (clothing) 
        * Am I happy with what I'm wearing?
        * Could I change something and then be happier about it?
        #### Physical Plant (the body) 
        * Am I fed? 
        * Do I need water?
        * Do I need to get up and move about?
        * Am I getting enough Vitamin D?
        * Do I need physical contact?
        #### Social
        * Am I underpeopled?
        * Am I overpeopled?
        * Do I feel alone?
        * Do I feel too much together?
        * Do I need to know that I am loved?
        #### Belief
        * Am I searching for meaning?
        * Am I feeling crushed by capitalism?
        * Am I feeling a need to connect with the divine?
        #### Meta
        * After running through this list, is it the wrong diagnostic?
          * Am I doing okay? Go look at [the list on the fridge](https://depts.washington.edu/fammed/wp-content/uploads/2019/03/Katers-selfcare_printable.pdf)?
          * Consider checking Kate Bornstein's _Hello Cruel World_
        * Do I need to consult an oracle?
          * One card draw?
            * Shortcut: [Daily Tarot Draw](https://www.dailytarotdraw.com/card-deck)
          * Three card reading?
            * Shortcut: Quick reading from [Madam Adam](https://www.tiktok.com/@officialmadamadam?lang=en)
          * I Ching? 
            * Three coin method
            * Sticks / Yarrow
        * Ask others in my household, close friends, or other people who know me what they think is going on.
        """
    )
    return


@app.cell
def __(mo):
    mo.md(
        r"""

        """
    )
    return


@app.cell
def __():
    import marimo as mo
    return mo,


if __name__ == "__main__":
    app.run()

