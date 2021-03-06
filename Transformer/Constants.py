# Transformer/Constants.py


# ----------------
# Module Docstring
# ----------------

""" Contains constants used by other modules. """


# --------------
# Periodic Table
# --------------

""" Periodic table for mapping atomic symbols to atom-type numbers. """

PeriodicTable = [
    # The symbol 'X' is assigned to zero -- spglib functions will happily accept this as a wildcard.

     'X',
     'H', 'He',
    'Li', 'Be',                                                                                                                                                  'B',  'C',  'N',  'O',  'F', 'Ne',
    'Na', 'Mg',                                                                                                                                                 'Al', 'Si',  'P',  'S', 'Cl', 'Ar',
     'K', 'Ca', 'Sc',                                                                                     'Ti',  'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
    'Rb', 'Sr',  'Y',                                                                                     'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te',  'I', 'Xe',
    'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta',  'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
    'Fr', 'Ra', 'Ac', 'Th', 'Pa',  'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og'
    ];

def SymbolToAtomicNumber(symbol):
    """ Lookup symbol in the periodic table and return the corresponding atomic number. """

    if symbol != None:
        for i, testSymbol in enumerate(PeriodicTable):
            # Make sure symbol has the correct casing.

            if symbol.title() == testSymbol:
                return i;

    return None;

def AtomicNumberToSymbol(atomicNumber):
    """ Lookup atomicNumber in the periodic table and return the corresponding atomic symbol. """

    if atomicNumber != None:
        if atomicNumber >= 0 and atomicNumber < len(PeriodicTable):
            return PeriodicTable[atomicNumber];

    return None;
