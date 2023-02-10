# TARP Assessment - 1

Some of the tools used in this project are: 

## Zotero

With the help of the free, open-source software Zotero, we can quickly gather, arrange, cite, and share sources. We can add source data to your library via a browser extension. 

### Adding Sources

There are many options available in Zotero for adding sources to our Library. The many methods for adding sources to our Zotero Library are described below: 

* **Browser Add-on (Connector)** <br>
  This will be the main method of adding sources from databases, the library catalogue, and free online resources.
  
* **Search Results List** <br> 
  When we wish to add numerous sources from a list of search results from a catalogue, database, or public web, use this option.
  
* **Google Schoolar** <br> 
  Normally, we should use the Browser Connector and navigate to the original source. That isn't always doable. Here is a different approach taken straight from the search results page.
  
* **PDF Files** <br>
  This is a quick and simple approach to add a source record to our Library if we have readable PDF files.
  
* **Manually Add a Source** <br>
  This will be the main method of adding sources from databases, the library catalogue, and free online resources.

### Modifying Source Records

It's not always possible to add sources correctly when adding them to our Zotero Library. The source records' entire content can be changed. Changing the source type, author's name, and title case is easy with the help of the following quick tips.

* In Zotero Library, select the source
* In the right hand pane, click the Source Type drop down menu
* Select the appropriate source type

### Citing and References

We can now add in-text citations and bibliographies to our research paper, thesis, dissertation, book chapter, book, or article once we have sources in our Zotero Library.

<br>

## Github Desktop

Github is a platform for sharing files or source code with others. Version control is one of the main uses of GitHub. When more than one individual is engaged in a project, it is beneficial. Imagine that a group of software developers are working on a website and that they all need to update their codes at the same time. In this situation, Github aids in the development of a central repository where all code files can be uploaded, edited, and managed.

### Creating a Repository

The project is kept in storage at a repository. It could be local, like a folder on our computer, or it might be an internet host like GitHub or another. Code files, text files, photos, or any other type of file can be stored in a repository. This GitHub repository acts as a remote repository. To create a Github repository, we follow these steps: 

* Go to the link: https://github.com/ . Fill the sign up form and click on "Sign up for Github".
* Click on "Start a new project".
* Enter any repository name and click on "Create Repository". 
* Give a description to the repository (optional).

In contrast to a private repository, which allows users to control who can see its contents, the default GitHub repository is public, making its contents accessible to anybody.

### Creating Branches

Branches enable concurrent work on many versions of a repository. Imagine that we want to add a new feature—which is still in development—but we are unsure whether to update our primary project or not. Git branching comes to the rescue in this situation. Using branches, we can switch back and forth between a project's many stages and versions. To test the new feature in the aforementioned scenario, we can establish a new branch without affecting the main branch. When we are finished, we may combine the modifications from the new branch with those from the main branch. The master branch, which is present in we repository by default, is used as the main branch in this case.

<center><img src="https://miro.medium.com/max/1400/0*RiQZEGNoU9HmyjFP.png"></center>

### Cloning our Repository

Next, we clone our newly created repository from GitHub to your local computer. From our repository page on GitHub, click the green button labeled Clone or download, and in the "Clone with HTTPs" section, copy the URL for our repository.

Next, on our local machine, we open our bash shell and change our current working directory to the location where we would like to clone your repository. 

For example, on a Unix based system, if we wanted to have our repository in our Documents folder, we change directories as follows:

```console
cd Documents
```

Once we have navigated to the directory where you want to put your repository, we can use:

```console
git clone https://github.com/URL-TO-REPO-HERE
````

The git clone command copies our repository from GitHub to our local computer. This is a git specific command.

```console
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

### Performing Git Operations

#### Commit Command

We can save the changes to our file with the aid of this process. To remember the modifications we made to a file, we should always include a message when we commit it. Although this message is optional, it is always advised in order to distinguish between the many versions or changes we have made to our repository thus far. These commit messages keep track of the file's history of modifications, which helps other authors better understand the file. Let's make our first commitment now by taking the following actions:

* Click on “readme- changes” file which we have just created.
* Click on the “edit” or a pencil icon in the righmost corner of the file.
* Once we click on that, an editor will open where we can type in the changes or anything.
* Write a commit message which identifies our changes.
* Click commit changes in the end.

#### Pull Command

The most significant GitHub command is pull. It details the file's modifications and invites other contributors to view it and merge it into the master branch. Once the commit is done, anyone can pull the file and can start a discussion over it. Once its all done, we can merge the file. Pull command compares the changes which are done in the file and if there are any conflicts, we can manually resolve it. Now let us see different steps involved to pull request in GitHub.

* Click the ‘Pull requests’ 
* Click ‘New pull request’.
* Once we click on pull request, we select the branch and click ‘readme- changes’ file to view changes between the two files present in our repository.
* Click "Create pull request".

#### Merge Command

Multiple commit sequences will be combined into a single, unified history by git merge. Git merge is most frequently employed to combine two branches. This document will emphasise this branch merging pattern in the examples that follow. In these cases, git merge will look for a common base commit between two commit pointers, typically the branch tips. The changes from each queued merge commit sequence will be combined into a new "merge commit" as soon as Git discovers a common base commit.

#### Git Workflow

<center><img src="https://crunchify.com/wp-content/uploads/2017/09/Github-WorkFlow-Tips-Crunchify-Tips.png"></center>

<br>

## Zettlr

Zettlr is a markdown editor for writing articles, ebooks, and other types of content across platforms. It is modelled after the personal knowledge management and note-taking Zettelkasten system. It supports presentations (using the reveal.js framework), autocorrection, snippets, localization, math formulae, citations, and custom templates.

### Folder Structure

The appeal of a Zettelkasten is that the hierarchy of our content develops organically as a result of our links, so we don't need to know it in advance. Thus, our Zettelkasten  is just a single folder with all files dumped into it. Ideally, we will be able to navigate using only our links rather than file names.

### Basic Zettls and links

The structure of a fundamental Zettel and the internal connections between them form the basis of every Zettelkasten. Zettlr offers all the necessary tools. The fundamental needs are:

* a special way to refer to a particular Zettel

* a method of linking to a Zettel that will remain active over time, such as when the title of a Zettel changes.

* a strategy for dealing with the same-named Zettel (the same topic might be a thing in different areas)

This means that whenever possible, we should link using IDs rather than file names or document titles because they can change as a Zettel expands or becomes more specific. 

### Tags

We can easily find Zettel by using sing tags for meta information, regardless of the relationship between them that is established by links and their content. We can use this to gather all Zettel from a specific lecture for review or to flag all Zettel that requires revision. Conveniently, we can add these tags as keywords in the YAML-header, where they are clearly separated from the Zettel's content and display the meta-data that this Zettel contains.

<br>

