# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 22:23:50 2017

@author: vase_
"""

from mrjob.job import MRJob


class MRWordFrequencyCount(MRJob):

    def mapper(self, key, line):
        for hashtag in line.split():
            yield hashtag, 1

    def reducer(self, hashtag, occurrences):
        yield hashtag, sum(occurrences)


if __name__ == '__main__':
    MRWordFrequencyCount.run()