import matplotlib as mpl    
import matplotlib.pyplot as plt

def main():
    font_dirs = ["/Users/bensappey/Library/Fonts/"]  # The path to the custom font file.
    font_files = mpl.font_manager.findSystemFonts(fontpaths=font_dirs)

    for font_file in font_files:
        mpl.font_manager.fontManager.addfont(font_file) 
    mpl.font_manager.findfont('JuliaMono')
    plt.style.use('/Users/bensappey/random/pretty_plotting_default.mplstyle')
   

def paper():
    plt.style.use('/Users/bensappey/random/pretty_plotting_paper.mplstyle')

if __name__ == '__main__':
    main()