import random

class Figure(object):
    def show(self):
        raise NotImplementedError()


class OrangeRickyFigure(Figure):
    def show(self):
        print('Picked figure: Orange Ricky', '\n  #', '\n###')


class BlueRickyFigure(Figure):
    def show(self):
        print('Picked figure: Blue Ricky', '\n#', '\n###')


class ClevelandZFigure(Figure):
    def show(self):
        print('Picked figure: Cleveland Z', '\n##', '\n ##')


class RhodeIslandZFigure(Figure):
    def show(self):
        print('Picked figure: Rhode Island Z', '\n ##', '\n##')


class HeroFigure(Figure):
    def show(self):
        print('Picked figure: Hero', '\n####')


class TeeweeFigure(Figure):
    def show(self):
        print('Picked figure: Teewee', '\n #', '\n###')


class SmashboyFigure(Figure):
    def show(self):
        print('Picked figure: Smashboy', '\n##', '\n ##')


class Application(object):
    def create_figure(self, fig_):
        # параметризованный фабричный метод `create_document`
        raise NotImplementedError()


class MyApplication(Application):
    def create_figure(self, fig_):
        if fig_ == 'orange ricky':
            return OrangeRickyFigure()
        elif fig_ == 'blue ricky':
            return BlueRickyFigure()
        elif fig_ == 'cleveland Z':
            return ClevelandZFigure()
        elif fig_ == 'rhode island Z':
            return RhodeIslandZFigure()
        elif fig_ == 'hero':
            return HeroFigure()
        elif fig_ == 'teewee':
            return TeeweeFigure()
        elif fig_ == 'smashboy':
            return SmashboyFigure()


app = MyApplication()
figures = ['orange ricky', 'blue ricky', 'cleveland Z', 'rhode island Z', 'hero', 'teewee', 'smashboy']
for choice in range(10):
    fig = random.choice(figures)
    app.create_figure(fig).show()
