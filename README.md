to do calculation, i need to calculate the rations; win draw and losses of current season, past season, and other older seasons in the tables. so if it is Arsenal vs Liverpool, i need to get calculations like Current league table standing. Arsenal total win current sesaon/ total matches played this season. Arsenal total draw this sesaon/total matches played. arsenal total losses this season/total game played. same for liverpool for current season. same calculations for last season for both home and away team. in this case example arsenal and liverpool. and for the history we get head to head ratios of arsenal and liverpool of course we set parameters to auto get home team and away team. but we get home total wins(arsenal)/total matches between them in past years, away total wins(liverpool)/total matches between them. and lastly total draws between them/total matches between them, of whaterver histroy db we have them off. this is it for now, further calculations will come. so just do this for now., current year or season, last season, and all head to head history

# scraper
# scraper	

1. head to (head home team win / total matches played), (draw / total matches played),  and (away team win/total matches played) for 5 years.

2. current league result.
(home team win / total matches played), (draw / total matches played),  and (home team loss/total matches played)

(away home team win / total matches played), (draw / total matches played),  and (away team loss/total matches played) 

3. last season league result.
(home team win / total matches played), (draw / total matches played),  and (home team loss/total matches played)

(away home team win / total matches played), (draw / total matches played),  and (away team loss/total matches played) 

4. the draw ratio from point 2 and draw ratio from point 3 is needed here for calculation. it get the draw ratio that is from point 2 (draw / total matches played) of current season. and also from point 3 same draw for last season. so the calculation being ((from point 2 (draw / total matches played) of current season x home team current year match played + point 3 (draw / total matches played)of last season x home team total matches last year))/ divided by (home team current year matches played + home team total matches last year played.)

5. same for away team. as point 4. so i guess this could be made a function that accepts maybe team id and season and calls my other functions and gets the ratios that can be used here.
the draw ratio from point 2 and draw ratio from point 3 is needed here for calculation. it get the draw ratio that is from point 2 (draw / total matches played) of current season. and also from point 3 same draw for last season. so the calculation being ((from point 2 (draw / total matches played) of current season x home team current year match played + point 3 (draw / total matches played)of last season x home team total matches last year))/ divided by (home team current year matches played + home team total matches last year played.)

6. (Draw ratio in bullet point 1 above + bullet point 4 + bullet point 5) divided by 3 = Draw Chance

7.  what we have done in point 4 - exactly the same but "Home Team Win" Ratio - current year and last year seasons 