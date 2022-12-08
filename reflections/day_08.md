Ran into an issue with the new day script as it considered the input with leading zeros as an ocatal number.
The problem only surfaced on day 8 because 8 is the first number that diverges from base 10.

Used a stackoverflow [answer](https://stackoverflow.com/questions/8078167/printf-in-bash-09-and-08-are-invalid-numbers-07-and-06-are-fine) to treat the input as base 10. Perhaps I might use the strip leading zeros one if that doesn't work.