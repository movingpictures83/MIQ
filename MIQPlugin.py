import sys
import numpy

class MIQPlugin:
    def input(self, filename):
       self.infile = open(filename, 'r')
       self.taxa = self.infile.readline().strip().split(',')

    def run(self):
       self.taxa = self.taxa[1:]

       self.IQL = dict()
       for taxon in self.taxa:
           self.IQL[taxon] = []
       N = len(self.taxa)

       self.IQL_1 = int(N/4)+1
       self.IQL_2 = int(N/2)+1
       self.IQL_3 = int(3*N/4)+1

       for line in self.infile:
           values = line.strip().split(',')
           values = values[1:]
           abundances = []
           for i in range(len(values)):
               abundances.append((float(values[i]), self.taxa[i]))
           abundances.sort()
           abundances.reverse()
           for i in range(self.IQL_1):
               self.IQL[abundances[i][1]] = 1
           for i in range(self.IQL_1+1, self.IQL_2):
               self.IQL[abundances[i][1]] = 2
           for i in range(self.IQL_2+1, self.IQL_3):
               self.IQL[abundances[i][1]] = 3
           for i in range(self.IQL_3+1, N):
               self.IQL[abundances[i][1]] = 4

    def output(self, filename):
       outfile = open(filename, 'w')
       for taxon in self.IQL:
           outfile.write(taxon+" "+str(numpy.median(self.IQL[taxon]))+"\n")
