# Multiscale Biological Modeling Test Website

*Remember to use F5 as a hard refresh when previewing the GitHub Pages website, as your computer might otherwise save the page information and not display updates* 

### Quick References: 

Github Pages References: https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/

Kramdown Markdown Reference: https://kramdown.gettalong.org/quickref.html

Which page layout to use? https://mmistakes.github.io/minimal-mistakes/docs/layouts/

Adding a footnote requires these symbols [^1]

Wonderful $$\LaTeX$$ can be processed with Kramdown using double dollar signs, even for inline content like $$x=42$$. A centered function just requires its own newline. Note that this content will not be visible through the Github Preview, and must be built with Github pages.

$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$

**Notice** This LaTex will only process if the layout is specified as "layout: single" 

**Notice** Text in a notice should start with a double asteriks for emphasis, and requires a special piece of code on the next line 
{: .notice--primary}

~~~~~~
This is also a code block.
~~~
Ending lines must have at least as
many tildes as the starting line.
~~~~~~~~~~~~

~~~ ruby
# specify the language at the starting tilde
def what?
  42
end
~~~

A [link](http://kramdown.gettalong.org "hp")
to the homepage.

Can also use a variable, delcared below, to [link][kramdown hp]
to the homepage.

[kramdown hp]: http://kramdown.gettalong.org "hp"

An image: ![gras](assets/images/bio-photo.jpg)

[^1]: The footnote can be clicked to return back to the original text as well

**Notice:** The home page of the website is the file *index.md*

### Quick guide to add a new module

1. Inside *_pages*, duplicate (or copy and paste) the "motifs" folder
2. Rename the folder to your desired code, hereby referenced as *moduleX*
3. For each file inside the *moduleX* folder, rename each file to replace *motifs* with *moduleX*
4. Inside each file, information about the file and how it should be rendered is contained within the "YAML Front Matter", within the two "---" lines at the top
    * Change the permalink, which is used by the *navigation.yml* file mentioned in step [], to swap *motifs* for *moduleX*
    * Change the variable *nav: "motifs"* to *nav: moduleX*
5. Go to the *_data/navigation.yml* file
    * If you wish to have this module shown in the menu at the top of the website, add in another *- title:* / *url:* pair to reflect the permalink of your module's homepage
    * Duplicate the *motifs:* variable and all its *title:*s and *children:*
    * Change the variable name from *motifs* to *moduleX*
    * Rename all *url: /motifs/pagename* to *url: /moduleX/pagename*
6. Change all titles and pagenames as you see fit

Lastly, you can repair or delete the "Previous" and "Next Page" buttons at the bottom of each *moduleX_pagename.md* file.   

The syntax shown here: 
~~~
[Previous](#)
~~~
represents 
~~~
[Text inside button](link)
~~~
where a pound sign "#" references a link to the header of the same page and a pagename, such as *setup*, references the permalink page */moduleX/setup*

### Small Notes

Only sometimes noticable- specific page build order: it seems certain elements do not update on Github Pages at same time. E.g.
  1. Edit text in file to say "Hi" + change navigation
  2. Wait a few minutes, refresh preview, see changed navigation but no text
  3. Edit text in file to say "Hi2"
  4. Wait a few minutes, refresh preview, see changed navigation and "Hi"


