# Evan Petersen - Anubis Interview Project
This is a very bare bones implementation meant to store files in a database for distribution.

## Functionality
- Files up to 16 Mb can be stored on the server, I considered including a filetype since that information was provided by the forms request. Given a different 
implementation of the download function that might have proved useful if I could avoid storing the download in a temp folder and take advantage of the Save dialog box.
- There is a counter for number of downloads and a timestamp of the original upload of a file. Though the counter only updates on page refresh.
- As it is the system seems to handle any filetype and leaves it up to the user's computer to interpret what kind of file it is.


Most of the flask basics was taught through CS-UY 3083 Intro to Databases, with Professor Ratan Dey, but going along with the permissions given by the assignment I took
  advantage of StackOverflow (among others) to develop an understanding of how to tackle the problem. Some of the data most notably the read and write conversions of 
  the binary data, saving the data to a temporary folder before transfer, and the send_file method. I chose to leave in the attempted file deletion just to show a 
  little more of my thought process. If you want a list of pages I sourced from, just let me know.
  
-- Evan Petersen - June 6th, 2021
