import pandas as pd
import numpy as np

class atb():
    def __init__(self, name:str) -> None:
        self.name = name

def main():
    pnc = atb("penicilin")
    print(pnc.name)


if __name__ == "__main__":
    main()