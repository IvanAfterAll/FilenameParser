# FilenameParser

## What it Does
In support of a book project I am writing, I had assembled a directory of hundreds of newspaper articles (PDFs from the Library of Congress' Chronicling America resource).

Each filename used this format: Newspaper {State} - {Year} {Month} {Day} {Fileblurb}, with "Fileblurb" being a short, one sentence description of the article's contents.

I wanted to avoid manually entering that information into a spreadsheet. This script uses the Pandas, Glob, and Parse packages to read the filepaths, parse those values that fit the specified pattern, then export the values into a CSV.

##Example
If my directory contains this file --> \Newspaper NY - 1899 Dec 25 Santa Comes to NYC On Schedule.pdf

This script would search for the pattern ---> \Newspaper {State} - {Year} {Month} {Day} {Fileblurb}.pdf

The final CSV will be sorted into five columns (State, Year, Month, Day, Fileblurb), e.g. ---> State: NY, Year: 1899, Month: Dec, Day: 25, Fileblurb: Santa Comes to NYC on Schedule and will export into your project directory

##How to Use
Currently, the program is set to look for the specific pattern noted above as it was the file naming convention I had used. To use it, set your "filepath=." It should also be simple enough to plug in a different "pattern=" value and the Parse library allows for considerable complexity.

####As currently written, the pattern looks for:
{State} - No set limit, anything after "Newspaper" and before "-" should be picked up. I use 2 character abbreviations (NY, GA, CA, etc...)
{Year} - 4 digits expected
{Month} - 3 letters expected (e.g. Jan, Feb, Mar...)
{Day} - 2 digits expected
{Fileblurb} - No set limit on characters
