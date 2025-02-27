import glob
import os
from gel import GraphToText as GTT

def main(graphPath, newGraphPath, dim):
    GTT.G2T(graphPath, newGraphPath)
    os.chdir('gel/Temporal-Network-Embedding/source_code/main')
    script = f'.\BCGDEmbed ../../../../{newGraphPath} -c {dim}'
    stream = os.popen(script)
    output = stream.read()
    print('out', output)
    GTT.T2A('../../../../'+newGraphPath, '../../../../'+newGraphPath)
    print('../../../../'+newGraphPath, '../../../../'+newGraphPath)
    os.chdir('../../../../')
    print(os.getcwd())