import matplotlib as mpl    
import matplotlib.pyplot as plt

def main():
    font_dirs = ["~/Library/Fonts/"]  # The path to the custom font file. Modify if your font library isn't here
    font_files = mpl.font_manager.findSystemFonts(fontpaths=font_dirs)

    for font_file in font_files:
        mpl.font_manager.fontManager.addfont(font_file) 
    try:    
        mpl.font_manager.findfont('JuliaMono')
        print("Found font: JuliaMono")
    except:
        print("Font 'JuliaMono' not found")
        
    plt.style.use('./pretty_plotting_default.mplstyle')
   

def paper():
    plt.style.use('./pretty_plotting_paper.mplstyle')

if __name__ == '__main__':
    main()
