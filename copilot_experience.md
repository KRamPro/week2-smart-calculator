
# Purpose of this document
This document is to plot out and reflect on my learning for the smart calculator assignment. 

## Critical Note:
I have intentionally deviated from assignment bounds and not used co-pilot for this work. I used code auto-completes via the Minuet plugin for the Neovim Terminal editor, with auto-completes performed by a local LLM running on my hardware (qwen 3 coder 4b served via Ollama). I already have the infrastructure for this in place. In general, I prefer working with agents, rather than auto-completes, as auto-completes interrupt my train of thought. Agents allow me to go into review mode and then back out into code-mode myself, auto-completes demand that I do both at once, which i find taxing. However, I have been using this model to do very light refactoring work for other projects over the summer months. 

I have followed the directions the assignment has laid out however, and configured co-pilot through my github education package as the previous week's instructions have requested.

## Where AI assistance was useful
The AI generated almost all code for this program. I described basic functions and then tested my understanding of each one. the first commit in this repo is the result of that generation. I kept all additions whether I understood them or not and committed them for posterity. 

As AI gets more and more powerful, it becomes increasingly easier to trust their output, but I found myself not getting the fundamental approach that the AI was following. The approach made heavy use of the 'ast' module. I had to take some time to learn about this library in order to find that I even remotely understood how it works. 

This library is called ast or Abstract Tree Syntax. to use it, you need to create node objects in the tree that you then parse.  I really liked this approach, but I still did not manage to understand the first set of functions in that first pass. After studying it for a while, I managed to put together enough to manage to say that it could be a little cleaner if I moved where the expression node was handled, and I was able to get rid of an extra wrapper. I must admit that it's still a little fuzzy, but I think I am able to get it just enough to be dangerous. 

another thing the LLM suggested that I liked was the use of docstrings, which make use of internal python helper functions to let documentation be derived programmatically through other libraries. I think i'm getting how those internal double underscore functions work. 

The LLM provided a very simple and bruteforce search algorithm for finding the value of x that I understood quite intuitively. 

## Where AI was not helpful... 

When the AI was outputting these very complex solutions, I did not understand them. I had to spend a lot more brain-power in figure it out mode than I probably would have reading through documents. I imagine this is significantly easier after one has been reviewing other people's code for some time, but this is not a skill I have developed as a novice. I still feel waaaay out of my depth when it comes to projects like this. In the past, I spent literal weeks on my one major project (my Oathplate Calculator in JS) which consisted of a lot of painstaking review, but at least I knew were and what I was weak on because I made the program myself and had a mental model of how it worked.


The LLM suggested a more complicated version of the ast expression handler that took arbitrary python code as an expression to evaluate. I rejected this outright. I felt that there was no reason to be doing any of that, as most calculators work fine and don't accept arbitrary code execution... out of scope!

I also rejected a very underwhelming solution that did not fit my requirements. when I was writing out the comments to outline the second improved version, it suggested a basic function that simply added, subtracted, multiplied or divided two numbers from the command line with no checks or safeguards. This did not sit right with me. I did not bother accepting or committing this one.  I was given extra time to complete this assignment, so I wanted to try to push myself and make an excellent submission. My Professor has been very kind!

I the LLM also suggested a test-suite. I felt this was overkill for a program of this size as if it was having problems I think the issue would be relatively easy to find depending on where the problem lay. If the outputs are not what is expected it is prudent to look directly at the parsing logic etc. I did not bother accepting or committing this one. I think the visualize_search() function is proof enough that it works. though I could maybe use a random value between 1 and 1000 here to expand possible coverage if I were trying to write something more durable?



## VS Code Documentation

![[Co-pilot-VSCodeExtension.png]]