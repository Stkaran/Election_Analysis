# Election_Analysis

## Purpose 
This audit was all about digging a bit deeper into the data than the first go-round, which focused on the ultimate and total vote count. This was taken even futher by breaking down the seperate counties from one another to see the counties percentage of the total vote along with the original data. We were able to accomplish this by replecating our code that was used to find information on the candidates, but instead look for information on the counties. The most important step of this was creating a list and dictionary to store this data and later have the code refer back to it.

county_options = []
county_votes = {} 

## Results
  -We found there was a total of 369,711 votes cast in this election. There were three candidates: Charkes Stockham, Diana Degette, and Raymon Doane. 
  -Out of the three counties we had data from Jefferson County had 10.5% (38,855 votes) of the vote, Arapahoe County had 6.7% (24,801 votes) of the vote, and Denver County had 82.8% (306,055 votes) of the vote.
  -As you can see Denver County, by a large margin, accounted for the majority of the votes in this election.
  -Charkes Stockham received 23.0% (85,213 votes) of the vote, Diana Degette received 73.8% (272,892 votes) of the vote, and Raymon Doane received 3.1% (11,606 votes) of the vote. 	
  -Diana Degette won the election overwhelmingly with 272,892 votes which came out to just under 74% of the total vote.	

## Summary
This first idea I would have for expanding on this code is looking at how citizens voted based on which county they lived in. Our code right now only tells us how many votes came from each county in relation to the total vote count, but not if the voters in that specific county leaned toward a candidate more than the others. If I was working for a politcal party's campaign effort, I would want to know which counties leaned which way as it would inform me of where I'd need to invest more time in or if that area was on lock. In order to get this data, we would have to create dictionaries and lists for each county and then create for loops to make a count for each candidates name when it appears.
Another idea on how to expand the code would be to flip the Larget County Turnout to find the county with the lowest turnout. There will always counties that are much larger than others due to high urban density and thus higher vote turnout, but I still think it is important for the election board to keep an eye out on which counties are having low turnout. This could lead to investigations on why turnout is low (poor access to polls, no mail in voting, restrictive voter registration) and could help point leaders in the right direction on how to resolve these issues. In order to find this data, we would once again a create list and dictionaries again to hold the data, and would then apply conditionals in order get our results.  
  
