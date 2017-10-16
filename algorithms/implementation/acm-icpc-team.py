#!/bin/python

import sys


def ones(i):
    s = bin(i)
    count = 0
    for i in range(2,len(s)):
        if (s[i] == '1'):
            count += 1
    return count

n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
know = []
topic_i = 0
for topic_i in xrange(n):
    topic_t = str(raw_input().strip())
    topic.append(topic_t)

max = 0;
for i in xrange(n):
    for j in xrange(i+1,n):
        length = ones((int(topic[i],base=2))|(int(topic[j],base=2)))
        know.append(length)
        if (max < length):
            max = length

count = 0
for i in xrange(len(know)):
    if (know[i] == max):
        count += 1
print(max)
print(count)
