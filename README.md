# Project Name:
MarkovText.v2

# Group Members:
Peike Li, Yuxuan Shi, Johnny Tu

# Project Description:
MarkovText.v2 is a simplified Markov Language Model. It models a text corpus and generates a fake text from it, using units of words. To compare two texts, it can compute the [Flesch reading ease score](https://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests) for the two texts.

# Instructions on Package Installments:
conda create --name NEWENV --file requirements.txt

# Description of Demo File:

1. After you download the repo, you'll find the demo file called demo.ipynb. Open it to test the functionalities of the class MarkovText.
2. Run the first cell to import the class and all the functions. Run the second cell to load the Emma text file into the environment.
3. Run the cell shown below to test what happens if the function cannot generate appropriate text with the original input seed and n. The function will automatically try n-1 and call itself again to generate the fake text. The expected output in this case should be the random text that is successfully generated.
<img width="989" alt="image" src="https://user-images.githubusercontent.com/97068696/157997642-55604b01-f1a8-432a-8b2d-6615eb843189.png">
4. Run the cell shown below to create an object of the class MarkovText. n represents n-gram, length represents the expected number of words of the text generated, and seed represents the starting word of the fake text. You can change the length to another number, but don't make it too large for your convenience. 
<img width="975" alt="image" src="https://user-images.githubusercontent.com/97068696/157997753-162ed15c-5485-44dd-bae9-4ff097894dc2.png">
5. Run the cell shown below to call the function that generates fake text. The expected output should be a string with about <length> words.
<img width="975" alt="image" src="https://user-images.githubusercontent.com/97068696/157997066-481b642d-58f1-4c35-b3a3-7edcb5c71f22.png">
6. Run the cell shown below to call the function that generates exactly one sentence. The expected output should be a string with only one sentence.
<img width="995" alt="image" src="https://user-images.githubusercontent.com/97068696/157997176-7725df5b-411b-45c4-8573-a4ad1e145367.png">
7. Run the cell shown below to call the function that computes and prints the Flesch reading ease score for the fake text and the original text with the same length. This reading score represents the readablity of the text. The higher the score is, the easier it is to read the text. The scores would change each time you run this cell, because our model generates different random text and select the original text randomly each time. To learn more about how the reading ease score is calculated, click the link in Project Description.
<img width="982" alt="image" src="https://user-images.githubusercontent.com/97068696/157997770-98b9412f-423e-4c70-b6d0-2405ee5a4cd4.png">

# Scopes and limitations:
The reading scores computed may have large variations and are only used as references for the comparison between fake text and original text.

# License and terms of use:
MIT License

Copyright (c) 2022 Peike Li, Yuxuan Shi, Johnny Tu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

# References and Acknowledgements:
[Reference link on splitting paragraphs into sentences with regular expressions.](http://pythonicprose.blogspot.com/2009/09/python-split-paragraph-into-sentences.html)

Also shoutout to Harlin and Puppycat for getting us through the quarter

# Background and source of dataset (if applicable):
[Link for Emma.txt source file](https://www.gutenberg.org/ebooks/158)
