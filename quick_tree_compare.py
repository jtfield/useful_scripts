#! /usr/bin/python3

import dendropy
import argparse
from dendropy.calculate import treecompare

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--true_tree')
    parser.add_argument('--new_tree')
    return parser.parse_args()

def main():
    args = parse_args()

    read_true = open(args.true_tree,'r').read()
    read_new = open(args.new_tree,'r').read()

    # establish common taxon namespace
    tns = dendropy.TaxonNamespace()

    # ensure all trees loaded use common namespace
    true = dendropy.Tree.get(
        data=read_true,
        schema='newick',
        taxon_namespace=tns, preserve_underscores=True)
    new = dendropy.Tree.get(
        data=read_new,
        schema='newick',
        taxon_namespace=tns, preserve_underscores=True)

    for tax in tns:
        print(tax)

    ## Unweighted Robinson-Foulds distance
    print(treecompare.symmetric_difference(true, new))

if __name__ == '__main__':
    main()
