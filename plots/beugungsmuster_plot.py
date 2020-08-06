import random

import matplotlib.pyplot as plt
import numpy as np


class BeugungsmusterPlot:
    def create_plot(self, spaltanzahl, spaltabstand, wellenlaenge, amplitude):
        xlist = np.linspace(0.0, 20.0, 100)
        ylist = np.linspace(-10.0, 10.0, 100)
        X, Y = np.meshgrid(xlist, ylist)

        for i in range(spaltanzahl):
            Z = amplitude*np.cos(np.sqrt(X**2+(Y+(spaltanzahl/2.0-0.5-i)*spaltabstand)**2)/wellenlaenge*2.0*np.pi)
            if i == 0:
                Zges = Z
            else:
                Zges += Z

        fig, ax = plt.subplots(1, 1, figsize=(25, 20))
        cp = ax.contourf(X, Y, Zges, 200)
        # Add a colorbar to a plot
        fig.colorbar(cp)
        ax.set_title(f'{spaltanzahl} Spalte, d= {spaltabstand}, lambda={wellenlaenge}', fontsize=50)
        ax.set_ylabel('y (cm)', fontsize=50)
        ax.set_xlabel('x (cm)', fontsize=50)
        #plt.show()
        filename = f"{str(random.randint(0,9999))}_{str(random.randint(0,999))}.png"
        plt.savefig(f"plots\outputs\plot{filename}", format="png")
        return filename

