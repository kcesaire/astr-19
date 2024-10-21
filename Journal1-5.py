import numpy as np

def main():
    #tabulate between 0 and 2pi with a thousand entries (googled how to do this)
    x_values = np.linspace(0, 2 * np.pi, 1000)
    sin_values = np.sin(x_values)
    
    #printing table header
    print("x\t\t\tsin(x)")
    print("-"*45)
    
    #printing x and sin(x) values 
    for x, sin_x in zip(x_values, sin_values):
        print(f"{x}\t{sin_x}")
if __name__=="__main__":
    main()