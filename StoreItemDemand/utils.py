import matplotlib.pyplot as plt


def test_print():
    print("Hello World in utils.py")

def show_two_chart_horizontal(title, df1, sub_title1, df2, sub_title2):
    fig, (ax1, ax2) = plt.subplots(1,2)
    fig.suptitle(title)

    fig.set_figwidth(16)
    fig.set_figheight(2)

    ax1.title.set_text(sub_title1)
    ax2.title.set_text(sub_title2)
    df1.plot(ax=ax1)
    df2.plot(ax=ax2)    
    
    
def show_four_chart_horizontal(title, df1, df2, df3, df4, st1, st2, st3, st4):
    fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4)
    fig.suptitle(title)

    fig.set_figwidth(4)
    fig.set_figheight(2)

    ax1.title.set_text(st1)
    ax2.title.set_text(st2)
    ax3.title.set_text(st3)
    ax4.title.set_text(st4)
    
    df1.plot(ax=ax1)
    df2.plot(ax=ax2)    
    df3.plot(ax=ax3)
    df4.plot(ax=ax4)    
    
    
