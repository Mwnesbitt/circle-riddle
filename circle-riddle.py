import random
import numpy

points = 10 #this is the points in addition to p0., thus fixing p0 at 0.5, right in the center of the number line  
sequence = []
iterations = 1000000

for z in range(1,points):
  success = []
  for x in range(iterations):
    pointpositions = []
    for i in range(z): #putting points on the circle
      pointpositions.append(random.uniform(0,1))
    if(max(pointpositions) - min(pointpositions) <= 0.5): success.append(1)
    else: success.append(0)

  overall = numpy.mean(success)
  sequence.append(overall)
  #print("The likelihood for %s is %r" %(z+1,overall)) #z+1 because 'points' refers the points in addition to p0
  
for item in sequence:
  print(str(round(item,4)*100)+"%")
  
"""
SOLUTION BELOW

After looking at the data and being completely unable to find a formula, 
I went back to paper and pencil and solved this the right way.

Note that I think the best way to do this is to think of a straight line 
as your circle, where the two ends of the line are the same point.  Assume
p0 was smack dab in the center of the line (i.e. you cut the circle directly
across from p0), and then work from there fitting the semicircle around p0 
and all the other points that were put on the line.

The trick was in realizing I needed the probability of point n+1 being
in the semicircle given that all points n were in the semicircle (induction).

The next part was dubious, and I probably wouldn't be confident in my answer
except for the fact that the data from the script back it up.  

Given that the probability distribution at play here is uniform, you should think
of the n existing points as being equidistant from one another.  Thus you can
think of 2 addition possible acceptable locations for n+1, namely extending the
line of n points in either direction.  But the way I think of it is that extending
to the right is a "deserved" acceptable location, but extending to the left is a 
"bonus" acceptable location that was snatached away from the "not-semicircle" territory.
So you can think of the probability of n+1 being in the semicircle as having stolen 
a location from the "not-semicircle" 's territory.  So that means there are 
n+1 acceptable "slots" (again, the slotting is the dubious aspect but we're working
with a uniform distribution...so yeah lots of hand waving and harrumphing here) 
and n-1 unacceptable slots.  That means your probability of getting an acceptable
slot for point n+1 is (n+1) / [(n+1) + (n-1)] or (n+1)/(2n).  Thus the probability 
for point n is n/(2*(n-1)).

Now to find the probability that n random points are all on the same 
semicircle, you need to take a cumulative product of the probability that each of 
the points up to n was successful.

So you take the product of all these, and you get some nice cancellation/telescoping:
n/(2*(n-1))  *  (n-1)/(2*((n-1)-1)  *  (n-2)/(2*((n-2)-1)  *  ...  *  (n- (n-1))/(2*((n-(n-1)-1)
n/(2*(n-1))  *  (n-1)/(2*(n-2))      *  (n-2)/(2*(n-3))     *  ...  *  1/(2*  WHOOPS undefined at n = 1
Ok so you take it down only to n=2.  But you get the idea.  The cancellations get you:

n/(2^(n-1)).  Hooray, that ties with the data so I feel less bad about my assumption 
of uniformity of the points.  I wish I were better at math but I suppose I limped through
this one.

A cool way to express the formula is:
1/(2^(n-1)) + (n-1)/(2^(n-1))

The reason I think this is cool is because the first term is intuitive-- it's the probability
of you having all your points in a semicircle if the first point defines the center of the semicircle,
i.e., the semicircle can't wiggle.  That's just intuitive-- the first point is a freebie that defines 
the semicircle, so all the other n-1 points just cut your odds in half.  The second term, therefore, 
is the benefit you get from being able to wiggle the semicircle.  I'll be real honest-- I have 
no intuition for why that term makes sense as the cumulative benefit of the "wiggle" capability, 
but the first term has intuitive value to me so I think it's an interesting expression of the formula.  

Another cool way to express it (and I'm not sure why I didn't express it this way initially) is:
n*(1/2)^(n-1).

This separates the benefit from wiggling in a multiplicative separation instead of an additive seaparation.
My intution when I first encountered the problem was to think that the answer was (1/2)^(n-1), since the first
point is a "freebee" that fixes the semicircle.  But I forgot about the wiggling, as I realized when thinking
about whether that answer was correct.  So it's interesting to see that the cumulative benefit of wiggling is 
the "n" term, but I still don't have a good intuition for why that's the case (although it seems closer than 
with the additive separation of the formula).

"""