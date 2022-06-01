# Git and GitHub tutorial

Last updated for remote use by D. Carr - May 2021

## 1. Go [here](https://github.com/capprogram/2021bootcamp/blob/master/git-prep.md) if you need a GitHub account or must install Git.

## 2. Configure Git.

Windows users should start git by starting the "Git Bash" program, while Mac users should just be able to open up a normal terminal. On your machine, run these `git config` commands below (in any directory) to set your name, email, and preferred options.

Examples:

    git config --global user.name “Sheila Kannappan”
    git config --global user.email sheila@physics.unc.edu
    git config --global color.ui "auto"
    git config --global core.autocrlf false

Note `user.name` is not your GitHub username but rather your name.

(Our git tutorial assumes you will use nano as your editor. If you accidentally have another text editor, such as vi, set as your default and would like to switch to use nano, you can use the command `git config --global core.editor "nano"`.) 

You can check what you’ve done with

    git config --list
    
Press q to quit out of the above command. You can get more details on config option by typing

    git config -h        # short version
    git config --help    # long version



## 3. Complete the tutorial below.

### Table of Contents

1. [Automated Version control](01-automated-version-control.md)
2. [Creating a repository](02-creating-a-repository.md)
3. [Tracking changes](03-tracking-changes.md)
4. [Exploring history](04-exploring-history.md)
5. [Working with branches](05-branches.md)
6. [Setting up a remote repository in GitHub](06-remotes-in-github.md)
7. [Collaborating](07-collaborating.md)

### Source

This tutorial borrows heavily from [Software Carpentry's](http://software-carpentry.org/) tutorial [Version control with git](http://swcarpentry.github.io/git-novice/) and Software Carpentry's [branching tutorial from erdavenport](https://github.com/erdavenport/git-lessons), both under a [Creative Commons Attribution license (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

## 4. Additional Resources

1. [Git cheat sheet](https://education.github.com/git-cheat-sheet-education.pdf)
2. [Quick overview](http://rogerdudler.github.io/git-guide/)
