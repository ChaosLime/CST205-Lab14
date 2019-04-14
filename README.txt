 
Lab #14: Files in Python (2-3 hours)
This is an Individual project (each student work on his/her own project, with or without help from others. Each student has to submit their individual work.
Problem 1: 

Rumor has it that the literary classic Green Eggs and Ham was written because Dr. Seuss's publisher bet him he couldn't write a book using only 50 words.  Write a Python program that opens the file Eggs.txt (containing a slightly modified version of Green Eggs and Ham) and verifies this urban legend by doing the following:

Create a count of how many total distinct words appear in Green Eggs and Ham
Create a count of how often each of the words appears (note that Eggs eggs Eggs! eggs? and eggs, should all be counted as the same word).  
Print out the total distinct count and the count for each of the words. 
Print out the most commonly occuring word in the book
Note that while this problem does use files, it also uses a variety of other Python structures we have learned about including strings, list and dictionary. 

[Note] You may notice the file eggs.txt contains some "typos". they are there intentionally to distinguish from the original file. 

Problem 2:

In Python you aren't limited to dealing with text files, you can also deal directly wtih HTML files.  This is very cool, because you can get information from your programs from the web! For this problem, let's assume you are writing a news aggregator.  You need to pull the headlines from the news webpage:  https://www.census.gov/newsroom/press-releases.html

[Hint] headlines are the bold lines under beneath "PRESS RELEASE" and the date.

Use the tools in your web browser to 
View the source for the page (this is the HTML code that makes up the page)
Save the page as an HTML file on your local drive
Then open the file in JES 
Use string processing techniques to extract the headlines from the paper.
Hint, refer back to the string documentation if you need to: http://docs.python.org/2/library/string.html
Hint: Remember that if you use the read command you end up with the whole file as a string this means you can boil this problem down to identifying the substring in the file that contains the headline
Here is the sample result that you could generate:

**** U.S. Census Bureau News! ****
U.S. Census Bureau Streamlines Reporting for Retailers
Save the Date: Census Bureau to Host 2020 Census News Conference
Census Bureau Projects U.S. and World Populations on New Year’s Day
2020 Census Quarterly Program Management Review
U.S. Census Bureau Continues to Hire for 2020 Census
